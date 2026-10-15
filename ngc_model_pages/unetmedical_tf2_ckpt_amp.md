# UNet_Medical TensorFlow2 checkpoint (AMP)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/unetmedical_tf2_ckpt_amp

## Description/Overview
"U-Net allows for seamless segmentation of 2D images, with high accuracy and performance." The model was trained using automatic mixed precision (AMP).

## Use Case
Biomedical image segmentation in 2D images. The architecture can be adapted for various segmentation tasks.

## Model Architecture
"UNet is composed of a contractive and an expanding path, that aims at building a bottleneck in its centermost part through a combination of convolution and pooling operations." The model includes skip connections to improve gradient flow during training. Based on the foundational paper by Olaf Ronneberger, Philip Fischer, and Thomas Brox.

## Training Data
The EM Segmentation dataset was used, consisting of 30 sections from serial section Transmission Electron Microscopy data of Drosophila first instar larva ventral nerve cord, with measurements of approximately 2 x 2 x 1.5 microns and resolution of 4x4x50 nm/pixel.

## Training Resources
Training scripts are available through NGC and the GitHub repository at https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow2/Segmentation/UNet_Medical

## Version & Date
Version 21.11.0, updated April 4, 2023 UTC

## Download/Getting Started
Use the NGC CLI to download the model. Compressed size: 394.99 MB

## License
License information should be referenced from the Deep Learning Examples repository license and the datasets used.

## Tags
- Computer Vision
- Deep Learning Examples

## Publisher
NVIDIA Deep Learning Examples

## Note on URL resolution
This slug resolved under `/orgs/nvidia/teams/dle/models/` (DLE = Deep Learning Examples team), not `/orgs/nvidia/models/`.
