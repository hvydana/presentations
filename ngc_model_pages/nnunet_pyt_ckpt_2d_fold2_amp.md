# nnUNet PyTorch checkpoint 2D AMP
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/models/nnunet_pyt_ckpt_2d_fold2_amp

## Model Name
nnUNet PyTorch checkpoint 2D AMP

## Description/Overview
"An optimized, robust and self-adapting framework for U-Net based medical image segmentation"

## Use Case
Medical image segmentation using 2D and 3D U-Net architectures for semantic segmentation of 3D images.

## Model Architecture
The nnU-Net supports two network types: 2D U-Net and 3D U-Net. The architecture features a contractive path leading to a bottleneck composed of convolution, instance normalization, and leaky ReLU operations. The expanding path reconstructs images through convolutions and upsampling, with skip connections facilitating gradient flow during training.

## Input/Output Format
Not explicitly specified in the provided content.

## Training Data
"MSD Task01 - Dataset with complex and heterogeneously-located targets" from the Medical Segmentation Decathlon.

## Intended Users
Researchers and practitioners working on medical image segmentation tasks.

## License
The model training utilized open-source software from the Deep Learning Examples repository. Users should consult the license terms of the training scripts and datasets used.

## Tags
- Computer Vision
- Deep Learning Examples

## Version/Date
Version 21.02.1, updated April 4, 2023 UTC

## Download Instructions
Use the NGC CLI to download (specific command shown on the NGC page).

## References
- Original paper: https://arxiv.org/abs/1809.10486
- NVIDIA implementation: NGC catalog and GitHub repository
