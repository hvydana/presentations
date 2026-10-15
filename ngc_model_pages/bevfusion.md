# BEVFusion for 3D Object Detection
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/bevfusion

## Model Name
BEVFusion for 3D Object Detection

## Description/Overview
"BEVFusion model detects the people within an image and a Lidar with 3D Bounding Boxes, a category label for each object and confidence scores."

## Use Case
The model is designed to estimate an object's 3D bounding box from a single camera and single lidar sensor setup, identifying person objects from RGB images aligned with lidar point cloud data.

## Model Architecture
- **Architecture Type:** Vision Transformer
- **Description:** "transformer-based network archteicture and fuses the lidar and camear features in Bird's-Eye View Feature space to perform 3D object detection"
- **Backbones Used:** Swin-Tiny (Image Backbone); SECOND (LiDAR Backbone)
- **Loss Functions:** Gaussian Focal Loss and L1 Loss
- **Notable Feature:** Supports three angles in 3D space (roll, pitch, yaw) for bounding box representation

## Input Format
- **Types:** Image and Point Cloud
- **Image Format:** Red, Green, Blue (RGB)
- **Image Dimensions:** 1920 x 1080 x 3 (TAO3DSynthetic); 370 x 1224 (KittiPerson)
- **Point Cloud Format:** N x 4 coordinates
- **Additional Requirements:** Calibration matrix (Lidar to Camera Projection Matrix, Camera Intrinsic Matrix)

## Output Format
- **Type:** 3D Bounding Boxes, Category labels, Confidence scores
- **Format:** Images with 3D Bounding Boxes visualization
- **Bounding Box Coordinates:** "(Cetner_x, Cetner_y, Center_z, Scale_x, Scale_y, Scale_z, Rotation_x, Rotation_y, Rotation_z)"

## Training Data
**TAO3DSynthetic Dataset (proprietary):**
- Generated using NVIDIA Omniverse and Isaac-Sim
- 465,373 images and point cloud pairs
- 1,510,704 person class objects
- Nine indoor scenes across five categories:
  - Warehouse: 41,526 images
  - Retail Store: 79,283 images
  - Hospital: 57,182 images
  - Office: 145,940 images
  - Factory: 141,442 images
- Collection method: Synthetic
- Labeling method: Synthetic
- Captured from two feet height with three lighting conditions (Normal, Dark, Very Dark)

**Fine-tuning Data (KittiPerson):**
Based on public KITTI dataset pedestrian class subset: 955 training images with 2,207 person objects; 824 validation images with 2,280 person objects

## Intended Users
Developers and enterprises using NVIDIA hardware and the TAO Toolkit for commercial 3D object detection applications.

## License
**License Name:** NVIDIA Open Model License

**License Link/Clause:** "License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

**Commercial Use Status:** "This model is ready for commercial use."

## Tags/Labels
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit

## Version/Date
- **Latest Version:** bevfusion_1.0
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 464.53 MB

## Download/Getting Started Instructions
"Use the NGC CLI to download:"
(Specific CLI command provided on page, download button labeled "Copied!")

**Runtime/Integration:**
- **Runtime Engine:** TAO 5.5.0
- **Primary Tool:** TAO Toolkit (PyTorch backend)
- **Supported Operating System:** Linux
- **Hardware Compatibility:** All NVIDIA GPUs (Ampere, Blackwell, Jetson, Hopper, Lovelace, Pascal, Turing, Volta)

## Performance Metrics
- **TAO3DSynthetic-BEVFusion:** 79.35% AP40 at IOU 0.5
- **KittiPerson-BEVFusion (From Scratch):** 38.383%
- **KittiPerson-BEVFusion (Fine-tuned):** 53.8747%
