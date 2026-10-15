# Mask2Former
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/mask2former

## Model Name
**Mask2Former**

## Description/Overview
"Masked-attention Mask Transformer or Mask2Former is a segmentation architecture capable of addressing panoptic, instance or semantic image segmentation tasks." The model leverages masked attention to efficiently extract localized features by constraining cross-attention within predicted mask regions.

## Use Case
The primary use case involves instance segmentation tasks. The model is intended for training and fine-tuning using NVIDIA's Train Adapt Optimize (TAO) Toolkit with users' custom datasets.

## Model Architecture
- **Architecture Type:** Instance segmentor accepting RGB color images as inputs, generating segmentation masks and associated labels as outputs
- **Network Backbone:** Swin-T model pretrained on ImageNet dataset

## Input/Output Format

**Input:**
- Type: Image
- Format: Red, Green, Blue (RGB)
- Minimum resolution: 32 x 32 pixels
- No alpha channel or bit depth requirements specified

**Output:**
- Types: Label, Mask, and Score for each detected object
- pred_classes: Batch size × Number of queries
- pred_masks: Batch size × Number of queries × Height × Width
- pred_scores: Batch size × Number of queries

## Training Data
The COCO dataset containing 118K training images with bounding boxes and segmentation masks across 80 thing categories, consolidated into a single "object" category for binary instance segmentation.

## Intended Users
Organizations requiring instance segmentation capabilities with access to NVIDIA GPUs (>12GB memory) and TAO Toolkit software infrastructure.

## License
**License Name:** NVIDIA Open Model License

**License Details:** "By downloading the model, you accept the terms and conditions of these licenses" with reference to [NVIDIA's enterprise software license agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

**Commercial Use:** Non-commercial use only

## Tags
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit

## Version Information
- **Latest Version:** mask2former_swint_trainable_v1.0
- **Updated:** November 12, 2024 UTC
- **Compressed Size:** 543.33 MB
- **Available Versions:**
  - mask2former_swint_trainable_v1.0 (for finetuning/inference)
  - mask2former_swint_deployable_v1.0 (for DeepStream deployment)

## Getting Started Instructions

Access the TAO Container from NVIDIA NGC, then use the following experiment spec template for training:

```
model:
  mode: "instance"
  backbone:
    type: "swin"
    swin:
      type: "tiny"
      window_size: 7
      ape: False
      pretrain_img_size: 224
  mask_former:
    num_object_queries: 100
  sem_seg_head:
    norm: "GN"
    num_classes: 1
```

Refer to the TAO Toolkit User Guide and documentation for comprehensive implementation details.
