# Retail Object Detection
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/retail_object_detection

## Description/Overview
"RetailObjectDetection detects retail items within an image; it classifies objects as retail or not." This model is ready for commercial use.

## Use Case
Detection of retail items on checkout counters, shelves, conveyor belts, and baskets in retail environments.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** EfficientDet, DINO-FAN_base

## Input/Output Format

**Input:**
- Type: Image
- Format: Red, Green, Blue (RGB)
- Resolution: 416x416 and 960x544 (W x H)
- Parameters: 2D

**Output:**
- Type: Label(s)
- Format: Text String
- Category: Single category label returning whether object is retail or not

## Training Data
- **Primary dataset:** 320,000 proprietary synthetic images created via domain randomization with variations in light types/intensities, object sizes/orientations, camera locations, and background textures
- **Fine-tuning data:** Approximately 600 real proprietary images from 6 different environments (checkout counter, shelf, baskets, conveyor belt)
- **Total synthetic data:** 1,500,000 images (1,425,000 training, 75,000 validation)
- **Real data:** 649 images across multiple retail scenarios

## Intended Users
Developers building retail automation and video analytics applications using NVIDIA TAO Toolkit and DeepStream SDK.

## License
Not explicitly stated on this page.

## Version/Date
- **Latest Version:** deployable_retail_object_detection_binary_v2.2.2.3 (Signed)
- **Updated:** August 19, 2024 UTC
- **Compressed Size:** 299.56 MB

## Download/Getting Started Instructions

**Using NGC CLI:**
```
ngc registry model download-version nvidia/tao/retail_object_detection:deployable_retail_object_detection_binary_v2.2.2.3
```

**With TAO Toolkit:**
Access the unpruned model as pretrained weights for transfer learning through TAO experiment spec files.

**With DeepStream SDK:**
Deploy using DeepStream 6.2+ with provided config files located in `$DS_TAO_APPS_HOME/configs/retailDetector_tao/`

## Tags
AI, Computer Vision, CV, Deep Learning, DeepStream, Metropolis, Smart City, Smart Infrastructure, TAO, TAO Toolkit, TLT, Transfer Learning, Transfer Learning Toolkit
