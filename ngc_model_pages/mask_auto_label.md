# Mask Auto Label (MAL)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/mask_auto_label

## Model Name
**Mask Auto Label (MAL)** / TAO Pretrained Mask Auto Labeler

## Description/Overview
"Mask Auto-Labeler (MAL) is a high-quality Transformer-based mask auto-labeling framework for instance segmentation using only box annotations." The model generates segmentation masks from box-cropped images as inputs.

## Use Case
The primary application is "weakly supervised instance segmentation and auto-labeling." It's designed for training and fine-tuning via the TAO Toolkit on users' object detection datasets.

## Model Architecture
The instance segmentator accepts RGB images and bounding boxes as inputs to produce segmentation masks. Its backbone is "ViT-MAE-Base that were pre-trained on the ImageNet dataset."

## Input/Output Format

**Input:**
- Image: B X 3 X 512 X 512 (B C H W)
- Label: Bounding box groundtruth in COCO format

**Output:**
- Segmentation mask for each detected object in the input image

## Training Data
"MAL was trained on the COCO 2017 dataset" containing "118K training images and 5K validation images" with bounding boxes for 80 object categories.

## Performance Metrics
Mean Intersection over Union (mIoU) evaluation on COCO 2017 validation dataset:
- mal_vit_base (FP32): 0.788
- mal_fan_base (FP32): 0.782

## Intended Users
Developers using NVIDIA GPUs who work with the TAO Toolkit for custom AI model development.

## License
"NVIDIA Open Model License" — users must accept terms at download.

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version & Date
**trainable_v1.1** (Signed) | Updated: March 23, 2026 | Compressed Size: 1.34 GB

## Getting Started
Access the TAO Container and refer to the experiment spec file template provided in documentation for checkpoint configuration and model architecture parameters.
