# Mask Grounding DINO Research
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_mask_grounding_dino_v2

## Description/Overview
This is an NVIDIA proprietary open-vocabulary object segmentation model. According to the documentation, it represents a "computer vision technique that can segment one or multiple objects in a frame based on the text input." The model takes RGB images and text phrases as input to produce bounding boxes, masks, and corresponding labels as output.

## Use Cases
1. **Open-Set Object Detection and Segmentation**: The model "can detect objects that were not pre-defined in the training categories" by accepting new category names via text input.
2. **Referring Expression/Text-Guided Detection**: The system "supports being given a referring expression" like "the bottom man with his head up" to localize described objects.

## Model Architecture
- **Type**: Transformer-Based Segmentation Model
- **Backbone**: Swin-Tiny
- **Parameters**: 182,668,026 params
- The model uses a "Swin-Tiny backbone with a segmentation head pretrained end-to-end on the COCO and RefCOCO variant datasets"

## Input Format
- **Image**: RGB, minimum 32×32 pixels, 8-bit color depth, no alpha channel
- **Text**: Tokenized string inputs via Hugging Face
- **Dimensions**: `B × 3 × 544 × 960` (batch × channels × height × width)
- **Text tokens**: `B × 256` (tokenized input IDs with attention masks and positional encoding)

## Output Format
- **Bounding Boxes**: `(cx, cy, w, h)` format, `B × 900 × 4` dimensions
- **Confidence Scores**: Classification logits `B × 900`
- **Segmentation Masks**: `B × 900 × H × W` dimensions
- **No-Target Indicator**: Binary logits `B × 2` (object/no-object classification)
- **Union Logit Masks**: `B × H × W` (objectness map across all queries)

## Training Data
**gRefCOCO Dataset**
- **Source**: https://github.com/henghuiding/gRefCOCO
- **Collection Method**: Human
- **Labeling Method**: Human
- **Composition**:
  - 19,994 images
  - 60,287 distinct object instances
  - 278,232 referring expressions total
  - 80,022 multi-target expressions
  - 32,202 no-target expressions

The model was "fine-tuned on the gRefCOCO dataset, which contains referring expressions paired with object segmentations" with "precise masks and bounding boxes for all target instances."

## Evaluation Datasets
- **gRefCOCO** (validation, test A, test B)
- **RefCOCO** (validation, test A, test B)
- **RefCOCO+** (validation, test A, test B)
- **RefCOCOg** (multiple validation and test sets)

**Metrics**: gIoU (%), Target Accuracy (T_acc %), No-Target Accuracy (N_acc %), and mask_mAP (%)

**Sample Results (gRefCOCO validation)**:
- gIoU: 65.41%
- T_acc: 97.73%
- N_acc: 65.14%
- mask_mAP: 55.40%

## Intended Users
These models are "intended for training and fine-tune with the TAO Toolkit and your datasets for object detection." They're designed for "easy edge deployment using TensorRT" and work with "NVIDIA hardware and software," including NVIDIA Jetson devices.

## License
**License Name**: NVIDIA License (Non-Commercial)

**License Link**: https://developer.download.nvidia.com/licenses/NVIDIA-OneWay-Noncommercial-License-22Mar2022.pdf

**Status**: "This model is ready for non-commercial use."

## Tags/Labels
- AI
- Computer Vision
- Manufacturing
- Metropolis
- Robotics
- Smart Cities / Spaces
- TAO Toolkit

## Version & Date
- **Latest Version**: mask_grounding_dino_swin_tiny_research_deployable_v2.0
- **Updated**: December 8, 2025 UTC
- **Release Date (NGC)**: November 25, 2025
- **Compressed Size**: 747.4 MB

## Getting Started Instructions

### Using with TAO Toolkit
Configure the experiment spec file with the following template:

```
train:
  pretrained_model_path: /path/to/the/mask_groundingdino.pth
  freeze: ["backbone.0", "bert"]
model:
  backbone: swin_tiny_224_1k
  num_feature_levels: 4
  dec_layers: 6
  enc_layers: 6
  num_queries: 900
  dropout_ratio: 0.0
  dim_feedforward: 2048
```

### Download
Use the NGC CLI to download (specific command shown on NGC page for authenticated users).

### Deployment
- **Compatible Engines**: TensorRT
- **Supported Hardware**: NVIDIA Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, Volta architectures
- **Operating Systems**: Linux, Linux 4 Tegra
- **Runtime Engine**: TAO 5.5.0

### Resources
- TAO Toolkit documentation: https://docs.nvidia.com/tao/tao-toolkit/index.html
- TAO Quick Start Guide available
- Jupyter Notebook available in TAO container for retraining
- Additional guidance in TAO Toolkit Developer Forums
