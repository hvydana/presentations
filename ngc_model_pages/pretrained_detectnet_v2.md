# TAO Pretrained DetectNet V2
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_detectnet_v2

## Model Name
TAO Pretrained DetectNet V2

## Description/Overview
"DetectNetV2 recognizes the individual objects in an image. This model is ready for commercial use."

## Use Cases
The model is applicable to applications involving:
- Computer Vision (CV)
- Smart Cities/Spaces
- Public Safety
- Retail
- Industrial Inspection
- Smart Infrastructure

## Model Architecture
**Architecture Type:** Convolutional Neural Network (CNN)
**Network Architecture:** DetectNet_v2

The model provides pretrained weights designed as a starting point for transfer learning with DetectNet_v2 object detection networks using the TAO Toolkit.

## Input Format
- **Type:** Image
- **Format:** Red, Green, Blue (RGB)
- **Parameters:** 3D
- **Resolution Range:** Minimum B × 3 × 224 × 224; Maximum B × 3 × 518 × 518

## Output Format
- **Types:** Labels, Bounding-Boxes, Confidence Scores
- **Label Format:** Text Strings
- **Bounding Box:** (x-coordinate, y-coordinate, width, height)
- **Confidence Scores:** Floating Point values

## Training Data
Approximately 400,000 images across thousands of classes from the Google OpenImages Version Three dataset, with validation using roughly 7,000 images. Human verification conducted by Google in-house annotators and crowdsourced verification.

## Evaluation Data
15,000 test images from the Google OpenImages Version Three dataset.

## Supported Hardware
Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures

## Supported Operating Systems
- Linux
- Linux 4 Tegra

## Model Versions Available
resnet10, resnet18, resnet34, resnet50, vgg16, vgg19, googlenet, mobilenet_v1, mobilenet_v2, squeezenet, darknet19, darknet53

## Runtime Requirements
- TAO 5.2
- DeepStream 6.1 or later

## Version Information
**Latest Version:** resnet34
**Updated:** August 19, 2024 UTC
**Compressed Size:** 170.65 MB

## Getting Started Instructions

1. Install NGC CLI from ngc.nvidia.com
2. Configure NGC CLI: `ngc config set`
3. View supported backbones: `ngc registry model list nvidia/tao_pretrained_detectnet_v2:*`
4. Download model: `ngc registry model download-version nvidia/tao_pretrained_detectnet_v2:<template> --dest <path>`
5. Download sample notebooks: `ngc registry resource download-version "nvidia/tao_cv_samples:v1.0.2"`
6. Run Jupyter: `jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root`

## Publisher
NVIDIA

## License Information
The webpage does not display a specific named license or license clause/link for this model. Users should refer to NVIDIA's Terms of Service and the Model Card++ documentation for usage terms.

## Tags
CV, DeepStream, DetectNet_v2, Industrial, Inspection, Metropolis, Public Safety, Retail, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit
