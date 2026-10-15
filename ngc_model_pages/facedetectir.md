# FaceDetectIR
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/facedetectir

## Model Name
**FaceDetectIR**

## Description/Overview
"The model described in this card detects one or more faces in the given image / video." Compared to PeopleNet, it provides superior performance detecting large faces such as those in webcam imagery.

## Use Case
The primary use case involves detecting faces from infrared camera feeds. Secondary applications include face detection in RGB color images, though this is not the intended primary focus.

## Model Architecture
"The model is based on NVIDIA DetectNet_v2 detector with ResNet18 as a feature extractor." The GridBox object detection system divides input images into grids predicting normalized bounding-box parameters (xc, yc, w, h) and confidence values per class. Post-processing via DBSCAN or NMS clustering is required for final bounding-box coordinates.

## Input/Output Format

**Input:**
- Grayscale images with identical RGB channel values
- Dimensions: 384 × 240 × 3 (W × H × C)
- Channel ordering: NCHW format
- Input scale: 1/255.0
- Mean subtraction: None

**Output:**
"Category labels (faces) and bounding-box coordinates for each detected face in the input image."

## Training Data
"FaceDetectIR v1.0 model was trained on a proprietary dataset with more than 846K faces." The dataset comprises images from varied camera heights, angles, and fields of view, with occlusions. Training data consists primarily of infrared imagery supplemented with RGB images for improved accuracy.

## Performance Metrics
Evaluation on 16,559 proprietary images yielded:
- Precision: 99.8%
- Recall: 96.40%
- Accuracy: 96.21%

(Metrics based on IOU criterion > 0.5)

## Intended Users
Developers and organizations utilizing NVIDIA hardware and software ecosystems for video analytics, particularly in healthcare, public safety, retail, and smart infrastructure sectors.

## License
"License to use these models is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)."

## Tags
CV, DeepStream, DetectNet_v2, Healthcare, IR, Object Detection, Public Safety, Retail, Smart Cities, TAO Toolkit

## Version/Date
**Latest Version:** pruned_v1.0.1
**Updated:** November 12, 2024 UTC
**Compressed Size:** 9.09 MB

## Download/Getting Started
Two model flavors available:
- **unpruned_v1.0**: For training with TAO Toolkit
- **pruned_v1.0**: For deployment via DeepStream SDK or TensorRT

Download via NGC CLI or direct HTTP access. Model requires load key: `tlt_encode`
