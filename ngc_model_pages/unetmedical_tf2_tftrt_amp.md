# UNet_Medical TensorFlow2 TF-TRT model (AMP)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/unetmedical_tf2_tftrt_amp

## Description/Overview
"U-Net allows for seamless segmentation of 2D images, with high accuracy and performance." The model was trained using Automatic Mixed Precision (AMP).

## Use Case
2D biomedical image segmentation tasks

## Model Architecture
This implementation is based on the original UNet architecture introduced by Olaf Ronneberger, Philip Fischer, and Thomas Brox. The model features:

- A contractive path that creates a bottleneck through convolution and pooling operations
- An expanding path that reconstructs the image through convolutions and upsampling
- Skip connections designed to improve gradient flow during training

## Input/Output Format
Not explicitly specified in the fetched page content.

## Training Data
The model was trained on the **EM Segmentation dataset** from MIT's ISBI Challenge:
- 30 sections of serial section Transmission Electron Microscopy (ssTEM) data
- Source: Drosophila first instar larva ventral nerve cord (VNC)
- Resolution: 4x4x50 nm/pixel
- Spatial dimensions: approximately 2 x 2 x 1.5 microns

## Intended Users
Researchers and practitioners working on biomedical image segmentation applications

## License
The model references the open-source Deep Learning Examples repository license. Specific license terms direct users to "refer to the license of the script and the datasets."

## Tags
- Computer Vision
- Deep Learning Examples

## Version/Date
- **Version:** 21.11.0
- **Updated:** April 4, 2023 UTC
- **Compressed Size:** 330.08 MB

## Download Instructions
Use the NGC CLI to download the model from the NVIDIA NGC Catalog

## Note on URL resolution
This slug resolved under `/orgs/nvidia/teams/dle/models/` (DLE = Deep Learning Examples team), not `/orgs/nvidia/models/`.
