# CenterPose - ISAAC Ros
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/centerpose_ros

## Model Name
**CenterPose - ISAAC Ros**

## Description/Overview
"CenterPose is a single-stage, keypoint-based method for category-level object pose estimation." It processes unknown object instances within a recognized category using a single RGB image to detect 3D keypoint projections, estimate 6-DoF pose, and regress 3D bounding cuboid dimensions.

## Use Case
Pose detection for retail objects, specifically designed for use with NVIDIA platforms including Jetson and x86_64 with dGPU in ROS 2 inference pipelines.

## Model Architecture
The model supports two backbone options: DLA34 (standard CNN) and FAN-Small-Hybrid (transformer-based). The architecture processes resized and padded RGB images, using the feature extractor combined with an upsampling module to output three prediction heads for 2D bounding box, 3D keypoint projections, and cuboid dimensions.

## Input/Output Format
- **Input:** RGB images resized to 512x512 pixels
- **Output:** 2D bounding box predictions, 3D keypoint projections, and cuboid dimension estimations

## Training Data
Trained on the Objectron dataset comprising:
- 15,000 annotated video clips totaling 4M+ frames
- Cereal Box category: 1,288 training videos (22,024 images)
- Bottle category: 1,542 training videos (26,090 images)
- Frames temporally downsampled to 15 fps from original videos

## Intended Users
Developers building AI applications on NVIDIA platforms for object pose estimation tasks in retail or smart infrastructure contexts.

## License
"NVIDIA Open Model License" - full terms available at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: deployable_bottle_dla34
Updated: November 12, 2024 UTC
Compressed Size: 75.68 MB

## Getting Started Instructions
"To use this model in an inference pipeline in ROS 2, please consult Isaac ROS Pose Estimation" at https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_pose_estimation/tree/main

Models are provided as decrypted ONNX files for inference deployment.
