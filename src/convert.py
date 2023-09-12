import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import file_exists, get_file_name
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer...", total=fsize) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###

    dataset_path = os.path.join("PCBSegClassNet", "data", "segmentation")
    batch_size = 50

    color_values = {
        "R": (255, 0, 0),
        "C": (255, 255, 0),
        "U": (0, 234, 255),
        "Q": (170, 0, 255),
        "J": (255, 127, 0),
        "L": (191, 255, 0),
        "RA": (0, 149, 255),
        "D": (106, 255, 0),
        "RN": (0, 64, 255),
        "TP": (237, 185, 185),
        "IC": (185, 215, 237),
        "P": (231, 233, 185),
        "CR": (220, 185, 237),
        "M": (185, 237, 224),
        "BTN": (143, 35, 35),
        "FB": (35, 98, 143),
        "CRA": (143, 106, 35),
        "SW": (107, 35, 143),
        "T": (79, 143, 35),
        "F": (115, 115, 115),
        "V": (204, 204, 204),
        "LED": (245, 130, 48),
        "S": (220, 190, 255),
        "QA": (170, 255, 195),
        "JP": (255, 250, 200),
    }

    def get_key(dict, value):
        for k, v in dict.items():
            if v == value:
                return k

    def replace_path(path, fr, to):
        head = path
        tail = None
        mask_name = os.path.basename(path)
        while tail != fr:
            head_tail = os.path.split(head)
            head = head_tail[0]
            tail = head_tail[1]
        return os.path.join(head, to, mask_name)

    def get_unique_colors(img):
        unique_colors = []
        img = img.astype(np.int32)
        h, w = img.shape[:2]
        colhash = img[:, :, 0] * 256 * 256 + img[:, :, 1] * 256 + img[:, :, 2]
        unq, unq_inv, unq_cnt = np.unique(colhash, return_inverse=True, return_counts=True)
        indxs = np.split(np.argsort(unq_inv), np.cumsum(unq_cnt[:-1]))
        col2indx = {unq[i]: indxs[i][0] for i in range(len(unq))}
        for col, indx in col2indx.items():
            if col != 0:
                unique_colors.append((col // (256**2), (col // 256) % 256, col % 256))

        return unique_colors

    def create_ann(image_path):
        labels = []
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        mask_path = replace_path(image_path, "images", "masks")
        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)
            if len(np.unique(mask_np)) != 1:
                uniq_color = get_unique_colors(mask_np)
                for color in uniq_color:
                    obj_class = meta.get_obj_class(get_key(color_values, color))
                    mask = np.all(mask_np == color, axis=2)
                    ret, curr_mask = cv2.connectedComponents(mask.astype("uint8"), connectivity=8)
                    for i in range(1, ret):
                        obj_mask = curr_mask == i
                        curr_bitmap = sly.Bitmap(obj_mask)
                        curr_label = sly.Label(curr_bitmap, obj_class)
                        labels.append(curr_label)
        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_classes = [sly.ObjClass(label, sly.Bitmap, color_values[label]) for label in color_values]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=obj_classes,
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset_val = api.dataset.create(project.id, "val", change_name_if_conflict=True)
    dataset = dataset_train = api.dataset.create(project.id, "train", change_name_if_conflict=True)

    total_files = 0

    image_val = []
    image_train = []

    for r, d, f in os.walk(dataset_path):
        for dir in d:
            if dir == "val":
                img_folder = os.path.join(r, dir, "images")
                img_paths = [os.path.join(img_folder, file) for file in os.listdir(img_folder)]
                total_files += len(img_paths)
                image_val.extend(img_paths)
            elif dir == "train":
                img_folder = os.path.join(r, dir, "images")
                img_paths = [os.path.join(img_folder, file) for file in os.listdir(img_folder)]
                total_files += len(img_paths)
                image_train.extend(img_paths)

    project_images = {"val": image_val, "train": image_train}
    progress = sly.Progress("Create dataset {}".format(dataset.name), total_files)

    for ds in project_images:
        if ds == "val":
            dataset = dataset_val
        else:
            dataset = dataset_train
        img_paths = project_images[ds]
        for img_pathes_batch in sly.batched(img_paths, batch_size=batch_size):
            img_names_batch = [os.path.basename(img_path) for img_path in img_pathes_batch]
            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]
            anns_batch = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns_batch)
            progress.iters_done_report(len(img_names_batch))

    return project
