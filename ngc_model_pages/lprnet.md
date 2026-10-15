# License Plate Recognition (LPRNet)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/lprnet

## Model Name
**License Plate Recognition (LPRNet)**

## Description/Overview
"Model to recognize characters from the image crop of a License Plate." This model is ready for commercial use and represents a pre-trained CNN designed specifically for alphanumeric character recognition in license plate images.

## Use Case
The primary intended use is "to recognize the license plate from the cropped RGB license plate image." The model supports both US and China license plate recognition through separate trained variants.

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** ResNet-based design

## Input Format
- **Type:** RGB image
- **Dimensions:** 3 × 48 × 96 (Channel, Height, Width)
- **Channel Ordering:** CHW format

## Output Format
- **Type:** Text labels
- **Content:** License plate alpha-numeric characters

## Training Data
The model was trained on:
1. Internal proprietary dataset of 310,000 US license plate images from dash and side cameras
2. Approximately 100,000 images from the Chinese City Parking Dataset (CCPD)

Characters recognized include digits (0-9) and letters (A-Z), with distribution details provided in the full documentation.

## Intended Users
Developers using NVIDIA Hardware and Software platforms who need to "re-train" models or "deploy to the edge using DeepStream SDK or TensorRT."

## License Information
No explicit license name or clause is presented on this page. The page references "Terms of Use" and "Terms of Service" as clickable links but does not reproduce the actual license text.

## Tags/Labels
Computer Vision, CV, DeepStream, License Plate recognition, Metropolis, NVIDIA AI, OCR, Public Safety, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, Traffic

## Version/Date
- **Latest Version:** deployable_onnx_v1.1 (Signed)
- **Updated:** November 27, 2024 UTC
- **Compressed Size:** 110.09 MB

## Getting Started/Download Instructions
"Use the NGC CLI to download" (specific command not fully detailed in excerpt). Users can access the model through NVIDIA's NGC Catalog platform or integrate it with Transfer Learning Toolkit, DeepStream SDK, or TensorRT for deployment and fine-tuning.
