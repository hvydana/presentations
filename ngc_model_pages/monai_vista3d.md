# MONAI VISTA3D Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_vista3d

## Model Name
**monai_vista3d**

## Description/Overview
"VISTA-3D is a specialized interactive foundation model for 3D medical imaging." The model supports both automatic segmentation using class prompts and interactive point-based segmentation for binary object detection.

## Use Cases
The model is designed for segmentation tasks in 3D medical imaging, particularly CT scans. It supports:
- Automatic segmentation of 127 organ and anatomical classes
- Interactive point-click segmentation for specific objects
- Continual learning/finetuning on custom datasets

## Model Architecture
The VISTA-3D architecture consists of:
- A vision encoder for processing 3D medical images
- A class head for label-based (automatic) segmentation
- A point branch for interactive segmentation via point prompts
- Support for TensorRT acceleration

## Input/Output Format

**Input:**
- 3D medical imaging data in NIfTI format (.nii.gz)
- Optional prompts: `label_prompt` (list of class indices) or `points` with `point_labels`
- Points formatted as "[x1,y1,z1],[x2,y2,z2]" in original image space

**Output:**
- Segmentation masks in NIfTI format matching input header information
- Class predictions mapped to VISTA-3D global class indices (1-132)
- Value 255 represents 'NaN' for unmapped regions

## Training Data Used
The foundation model was trained on "over 20 partial datasets" including:
- Medical Segmentation Decathlon datasets
- AbdomenCT-1K
- Multiple organ and anatomical structure datasets

The bundle documentation references the spleen task from Medical Segmentation Decathlon as an example for continual learning.

## Intended Users
- Healthcare/medical imaging professionals
- Researchers in medical image analysis
- Developers implementing 3D segmentation pipelines
- Advanced users capable of dataset preparation and model finetuning

## License

**Code License:**
"Apache License 2.0" - accessible at http://www.apache.org/licenses/LICENSE-2.0

**Model Weights License:**
"NCLS v1 License"

Both licenses are combined in the project's LICENSE file.

## Tags
- Bundle
- Deep Learning
- Healthcare
- Imaging
- Medical
- Medical Imaging
- MONAI
- PyTorch
- Segmentation

## Version and Date
**Version:** 0.5.4
**Updated:** November 27, 2024 UTC
**Compressed Size:** 831.69 MB

## Getting Started Instructions

### Single Image Inference
```bash
python -m monai.bundle run --config_file configs/inference.json
```

### Batch Inference
```bash
python -m monai.bundle run --config_file="['configs/inference.json', 'configs/batch_inference.json']" \
  --input_dir="/data/Task09_Spleen/imagesTr" --output_dir="./eval_task09"
```

### Single-GPU Training
```bash
python -m monai.bundle run \
  --config_file="['configs/train.json','configs/train_continual.json']" \
  --epochs=320 --learning_rate=0.00005
```

### Multi-GPU Training
```bash
torchrun --nnodes=1 --nproc_per_node=8 -m monai.bundle run \
  --config_file="['configs/train.json','configs/train_continual.json','configs/multi_gpu_train.json']" \
  --epochs=320 --learning_rate=0.00005
```

### TensorRT Acceleration
```bash
python -m monai.bundle run --config_file "['configs/inference.json', 'configs/inference_trt.json']"
```

## Key Configuration Parameters

- **patch_size**: Default [128, 128, 128]; adjust based on GPU memory
- **resample_to_spacing**: Default [1.5, 1.5, 1.5] mm; optimize per task
- **label_mappings**: Maps local dataset labels to global VISTA classes
- **drop_label_prob** / **drop_point_prob**: Control prompt types during training (default 0.25 each)
