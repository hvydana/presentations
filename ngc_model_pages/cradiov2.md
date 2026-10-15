# TAO Commercial Pretrained C-RADIOv2 Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cradiov2

## Model Name
TAO Commercial Pretrained C-RADIOv2 Model

## Description/Overview
"C-RADIOv2 specializes in visual feature extraction. For instance, C-RADIOv2 generates image embeddings that can be used by a downstream model to classify images."

The model is available in four sizes: Base (90M parameters), Large (320M parameters), Huge (653M parameters), and Gigantic (1.8B parameters). It was trained for 1M steps using inverse frequency sampling for data balancing and PHI Standardization for teacher distribution balance.

## Use Case
"C-RADIOv2 is designed for developers and researchers to extract visual features at scale (via image embeddings) for image classification."

## Model Architecture
- **Architecture Type:** Neural Network
- **Network Architecture:** Vision Transformer
- **ViT-B:** 90 million parameters
- **ViT-L:** 320 million parameters
- **ViT-H:** 653 million parameters
- **ViT-G:** 1.8 billion parameters

## Input/Output Format

**Input:**
- Type: Image
- Format: Red, Green, Blue (RGB)
- Parameters: Two Dimensional (2D)
- "Image resolutions up to 2048x2028 in increments of 16 pixels"

**Output:**
- Type: Embeddings
- Format: Tensor
- Parameters: Two Dimensional (2D)
- "Downstream model required to leverage image features"

## Training Data
"700 Million Image-Text pairs NV Internal Data" collected via automated methods with no labeling required.

## Intended Users
Developers and researchers working with visual feature extraction and image classification tasks.

## License
"License to use these models is covered by the NVIDIA Open Model License." Users must accept terms by downloading, available at: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
- Computer Vision
- TAO Toolkit
- NVIDIA AI Enterprise Supported

## Version/Date
- Latest Version: cradiov2-b
- Release Date: NGC 04/15/2025
- Updated: May 9, 2025 UTC
- Compressed Size: 374.78 MB

## Getting Started
"Use the NGC CLI to download" (specific command shown but implementation details available via NGC CLI documentation)
