# Visual ChangeNet - Segmentation (LandSat-SCD)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/visual_changenet_segmentation_landsatscd

## Description/Overview
This model "detects land cover semantic changes given remote sensing imagery (RSI)." The system processes pairs of images -- a reference image and a test image of the same area -- and outputs a semantic change map showing differences between them.

## Use Case
The primary use case involves analyzing remote sensing imagery captured between 1990 and 2010 to identify land cover changes. The model is "intended for training and fine-tune using TAO Toolkit and user datasets for image comparison."

## Model Architecture
Visual ChangeNet-Segmentation uses a transformer-based Siamese Network architecture. The model employs "a pretrained FAN backbone, trained on NVImageNet dataset, and then fine-tunes on the LandSat-SCD dataset." The FAN backbone is specifically the "FAN-Hybrid Small" variant.

## Input/Output Format

**Input:** Two RGB images, each 416 x 416 x 3 (H x W x C), with channel ordering NCHW (batch size, 3 channels, 416 height, 416 width)

**Output:** Segmentation change map with dimensions 416 x 416 x 10, where the final dimension represents output change classes

## Training Data
The model was trained on the LandSat-SCD dataset, an open-source remote sensing semantic land change detection dataset containing 8,468 images at 416 x 416 resolution, split into training (6,053), validation (1,729), and test (686) sets.

## Intended Users
Organizations and developers using NVIDIA hardware and software, specifically those working with the "Train Adapt Optimize (TAO) Toolkit, or TensorRT" for edge deployment applications.

## License
"License to use this model is covered by CCBY 4.0." The full license is available at https://creativecommons.org/licenses/by/4.0/

## Tags
Computer Vision, CV, Deep Learning, TAO, TAO Toolkit

## Version/Date
**Latest Version:** deployable_v1.2
**Updated:** November 12, 2024 UTC
**Compressed Size:** 145.81 MB

## Download/Getting Started
Download via NGC CLI using the provided command. Access the TAO Container at: https://ngc.nvidia.com/catalog/containers/nvidia:tao:tao-toolkit
