# TAO Pretrained DINO with Foundational Model Backbone
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/dino_with_fm_backbone

## Model Name
TAO Pretrained DINO with Foundational Model Backbone

## Description/Overview
"Object detection is a popular computer vision technique that can detect one or multiple objects in a frame." This model provides pre-trained weights for DINO object detection networks trained on the COCO dataset, designed to facilitate transfer learning through the TAO Toolkit.

## Use Case
The model is intended for detecting objects in color (RGB) images from photos and videos. It supports applications in smart cities, retail, healthcare, and industrial inspection. The model is designed for training and fine-tuning with the TAO Toolkit on custom datasets for object detection purposes.

## Model Architecture
The detector uses an NVDINOv2 backbone trained via self-supervised learning on NVIDIA proprietary data. "The ViT-Adapter improves the accuracy on dense predictions, such as object detection." The architecture takes RGB images as input and outputs bounding boxes and object classes. Images are resized to 1536 x 1536 using Large Scale Jittering during training, as ViT requires square resolutions divisible by 16.

## Input/Output Format

**Input:** B X 3 X 1536 X 1536 (B C H W)

**Output:** "Category labels (80 COCO) and bounding-box coordinates for each detected objects in the input image."

## Training Data
"DINO was trained on the COCO 2017 dataset, which contains 118K training images and 5K validation images with corresponding annotation files." The annotations include bounding boxes for 80 object categories.

## Performance Metrics
Evaluated on COCO 2017 validation dataset:
- mAP: 57.8 (FP16)
- mAP50: 76.7
- mAP75: 63.1
- mAPs: 41.2
- mAPm: 61.4
- mAPl: 72.7

Real-time inference performance varies by platform (0.46 FPS on AGX Orin to 6.99 FPS on H100 at batch size 2, INT8 precision).

## Intended Users
Organizations requiring NVIDIA hardware and software. Users must have access to NVIDIA GPUs (including Jetson devices). Models are intended for use with TAO Toolkit, DeepStream SDK, or TensorRT only.

## License
"This work is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 License (CC-BY-NC-SA-4.0)."

License link: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Tags
- Computer Vision
- CV
- Deep Learning
- Object Detection
- TAO
- TAO Toolkit

## Version and Date
- **Latest Version:** trainable_v1.0
- **Updated:** January 5, 2024 UTC
- **Compressed Size:** 3.61 GB
- **Available Versions:**
  - dino_dinov2_trainable_v1.0 (pre-trained for fine-tuning)
  - dino_dinov2_deployable_v1.0 (deployable to DeepStream)

## Getting Started Instructions

### Download
"Use the NGC CLI to download:" (specific command provided via NGC platform)

### Using with TAO Toolkit
Use this configuration template in the experiment spec file:

```
train:
  pretrained_model_path: /path/to/the/dino_dinov2.pth
dataset:
  augmentation:
    fixed_random_crop: 1536
    test_random_resize: 1536
    random_resize_max_size: 1536
    fixed_padding: True
  num_classes: 91
model:
  backbone: vit_large_dinov2
  train_backbone: False
  num_feature_levels: 4
  dec_layers: 6
  enc_layers: 6
  num_queries: 900
  dropout_ratio: 0.0
  dim_feedforward: 2048
```

### Deployment
"Documentation to deploy with DeepStream is provided in 'Deploying to DeepStream' chapter of TAO User Guide" at https://docs.nvidia.com/tao/tao-toolkit/index.html

### Additional Resources
- [TAO Toolkit Documentation](https://docs.nvidia.com/tao/tao-toolkit/index.html)
- [TAO Toolkit Quick Start Guide](https://docs.nvidia.com/tao/tao-toolkit/text/tao_quick_start_guide.html)
- [TAO Toolkit Developer Forums](https://forums.developer.nvidia.com/c/accelerated-computing/intelligent-video-analytics/tao-toolkit/17)
