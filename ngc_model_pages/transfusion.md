# Transfusion for 3D Object Detection
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/transfusion

## Description/Overview
"The model described in this card detects the people within an image and a Lidar with 3D bounding boxes. It also provides a category label for each object."

## Use Case
Detection of people in indoor environments using multimodal sensor fusion from RGB images and LiDAR point clouds.

## Model Architecture
The architecture is based on BEVFusion, which combines feature representations from different modalities (LiDAR and image) into a unified representation suitable for 3D object detection tasks.

## Training Details
The BEVFusion codebase from mmdet3d was modified to support three rotation angles in 3D space (roll, pitch, yaw), whereas the original supported only yaw. The network optimization uses Gaussian Focal Loss and L1 Loss.

### Training Dataset
A proprietary synthetic dataset generated with Omniverse and Isaac-Sim containing:
- 465,373 image-point cloud pairs
- 1,510,704 objects (person class)
- Nine indoor scenes (warehouse, retail, hospital, office, factory)
- Three lighting conditions per scene (normal, dark, very dark)
- Data captured from two feet height with perpendicular sensor placement

## Input Format
- RGB Image: 1920 x 1080 x 3
- LiDAR Point Cloud: N x 4 (xyz coordinates plus intensity)
- Calibration matrices (LiDAR-to-camera projection, camera intrinsics)

## Output Format
Category labels (people) and "3D bounding-box coordinates in nine dimension representation (center_x, center_y, center_z, scale_x, scale_y, scale_z, rotation_x, rotation_y, rotation_z)"

## Performance
KITTI 3D Metric evaluation at IOU 0.5:
- AP11: 77.71%
- AP40: 79.35%

## Intended Users
Developers building computer vision and 3D object detection applications using NVIDIA TAO Toolkit.

## License
"License to use these models is covered by the Model EULA. By downloading the model, you accept the terms and conditions of these licenses" - Link provided: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
Computer Vision, CV, Deep Learning, Industrial Inspection, Optical Inspection, TAO, TAO Toolkit, NSPECT-K61X-1669

## Version & Date
- Version: v1.0
- Updated: November 27, 2024 UTC
- Compressed Size: 425.05 MB

## Getting Started
Access through NVIDIA NGC Catalog using NGC CLI. Documentation available at: https://docs.nvidia.com/tao/tao-toolkit/index.html
