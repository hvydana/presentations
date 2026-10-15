# PCB Defect Classification Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pcb_classification

## Model Name
PCB Defect Classification

## Description/Overview
"Model to classify defects in soldered components on a Printed Circuit Board." The model performs image classification to categorize images into designated classes based on features, specifically detecting missing component defects using component-level images extracted from PCBs.

## Use Case
The primary application involves detecting missing component defects in RGB PCB component-level images. It functions as a binary classifier predicting whether a component is present or missing in photographs and videos.

## Model Architecture
This implementation uses "GCViT architecture" with a "GCViT-xxTiny" backbone pretrained on NVImageNet dataset and fine-tuned on proprietary PCB data. The model incorporates a single linear binary classifier head.

NVImageNet is described as "a commercially friendly image dataset whose category names are aligned with original ImageNet-1k's category names," collected from 84 websites permitting commercial use.

## Input/Output Format

**Input:** "RGB Image of dimensions: 224 X 224 X 3 (W x H x C)" with "Channel Ordering of the Input: NCHW"

**Output:** "binary label assigned to the image by the PCBClassification model" with "Category labels (2 classes - Missing/Present)" and "Channel Ordering of the Input: NC"

## Training Data
The model was trained on a proprietary dataset containing 19,605 images of individual components from 71 PCB boards. The dataset breakdown:
- Training images: 15,573
- Testing images: 2,079
- Component present images: 14,226
- Component missing images: 5,379

Components included resistors, capacitors, inductors, and other types treated as single "component-present" class during training.

## Performance Metrics
Evaluation used 2,079 proprietary test images. The model achieved "0.99" accuracy. Real-time inference performance varies by hardware platform, ranging from 133.9 FPS on Jetson Orin Nano to 12,273 FPS on H100.

## Intended Users
Developers requiring NVIDIA hardware and software, utilizing TAO Toolkit, DeepStream SDK, or TensorRT for deployment. Users can fine-tune the model for custom PCB defect detection applications.

## License
"License to use this model is covered by the Model EULA." Users must accept terms upon download, governed by NVIDIA AI Enterprise EULA available at: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit

## Version/Date
**Version:** deployable_v1.0
**Updated:** October 16, 2023 UTC
**Compressed Size:** 154.98 MB

## Getting Started
Access the model through NVIDIA NGC. Use TAO Toolkit with provided experiment spec template configuration for transfer learning, or deploy via DeepStream SDK 6.1+ following documentation in the TAO User Guide's "Deploying to DeepStream" chapter.
