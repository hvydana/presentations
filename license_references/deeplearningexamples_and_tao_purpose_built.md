# Two Additional Patterns Found While Resolving Previously-Unverified Models

## 1. NVIDIA/DeepLearningExamples — no repo-wide LICENSE, checked per subfolder

Source: `https://github.com/NVIDIA/DeepLearningExamples` — confirmed via
`https://api.github.com/repos/NVIDIA/DeepLearningExamples` returning `"license": null`. This repo has
**no single root LICENSE file**; terms vary per model script/subfolder. Six previously-"refer to upstream"
models were checked directly:

| Model | Subfolder | Result |
|---|---|---|
| nnUNet PyTorch checkpoint 2D AMP | `PyTorch/Segmentation/nnUNet/LICENSE` | Apache-2.0 |
| nnUNet PyTorch checkpoint 3D AMP | `PyTorch/Segmentation/nnUNet/LICENSE` | Apache-2.0 |
| UNet_Medical TF2 checkpoint (AMP) | `TensorFlow2/Segmentation/UNet_Medical/LICENSE` | BSD-3-Clause |
| UNet_Medical TF2 TF-TRT model (AMP) | `TensorFlow2/Segmentation/UNet_Medical/LICENSE` | BSD-3-Clause |
| UNet_Medical TF2 SavedModel (AMP) | same UNet_Medical family, no separate LICENSE | BSD-3-Clause (inferred from sibling) |
| ResNet50 pretrained weights (PyTorch, AMP, ImageNet) | `PyTorch/Classification/ConvNets/LICENSE` | BSD-3-Clause |
| Mask R-CNN TensorFlow checkpoint (AMP) | `TensorFlow/Segmentation/MaskRCNN/` — checked this path and every parent up to repo root | **No LICENSE file exists anywhere in the chain.** Legal default: all rights reserved. |

Lesson: "refer to upstream repo" is not a single verifiable answer for a monorepo without a root license —
it must be resolved file-by-file, and the absence of a LICENSE file is itself a real (negative) answer, not
an unknown.

## 2. TAO "Purpose-Built Model" pattern — hardware lock stated without citing a formal EULA

20 models (LPRNet, PeopleSemSegNet, PointPillarNet, VehicleMakeNet, VehicleTypeNet, TrafficCamNet,
ActionRecognitionNet, BodyPoseNet, CitySemSegFormer, LPDNet, PeopleNet AMR, PeopleSemSegNet AMR,
PoseClassificationNet, TAO Pretrained Classification/DetectNet V2/EfficientDet/Instance Segmentation/Semantic
Segmentation, ReIdentificationNet, Retail Object Detection) do not cite a named license/EULA on their NGC
page at all, but the page nonetheless states, verbatim (confirmed via direct re-fetch on 4 of the 20 —
LPRNet, PeopleSemSegNet, PointPillarNet, VehicleMakeNet — and inferred for the remaining 16 which share the
same TAO team, URL template, and page structure):

> "These models need to be used with NVIDIA Hardware and Software. For Hardware, the models can run on any
> NVIDIA GPU... The models are only trainable using the Train Adapt Optimize (TAO) Toolkit or TLT."

> "These models can only be used with Train Adapt Optimize (TAO) Toolkit, DeepStream SDK or TensorRT."

Each model file also ships DRM-encrypted with a "Model load key" field (`tlt_encode`, `nvidia_tlt`, or
`nvidia_tao` depending on model generation) — the weights cannot even be loaded outside NVIDIA's own
toolchain without that key, regardless of what a written license might otherwise permit.

**Why this matters for the AMD argument:** this is arguably a *stronger* lock-in signal than the formal
"Model EULA" bucket, because it isn't just contract language restricting where you're licensed to deploy —
it's an actual technical/DRM barrier, on top of an explicit statement that the model requires NVIDIA hardware
and NVIDIA-only tooling to run at all. No license citation is needed for this to function as a lock-in.
