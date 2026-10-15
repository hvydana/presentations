# TAO Commercial Pretrained NV-Dinov2 Model (ViT-G backbone)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/nvdinov2_vitg

## Model Name
TAO Commercial Pretrained NV-Dinov2 Model (ViT-G backbone)

## Description/Overview
"This model card contains pretrained weights of NV-Dinov2 model which can be used as a backbone for most of the popular computer vision tasks such as Classification, Segmentation, Detection. This model is ready for commercial use."

The model produces embeddings useful for downstream computer vision applications without requiring fine-tuning across different image distributions and tasks.

## Use Cases
- Classification
- Segmentation
- Detection
- Change detection
- Image comparison and feature extraction for downstream tasks

## Model Architecture
**Type:** Transformer-Based

The model employs a self-supervised learning approach combining DINO and iBOT techniques. "NV-Dinov2 is a visual foundational model trained on NVIDIA proprietary large scale dataset." It was trained to learn robust fine-grained representations for localization and classification tasks.

## Input/Output Format

**Input:**
- Types: Images in RGB format
- Minimum resolution: 224 x 224
- Maximum resolution: 518 x 518
- Format: 3D RGB images (H x W x C)
- Channel ordering: NCHW (Batch, Channels, Height, Width)

**Output:**
- "Embedding - Float tensor" in 3D vector format
- Size: 1024 for ViT-L variant; 1536 for ViT-G

## Training Data
Two dataset versions exist:
- **NV-DinoV2-224-V0:** "130M internal dataset pre-trained model at 224 resolution"
- **NV-DinoV2-518-V0:** "700M internal dataset pre-trained model at 518 resolution"

Collection and labeling methods were automated on NVIDIA proprietary datasets.

## Intended Users
Developers and organizations using NVIDIA hardware and software who need computer vision feature embeddings for transfer learning applications.

## License
"License to use these models is covered by the NVIDIA Open Model License. By downloading the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)."

## Tags
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit
- NVIDIA AI Enterprise Supported

## Version & Date
**Latest Version:** NV-DinoV2-518-V0
**Updated:** October 2, 2024 UTC
**Compressed Size:** 4.23 GB

## Getting Started/Download Instructions
"Use the NGC CLI to download:" (specific command provided on page for authenticated users)

Models require **TAO Toolkit 5.2** runtime and work with NVIDIA Ampere, Jetson, Hopper, Lovelace, Pascal, Turing, and Volta architectures on Linux and Linux 4 Tegra operating systems.
