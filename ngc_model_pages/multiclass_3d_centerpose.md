# Multiple 3D CenterPose
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/multiclass_3d_centerpose

## Model Name
**Multiple 3D CenterPose**

## Description/Overview
"The Multi-category CenterPose model detects the projections of Three-Dimensional (3D) key points, estimates a 6-Degree of Freedom (DOF) pose, and creates a 3D bounding box. This model is ready for commercial use."

## Use Case
The model is designed for estimating an object's pose from single RGB images. It identifies objects and provides their spatial orientation and dimensions.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN) and transformer-based
- **Backbone Options:** DLA34 (standard CNN) or FAN-Small-Hybrid (transformer-based)
- The network processes rescaled, padded RGB images and outputs predictions for 3D bounding box keypoints and cuboid dimensions

## Input Format
- **Type:** RGB Images
- **Dimensions:** 512 × 512 × 3 (Width × Height × Channels)
- **Channel Ordering:** NCHW (Batch Size, 3 channels, 512 height, 512 width)

## Output Format
- 9 Three-Dimensional (3D) Bounding Box Vertices with x, y, z coordinates
- Cuboid Dimensions (X-scale, Y-scale, Z-scale)
- 6-DoF pose estimation as floating-point values

## Training Data
"Trained on a dataset comprised of 15,000 annotated video clips, totaling over 4M annotated frames." Objects span eight categories: bikes, books, bottles, cameras, cereal boxes, chairs, laptops, and shoes.

**Dataset breakdown:**
- Training: 185,462 images across 8 categories
- Testing: 46,290 images
- Collection method: Automatic/Sensors
- Labeling method: Human annotated

## Intended Users
Developers using NVIDIA hardware and software frameworks, including those deploying on Jetson devices, leveraging TAO Toolkit, or using TensorRT for inference.

## License
**License Name:** NVIDIA Open Model License

**License Clause/Link:** "License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

## Tags
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit

## Version/Date
- **Latest Version:** deployable_dla34
- **Updated:** November 12, 2024 UTC
- **Compressed Size:** 70.16 MB

## Download/Getting Started Instructions

**Deployment with TAO-Deploy:**
- Convert pretrained ONNX models to TRT engine using TensorRT
- Configure intrinsic camera matrix in experiment spec file
- Run TAO-Deploy inference pipeline
- Note: FAN-Small-Hybrid requires TensorRT version ≥ 8.6 for FP16 support

**Deployment with Triton Inference Server:**
Refer to [TAO Triton apps](https://github.com/NVIDIA-AI-IOT/tao-toolkit-triton-apps) for end-to-end inference deployment.

**Use the NGC CLI to download:** (Command available on NGC platform)
