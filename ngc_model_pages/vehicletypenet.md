# VehicleTypeNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/vehicletypenet

## Description/Overview
"Resnet18 model to classify a car crop into 1 out 6 car types." The model categorizes vehicle images into six classes: coupe, sedan, SUV, van, large vehicle, and truck. "This model is ready for commercial use."

## Use Case
Vehicle type classification for video analytics applications, typically deployed as a secondary classifier following primary object detection in traffic monitoring and smart cities scenarios.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** ResNet18
- "This is a classification model with a Resnet18 backbone."

## Input Format
- **Type:** Images in Red, Green, Blue (RGB) format
- **Dimensions:** 224 x 224 x 3 (W x H x C)
- **Channel Ordering:** NCHW (N = Batch Size, C = 3 channels, H = 224, W = 224)
- **Mean Subtraction:** [103.939, 116.779, 123.68]

## Output Format
- **Type:** Label (Text String)
- **Classes:** coupe, sedan, SUV, van, large vehicle, truck
- **Tensor Shape:** 1x6 class confidence tensor

## Training Data
"VehicleTypeNet was trained on a proprietary dataset with more than 60K car images." The dataset includes "car crops from a mix of camera heights, camera angles, field-of view (FOV) and occlusions."

## Evaluation Data
"3000 images from an internal, private dataset of cars with a mix of camera heights, camera angles, field-of view (FOV) and occlusions represented."

### Performance Metrics
**Top-1 Accuracy on Evaluation Set:** 88%

## Intended Users
Developers using NVIDIA hardware and software platforms who need vehicle type classification capabilities for video analytics applications.

## License
No specific license name or clause is provided in the document. The model is available through NVIDIA NGC with "NVIDIA AI Enterprise Supported" designation.

## Version/Date
- **Latest Version:** pruned_onnx_v1.1.0 (Signed)
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 18.97 MB

## Available Model Versions
- unpruned_v1.0
- pruned_v1.0
- pruned_v1.0.1
- pruned_v1.0.2
- pruned_onnx_v1.1.0

## Getting Started/Download Instructions

### NGC CLI Download
"Use the NGC CLI to download:" (specific command provided but requires NGC account setup)

### Deployment with DeepStream
1. Download model files:
```
mkdir -p $HOME/vehicletypenet && \
wget https://api.ngc.nvidia.com/v2/models/nvidia/tao/vehicletypenet/versions/pruned_v1.0/files/resnet18_vehicletypenet_pruned.etlt\
-O $HOME/vehicletypenet/resnet18_vehicletypenet_pruned.etlt && \
wget https://api.ngc.nvidia.com/v2/models/nvidia/tao/vehicletypenet/versions/pruned_v1.0/files/vehicletypenet_int8.txt \
-O $HOME/vehicletypenet/vehicletypenet_int8.txt
```

2. Run with DeepStream Docker container or local installation

### Model Load Key
"The `unpruned` and `pruned` models are encrypted and will only operate with the following key: Model load key: `tlt_encode`"

## Software Integration
- **Runtime Engines:** TAO 5.1, DeepStream 6.1 or later
- **Supported Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing
- **Operating Systems:** Linux, Linux 4 Tegra

## Tags
CV, DeepStream, Metropolis, NVIDIA AI, Object Detection, Public Safety, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, Traffic, Vehicle Classification
