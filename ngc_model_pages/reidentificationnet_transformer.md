# Re-Identification Transformer (ReIdentificationNet Transformer)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/reidentificationnet_transformer

## Description/Overview
"SWIN Transformer based Re-Identification network to generate embeddings for identifying persons in different scenes." The model generates embeddings for identifying objects captured in different scenes and was pre-trained via self-supervised learning on approximately 3 million image crops, then fine-tuned on supervised person re-identification datasets.

## Use Case
The primary intended use case is generating embeddings for objects and performing similarity matching. The model is designed for training and fine-tuning using the TAO Toolkit and for deployment to edge devices via DeepStream SDK or TensorRT.

## Model Architecture
"The model backbone is a SWIN Transformer at its core. It processes images in a non-overlapping window fashion, using self-attention to learn both local and global features." The training approach uses tricks from SOLIDER research. The model optimizes via "triplet loss, center loss and cross entropy loss."

## Input/Output Format
**Input:** B X 3 X 256 X 128 (B C H W)

**Output:** The feature embedding

## Training Data
The model was trained on:
- Market-1501 dataset (751 annotated people)
- Sampled MTMC people tracking dataset from 2023 AI City Challenge (106 annotated people)
- NVIDIA proprietary dataset (2,969 annotated people)

Training set: 3,826 total identities, 54,183 total images across 130 cameras

## Intended Users
Organizations and developers using NVIDIA GPUs (including Jetson devices) who need person re-identification capabilities within NVIDIA's ecosystem tools.

## License
"License to use the model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
- Computer Vision
- CV
- Deep Learning
- TAO
- TAO Toolkit

## Version/Date
Latest version: swin_base_1024
Updated: September 23, 2024 UTC
Compressed Size: 836.76 MB

## Download/Getting Started Instructions
Use the NGC CLI to download. Access the TAO Container and refer to the TAO Toolkit documentation at https://docs.nvidia.com/tao/tao-toolkit/index.html for implementation details.
