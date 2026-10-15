# ResNet50 pretrained weights (PyTorch, AMP, ImageNet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/resnet_50_pyt_ckpt

## Description/Overview
"With modified architecture and initialization this ResNet50 version gives ~0.5% better accuracy than original. This model is ready for commercial use."

## Use Case
Computer Vision - Image classification on ImageNet dataset

## Model Architecture
The ResNet50 v1.5 is a modified version of the original ResNet50 v1. "The difference between v1 and v1.5 is that, in the bottleneck blocks which requires downsampling, v1 has stride = 2 in the first 1x1 convolution, whereas v1.5 has stride = 2 in the 3x3 convolution."

"This difference makes ResNet50 v1.5 slightly more accurate (~0.5% top1) than v1, but comes with a small performance drawback (~5% imgs/sec)."

The model uses "mixed precision using Tensor Cores on Volta, Turing, and the NVIDIA Ampere GPU architectures."

## Input/Output Format
Not explicitly specified in the fetched page content.

## Training Data
ImageNet - "Image database organized according to the WordNet hierarchy, in which each noun is depicted by hundreds and thousands of images."

## Intended Users
Researchers and developers for commercial computer vision applications

## License
"For terms of use, please refer to the license of the script and the datasets the model was derived from." Specific license details referenced in the [Deep Learning Examples GitHub repository](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets/resnet50v1.5)

## Tags
- Computer Vision

## Version/Date
Latest Version: 20.06.0_amp
Updated: July 5, 2024 UTC
Compressed Size: 97.74 MB

## Download Instructions
"Use the NGC CLI to download" (specific command shown on page but requires NGC CLI setup)

## Note on URL resolution
The slug `resnet_50_pyt_ckpt` did not resolve under `/orgs/nvidia/teams/tao/models/` or `/orgs/nvidia/models/`; it resolved under `/orgs/nvidia/teams/dle/models/` (DLE = Deep Learning Examples team).
