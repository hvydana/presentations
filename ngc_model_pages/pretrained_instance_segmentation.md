# TAO Pretrained Instance Segmentation
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_instance_segmentation

## Description/Overview
"The Instance Segmentation model identifies each instance of multiple objects in a frame at the pixel level. This model is ready for commercial use."

Instance segmentation is a computer vision technique that produces both bounding boxes and segmentation masks for detected objects at the pixel level.

## Use Cases
- Public Safety
- Smart Cities / Spaces
- Smart Infrastructure
- Retail
- Robotics
- Inspection

## Model Architecture
- **Architecture Type:** MaskRCNN
- **Network Architecture:** ResNet
- **Supported Backbones:** resnet10, resnet18, resnet34, resnet50, resnet101

## Input Format
- **Type:** Image (RGB)
- **Dimensions:** 3D
- **Resolution Range:** Minimum B X 3 X 224 X 224; Maximum B X 3 X 518 X 518

## Output Format
- **Types:** Labels, Bounding Boxes, Segmentation Masks
- **Label Format:** Text strings
- **Bounding Box Format:** (x-coordinate, y-coordinate, width, height)
- **Segmentation Mask:** 2D format with confidence scores

## Training Data
"Roughly 400,000 images and 7,000 validation images across thousands of classes" from the Google OpenImages Version Three dataset, with approximately 15,000 test images used for evaluation.

## Supported Hardware & Software
- **Runtime:** TAO 5.2, DeepStream 6.1
- **Hardware:** Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta
- **Operating Systems:** Linux, Linux 4 Tegra

## Intended Users
Developers using NVIDIA TAO Toolkit for transfer learning on instance segmentation tasks.

## License
Not explicitly stated in fetched content.

## Tags
CV, DeepStream, Inspection, Instance Segmentation, MaskRCNN, Metropolis, Public Safety, Retail, Robotics, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit

## Version & Date
**Latest Version:** resnet10
**Updated:** August 19, 2024 UTC
**Compressed Size:** 38.31 MB

## Getting Started Instructions

1. Install NGC CLI from `ngc.nvidia.com`
2. Configure NGC CLI: `ngc config set`
3. List supported backbones: `ngc registry model list nvidia/tao/pretrained_instance_segmentation:*`
4. Download model: `ngc registry model download-version nvidia/tao/pretrained_instance_segmentation:<template> --dest <path>`
5. Download sample notebooks: `ngc registry resource download-version "nvidia/tao_cv_samples:v1.0.2"`
6. Run Jupyter: `jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root`

For detailed TAO documentation, visit: https://docs.nvidia.com/tao/tao-toolkit/index.html
