# NVOneFormer Commercial
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/oneformer_its_pretrained_commercial

## Model Name
**NVOneFormer Commercial**

## Description/Overview
"One Transformer to Rule all Segmentation Tasks or OneFormer is a universal segmentation architecture capable of addressing panoptic, instance, or semantic image segmentation tasks." The model employs a task token to dynamically guide predictions by conditioning the architecture on the desired segmentation type during unified training and inference. This model is ready for commercial use.

## Intended Users
Computer vision engineers, robotics engineers, and researchers requiring pixel-level image understanding.

## Use Cases
- Autonomous Systems: Scene understanding for self-driving cars or drones
- Robotic Perception: Object identification and "pick-and-place" tasks
- Medical Image Analysis: Cell/tumor segmentation and anatomical classification
- Geospatial Analysis: Land use mapping and object detection in satellite imagery
- Computational Photography: AR effects and portrait mode features

## Model Architecture

**Architecture Type:** Unified segmentor accepting RGB images and generating segmentation masks with associated labels.

**Network Components:**
- Backbone: DiNaT-L feature extractor trained on NVImageNet with commercial licensing
- Pixel Decoder: FPN-similar multi-scale feature map generation
- Transformer Decoder: Processes multi-scale features and learnable queries
- Task Token: Learnable token conditioning model for specific segmentation tasks
- Prediction Heads: Classification head (linear/MLP) and mask head (MLP)

**Parameters:** 230×10^7

## Input Format
- **Type:** Image and Text
- **Image:** RGB, 2D format; "image size should be divisible by 32"
- **Text:** 1D string; "should state 'This task is semantic/instance/panoptic'"

## Output Format
- **Types:** Label, Mask, Score per detected object
- **Label:** Integer, 1D
- **Mask:** RGB, 2D
- **Score:** Float, 1D
- **Structure:** pred_classes (Batch × Queries), pred_masks (Batch × Queries × Height × Width), pred_scores (Batch × Queries)

## Training Data

**Datasets Used:**
1. **NV-ImageNet:** 5,458,059 images across 1,000 classes; commercially licensed from 84 websites
2. **OpenImagesv5 Subset:** 670,612 training images with 133 categories (80 "Thing," 53 "Stuff")
3. **MSCOCO 2017 Subset:** Validation set included
4. **ITS:** 227,763 training images, 5,404 validation images across 4 categories (person, car, bicycle, road_sign)

**Data Augmentation:** Random horizontal flipping (50% probability) and photometric jitter (brightness, contrast, saturation adjustment).

## License
**License Type:** NVIDIA proprietary

**Governing Terms:** "Use of this model is governed by the NVIDIA Open Model Agreement"

**License Link:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/

## Tags/Labels
- Automotive / Transportation
- Computer Vision
- Image Segmentation
- Smart Cities / Spaces
- TAO Toolkit

## Version & Date
- **Version:** v1.0
- **Latest Version Name:** oneformer_pretrained_commercial_dinat_its
- **Updated:** May 31, 2026 UTC
- **Release Date:** NGC 05/25/2026
- **Compressed Size:** 2.69 GB

## Getting Started/Download
Use the NGC CLI to download the model. Supported runtime: TAO v6.25.11

**Hardware Support:** NVIDIA Ampere, Blackwell, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures

**Preferred OS:** Linux

**Test Hardware:** NVIDIA A100 80GB, NVIDIA H100 80GB
