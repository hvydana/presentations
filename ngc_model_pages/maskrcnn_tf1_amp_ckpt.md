# Mask R-CNN TensorFlow Checkpoint (AMP)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/models/maskrcnn_tf1_amp_ckpt

## Model Name
Mask R-CNN TensorFlow checkpoint (AMP)

## Description/Overview
"Mask R-CNN is a convolution based network for object instance segmentation."

## Use Case
Object instance segmentation and image segmentation tasks.

## Model Architecture
The model incorporates several key components:
- ResNet-50 backbone with Feature Pyramid Network (FPN)
- Region proposal network (RPN) head
- RoI Align
- Bounding and classification box head
- Mask head

"Mask R-CNN builds on top of Faster R-CNN adding a mask head for the task of image segmentation."

## Input/Output Format
Not explicitly specified in the provided content.

## Training Data
"The following datasets were used to train this model: COCO 2017 - Dataset for large-scale object detection, segmentation and captioning."

## Intended Users
Computer vision practitioners and researchers using TensorFlow for segmentation tasks.

## License
"This model was trained using open-source software available in Deep Learning Examples repository." For specific license terms, users should refer to the Deep Learning Examples repository license and associated dataset licenses.

## Tags
- Computer Vision
- Deep Learning Examples

## Version/Date
**Latest Version:** 20.06.1
**Updated:** April 4, 2023 UTC
**Compressed Size:** 780.49 MB

## Getting Started
Use the NGC CLI to download the checkpoint. Additional resources available at the [NVIDIA GitHub repository](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow2/Segmentation/MaskRCNN).
