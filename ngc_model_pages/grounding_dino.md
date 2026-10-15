# Grounding DINO
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/grounding_dino

## Model Name
**Grounding DINO** (Latest version: grounding_dino_swin_tiny_commercial_trainable_v1.1)

## Description/Overview
"Open vocabulary object detection is a computer vision technique that can detect one or multiple objects in a frame based on the text input." This model performs detection by recognizing individual objects in images and placing bounding boxes around them. The pretrained weights are available for transfer learning through the TAO Toolkit, with commercial usage rights.

## Use Case
The model is intended for detecting objects in RGB images from photos and videos. It can be finetuned with custom datasets for specific object detection applications and deployed at the edge using TensorRT.

## Model Architecture
- **Type:** Transformer-based Network Architecture
- **Backbone:** Swin-Tiny (trained on NVImageNetv2 proprietary dataset)
- **Text Encoder:** BERT-Base
- **Encoder/Decoder:** 6 layers each with multi-headed attention and deformable attention mechanisms

## Input/Output Format

**Inputs:**
- Images: B x 3 x 544 x 960 (RGB format, any resolution supported)
- Tokenized text inputs via HuggingFace (max 256 tokens)
- Additional mask and position tensors (B x 256 dimensions)

**Outputs:**
- `pred_logits`: B x 900 (confidence scores)
- `pred_boxes`: B x 900 x 4 (bounding boxes in cxcywh format)

## Training Data
Pretrained on 1,815,237 images with 14,794,974 annotations from commercial datasets:
- OpenImages subset (803,826 images, pseudo-labeled)
- Localized Narrative OpenImages (670,553 images)
- LVIS, Mixed Grounding, RefCOCO variants (human-labeled, commercial subsets only)
- Total: approximately 1.8M images

## Intended Users
Developers using NVIDIA hardware and software who need to perform object detection tasks and can leverage the TAO Toolkit or TensorRT for training and deployment.

## License
"License to use these models is covered by the NVIDIA Open Model License." Full terms available at: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
Computer Vision, CV, Deep Learning, TAO, TAO Toolkit

## Version & Date
**Version:** grounding_dino_swin_tiny_commercial_trainable_v1.1
**Updated:** March 23, 2026 UTC
**Compressed Size:** 1.93 GB

## Getting Started
Download via NGC CLI. Use with TAO Toolkit or TensorRT. Reference the TAO documentation and provided Jupyter Notebook for training and fine-tuning workflows.

## Note
The slug that resolved was the underscore form `grounding_dino` at the TAO team path (not the hyphenated `grounding-dino` variant).
