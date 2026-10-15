# PointPillarNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pointpillarnet

## Description/Overview
"Model to detect one or more objects from a LIDAR point cloud file and return 3D bounding boxes." This model is ready for commercial use.

## Use Case
The primary intended use case is detecting objects in point cloud files, particularly for autonomous vehicle and smart infrastructure applications involving LIDAR data analysis.

## Model Architecture
- **Architecture Type:** Convolution Neural Network (CNN)
- **Network Architecture:** PointPillars Architecture

## Input Format
- **Input Type:** Point Cloud File
- **Input Format:** LIDAR
- **Input Parameters:** Points (shape N, P, 4 where N is batch size, P is maximum points, 4 is features per point) and Num_Points (shape N)

## Output Format
"Label: Text String(s); Bounding Box: (x-coordinate, y-coordinate, z-coordinate, width, height, depth), Confidence Scores: Floating Point"

**Category Labels:** Vehicle, Pedestrian, Cyclist

## Training Data
"7481 training images of 80,256 labeled objects from a proprietary LIDAR point cloud dataset of vehicles, pedestrians, and cyclists" collected by solid state LIDAR with human labeling.

## Evaluation Performance
- **trainable model:** 65.2167% mAP BEV / 51.7159% mAP 3D
- **deployable model:** 66.6860% mAP BEV / 52.8530% mAP 3D

## Intended Users
Developers using NVIDIA Hardware and Software who need to deploy object detection on point clouds via TAO Toolkit or TensorRT on NVIDIA GPUs or Jetson devices.

## License
No specific license name or clause is provided in the fetched content.

## Tags
AI, Computer Vision, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO Toolkit, Transfer Learning

## Version/Date
**Latest Version:** deployable_v1.1 (Signed)
**Updated:** November 27, 2024 UTC
**Compressed Size:** 5.31 MB

## Getting Started Instructions

Two model types are provided:
- `pointpillars_trainable.tlt` - for training and fine-tuning with TAO Toolkit
- `pointpillars_deployable.etlt` - for deployment using TensorRT

**Model Load Key:** `tlt_encode`

**For TAO Toolkit:** Set `PRETRAINED_MODEL_PATH: "/path/to/the/model.tlt"` in the OPTIMIZATION config component.

**For TensorRT Deployment:** Requires TensorRT 8.2 and TensorRT OSS 22.02. Generate engine using tao-converter, then run the C++ sample from the tao_toolkit_recipes repository.

## Download
Use the NGC CLI to download from the NVIDIA NGC Catalog at: https://ngc.nvidia.com/catalog/models/nvidia:tao:pointpillarnet
