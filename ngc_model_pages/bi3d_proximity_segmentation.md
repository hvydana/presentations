# Bi3D Proximity Segmentation
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/bi3d_proximity_segmentation

## Model Name
Bi3D Proximity Segmentation

## Description/Overview
"Bi3D is a network that performs binary depth classification from a stereo camera." It identifies objects closer than a specified distance by classifying them against fronto-parallel planes rather than estimating absolute depth values.

## Use Case
"Bi3D can be used for collision avoidance applications, similar to those used in current industrial autonomous mobile robot (AMR) systems." The model creates safety zones at multiple depths to trigger appropriate robot responses based on object proximity.

## Model Architecture
Bi3D employs two components: a feature extraction model using Spatial Pyramid Pooling and a UNet segmentation model. The architecture includes a ResNet18 encoder with four decoder convolution layers that classify binary depth by matching warped stereo features.

## Input/Output Format

**Input:** Two stereo RGB images at 576 x 960 x 3 resolution and a set of disparity values (e.g., [9, 27, 45])

**Output:** A color-coded map indicating various depth zones detected

## Training Data
The model was trained on "over 1 million synthetically generated object examples in rendered scenes from Omniverse, using Replicator Composer." Training employed binary cross-entropy loss optimization with camera heights randomly varied between 0.3-1.5 meters.

## Intended Users
Developers integrating proximity sensing into autonomous mobile robots, particularly for industrial warehouse and indoor navigation applications.

## License
"License to use this model is covered by the Model EULA. By downloading the public and release version of the model, you accept the terms and conditions of these licenses."

License link: https://developer.download.nvidia.com/licenses/tao_toolkit_21-08_models_eula.pdf

## Tags
- Proximity Segmentation
- Robotics

## Version/Date
**Version:** 2.0.0
**Updated:** August 19, 2024 UTC
**Compressed Size:** 62.98 MB

## Getting Started
Users must download pre-trained ONNX models and convert them to TensorRT engine plans using trtexec. Detailed instructions are available on the Isaac ROS Proximity Segmentation GitHub page: https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_proximity_segmentation
