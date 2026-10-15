# UNet_Medical TensorFlow2 SavedModel (AMP)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/unetmedical_tf2_savedmodel_amp

## Description/Overview
"U-Net allows for seamless segmentation of 2D images, with high accuracy and performance." The model represents a TensorFlow2 implementation trained with Automatic Mixed Precision (AMP).

## Use Case
Biomedical image segmentation, particularly for 2D medical imaging applications.

## Model Architecture
The UNet architecture consists of two primary pathways:

- **Contractive Path**: Uses convolution and pooling operations to create a bottleneck at the center
- **Expanding Path**: Reconstructs the image through convolutions and upsampling operations
- **Skip Connections**: Added to improve gradient flow during backward propagation

This design enables the model to effectively segment medical images while maintaining spatial information through skip connections between corresponding layers in the contractive and expanding paths.

## Input/Output Format
Not explicitly detailed in the fetched page content.

## Training Data
The model was trained on the **EM Segmentation dataset**, described as "Set of 30 sections from a serial section Transmission Electron Microscopy (ssTEM) data set of the Drosophila first instar larva ventral nerve cord (VNC)." The dataset has a microcube measuring approximately 2 x 2 x 1.5 microns with 4x4x50 nm/pixel resolution.

## Intended Users
Researchers and practitioners in biomedical image analysis and computer vision applications.

## License
Licensing information directs users to refer to the licenses of the Deep Learning Examples repository and the datasets used. No specific license clause is provided on this page.

## Tags
- Computer Vision
- Deep Learning Examples

## Version/Date
- **Version**: 21.11.0 (Latest)
- **Updated**: April 4, 2023 UTC
- **Compressed Size**: 132.57 MB

## Download/Getting Started
Users can "Use the NGC CLI to download" the model, with specific commands available on the NGC catalog page.

## References
- Original paper: [UNet: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
- NGC resource and GitHub repository links provided for implementation details

## Note on URL resolution
This slug resolved under `/orgs/nvidia/teams/dle/models/` (DLE = Deep Learning Examples team), not `/orgs/nvidia/models/`.
