**FICS PCB Image CollectionFPIC (FPIC) Component** dataset is specifically designed for instance segmentation tasks. Comprising 6260 images, this dataset contains 29639 labeled objects distributed across 25 distinct classes, encompassing components such as *C*, *R*, *U*, as well as other classes like *J*, *L*, *Q*, *P*, and more. Derived from the FPIC dataset, this compilation involves the cropping of images representing 25 component classes. This dataset serves as a valuable resource for training models in instance segmentation, particularly focused on identifying and delineating various electronic component classes within PCB (Printed Circuit Board) images.

Authors propose **PCBSegClassNet**, a novel deep neural network for PCB component segmentation. The network uses a two-branch design that captures the global context in one branch and spatial features in the other. The fusion of two branches allows the effective segmentation of components of various sizes and shapes. They reinterpret the skip connections as a learning module to learn features efficiently. 

Authors evaluate the performance on publicly available dataset FPIC (Jessurun et al., 2022). There are 230 images of 73 distinct PCBs in the dataset, taken from both the front and rear sides of the PCBs. Over 58,000 annotations are included in the images, including annotations for the text and any attached components. There are total of 58 different components annotated. Of these, we use 25 components for evaluation:

<table>
  <tr>
    <th>No.</th>
    <th>Component</th>
    <th>Count</th>
    <th>No.</th>
    <th>Component</th>
    <th>Count</th>
    <th>No.</th>
    <th>Component</th>
    <th>Count</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Resistor (R)</td>
    <td>7246</td>
    <td>9</td>
    <td>Resistor Network (RN)</td>
    <td>330</td>
    <td>17</td>
    <td>CRA</td>
    <td>54</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Capacitor (C)</td>
    <td>6896</td>
    <td>10</td>
    <td>Test Point (TP)</td>
    <td>266</td>
    <td>18</td>
    <td>Switch (SW)</td>
    <td>50</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Integrated Circuit (U)</td>
    <td>761</td>
    <td>11</td>
    <td>Integrated Circuit (IC)</td>
    <td>237</td>
    <td>19</td>
    <td>Transformer (T)</td>
    <td>47</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Discrete Transistor (Q)</td>
    <td>616</td>
    <td>12</td>
    <td>Plug (P)</td>
    <td>200</td>
    <td>20</td>
    <td>Fuse (F)</td>
    <td>44</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Connector (J)</td>
    <td>579</td>
    <td>13</td>
    <td>Thyristor (CR)</td>
    <td>194</td>
    <td>21</td>
    <td>Vaccum Tube (V)</td>
    <td>41</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Inductor (L)</td>
    <td>473</td>
    <td>14</td>
    <td>Motor (M)</td>
    <td>74</td>
    <td>22</td>
    <td>Light Emitting Diode (LED)</td>
    <td>39</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Resistor Coil (RA)</td>
    <td>404</td>
    <td>15</td>
    <td>Button (BTN)</td>
    <td>72</td>
    <td>23</td>
    <td>Switch (S)</td>
    <td>37</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Diode (D)</td>
    <td>362</td>
    <td>16</td>
    <td>Ferrite Bead (FB)</td>
    <td>69</td>
    <td>24</td>
    <td>QA</td>
    <td>36</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>25</td>
    <td>Jumper Link (JP)</td>
    <td>31</td>
  </tr>
</table>

The “count” column shows the number of images of that component in the FPIC-component dataset.

The FPIC dataset provides images of the whole PCB. For performing component-level classiﬁcation, authors create a new dataset named FPIC-component, which contains component images cropped from the PCB images. Figure bellow shows the steps taken to crop the component images; they are as follows:

- Perform contour operation on the ground truth mask to ﬁnd the boundary of each component.
- From contour and boundary information, ﬁnd a rectangular bounding box that covers the whole contour for everycomponent.
- From the rectangular bounding box, crop the component region from the original image.- Color information from the ground truth mask in the contour region provides us with the ground truth label for thecorresponding PCB component.

<img width="851" alt="pcb_preview" src="https://github.com/dataset-ninja/fpic-component/assets/123257559/192cb8aa-0002-4cf3-8fbe-f61c0968c8c2">

The resolution of PCB images in the FPIC dataset varies from 2266×1832 to 8291×6929. Thus, the highest resolutionimage has a resolution higher than that of even an 8K UHD (ultra-high deﬁnition) image. Since processing large images canoverwhelm the GPU, authors operate on image patches instead of the entire image. They have experimented with the patches of sizes 256×256,512×512,768×768, and 1024×1024. The results obtained with patches of size 1024×1024 and 768×768 werefound to be comparable, whereas smaller patch sizes provided inferior results. Hence, authors choose a patch size of 768×768,which captures the most representative sections without overwhelming the GPU. From this, they obtain 5048 patch images for *train* and 1262 patch images for *val*.
