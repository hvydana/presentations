# Pre-trained Deformable DETR ImageNet Weights
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_deformable_detr_imagenet

## Model Name
**Pre-trained Deformable DETR ImageNet weights**

## Description/Overview
"Pre-trained deformable_detr weights trained on ImageNet to facilitate transfer learning using TAO Toolkit." These are backbone weights designed for use with the Deformable-DETR object detection network within NVIDIA's Train Adapt Optimize (TAO) Toolkit ecosystem.

## Use Case
Object detection applications that recognize individual objects in images and place bounding boxes around them. Suitable for smart cities, retail, healthcare, industrial inspection, and related computer vision tasks requiring transfer learning approaches.

## Model Architecture
The model supports multiple GCViT (Gated Convolutional Vision Transformer) backbone variants:
- gc_vit_xxtiny
- gc_vit_xtiny
- gc_vit_tiny
- gc_vit_small
- gc_vit_base
- gc_vit_large
- gc_vit_large_384

Also supports resnet_50 backbone.

## Model Versions Available
- gcvit_xxtiny_imagenet1k
- gcvit_xtiny_imagenet1k
- gcvit_tiny_imagenet1k
- gcvit_small_imagenet1k
- gcvit_base_imagenet1k (latest)
- gcvit_large_imagenet1k
- gcvit_large_imagenet22k_384

## Training Data
ImageNet-1K and ImageNet-22K datasets

## Input/Output Format
Experiment spec configuration requiring `model` and `train` components. Example template provided for integration with TAO Toolkit workflows.

## Intended Users
Developers and AI practitioners using NVIDIA TAO Toolkit for customizing pre-trained models with their own datasets.

## License
"Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)" with link to [full license text](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit

## Version/Date
Latest Version: gcvit_base_imagenet1k | Updated: October 16, 2023 UTC | Compressed Size: 350.51 MB

## Download Instructions
Use NGC CLI with provided download command available on the model page at NVIDIA NGC Catalog.
