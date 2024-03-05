**FICS PCB Image CollectionFPIC (FPIC) Component** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the waste recycling industry. 

The dataset consists of 6260 images with 29639 labeled objects belonging to 25 different classes including *C*, *R*, *U*, and other: *J*, *L*, *Q*, *P*, *D*, *IC*, *RN*, *CR*, *RA*, *M*, *T*, *V*, *TP*, *FB*, *S*, *BTN*, *CRA*, *QA*, *LED*, *F*, *SW*, and *JP*.

Images in the FPIC-Component dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 1608 (26% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *train* (5008 images) and *val* (1252 images). The dataset was released in 2023 by the Indian Institute of Technology.

Here are the visualized examples for the classes:

[Dataset classes](https://github.com/dataset-ninja/fpic-component/raw/main/visualizations/classes_preview.webm)
