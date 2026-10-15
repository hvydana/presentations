# Cosmos-Embed1
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1

## Model Name
**Cosmos-Embed1**

## Description/Overview
"Cosmos-Embed1 is a joint video-text embedder tailored for physical AI." The model supports text-to-video retrieval, inverse video search, semantic deduplication, zero-shot and k-nearest-neighbors classification, and serves as a foundation for video curation tasks. It demonstrates state-of-the-art performance on autonomous vehicle and robotics datasets while maintaining competitive general-domain performance. A specialized variant exists for video anomaly detection applications.

## Use Case
The model targets "Physical AI developers and engineers for video-text embedding tasks including text-to-video retrieval, video-to-video search, zero-shot classification, and semantic deduplication across robotics, autonomous vehicles (AV), video anomaly detection, and diverse video understanding domains."

## Model Architecture

**Type:** Transformer-based

**Network:** "QFormer-based video-text embedder with EVA-ViT-G visual backbone"

The system processes video frames individually through a ViT backbone, concatenates per-frame features temporally with temporal embeddings, then passes them through QFormer to produce compact visual query tokens. Text undergoes tokenization via QFormer's self-attention branch. Both modalities align through contrastive video-text loss plus auxiliary losses (matching and captioning). The 336p and 448p variants employ additional summary and dense distillation losses.

**Parameters:** Approximately 1.0×10^9

## Input/Output Format

**Input:**
- Mode: Text OR video (one per forward pass, not simultaneous)
- Text: "String (UTF-8)" truncated/padded to 128 tokens
- Video: "Tensor scaled from 0 to 1 of RGB frame sequences" with shape [batch_size, channels, num_frames, height, width]
- Supports "arbitrary, non-square resolutions" and optimizes for 8 frames at 1-2 FPS

**Output:**
- "Floating-point normalized embedding vector" in shared vector space
- Dimensions: 256 (224p variant) or 768 (336p and 448p variants)
- L2-normalized for cosine similarity calculation

## Model Variants

| Variant | Resolution | Frames | Embedding Dim |
|---------|-----------|--------|---------------|
| Cosmos-Embed1-224p | 224×224 | 8 | 256 |
| Cosmos-Embed1-336p | 336×336 | 8 | 768 |
| Cosmos-Embed1-448p | 448×448 | 8 | 768 |
| Cosmos-Embed1-448p-anomaly-detection | 448×448 | 8 | 768 |

## Training Data

**Dataset:** Vad-Reasoning SFT subset containing 593 training videos aggregated from six sources:
- UCF-Crime (real-world crime footage)
- XD-Violence (violent events)
- TAD (traffic anomalies)
- ShanghaiTech (campus scenes)
- ECVA (multi-scene benchmark)
- Internet videos

**Processing:** Original videos split into 5-second chunks paired with text captions derived from anomaly type annotations

**Data Modality:** Video

**Total Size:** Less than 10,000 hours

**Annotation:** "Hybrid: Human, Automated (multi-stage annotation pipeline using proprietary models)"

**Anomaly Categories:** 24 unique types including abuse, arson, explosions, fighting, fire, flooding, illegal lane changing, obstacles, pedestrian violations, robberies, shootings, theft, tornadoes, traffic accidents, vandalism, and wrong-way driving

## Evaluation Datasets

**Vad-Reasoning Test Set:** 152 video clips from public cameras used for anomaly classification and retrieval evaluation

**Kinetics-400 Validation Set:** "19,877 video clips (~10s each) covering 400 human action classes" for zero-shot action classification

## Intended Users
The model suits physical AI developers and robotics/autonomous vehicle engineers requiring video-text embedding capabilities across multiple applications.

## License

**License Name:** NVIDIA Open Model License

**Terms:** "Use of this model is governed by the NVIDIA Open Model License."

**Additional Information:** Apache 2.0 and MIT licensing components included

**Location:** https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/

## Tags
- Cosmos
- NSPECT-WSL3-G6WC
- Physical AI
- PyTorch
- Transformer

## Version & Date
- **Version:** v1.0
- **Updated:** May 9, 2026 UTC
- **Hugging Face Release:** 06/15/2025
- **Compressed Size:** 4.46 GB

## Getting Started / Download Instructions

**Via HuggingFace Transformers:**

```python
from transformers import AutoProcessor, AutoModel
import torch

model = AutoModel.from_pretrained(
    "nvidia/Cosmos-Embed1-448p", trust_remote_code=True
).to("cuda", dtype=torch.bfloat16)
```

**Via TAO Toolkit:** Supports fine-tuning with full training or LoRA, evaluation with metrics visualization, inference for similarity search, ONNX export, and HuggingFace export.

**Supported Frameworks:**
- PyTorch
- Transformer Engine (optional)
- ONNX Runtime
- NVIDIA TensorRT

**Hardware Compatibility:** NVIDIA Ampere, Hopper, and Blackwell GPUs

**Operating System:** Linux
