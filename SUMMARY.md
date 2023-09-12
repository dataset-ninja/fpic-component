**PCBSegClassNet - A Light-weight Network for Segmentation and Classification of PCB Component** is a dataset for an instance segmentation task. It is used in the engineering research. 

The dataset consists of 6260 images with 29639 labeled objects belonging to 25 different classes including *C*, *R*, *U*, and other: *J*, *L*, *Q*, *P*, *D*, *IC*, *RN*, *CR*, *RA*, *M*, *T*, *V*, *TP*, *FB*, *S*, *BTN*, *CRA*, *QA*, *LED*, *F*, *SW*, and *JP*.

Images in the PCBSegClassNet dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 1608 (26% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *train* (5008 images) and *val* (1252 images). The dataset was released in 2023.

<img src="https://github.com/dataset-ninja/pcbsegclassnet/raw/main/visualizations/poster.png">
