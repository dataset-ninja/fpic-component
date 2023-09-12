PCB component classification and segmentation can be helpful for PCB waste recycling. However, the variance in shapes and sizes of PCB components presents crucial challenges. Authors propose **PCBSegClassNet**, a novel deep neural network for PCB component segmentation. The network uses a two-branch design that captures the global context in one branch and spatial features in the other. The fusion of two branches allows the effective segmentation of components of various sizes and shapes. Authors reinterpret the skip connections as a learning module to learn features efficiently. They propose a texture enhancement module that utilizes texture information and spatial features to obtain precise boundaries of components. They introduce a loss function that combines DICE, IoU, and SSIM loss functions to guide the training process for precise pixel-level, patch-level, and map-level segmentation.

Flow of network:

The dataset uses the following conventions:

- _R_: Resistor
- _C_: Capacitor
- _U_: Integrated Circuit (IC) or Microcontroller
- _Q_: Transistor
- _J_: Connector (e.g., a header or jack)
- _L_: Inductor
- _RA_: Relay (assuming it's a relay, RA is often used for relay designations)
- _D_: Diode
- _RN_: Resistor Network
- _TP_: Test Point
- _IC_: Integrated Circuit
- _P_: Connector (similar to J)
- _CR_: Crystal Oscillator or Ceramic Resonator
- _M_: Motor (assuming it's a motor)
- _BTN_: Button
