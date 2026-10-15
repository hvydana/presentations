# OneFormer Research
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/oneformer

## Model Name
OneFormer Research

## Description/Overview
"One Transformer to Rule all Segmentation Tasks or OneFormer is a universal segmentation architecture capable of addressing panoptic, instance, or semantic image segmentation tasks." The model uses a task token to dynamically guide outputs for specific segmentation types during unified training and inference.

## Intended Users
"Computer vision engineers, robotics engineers, and researchers who require a comprehensive and detailed pixel-level understanding of an image."

## Use Cases
The model is designed for:
- Autonomous Systems: Scene understanding for self-driving cars and drones
- Robotic Perception: Object identification and separation for pick-and-place tasks
- Medical Image Analysis: Cell/tumor segmentation and anatomical classification
- Geospatial Analysis: Land use mapping and object detection in satellite imagery
- Computational Photography: AR effects and portrait mode masks

## Model Architecture
The backbone is Swin-L pretrained on ImageNet. Multi-scale features feed into a Pixel Decoder (similar to FPN) generating high-resolution feature maps. A transformer decoder processes multi-scale features and learnable queries, with a task token conditioning the model for specific segmentation tasks. Two parallel prediction heads output class labels and dynamic masks. Model parameters: 223M×10^7

## Input Format
- **Type:** Image (RGB) and Text
- **Image:** 2D RGB format, size divisible by 32
- **Text:** 1D string specifying "semantic/instance/panoptic"

## Output Format
- **Types:** Label (Integer), Mask (RGB), Score (Float)
- **Dimensions:**
  - pred_classes: Batch size × Number of queries
  - pred_masks: Batch size × Number of queries × Height × Width
  - pred_scores: Batch size × Number of queries

## Training Data
**COCO 2017:**
- Training: 118,000 images
- Validation: 5,000 images
- 133 total categories (80 "things," 53 "stuff")
- 1.5+ million annotated instances

**ADE20K:**
- Training: 20,210 images
- Validation: 2,000 images
- 150 semantic categories
- 700,000+ unique instances

## License
"Use of this model is governed by NVIDIA License" and "MIT License" (available via GitHub repository)

## Version & Date
Latest Version: oneformer_coco_pretrained_research
Updated: December 8, 2025 UTC
Compressed Size: 2.65 GB

## Tags
AI, Computer Vision, English, Image Segmentation, Metropolis, Robotics, Smart Cities/Spaces, TAO Toolkit

## Getting Started
Download using NGC CLI. Supported on TAO v6.25.11 with Ampere, Blackwell, Jetson, Hopper, Lovelace, Pascal, Turing, and Volta hardware. Linux operating system preferred.
