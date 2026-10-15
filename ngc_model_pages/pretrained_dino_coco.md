# DINO Model Card (Pretrained DINO COCO)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_dino_coco

## Model Name
**DINO** (DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection)

## Description/Overview
"Object detection is a popular computer vision technique that can detect one or multiple objects in a frame." The DINO model detects objects in images and places bounding boxes around them. It was trained on the COCO dataset to facilitate transfer learning through the TAO Toolkit.

## Use Case
Primary use case involves "detecting objects in a color (RGB) image. The model can be used to detect objects from photos and videos." Applications span smart cities, retail, healthcare, and industrial inspection.

## Model Architecture
The model offers four backbone options:
- ResNet50
- GCViT-Tiny
- FAN-Small
- FAN-Large

"The backbone networks are classification networks that were pre-trained on the ImageNet1K dataset--except for FAN-Large, which was pre-trained on the ImageNet22K dataset."

## Input/Output Format
**Input:** B X 3 X 544 X 960 (B C H W)
**Output:** "Category labels (80 COCO) and bounding-box coordinates for each detected objects"

## Training Data
"DINO was trained on the COCO 2017 dataset, which contains 118K training images and 5K validation images." The dataset includes "bounding boxes for 80 object categories."

## Intended Users
Models require "NVIDIA Hardware and Software" and can only be used with "Train Adapt Optimize (TAO) Toolkit, DeepStream SDK or TensorRT." Developers using TAO for transfer learning or DeepStream for edge deployment.

## License
Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)
[https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
Latest Version: **dino_fan_large_trainable_v1.0**
Updated: February 3, 2024 UTC
Compressed Size: 1.12 GB

## Available Model Variants
- dino_resnet_50_trainable_v1.0 / deployable_v1.0
- dino_gc_vit_tiny_trainable_v1.0 / deployable_v1.0
- dino_fan_small_trainable_v1.0 / deployable_v1.0
- dino_fan_large_trainable_v1.0 / deployable_v1.0

## Getting Started
Download via NGC CLI or access through the TAO Container. "A Jupyter notebook is available as a part of the TAO container and can be used to re-train." Refer to TAO Toolkit documentation at [https://docs.nvidia.com/tao/tao-toolkit/index.html](https://docs.nvidia.com/tao/tao-toolkit/index.html)
