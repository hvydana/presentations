# SegIC (Segment-In-Context)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/segic

## Description/Overview
"The SegIC (Segment-In-Context) model is designed for in-context segmentation, which aims to segment novel images using a few labeled example images (in-context examples)." The model demonstrates strong performance as a generalist segmentation tool and is "ready for commercial use."

## Use Case
In-context segmentation tasks, including:
- General object segmentation across diverse categories
- Few-shot learning scenarios with minimal labeled examples
- Retail object detection applications

## Model Architecture
**Architecture Type:** Vision Transformer

The model comprises three main components:
- **Image encoder:** DINOv2-L trained with NVIDIA proprietary images
- **Meta description encoder:** CLIP-B trained with NVIDIA proprietary images
- **Mask Decoder:** "mainly composed of a few convolutional layers, projection layers and a transformer decoder"

## Input Format
- Example images: RGB format, resized to 896x896, batch_size x 3 x 896 x 896
- Example masks: Grayscale, 896x896 resolution, batch_size x 1 x 896 x 896
- Meta description: Tokenized string (max 77 words), batch_size x 64
- Target image: RGB, 1 x 3 x 896 x 896 (single image per inference)
- Original sizes: 1 x 2

## Output Format
"Predicted segmentation masks" with tensor shape of batch_size x 1 x 896 x 896 at 896x896 resolution. Post-processing is required to resize masks to original image dimensions.

## Training Data
- MSCOCO 2017 subset: 48,000 images, 80 classes
- OpenImage subset: 64,000 images, 80 classes
- Synthetic retail data: 48,000 images, 315 classes (generated via NVIDIA Omniverse Replicator)

## Evaluation Data
- COCO-20i: 5,000 images for one-shot segmentation benchmarking
- Voyager Cafe KPI: 6,042 retail images across 7 scenes

## Evaluation Results
- COCO-20i (one-shot): mIoU of 69.57
- Voyager Cafe KPI (retail): mAP of 0.904

## Intended Users
Developers working on computer vision and segmentation tasks requiring commercial-grade models with synthetic data support.

## License
"NVIDIA Open Model License" — Users must accept terms at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
Computer Vision, CV, Deep Learning, TAO Toolkit

## Version/Date
**Latest Version:** segic_deployable_v1.0
**Updated:** November 27, 2024 UTC
**Compressed Size:** 1.15 GB

## Getting Started
"NVIDIA TAO Toolkit now provides a Gradio app to the deployable SegIC models." Instructions available at the tao_pytorch_backend repository for interactive setup and deployment.
