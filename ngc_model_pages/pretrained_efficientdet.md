# TAO Pretrained EfficientDet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_efficientdet

## Model Name
TAO Pretrained EfficientDet

## Description
"EfficientDet recognizes the individual objects in an image. This model is ready for commercial use."

## Use Case
Object detection for identifying and localizing individual objects within images across various applications including video analytics and smart city solutions.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** EfficientNet-based feature extractors
- **Backbone Versions Available:**
  - efficientnet-b0
  - efficientnet-b1
  - efficientnet-b2 (latest)
  - efficientnet-b3
  - efficientnet-b4
  - efficientnet-b5

## Input/Output Format

**Input:**
- Type: Image
- Format: RGB (Red, Green, Blue)
- Resolution: 224 × 224 × 3 (Width × Height × Channels)

**Output:**
- Labels as text strings
- Bounding boxes as (x-coordinate, y-coordinate, width, height)
- Confidence scores as floating-point values

## Training Data
Approximately 400,000 training images and 7,000 validation images from the Google OpenImages Version Three (3) dataset across thousands of object classes. Annotations primarily performed by Google in-house teams with supplementary crowdsourced verification.

## Evaluation Data
"15,000 test images from Google OpenImages Version Three (3) dataset."

## Intended Users
Developers and organizations using NVIDIA TAO Toolkit for transfer learning and custom object detection model development.

## License
The webpage does not specify an explicit license name or clause. Users should review NVIDIA's standard terms of service referenced on the page.

## Tags
- AI
- CV (Computer Vision)
- DeepStream
- Metropolis
- Smart Cities/Spaces
- Smart Infrastructure
- TAO Toolkit
- Transfer Learning

## Version/Date
- **Latest Version:** efficientnet_b2
- **Updated:** August 19, 2024 UTC
- **Compressed Size:** 61.86 MB

## Getting Started Instructions

1. Install NGC CLI from ngc.nvidia.com
2. Configure NGC CLI: `ngc config set`
3. List supported backbones: `ngc registry model list nvidia/tao/pretrained_efficientdet:*`
4. Download model: `ngc registry model download-version nvidia/tao/pretrained_efficientdet:<template> --dest <path>`

## Technical Requirements
- **Runtime Engine:** TensorRT
- **Supported Platforms:** DeepStream 6.1 or later; TAO 5.2
- **Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing architectures
- **Operating Systems:** Linux, Linux 4 Tegra
