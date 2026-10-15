# NV-DINOv2 Classification Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/nv_dinov2_classification_model

## Model Name
NV-DINOv2 Classification Model (TAO Commercial Pretrained)

## Description/Overview
"Image Classification is a popular computer vision technique in which an image is classified into one of the designated classes based on the image features." The model serves as a visual foundation model trained on NVIDIA's proprietary large-scale dataset using self-supervised learning methods.

## Use Case
The primary application involves "classifying objects in a color (RGB) image" from photos and videos. It functions as a backbone for downstream tasks including classification, detection, and segmentation with few labeled examples.

## Model Architecture
NV-Dinov2 combines two self-supervised learning techniques: DINO and iBOT. The architecture uses "vit_large_patch14_dinov2_swiglu" as the backbone, producing "all purpose visual features" that work across image distributions without fine-tuning.

## Input/Output Format

**Input:**
- B X 3 X 224 X 224 (B C H W) to B X 3 X 518 X 518 (B C H W)

**Output:**
- "Output is an embedding and can be used as pre-trained backbone weights for different downstream tasks"

## Training Data
"NV-Dinov2 was trained on NVIDIA proprietary collected data that are of commercial license." Training involved 130M images using the DINOV2 SSL method.

## Performance Metrics
- **Top-1 Accuracy on ImageNet validation:** 79.9%
- Inference performance varies by platform (Orin NX: 31.55 FPS to H100: 2500.6 FPS at FP16 precision)

## Intended Users
Organizations needing to deploy image classification models on NVIDIA hardware, particularly those using TAO Toolkit, DeepStream SDK, or TensorRT for edge deployment.

## License
**NVIDIA Open Model License** – "By downloading the model, you accept the terms and conditions of these licenses" with a link provided to [nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

## Tags
- AI
- Computer Vision
- NVIDIA AI
- TAO Toolkit

## Version/Date
**Latest Version:** deployable_v1.0 (Also available: deployable_v1.1, trainable_v1.1)
**Updated:** August 5, 2025 UTC
**Compressed Size:** 1.14 GB

## Download/Getting Started
Access via NGC CLI or download from the NGC Catalog. Use with the TAO Toolkit container available at: [ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit](https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit)

Reference the TAO Toolkit documentation for fine-tuning instructions using experiment spec files.
