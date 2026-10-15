# TAO Toolkit ODISE 1.1
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/odise

## Model Name
TAO Toolkit ODISE 1.1

## Description/Overview
"Open-vocabulary DIffusion-based panoptic SEgmentation (ODISE) developed by NVIDIA Research is an open vocabulary panoptic segmentation model." This TAO-optimized version replaces the diffusion backbone with a ConvNext-based CLIP backbone for improved performance.

## Use Cases
The primary applications include open-vocabulary segmentation and auto-labeling, with suitability for smart cities, retail, healthcare, and industrial inspection scenarios.

## Model Architecture
The model functions as a panoptic segmentator accepting RGB images and text prompts as inputs. "The backbone feature extractor of this model is the ConvNext-L CLIP model pretrained on LAION-2B dataset."

## Input/Output Format

**Input:**
- Image: B X 3 X 1024 X 1024 (B C H W)
- Label: Panoptic segmentation groundtruth in COCO format

**Output:**
Segmentation mask and label for each detected object in the input image.

## Training Data
"ODISE 1.1 was trained on the COCO dataset for Panoptic Segmentation. The COCO dataset contains 118K training images and 5K validation images and corresponding annotation files."

## Intended Users
Developers using NVIDIA hardware and the TAO Toolkit framework for training, fine-tuning, and deploying custom segmentation models.

## License
"This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)." Full details available at: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
Panoptic Segmentation, Open Vocabulary Segmentation, Instance Segmentation, Semantic Segmentation, ConvNext-L, Transfer Learning, TAO Toolkit, Computer Vision, Deep Learning, COCO

## Version/Date
**Version:** odise_trainable_v1.0
**Updated:** November 27, 2024 UTC
**Compressed Size:** 1.43 GB

## Getting Started
Access the model through NGC CLI download or via the TAO Container. Documentation and implementation details are available in the [NVIDIA TAO GitHub repository README](https://github.com/NVIDIA/tao_pytorch_backend/tree/main/nvidia_tao_pytorch/cv/odise/README.md).
