# CWIP (Contrastive World-Image Pre-training)
Source: https://catalog.ngc.nvidia.com/orgs/nvidia/cosmos/models/cwip

## Model Name
CWIP (Contrastive World-Image Pre-training)

## Description/Overview
"CWIP projects a camera frame and a world-model frame into a joint embedding space to score camera-to-world consistency and emit per-patch object-presence and object-type classifications." It was developed by NVIDIA for the Cosmos Evaluator suite to assess generative world foundation models.

## Use Case
The model targets "developers and researchers building, evaluating, or auditing generative world foundation models for autonomous driving." Applications include per-frame embeddings, alignment scoring, defect detection, object classification, and quality assessment of driving-video generations.

## Model Architecture
**Type:** Transformer-based dual-encoder

"A custom dual-encoder architecture that encodes a pair of world-model control frame and camera frame, and outputs global embeddings for each frame and two segmentation masks for consistency and object-type prediction respectively."

The model uses PE-Spatial-B16-512 as a frozen image encoder with trainable alignment layers and patch classifiers. It contains 0.3 billion parameters and was trained at 1280x720 resolution with BF16 precision.

## Input Format
- **Type:** Image (RGB)
- **Dimensions:** Three-Dimensional
- **Details:** Paired camera and world-model frames; camera frames are resized to match world frame dimensions if needed

## Output Format
- **Types:** Embeddings and Segmentation Masks
- **Format:** 1D and 3D tensors
- **Details:** L2-normalized 1024-dimensional global embeddings per frame, defect classifications (MATCH, EXTRA, MISSING, WRONG, DONT_CARE), and 18-class object-type classifications

## Training Data
"Approximately 136,000 camera and world-model video pairs of driving scenes. Each video is approximately 20 seconds long." Collection and labeling were automated.

## Evaluation Data
- Real driving scenes: ~7K video pairs (~20 seconds each) with automated and manual labeling
- Synthetic scenes: ~1.2K video pairs (~10 seconds each) with human labels

## Intended Users
Developers and researchers working with generative world models for autonomous driving applications, including NVIDIA Cosmos users and Cosmos Evaluator suite users.

## License
**Name:** OpenMDW-1.1

**Link/Clause:** https://openmdw.ai/license/1-1/

## Tags/Labels
- Automotive / Transportation
- Cosmos Evaluator
- NSPECT-1Z2M-A9U5

## Version & Release Date
**Version:** 1.0.1 (Latest)

**Release Date:** July 7, 2026

**Availability:**
- GitHub: https://github.com/nvidia-cosmos/cosmos-evaluator
- NGC: https://catalog.ngc.nvidia.com/orgs/nvidia/cosmos/models/cwip
- HuggingFace: https://huggingface.co/nvidia/CWIP-1.0

## Getting Started / Download Instructions
"Use the NGC CLI to download" the model. Model weights are available in HuggingFace safetensors format. PyTorch is required for inference. Reference implementation is available in the Cosmos Evaluator repository.

## Technical Specifications
- **Runtime Engines:** PyTorch, Transformers (optional)
- **Supported Hardware:** NVIDIA Ampere, Hopper, Lovelace
- **Operating System:** Linux
- **Compressed Size:** 569.64 MB
