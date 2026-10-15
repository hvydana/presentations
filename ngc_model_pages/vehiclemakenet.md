# VehicleMakeNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/vehiclemakenet

## Description/Overview
"Resnet18 model to classify a car crop into 1 out 20 car brands." The model performs classification of vehicle makes across twenty distinct automotive brands.

## Use Cases
The model is designed for vehicle classification applications, particularly suited for video analytics pipelines in traffic monitoring, parking management, and smart city applications. It can function as a secondary classifier following primary vehicle detection.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Network:** ResNet18
- **Classification Model:** Features a ResNet18 backbone for image classification

## Input/Output Format

**Input Specifications:**
- Type: Images in RGB format
- Resolution: 224 x 224 x 3 (Width x Height x Channels)
- Channel Ordering: NCHW (Batch Size, Channels=3, Height=224, Width=224)
- Mean Subtraction: [103.939, 116.779, 123.68]

**Output Specifications:**
- Type: Text string labels
- Categories: "Acura, Audi, BMW, Chevrolet, Chrysler, Dodge, Ford, GMC, Honda, Hyundai, Infiniti, Jeep, Kia, Lexus, Mazda, Mercedes, Nissan, Subaru, Toyota, and Volkswagen"

## Training Data
- Dataset size: Over 60,000 car images
- Source: Internal proprietary dataset
- Characteristics: "Mix of camera heights, camera angles, field-of view (FOV) and occlusions"
- Labeling method: Human-annotated
- Collection: Automatic/Sensors-based

## Evaluation Performance
- Evaluation dataset: 2,000 images from internal proprietary collection
- Top-1 Accuracy: 91%

## Intended Users
Developers building video analytics applications using NVIDIA hardware and software frameworks, including those utilizing DeepStream SDK, TAO Toolkit, or TensorRT.

## License
No specific license name or terms are displayed on this model page. The page references "Terms of Use" and "Terms of Service" links but does not specify an open-source license.

## Tags
Computer Vision, CV, DeepStream, Metropolis, NVIDIA AI, Public Safety, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, Traffic, Vehicle Classification

## Version/Date
- Latest Version: pruned_onnx_v1.1.0 (Signed)
- Last Updated: November 27, 2024 UTC
- Compressed Size: 7.07 MB

## Getting Started/Download Instructions

**Using NGC CLI:**
Users can download via the NGC Command Line Interface with provided commands.

**Model Variants Available:**
- unpruned_v1.0 (for training/transfer learning)
- pruned_v1.0 and pruned_onnx_v1.1.0 (for deployment)

**Model Load Key:** `tlt_encode`

**Deployment with DeepStream:**
Download model files and configure using provided config files. "Run deepstream-app with configuration that deploys DashCamNet as primary detector and VehicleMakeNet as secondary classifier."

**TAO Toolkit Instructions:**
Use provided experiment spec templates with training configuration specifying batch size, learning rate, epochs, and regularization parameters for fine-tuning on custom datasets.
