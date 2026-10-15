# TrafficCamNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/trafficcamnet

## Description/Overview
"4 class object detection network to detect cars in an image." The model detects cars, persons, road signs, and two-wheelers in images and is ready for commercial use.

## Use Case
The intended primary use is detecting vehicles in color (RGB) images from photos and videos. Secondary use cases include detecting persons, road signs, and two-wheelers from images or videos.

## Model Architecture
- **Architecture Type:** Convolutional Neural Network (CNN)
- **Network Architecture:** DetectNet_v2 + ResNet18 (Feature Extractor)

The system divides input images into a grid which predicts normalized bounding-box parameters (xc, yc, w, h) and confidence values per output class. Raw detections require post-processing with algorithms such as DBSCAN or NMS.

## Input Format
- **Type:** Images
- **Format:** Red, Green, Blue (RGB)
- **Dimensions:** 960 x 544 x 3 (W x H x C)
- **Channel Ordering:** NCHW (N = Batch Size, C = 3 channels, H = 544, W = 960)
- **Input Scale:** 1/255.0
- **Mean Subtraction:** None

## Output Format
- **Types:** Labels, Bounding-Boxes, Confidence Scores
- **Labels:** Text strings for persons, road signs, two-wheelers, vehicles
- **Bounding Box Format:** (x-coordinate, y-coordinate, width, height)
- **Confidence Scores:** Floating point values

## Training Data
Two proprietary internal datasets were used:

1. **Traffic Camera Dataset:** 160,000 images containing 1.1M cars, 53,500 persons, 184,000 road signs, 11,000 two-wheelers from US traffic cameras
2. **Dashcam Dataset:** 40,000 images containing 1.7M cars, 720,000 persons, 354,127 road signs, 54,000 two-wheelers

**Total:** 200,000 images with 2.8M cars, 773,500 persons, 538,127 road signs, 65,000 two-wheelers

**Collection Method:** Automatic/Sensors
**Labeling Method:** Human

Objects smaller than 10px height or width were excluded. Partially occluded objects with 60%+ visibility were annotated.

## Performance Metrics
Evaluated on 19,000 internal proprietary images using Intersection-over-Union (IOU) > 0.5:

- **Precision:** 92.65%
- **Recall:** 89.95%
- **Accuracy:** 83.9%

Metrics focused on car detection class only.

## Runtime Engines
- TAO 5.1
- DeepStream 6.1 or later

## Supported Hardware
- Ampere, Jetson, Hopper, Lovelace, Pascal, Turing

## Preferred Operating Systems
- Linux
- Linux 4 Tegra

## Model Versions
- **unpruned_v1.0:** ResNet18 pre-trained model for training
- **pruned variants:** Deployment-optimized models with INT8 calibration caches

## License
No explicit license name or clause was provided on this page. Access appears governed by NVIDIA's NGC Catalog Terms of Use and NVIDIA AI Enterprise support designation.

## Tags
AI, CV, DeepStream, NVIDIA AI, Smart Cities/Spaces, Smart Infrastructure, TAO Toolkit, Transfer Learning

## Version & Date
**Latest Version:** pruned_onnx_v1.0.4 (Signed)
**Updated:** July 17, 2025 UTC
**Compressed Size:** 5.13 MB

## Getting Started / Download Instructions

### NGC CLI Download
Use the NGC CLI command (specific command shown as copyable in interface)

### DeepStream Deployment
1. Download model and calibration file:
```
mkdir -p $HOME/trafficcamnet && \
wget https://api.ngc.nvidia.com/v2/models/nvidia/tao/trafficcamnet/versions/pruned_v1.0/files/resnet18_trafficcamnet_pruned.etlt \
-O $HOME/trafficcamnet/resnet18_trafficcamnet_pruned.etlt && \
wget https://api.ngc.nvidia.com/v2/models/nvidia/tao/trafficcamnet/versions/pruned_v1.0/files/trafficnet_int8.txt \
-O $HOME/trafficcamnet/trafficnet_int8.txt
```

2. Run with Docker:
```
xhost +
sudo docker run --gpus all -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY \
-v $HOME:/opt/nvidia/deepstream/deepstream-5.1/samples/models/tlt_pretrained_models \
-w /opt/nvidia/deepstream/deepstream-5.1/samples/configs/tlt_pretrained_models \
nvcr.io/nvidia/deepstream:5.1-21.02-samples \
deepstream-app -c deepstream_app_source1_trafficcamnet.txt
```

### TAO Toolkit Usage
Models use encryption key: **tlt_encode**

## Model Load Key
"tlt_encode" required for all TAO commands

## Ethical Considerations
"Training and evaluation dataset mostly consists of North American content. An ideal training and evaluation dataset would additionally include content from other geographies."

Developers should evaluate algorithmic bias when deploying and verify the model meets industry requirements and use case specifications.
