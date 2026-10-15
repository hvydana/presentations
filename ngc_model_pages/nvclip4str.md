# nvCLIP4STR
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/nvclip4str

## Model Name
**nvCLIP4STR**

## Description/Overview
"nvCLIP4STR is optical character recognition network, which aims to recognize characters from the images."

One pretrained model is available, trained on 7 datasets with alphanumeric labels and ready for commercial use.

## Use Case
This model recognizes text within images for computer vision applications, particularly suited to identify characters from detected text regions.

## Model Architecture
- **Type:** Convolutional Neural Network + Transformer Encoder Decoder
- **Based on:** CLIP4STR architecture
- **Structure:** Two encoder-decoder branches—a visual branch providing initial predictions and a cross-modal branch refining predictions by addressing discrepancies between visual features and text semantics

## Input/Output Format

**Input:**
- Type: Image
- Format: RGB
- Parameters: 2D, 224x224 resolution required, no alpha channel

**Output:**
- Type: Text
- Format: String
- Parameters: 1D
- Content: Numbers, capital/lowercase letters, symbols

## Training Data
- **Total:** 6M images across 7 datasets
- **Datasets:** ICDAR15, MLT19, Uber-Text, COCO-Text v2.0, OpenVINO, TextOCR, Union14M-L
- **Collection:** Hybrid (automated and human)
- **Labeling:** Hybrid (automated and human)

## Evaluation Datasets
ICDAR13, ICDAR15, Uber-Text (3 datasets, 83,643 total images)

## License
"License to use these models is covered by the NVIDIA Open Model License."

[Full license terms](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

## Tags
- AI
- English
- Smart Cities/Spaces
- TAO Toolkit

## Version & Date
- **Version:** deployable_v1.0
- **Released:** NGC [05/30/2025]
- **Updated:** August 5, 2025 UTC
- **Compressed Size:** 1.62 GB

## Getting Started/Download
Use the NGC CLI to download. Requires NVIDIA Hardware and the NVIDIA-Optical-Character-Detection-and-Recognition-Solution (nvOCDR lib). Consult the [nvCLIP4STR C++ Sample](https://github.com/NVIDIA-AI-IOT/NVIDIA-Optical-Character-Detection-and-Recognition-Solution/tree/main/c%2B%2B_samples#nvclip4str) for deployment guidance.
