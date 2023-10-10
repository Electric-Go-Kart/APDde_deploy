# AutoDepthNet Project

## Team Members
- Spencer Beer, beersc@colostate, 832-925-472
- Kyle Nilsson, kylenils@colostate.edu, 832-230-750

## Problem Statement

LiDAR modules, operating at wavelengths of 905 nanometers (nm) and 1550 nanometers, face challenges such as sensitivity to sunlight's energy spectrum (as depicted in Figure 1) and crosstalk between modules using the 905 nm and 1550 nm spectrum. Addressing these issues, AutoDepthNet aims to leverage cameras and machine learning to predict object depth accurately in front of a vehicle. This innovation is pivotal for enhancing safety and reliability in collision avoidance systems, specifically the Autonomous Pedestrian Detection (APD) model for the Go-Kart senior design project. Moreover, AutoDepthNet potentially offers a cost-effective alternative to expensive LiDAR modules, saving space and weight in automotive design optimizations.

## Relevant Online Resources

- **MiDaS (Monocular Depth Estimation) by Intel:**
  - GitHub Repository: [MiDaS GitHub Repository](https://github.com/intel-isl/MiDaS)
  - This repository provides the MiDaS model for monocular depth estimation, serving as a valuable starting point for our project. Fine-tuning the model based on the Go-Kart dataset is a potential approach.

- **Depth Estimation with Deep Learning by TensorFlow:**
  - GitHub Repository: [TensorFlow Depth Estimation](https://github.com/tensorflow/models/tree/master/research/vid2depth)
  - TensorFlow offers a research repository with implementations of various depth estimation models, including vid2depth. These implementations can provide insights and guide our project.

- **PyTorch3D:**
  - GitHub Repository: [PyTorch3D GitHub Repository](https://github.com/facebookresearch/pytorch3d)
  - PyTorch3D, a library by Facebook, offers efficient, reusable 3D operators for PyTorch, potentially useful if we transition from the 2D to 3D domain.

## Background Papers

1. **Hierarchical Detail Enhancing Mesh-Based Shape Generation with 3D Generative Adversarial Network**
   - Provides context on using unsupervised learning from monocular videos for depth estimation.

2. **Deeper Depth Prediction with Fully Convolutional Residual Networks**
   - Explores the use of deeper convolutional networks for monocular depth estimation and its impact on accuracy.

3. **Digging Into Self-Supervised Monocular Depth Estimation**
   - Discusses self-supervised learning techniques for monocular depth prediction, especially useful for applications with limited labeled data.

## Data Collection

- **Existing Dataset:**
  - Utilizing the KITTI dataset (http://www.cvlibs.net/datasets/kitti/) for training and validation.

- **New Data Collection:**
  - Recording video, images, and LiDAR data during Go-Kart drives to collect new data for our project.

## Proposed Method

We plan to utilize Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) due to their effectiveness in depth estimation and feature extraction. Techniques such as transfer learning and ensemble learning will be employed. The final model will undergo quantization, pruning, and compression to fit on an embedded platform.

## Prototyping Platforms

The data will be hosted on a Raspberry Pi model 4 with a Google Coral TPU serving as the model accelerator.

## Evaluation of Results

- **Qualitative Evaluation:**
  - Visualization of depth maps for input images and ground truth maps for direct comparison.
  - Overlaying predicted depth maps augmented on the Go-Kart dash for better visualization.

- **Quantitative Evaluation:**
  - Depth estimation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
  - Accuracy measurements and real-time inference evaluation to ensure safety enhancement applicability.

We aim to achieve accurate depth prediction, leading to a reliable collision avoidance system, ultimately contributing to the safety and success of the Go-Kart senior design project.
