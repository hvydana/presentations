# nnUNet PyTorch checkpoint 3D AMP
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/models/nnunet_pyt_ckpt_3d_fold2_amp

## Model Name
nnUNet PyTorch checkpoint 3D AMP (nnUNet3d PyTorch checkpoint trained with AMP on fold 2)

## Description/Overview
"An optimized, robust and self-adapting framework for U-Net based medical image segmentation"

## Use Case
Medical image segmentation using 3D deep learning models for semantic segmentation of 3D images with high accuracy and performance.

## Model Architecture
The nnU-Net framework supports two network types: 2D U-Net and 3D U-Net. The 3D U-Net consists of a contractive path and expanding path forming a bottleneck through convolution, instance normalization, and leaky ReLU operations. The reconstruction phase uses convolutions and upsampling, with skip connections facilitating gradient backflow during training.

## Input/Output Format
Not explicitly specified in the provided content.

## Training Data
"MSD Task01 - Dataset with complex and heterogeneously-located targets" from the Medical Segmentation Decathlon (http://medicaldecathlon.com/index.html)

## Intended Users
Researchers and practitioners in medical imaging and deep learning using PyTorch.

## License
The model was trained using open-source software from the Deep Learning Examples repository. Users should refer to the license of the training scripts and datasets for specific terms.

## Tags
- Computer Vision
- Deep Learning Examples

## Version/Date
Latest Version: 21.02.1 | Updated: April 4, 2023 UTC | Compressed Size: 357.06 MB

## Download/Getting Started
Download via NGC CLI using commands provided on the NGC Catalog resource page. Implementation available at the [NVIDIA GitHub repository](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Segmentation/nnUNet)
