# Visual ChangeNet Classification
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/visual_changenet_classification

## Description/Overview
The model "detects defective PCB components given component level PCB images." It takes a reference image and an inspection image as inputs and outputs a binary classification indicating whether a defect is present.

## Use Case
This model is intended for PCB component optical inspection, specifically to identify defects in electronic components like resistors, capacitors, and inductors on circuit boards.

## Model Architecture
Visual ChangeNet-Classification is described as "a state of the art transformer-based Change Detection model" based on Siamese Network architecture. The model supports two primary architectures:

- **Architecture 1**: Uses the final feature map from FAN backbone with Euclidean distance computation for contrastive loss optimization
- **Architecture 2**: Leverages feature maps from four transformer layers with MLP decoder and cross-entropy loss

The backbone network is FAN (Fully Attentional Networks).

## Input/Output Format

**Input:**
- Two RGB images: Golden (reference) and Sample (test image)
- Dimensions: 512 x 128 x 3 (H x W x C)
- Channel ordering: NCHW format

**Output:**
- "Classification score for the two input images. A threshold is specified to classify each as change vs no-change."

## Training Data
The model was trained on a proprietary NVIDIA internal dataset consisting of:
- 168,828 total images
- 42,207 individual components
- 105 PCB boards
- 4 different PCB designs
- 4 LED lighting conditions per component (Solder, Uniform, LowAngle, White)
- Defect rate: 0.15% (65 defects in 42,207 components)

## Performance
**Evaluation Results (21,148 validation components):**
- False Positive Rate: 0.3%
- Defect Capture Rate: 97.4%
- Score Cutoff: 0.03

**Real-time Inference Performance (FP16):**
- Orin Nano 8GB (BS 16): 30.97 FPS
- Orin NX 16GB (BS 16): 44.74 FPS
- AGX Orin 64GB (BS 16): 113.20 FPS

## Intended Users
Developers and organizations using NVIDIA hardware and software who need to:
- Train and fine-tune models with TAO Toolkit
- Deploy edge models using TensorRT
- Conduct PCB quality assurance and optical inspection

## License
License terms are covered by the "Model EULA" with specific reference to NVIDIA's standard licenses. Users must accept terms "by downloading the unpruned or pruned version of the model."

**License Link:** https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

## Tags
- Computer Vision
- CV
- Deep Learning
- Industrial Inspection
- Optical Inspection
- TAO
- TAO Toolkit
- NSPECT-6WYF-WMQW

## Version/Date
- **Latest Version:** visual_changenet_nvpcb_trainable_v1.0
- **Updated:** November 12, 2024 UTC
- **Compressed Size:** 270.12 MB

## Available Model Variants
1. changenet_nvpcb_solderlight_trainable_v1.0
2. changenet_nvpcb_solderlight_deployable_v1.0
3. changenet_nvpcb_trainable_v1.0
4. changenet_nvpcb_deployable_v1.0

## Getting Started Instructions
To use as pretrained weights for transfer learning, configure the experiment spec file with:

```
model:
  backbone:
    type: "fan_small_12_p4_hybrid"
    pretrained_backbone_path: null
  classify:
    train_margin_euclid: 2.0
    eval_margin: 0.005
    embedding_vectors: 5
    embed_dec: 30
    difference_module: 'learnable'
    learnable_difference_modules: 4
```

Refer to the TAO Toolkit User Guide for complete experiment specification details.

## Key Limitations
The model was trained exclusively on images with 4 LED lighting conditions. "Images captured different lighting conditions or less than 4 LED illuminations might not provide good detection results."
