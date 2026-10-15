# Pre-trained DINO ImageNet Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_dino_imagenet

## Model Name
**Pre-trained DINO ImageNet weights**

## Description/Overview
"Pre-trained DINO weights trained on ImageNet to facilitate transfer learning using TAO Toolkit." These are backbone models for the DINO object detection network within NVIDIA's Train Adapt Optimize (TAO) Toolkit.

## Use Case
Object detection applications that recognize individual objects in images and place bounding boxes around them. Suitable for deployment in "smart cities, retail, healthcare, industrial inspection, and more."

## Model Architecture
Supported backbones include:
- resnet_50
- GCViT variants (xxtiny through large)
- FAN (Fully Attentional Networks) hybrid variants

## Input/Output Format
Not explicitly specified in the documentation provided.

## Training Data
Models trained on ImageNet-1K or ImageNet-22K datasets, with some variants fine-tuned on ImageNet-1K after initial ImageNet-22K pre-training.

## Intended Users
Developers using NVIDIA TAO Toolkit for transfer learning and custom AI model development.

## License
**Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)**

"This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)." Full license available at: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
**Latest Version:** gcvit_large_imagenet22k_384
**Updated:** October 16, 2023 UTC
**Compressed Size:** 824.03 MB

## Getting Started Instructions
Users should reference the TAO Toolkit experiment spec file template provided in the documentation, configuring the pretrained_backbone_path, backbone type, and training parameters accordingly.
