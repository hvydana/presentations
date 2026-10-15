# Mask Grounding DINO CC
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/mask_grounding_dino

## Model Name
Mask Grounding DINO CC (TAO Pretrained Mask Grounding DINO with Commercial License)

## Description/Overview
An "open vocabulary instance segmentation" model capable of segmenting objects based on text input. The system recognizes individual objects in images and generates bounding boxes plus segmentation masks. The model uses pretrained weights on commercial datasets and is intended for transfer learning via the Train Adapt Optimize (TAO) Toolkit.

## Use Cases
1. **Open-Set Object Detection and Segmentation**: Detect objects not predefined in training by providing new category names via text (e.g., "lion," "bench")
2. **Referring Expression/Text-Guided Detection**: Accept referring expressions like "the bottom man with his head up" and localize described objects

## Model Architecture

**Type**: Transformer-Based Segmentation Model
**Network**: Swin-Tiny backbone with transformer-based segmentation head
**Parameters**: 182,668,026

The model processes RGB images and text inputs (either phrase lists or referring expressions) to output bounding boxes, segmentation masks, and labels. It was initialized from a commercial GroundingDINO checkpoint and pretrained end-to-end on approximately 1.2 million image-expression pairs sourced from Open Images V5, Localized Narratives, COCO, and RefCOCO variants.

## Input Format

**Image Input**:
- Format: RGB (Red, Green, Blue)
- Resolution: Minimum 32 × 32 pixels
- Tensor shape: `B × 3 × 544 × 960` (Batch × Channels × Height × Width)
- Properties: No alpha channel; standard 8-bit color depth

**Text Input**:
- Format: Tokenized strings via Hugging Face
- Tensor shapes:
  - `input_ids`: `B × 256`
  - `attention_mask`: `B × 256`
  - `position_ids`: `B × 256`
  - `token_type_ids`: `B × 256`
  - `text_token_mask`: `B × 256 × 256`

## Output Format

**Output Types**: Bounding boxes, confidence scores, segmentation masks, no-target indicator

**Output Parameters**:
- `pred_logits`: `B × 900` (classification logits)
- `pred_boxes`: `B × 900 × 4` (boxes in cx, cy, w, h format)
- `pred_masks`: `B × 900 × H × W` (segmentation masks)
- `no_targets`: `B × 2` (binary logits for object/no-object)
- `union_logit_masks`: `B × H × W` (objectness map)

## Training Data

The model was fine-tuned on approximately 100,000 referring expression-image pairs from:

- **RefCOCO**: 36,459 samples; short expressions (~3.5 words average) with spatial terms
- **RefCOCO+**: 36,302 samples; appearance-focused, no spatial terms
- **RefCOCOg**: 23,695 samples; longer, descriptive expressions
- **COCO (Subset)**: 36,055 images with 80 object categories
- **OpenImages V5**: 662,956 samples covering 350+ categories
- **Localized Narratives**: 459,999 samples with dense vision-language annotations

All datasets verified for commercial-use license compatibility.

## Intended Users
Developers using NVIDIA hardware and software frameworks (TAO Toolkit or TensorRT) for object detection and segmentation tasks in commercial applications.

## License

**License Name**: NVIDIA Open Model License

**Governing Terms**: "Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)"

**Commercial Status**: This model is approved for commercial use.

## Tags/Labels
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit

## Version and Release Information

**Latest Version**: mask_grounding_dino_swin_tiny_commercial_deployable_v2.1_wo_mask_arm (Signed)

**Release Date**: November 25, 2025

**Last Updated**: March 10, 2026 UTC

**Compressed Size**: 685.8 MB

## Getting Started / Download Instructions

Models should be accessed through the NGC Catalog using the NGC CLI. The model is available in multiple versions:
- Deployable (v2.1, v2.0, v1.0)
- Trainable (v2.1, v2.0, v1.0)

For implementation, developers should reference the TAO Toolkit User Guide and use pretrained model paths in experiment spec files with backbone configuration `swin_tiny_224_1k`.

## Supported Hardware

- NVIDIA Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures
- Tested on: A2, A30, DGX H100, DGX A100, Jetson AGX Xavier, L4, L40, Orin Nano 8GB, Orin NX

**Operating Systems**: Linux, Linux 4 Tegra
