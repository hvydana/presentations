# Visual ChangeNet Segmentation - MvTEC
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/visual_changenet_segmentation_mvtec

## Description/Overview
"The model described in this model card is designed for the segmentation of industrial defects using the MVTec-AD dataset." It accepts paired co-registered images (a golden reference image and a test image) and outputs a binary segmentation change map highlighting defects.

## Use Case
Industrial defect detection and segmentation at the component level, specifically trained on transistor images from the MVTec-AD dataset.

## Model Architecture
The model employs a Siamese Network architecture based on Visual ChangeNet, a transformer-based change detection system. It uses "a pretrained FAN backbone, trained on NVImageNet dataset, and then fine-tunes on the MVTec-AD dataset for the transistor class."

## Input Format
- **Golden Image**: RGB, 256x256x3 (HxWxC)
- **Test Image**: RGB, 256x256x3 (HxWxC)
- **Channel Ordering**: NCHW format

## Output Format
"Segmentation change map with the same spatial resolution as the input images: 256 X 256 X 2 (H x W x C), where C = number of output change classes."

## Training Data
MVTec-AD (transistor class): 303 total images split into 212 training and 91 validation samples.

## Performance Metrics
- Precision: 94.5%
- Recall: 89.8%
- IoU: 86.15%
- F1: 92%
- Overall Accuracy: 99.57%

## Intended Users
Developers using NVIDIA hardware with TAO Toolkit or TensorRT for industrial inspection applications.

## License
CC-BY-NC-SA-4.0. Access the full license at: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

## Tags
Computer Vision, CV, Deep Learning, Industrial Inspection, Optical Inspection, TAO, TAO Toolkit

## Version & Date
- **trainable_v1.0** (Latest)
- **deployable_v1.0**
- Updated: December 12, 2023 UTC
- Compressed Size: 621.44 MB

## Download Instructions
Use NGC CLI to download from the NVIDIA NGC Catalog at: https://ngc.nvidia.com/catalog/models/nvidia:tao:visual_changenet_segmentation_mvtec
