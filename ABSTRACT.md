PCB component classification and segmentation can be helpful for PCB waste recycling. However, the variance in shapes and sizes of PCB components presents crucial challenges. Authors propose **PCBSegClassNet**, a novel deep neural network for PCB component segmentation. The network uses a two-branch design that captures the global context in one branch and spatial features in the other. The fusion of two branches allows the effective segmentation of components of various sizes and shapes. They reinterpret the skip connections as a learning module to learn features efficiently. 

Authors evaluate the performance on publicly available dataset FPIC (Jessurun et al., 2022). There are 230 images of 73 distinct PCBs in the dataset, taken from both the front and rear sides of the PCBs. Over 58,000 annotations are included in the images, including annotations for the text and any attached components. There are total of 58 different components annotated. Of these, we use 25 components for evaluation:

![PCB Components](https://i.ibb.co/tYqL4CS/Screenshot-2023-09-13-101900.png)

The “count” column shows the number of images of that component in the FPIC-component dataset.

The FPIC dataset provides images of the whole PCB. For performing component-level classiﬁcation, authors create a new dataset named FPIC-component, which contains component images cropped from the PCB images. Figure bellow shows the steps taken to crop the component images; they are as follows:

- Perform contour operation on the ground truth mask to ﬁnd the boundary of each component.
- From contour and boundary information, ﬁnd a rectangular bounding box that covers the whole contour for everycomponent.
- From the rectangular bounding box, crop the component region from the original image.- Color information from the ground truth mask in the contour region provides us with the ground truth label for thecorresponding PCB component.

![Extracting component images from PCB images](https://i.ibb.co/H2fBx3L/Extracting-component-images-from-PCB-images.png)

The resolution of PCB images in the FPIC dataset varies from 2266×1832 to 8291×6929. Thus, the highest resolutionimage has a resolution higher than that of even an 8K UHD (ultra-high deﬁnition) image. Since processing large images canoverwhelm the GPU, authors operate on image patches instead of the entire image. They have experimented with the patches of sizes 256×256,512×512,768×768, and 1024×1024. The results obtained with patches of size 1024×1024 and 768×768 werefound to be comparable, whereas smaller patch sizes provided inferior results. Hence, authors choose a patch size of 768×768,which captures the most representative sections without overwhelming the GPU. From this, they obtain 5048 patch images for ***train*** and 1262 patch images for ***val***.
