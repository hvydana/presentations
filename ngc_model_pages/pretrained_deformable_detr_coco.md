# Deformable DETR (TAO Pretrained Deformable DETR)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_deformable_detr_coco

## Description/Overview
"Model trained on COCO2017 to detect and classify objects." This is an object detection model that "recognizes the individual objects in an image and place bounding boxes around the object."

## Use Case
Primary applications include detecting objects in color (RGB) images from photos and videos. The model supports transfer learning and fine-tuning for custom object detection tasks across domains such as "smart cities, retail, healthcare, industrial inspection."

## Model Architecture
The Deformable DETR model uses two backbone options:
- **ResNet50**: A classification network pre-trained on ImageNet
- **GCViT-Tiny**: A Vision Transformer backbone pre-trained on ImageNet

The model accepts "color (RGB) images as input and produce bounding boxes and classes as output."

## Input/Output Format
**Input:** "B X 3 X 544 X 960 (B C H W)"

**Output:** "Category labels (80 COCO) and bounding-box coordinates for each detected objects in the input image."

## Training Data
"Deformable DETR was trained on the COCO 2017 dataset." The dataset comprises "118K training images and 5K validation images and corresponding annotation files. The annotation contains bounding boxes for 80 object categories."

## Intended Users
Organizations requiring object detection capabilities with NVIDIA hardware. Users should have access to "NVIDIA Hardware" and software tools including "TAO Toolkit, DeepStream SDK or TensorRT."

## License
**Name:** Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)

**License Clause/Link:** "This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0). To view a copy of this license, please visit this [link](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)"

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, Transfer Learning

## Version/Date
**Latest Version:** ddetr_gc_vit_tiny_deployable_v1.0

**Updated:** February 3, 2024 UTC

**Compressed Size:** 194.48 MB

## Model Versions Available
- ddetr_resnet_50_trainable_v1.0
- ddetr_resnet_50_deployable_v1.0
- ddetr_gc_vit_tiny_trainable_v1.0
- ddetr_gc_vit_tiny_deployable_v1.0

## Getting Started Instructions
1. "Get TAO Container" from NGC
2. Use the provided experiment spec template for the model and train components
3. Reference the "TAO Toolkit User Guide" for detailed configuration
4. Deploy using "DeepStream SDK" or "TensorRT" following deployment documentation in the TAO User Guide
