# FaceNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/facenet

## Model Name
**FaceDetect** (also referenced as FaceNet)

## Description/Overview
"The model described in this card detects one or more faces in the given image / video. Compared to the FaceirNet model, this model gives better results on RGB images and smaller faces."

## Use Case
Face detection for video analytics applications across multiple domains including public safety, retail, smart cities/spaces, and healthcare.

## Model Architecture
The model employs "NVIDIA DetectNet_v2 detector with ResNet18 as a feature extractor." This GridBox object detection system "divides an input image into a grid which predicts four normalized bounding-box parameters (xc, yc, w, h) and confidence value per output class." Post-processing requires clustering algorithms like DBSCAN or NMS.

## Input/Output Format

**Input:**
- "736 X 416 X 3" dimension tensors
- "Channel Ordering of the Input: NCHW"
- "Input scale: 1/255.0"
- Grayscale images with identical RGB channel values

**Output:**
- "46x26x4 bbox coordinate tensor and 46x26x1 class confidence tensor"
- Category labels and bounding-box coordinates for detected faces

## Training Data
"FaceNet v2.0 model was trained on a proprietary dataset with more than 1.8M faces." The dataset includes "images taken from cameras mounted at varied heights and angles, cameras of varied field-of view (FOV) and occlusions."

**Labeling Guidelines:**
- "Face bounding boxes should be as tight as possible"
- Occlusion levels 0-5 considered for training
- Images with truncation visibility below 60% excluded

## Intended Users
Developers using NVIDIA hardware and software, specifically those working with "Train Adapt Optimize (TAO) Toolkit, DeepStream 6.0 or TensorRT."

## License
"License to use this model is covered by the Model EULA." Users "accept the terms and conditions of these licenses" at: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
Computer Vision, Object Detection, DeepStream, DetectNet_v2, TAO Toolkit, Healthcare, Public Safety, Retail, Smart Cities/Spaces

## Version & Date
**Latest Version:** pruned_quantized_v2.0.1
**Updated:** November 27, 2024 UTC
**Compressed Size:** 5.51 MB

## Download/Getting Started
Access via NGC CLI or visit the NGC Catalog. "Get TAO Container" for training; deploy using DeepStream or TensorRT. Model load key: `nvidia_tlt`
