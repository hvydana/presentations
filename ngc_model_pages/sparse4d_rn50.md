# Sparse4D (ResNet-50)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/sparse4d_rn50

## Description/Overview
"TAO Sparse4D is an advanced three-dimensional (3D) multi-camera detection and tracking network." The model generates precise 3D bounding boxes and tracking IDs for diverse objects across multiple camera views. It was pre-trained on the Multi-Target Multi-Camera (MTMC) Tracking 2025 subset from the NVIDIA PhysicalAI-SmartSpaces dataset and is ready for commercial use.

## Use Case
"TAO Sparse4D is designed for 3D multi-camera object detection and tracking in indoor environments like warehouses and logistics facilities." Applications include warehouse automation, safety optimization, and workflow improvements in industrial settings.

## Model Architecture
- **Type:** Convolution Neural Network (CNN) based backbone with Transformer decoder layers
- **Backbone:** ResNet-50 (lower latency variant; ResNet-101 also available)
- **Key Components:** Feature Pyramid Network (FPN), Multi-Scale Deformable Aggregation blocks, refinement and classification layers, Instance Bank module
- **Parameters:** 7.8 x 10^7 parameters
- The ResNet-50 variant "is built on top of an RT-DETR R50 pre-training initialization for stronger image features"

## Input Format
- **Type:** RGB images with camera calibration files and 3D ground truth bounding boxes
- **Resolution:** 3 x 1080 x 1920 (Channels x Height x Width); processed at 540 x 960
- **Format:** PNG/JPG/HDF5; optional depth maps in PNG/HDF5
- **Structure:** Data organized into Bird's Eye View (BEV) groups containing multiple synchronized cameras

**Key Input Tensors:**
- `img`: (B, N, 3, 540, 960) - image tensor
- `projection_mat`: (B, N, 4, 4) - projection matrices
- `image_wh`: (B, N, 2) - image dimensions
- `input_cached_feature`: (B, 600, 256) - cached features for temporal consistency
- `input_cached_anchor`: (B, 600, 11) - cached anchor points

## Output Format
**Output Type:** List of tensors per batch element containing:
- `boxes_3d`: (B, M, 10) - 3D boxes as "(x, y, z, width, length, height, yaw, velocity_x, velocity_y, velocity_z)" in world coordinates
- `scores_3d`: (B, M) - object confidence scores
- `labels_3d`: (B, M) - class labels
- `cls_scores`: (B, M) - classification scores
- `instance_ids`: (B, M) - tracking IDs
- `instance_feats`: (B, M, 256) - instance features

Coordinates are in meters; yaw is in radians; velocity in m/s.

## Training Data
- **Primary Dataset:** MTMC Tracking 2025 subset from NVIDIA PhysicalAI-SmartSpaces (HuggingFace)
- **Composition:** 80% synthetic data from NVIDIA Isaac Sim Replicator; 20% COSMOS-augmented real data
- **Scale:** 1 Million to 1 Billion images
- **Scenes:** 90 training scenes with 3,469 BEV groups
- **Classes Trained:** Person, Fourier_GR1_T2_Humanoid, Agility_Digit_Humanoid, Nova_Carter, Transporter, Forklift, Pallet_Truck
- **Data Split:** Training 80%, Testing 10%, Validation 10%
- **Collection Period:** 2024-2025

## Performance Metrics (v2.2 ResNet-50)
Average HOTA: 50.99
- Person: 53.93 HOTA
- Fourier_GR1_T2_Humanoid: 59.31 HOTA
- Agility_Digit_Humanoid: 52.69 HOTA
- Nova_Carter: 58.26 HOTA
- Transporter: 33.70 HOTA
- Forklift: 48.05 HOTA

## Intended Users
Developers and organizations building warehouse automation, industrial monitoring, and logistics optimization systems requiring multi-camera 3D detection and tracking capabilities.

## License
**Name:** NVIDIA Open Model License

**Link/Text:** "Use of this model is governed by the NVIDIA Open Model License" at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
- Computer Vision
- CV
- Deep Learning
- Multi-Camera Network
- Object Detection and Tracking in 3D
- TAO
- TAO Toolkit

## Version & Date
- **Latest Version:** trainable_v2.2 (ResNet-50)
- **Release Date:** May 12, 2026
- **Compressed Size:** 548.27 MB
- **Updated:** May 29, 2026 UTC

## Getting Started / Download Instructions

Use the NGC CLI to download:
```
ngc registry model download-version nvidia/tao/sparse4d_rn50:trainable_v2.2
```

**Available Versions:**
- `trainable_v2.2` - Pre-trained model for fine-tuning
- `deployable_v2.2` - Model optimized for DeepStream or TensorRT deployment

**Documentation:** Refer to the TAO Toolkit User Guide and Nvidia Video Search and Summarization (VSS) - Warehouse Blueprint release documentation for detailed usage and deployment instructions.

**Runtime Support:**
- DeepStream 7.1
- TAO 6.1.0
- TensorRT acceleration
- Compatible with NVIDIA Ampere, Lovelace, Hopper, and Blackwell architectures
- Linux operating system required
