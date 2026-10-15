# SyntheticaDETR
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/models/synthetica_detr

## Description/Overview
"SytheticaDETR is a real-time object detection model based on a transformer architecture trained entirely in simulation and works on real images zero-shot." The model represents an efficient real-time object detection transformer inspired by RT-DETR, designed to accept RGB images as input and produce 2D bounding boxes with detection confidence scores. It is named for its completely synthetic training dataset and achieves detection accuracies exceeding models trained with real data included.

## Use Cases
The model supports multiple deployment scenarios including:
- Robotic arm manipulation tasks
- Autonomous robot navigation
- Target tracking in delivery robots
- Robot grasping applications
- Autonomous Mobile Robot (AMR) operations

## Model Architecture
The pipeline consists of four modules: "A backbone module, an efficient hybrid encoder, a query selector and a decoder head." Two backbone architectures are assessed: ConvNeXt-small and ResNet-50. The backbone extracts multi-scale image features, the encoder tokenizes these into embeddings using attention mechanisms, the query selector identifies important image features as initial object queries, and the decoder iteratively optimizes queries to generate bounding boxes and confidence scores. Confidence thresholds are set at 0.9 for grasp objects and 0.7 for non-grasp objects.

## Input/Output Format
**Input:** RGB images at 640x640 resolution

**Output:** 2D bounding boxes with associated detection confidence scores for detected objects

## Training Data
The model was trained on "13 million SDG image samples using Isaac Sim Replicator" with procedurally generated scenes featuring random domain parameters. Training assets sourced from YCB-V datasets, Google Scanned Objects (GSO), random 3D assets, and custom grocery assets. Two separate models were trained: one for grasping objects and one for non-grasp commercial applications (AMR objects).

## Key Performance Indicators
**Mean Average Precision (mAP) and Mean Average Recall (mAR)** are the standard metrics used. On YCB-V BOP benchmark at 640x480 resolution:
- Synthetic training only: mAP 0.839, mAR 0.860
- Synthetic and real training: mAP 0.885, mAR 0.903

**Inference Performance** (FP16 precision):
- Jetson Orin: 86.1 FPS (ResNet50), 31.7 FPS (ConvNeXt-small)
- RTX 4060Ti: 278.2 FPS (ResNet50), 104.5 FPS (ConvNeXt-small)
- RTX 4090: 540.5 FPS (ResNet50), 219.7 FPS (ConvNeXt-small)

## Intended Users
Organizations deploying object detection for robotic systems, autonomous vehicles, warehouse automation, and industrial applications on NVIDIA hardware platforms.

## Technical Requirements
"The model is intended to be run using NVIDIA hardware and software...The model is intended for Ubuntu 22.04 with CUDA 11.6 or Jetpack 6.0 DP and later. This model can only be used with TensorRT." Models must be converted from .etlt files to TensorRT engine plans using TAO Toolkit with encryption key "sdetr".

## Available Models
- **sdetr_grasp.etlt** - trained for graspable objects
- **sdetr_amr.etlt** - trained for non-grasp (AMR) objects

## Conversion Instructions
```
./tao-converter -k sdetr -t fp16 -e sdetr_grasp.plan -p images,1x3x640x640,2x3x640x640,4x3x640x640 -p orig_target_sizes,1x2,2x2,4x2  sdetr_grasp.etlt

./tao-converter -k sdetr -t fp16 -e sdetr_amr.plan -p images,1x3x640x640,2x3x640x640,4x3x640x640 -p orig_target_sizes,1x2,2x2,4x2  sdetr_amr.etlt
```

## ROS 2 Integration
The model integrates with NVIDIA's Isaac ROS RT-DETR package, which includes preprocessing and postprocessing for standard ROS message formats.

## License
No explicit license name or clause is provided on this NGC model page. Users should consult NVIDIA's Terms of Use and model-specific licensing documentation.

## Tags
AI, Computer Vision, CUDA, Object Detection, Robotics, Machine Learning, PyTorch, TAO Toolkit, TensorRT

## Version & Date
**Version:** 1.0.0
**Updated:** December 3, 2024 UTC
**Compressed Size:** 322.68 MB

## Publisher
NVIDIA
