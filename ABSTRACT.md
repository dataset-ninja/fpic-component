PCB component classification and segmentation can be helpful for PCB waste recycling. However, the variance in shapes and sizes of PCB components presents crucial challenges. Authors propose **PCBSegClassNet**, a novel deep neural network for PCB component segmentation. The network uses a two-branch design that captures the global context in one branch and spatial features in the other. The fusion of two branches allows the effective segmentation of components of various sizes and shapes. They reinterpret the skip connections as a learning module to learn features efficiently. 

Authors evaluate the performance on publicly available dataset FPIC (Jessurun et al., 2022). There are 230 images of 73 distinct PCBs in the dataset, taken from both the front and rear sides of the PCBs. Over 58,000 annotations are included in the images, including annotations for the text and any attached components. There are total of 58 different components annotated. Of these, we use 25 components for evaluation:
- *R*: Resistor
- *C*: Capacitor
- *U*: Integrated Circuit (IC) or Microcontroller
- *Q*: Transistor
- *J*: Connector
- *L*: Inductor
- *RA*: Relay
- *D*: Diode
- *RN*: Resistor Network
- *TP*: Test Point
- *IC*: Integrated Circuit
- *P*: Connector 
- *CR*: Crystal Oscillator or Ceramic Resonator
- *M*: Motor 
- *BTN*: Button
