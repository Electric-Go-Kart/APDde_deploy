# CS/ECE528 Project at the Walter Scott Jr. College of Engineering
## APDde (Autonomous Pedestrian Detection with Depth Estimation)

**Authors:**
- Spencer Beer, beersc@colostate.edu
- Kyle Nilsson, kylenils@colostate.edu

---

## Problem Statement

The project, APDde (Autonomous Pedestrian Detection with Depth Estimation), aims to address several critical issues related to LiDAR modules and depth perception sensors in autonomous vehicles. LiDAR modules, operating at wavelengths of 905 nanometers (nm) and 1550 nanometers, face challenges when operating in sunlight due to interference from the Sun's energy spectrum. Additionally, crosstalk between modules using the 905 nm and 1550 nm spectrum is a common issue. APDde seeks to reduce these problems to enhance the safety and reliability of depth perception sensors, such as LiDAR, in autonomous vehicles.

![image](https://github.com/Electric-Go-Kart/APDde/assets/101066043/51e188e7-c113-456b-a328-695503eb3fda)

The project also involves using cameras to accurately predict the depth of objects in front of a vehicle through a machine learning model trained on image data. This approach improves the safety and reliability of collision avoidance systems, particularly in the context of the APD (Autonomous Pedestrian Detection) model for a Go-Kart senior design project. APDde may also offer cost-effective solutions as high-precision LiDAR modules can be expensive. APDde could potentially save space and weight, optimizing designs in the automotive industry if needed.

---

## Existing Implementations and Resources

Relevant resources and implementations related to the project include:

1. **PyTorch3D**
   - [GitHub Repository](https://github.com/facebookresearch/pytorch3d)
   - PyTorch3D is a library by Facebook that provides efficient, reusable 3D operators for PyTorch. It could be useful if the project transitions from the 2D to 3D domain.

2. **Depth Estimation using Depth Camera D435i**
   - [GitHub Repository](https://github.com/jithin8mathew/Depth-estimation-using-Depth-Camera-D435i-for-YOLOv5-detected-objects)
   - This repository is a useful resource for learning how to manipulate the model for depth estimation.

---

## Relevant Papers

To provide context and background for the project, the following papers will be examined:

1. Choi, H. (2022). "YOLO MDE: Object Detection with Monocular Depth Estimation." Electronics, 11(1), 76. [Read the paper](https://doi.org/10.3390/electronics11010076)

2. Vajgl, Marek, Petr Hurtik, and Tomáš Nejezchleba. (2022) "Dist-YOLO: Fast Object Detection with Distance Estimation." Applied Sciences 12, no. 3: 1354. [Read the paper](https://doi.org/10.3390/app12031354)

3. H. Kato, F. Nagata, Y. Murakami and K. Koya. (2022) "Partial Depth Estimation with Single Image Using YOLO and CNN for Robot Arm Control." 2022 IEEE International Conference on Mechatronics and Automation (ICMA). (doi: 10.1109/ICMA54519.2022.9856055)

---

## Data Sources

The project will use the following data sources:

- **KITTI Dataset**: [KITTI Dataset](http://www.cvlibs.net/datasets/kitti/)
  - This dataset will be utilized for training and testing the depth estimation model. Additionally, LiDAR and camera data may be used to fine-tune the model for the specific use case. Synchronization of timestamps for LiDAR and camera data will be ensured if new data is collected.

---

## Proposed Method and Algorithm

The project will employ the following methods and algorithms:

- **Convolutional Neural Networks (CNNs) or Recurrent Neural Networks (RNNs)**: These widely-used techniques for depth estimation will be explored, leveraging their capability to learn intricate features from images, potentially using architectures like ResNet.

- **Transfer Learning**: Transfer learning will be considered to leverage pre-trained models and adapt them to the project's needs.

- **Ensemble Learning**: Techniques such as ensemble learning will be applied to enhance model performance.

- **Model Optimization**: The model will be quantized, pruned, and compressed to fit on an embedded platform.

---

## Embedded/IoT Platforms

The project will prototype the implementation on the following embedded platforms:

- **Raspberry Pi model 4**: This platform will host the data.
- **Google Coral TPU**: This TPU will serve as the model accelerator.

---

## Evaluation of Results

To evaluate the results, the following methods will be employed:

- **Qualitative Evaluation**: Depth maps will be used to visualize input images alongside a ground truth map for direct comparison. If feasible, predicted depth maps will be augmented on the dashboard of the Go-Kart to visualize the relationship.

- **Quantitative Evaluation**: Various depth estimation metrics, such as Mean Absolute Error and Root Mean Squared Error, will be used to evaluate the model's performance. The accuracies of the model and its real-time inference will also be measured to ensure its suitability as a safety enhancement.

---

## Training and Acknowledgements

Please visit our training and evaluation page [here](https://github.com/Electric-Go-Kart/AudoDepthNet_train)

