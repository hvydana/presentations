# PeopleSemSegNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplesemsegnet

## Model Name
**PeopleSemSegNet**

## Description
"Semantic segmentation of persons in an image." This model is ready for commercial use and detects persons in images by providing pixel-level classification.

## Use Case
Primary use case involves segmenting people from color (RGB) images in photos and videos. The model performs semantic segmentation rather than instance-based segmentation, making it suitable for applications requiring person identification at the pixel level.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** U-Net
- Two primary variants available:
  - Vanilla UNet Dynamic
  - ShuffleSeg UNet

## Input Specifications
- **Type:** Images (RGB)
- **Format:** Red, Green, Blue (RGB) color
- **Parameters:** 3D input
- **Resolution:** 960 × 544 × 3 (Width × Height × Channels)
- **Properties:** No minimum bit depth, alpha channel, or gamma requirements specified

## Output Specifications
- **Types:** Label text strings and semantic segmentation mask
- **Format:** 2D segmentation mask
- **Categories:** Person or background classification
- Output includes segmentation mask visualization

## Training Data
The proprietary training dataset contains:
- **Total images:** 876,950
- **Total persons annotated:** 8,625,070
- **Environments:** Mixed indoor office, outdoor, varying heights (5ft, 10ft, 20ft)
- **Collection method:** Automatic/Sensors
- **Labeling method:** Human annotation
- **Characteristics:** Multiple camera types, varying crowd density and field-of-view

Training data ground-truth guidelines specify minimum object sizes (height ≥ 10px OR width ≥ 10px @ 1920x1080), occlusion handling (60% visibility threshold), and truncation rules for edge objects.

## Evaluation Data
- **Size:** 50,000 proprietary images
- **Resolution:** 1920×1080 pixels (resized to 960×544)
- **Collection:** Automatic/Sensors across varied environments
- **Labeling:** Human annotation
- **Metric:** Mean Intersection-Over-Union (MIOU)

Performance ranges from 84-95.01 MIOU depending on distance and environment.

## Intended Users
Developers and organizations requiring:
- Video analytics applications
- Person segmentation in surveillance or monitoring systems
- Smart city and smart infrastructure solutions
- Integration with NVIDIA hardware and software ecosystems

## License
Not explicitly stated in the fetched content. The page references "Terms of Use" but does not display specific license clause text.

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning, Ethical AI

## Version and Date
- **Latest Version:** deployable_shuffleseg_unet_onnx_v1.0.1
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 3.73 MB

## Getting Started / Download Instructions

### Using TAO Toolkit
Obtain the TAO Container and reference Jupyter notebooks for retraining with custom datasets. Model configuration templates provided for both Vanilla UNet Dynamic and ShuffleSeg architectures.

### Using DeepStream SDK
1. Download and install DeepStream SDK (version 6.1 or later)
2. Access configuration files from `/opt/nvidia/deepstream` installation directory
3. Required files: configuration text files and labels.txt
4. Convert .etlt models to TensorRT engines using tao-converter with key "tlt_encode"
5. Run segmentation application with appropriate config file

### Model Load Key
"tlt_encode" - Required for all TAO commands

## Software Integration
- **Runtime Engines:** TAO 5.2, DeepStream 6.1 or later
- **Supported Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures
- **Operating Systems:** Linux, Linux 4 Tegra
