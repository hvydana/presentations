# MONAI VISTA2D Model
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/monaitoolkit/models/monai_vista2d

## Model Name
**monai_vista2d**

## Description/Overview
"VISTA-2D is a comprehensive training and inference pipeline for cell segmentation in imaging applications." The model represents a generalist approach to cell segmentation, trained on approximately 15,000 public microscopy images across diverse cell types and imaging modalities.

## Use Case
Cell segmentation in microscopy imaging applications, supporting multiple imaging modalities and cell types with capability for fine-tuning on custom datasets.

## Model Architecture
The system employs "a robust deep learning algorithm based on transformers" and incorporates components from SegmentAnything and Cellpose projects. It follows MONAI bundle format specifications.

## Input/Output Format
- **Input:** Microscopy images (supports multiple file formats and modalities)
- **Output:** Segmented cell masks and annotations

## Training Data
Approximately 15,000 annotated cell images from public datasets including TissueNet, LIVECell, Omnipose, DeepBacs, and Cellpose datasets. Training ensures "broad coverage of many different types of cells, which were acquired by various imaging acquisition types."

## Intended Users
Researchers and practitioners in medical imaging, cell biology, and computational microscopy requiring automated cell segmentation capabilities.

## License
- **Codebase:** Apache 2.0
- **Model Weights:** CC-BY-NC-SA-4.0
- **Data:** Multiple licenses—refer to `data_license.txt`

## Tags
Bundle, Deep Learning, Healthcare, Imaging, Medical, Medical Imaging, MONAI, PyTorch, Segmentation

## Version & Date
**Version:** 0.3.0
**Updated:** November 12, 2024 UTC
**Compressed Size:** 703.87 MB

## Getting Started / Download Instructions

Install dependencies:
```bash
pip install fastremap==1.15.0 roifile==2024.5.24 natsort==8.4.0
pip install --no-deps cellpose
```

Execute inference:
```bash
python -m monai.bundle run --config_file configs/inference.json
```

Execute training:
```bash
python -m monai.bundle run_workflow "scripts.workflow.VistaCell" --config_file configs/hyper_parameters.yaml
```

Multi-GPU training:
```bash
torchrun --nproc_per_node=gpu -m monai.bundle run_workflow "scripts.workflow.VistaCell" --config_file configs/hyper_parameters.yaml
```

**Compute Requirements:** Minimum 16GB GPU memory
