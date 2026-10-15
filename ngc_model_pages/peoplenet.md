# PeopleNet
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplenet

## Description/Overview
"3 class object detection network to detect people in an image." The model detects persons, bags, and faces and is ready for commercial use.

## Use Cases
- Primary: Detecting people in color (RGB) images from photos and videos
- Secondary: Detecting bags and faces from images or videos
- Specific application: Convenience-store retail analytics

## Model Architecture
- **Type:** Convolutional Neural Network (CNN)
- **Architecture:** DetectNet_v2 + ResNet34 (Feature Extractor)
- **Description:** Uses bounding-box regression on a uniform grid, dividing input images into grids that predict normalized bounding-box parameters (xc, yc, w, h) and confidence values per output class

## Input Format
- **Type:** Images (RGB)
- **Resolution:** 960 × 544 × 3 (W × H × C)
- **Channel Order:** NCHW (Batch Size, 3 channels, 544 height, 960 width)
- **Scale:** 1/255.0
- **Preprocessing:** No mean subtraction required

## Output Format
- **Types:** Labels, Bounding-Boxes, Confidence Scores
- **Labels:** Text strings (Bag, Face, Person)
- **Bounding Box:** (x-coordinate, y-coordinate, width, height)
- **Confidence Scores:** Floating point values

## Training Data
- **Dataset Size:** Internal proprietary dataset exceeding 7.6 million images of more than 71 million people
- **Collection Method:** Automatic/Sensors
- **Labeling Method:** Human-annotated
- **Composition:** Mix of cameras, heights, crowd densities, and field-of-view angles
- **Notable Details:** Approximately 50% indoor office environment at ~10 feet height, 45-degree angle; ~500K low-density images with extended hands/feet for pose estimation
- **Distribution:** 4.8M natural, 5.7M rotated, 566K broadcast images, plus simulation and blended variants
- **Total Annotations:** 41.3M persons, 12.3M bags, 18.4M faces

## Intended Users
Developers and organizations using NVIDIA hardware and software for video analytics applications requiring person detection capabilities.

## License
**License Name:** NVIDIA Open Model License

**License Link/Clause:** "By downloading the unpruned or pruned version of the model, you accept the terms and conditions of NVIDIA Open Model License."

## Tags/Labels
- DetectNet_v2 Architecture
- NSPECT-ITZN-CAOK

## Version Information
- **Latest Version:** pruned_quantized_decrypted_v2.3.4
- **Updated:** June 12, 2025 UTC
- **Compressed Size:** 8.4 MB

## Model Variants Available
- trainable_v2.5 (unpruned, floating-point)
- pruned_v2.3 (pruned, floating-point)
- pruned_quantized_v2.3 (pruned, INT8)
- deployable_quantized_v2.5 (unpruned, floating-point and INT8)

## Getting Started/Download Instructions

### Using NGC CLI
Models can be downloaded via NGC CLI with provided commands (copy available on page).

### Deployment with TAO Toolkit
Use ResNet34 configuration with model load key: `tlt_encode`

```
model_config {
  num_layers: 34
  pretrained_model_file: "/path/to/the/model.tlt"
  use_batch_norm: true
  objective_set {
    bbox {
      scale: 35.0
      offset: 0.5
    }
    cov {
    }
  }
  training_precision {
    backend_floatx: FLOAT32
  }
  arch: "resnet"
  all_projections: true
}
```

### Deployment with DeepStream
Models integrate with DeepStream SDK 6.1 or later via Docker or local installation with config files located in `/opt/nvidia/deepstream/deepstream-5.1/samples/configs/tlt_pretrained_models`

Required files:
- deepstream_app_source1_peoplenet.txt
- config_infer_primary_peoplenet.txt
- labels_peoplenet.txt

## Supported Hardware
Ampere, Jetson, Hopper, Lovelace, Pascal, Turing GPU architectures

## Operating Systems
Linux, Linux 4 Tegra
