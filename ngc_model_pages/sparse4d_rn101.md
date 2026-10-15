# Sparse4D (ResNet-101)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/sparse4d_rn101

## Description/Overview
TAO Sparse4D is "an advanced three-dimensional (3D) multi-camera detection and tracking network." It generates precise 3D bounding boxes and tracking IDs for diverse objects across multiple camera views. The model was developed by NVIDIA as part of the TAO model family and is pre-trained on the Multi-Target Multi-Camera (MTMC) Tracking 2025 subset from the NVIDIA PhysicalAI-SmartSpaces dataset.

## Use Case
"TAO Sparse4D is designed for 3D multi-camera object detection and tracking in indoor environments like warehouses and logistics facilities." Applications include warehouse automation, safety monitoring, and workflow optimization with spatial scene understanding.

## Model Architecture
- **Type**: Convolution Neural Network (CNN) backbone with Transformer-based decoder layers
- **Backbone**: ResNet101 with Transformer decoder layers
- **Parameters**: 7.8 x 10^7 parameters
- **Key Components**: Feature Pyramid Network (FPN), Multi-Scale Deformable Aggregation blocks, refinement and classification layers, and Instance Bank module for tracking ID assignment

## Input Format
- **Type**: RGB images from multiple cameras with calibration files
- **Shape**: (B, N, C, H, W) where standard is (1, N, 3, 540, 960)
- **Additional inputs**: Projection matrices, image dimensions, cached features and anchors from previous frames
- **Optional**: Depth maps in PNG/HDF5 format

## Output Format
List of tensors per batch item containing:
- **boxes_3d**: 3D coordinates (x, y, z), dimensions (width, length, height), yaw angle, and velocity vector
- **scores_3d**: Object confidence scores
- **labels_3d**: Class labels
- **instance_ids**: Tracking IDs
- **instance_feats**: High-dimensional semantic features (256-dimensional)

## Training Data
- **Primary dataset**: MTMC Tracking 2025 from NVIDIA PhysicalAI-SmartSpaces
- **Data composition**: "80% of the overall data used for training was synthetic data collected from NVIDIA Isaac Sim Replicator"
- **Size**: 1 Million to 1 Billion Images
- **Classes trained**: Person, Fourier_GR1_T2_Humanoid, Agility_Digit_Humanoid, Nova_Carter, Transporter, Forklift
- **Data split**: Training 80%, Testing 10%, Validation 10%
- **Augmentation**: NVIDIA COSMOS-augmented versions for improved diversity

## Intended Users
Organizations implementing warehouse automation, logistics monitoring, and indoor multi-camera surveillance systems requiring 3D object detection and tracking capabilities.

## License
**Name**: NVIDIA Open Model License

**Clause/Link**: "Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

## Tags
- Computer Vision
- CV
- Deep Learning
- Multi-Camera Network
- Object Detection and Tracking in 3D
- TAO
- TAO Toolkit

## Version & Date
- **Latest**: trainable_v2.2 (ResNet101)
- **Release date**: May 12, 2026 via NGC
- **Updated**: May 29, 2026 UTC

## Getting Started / Download
Use the NGC CLI with command provided on the model page. For deployment, refer to NVIDIA Video Search and Summarization (VSS) - Warehouse Blueprint documentation. The model is compatible with DeepStream 7.1 and TAO Toolkit 6.1.0, running on NVIDIA Blackwell, Hopper, Lovelace, and Ampere architectures.
