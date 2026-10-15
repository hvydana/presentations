# NVIDIA Deep Learning Models License Agreement ("Model EULA")

Full text saved as: `nvidia_deep_learning_models_license_agreement.pdf` (fetched from
https://developer.download.nvidia.com/licenses/tao_toolkit_21-08_models_eula.pdf — version dated August 10, 2021).

This is the document NGC catalog pages refer to as "Model EULA." It is a **separate document from the TAO
Toolkit SDK license** and applies directly to the downloaded model weights themselves. Used by 20 models in
the NGC physical-AI list (older TAO purpose-built models: LPRNet, LPDNet, TrafficCamNet, VehicleMakeNet,
PointPillarNet, FaceNet, GazeNet, OCDNet, OCRNet, ActionRecognitionNet, Bi3D Proximity Segmentation, etc.)

## Commercial Use
Permitted in general (Section 1.1: install and use the SOFTWARE). No blanket "non-commercial only" clause.

## Hardware Restriction — explicit, on the model's own license
> "The SOFTWARE is licensed for you to develop applications **only for use in systems with NVIDIA GPUs**."
(Section 1.1)

This is the same class of clause previously found only in the separate TensorRT SDK Supplement — here it is
present in the model's own EULA, not just the tooling's.

## Redistribution — restricted
> Section 2.2: "Except as expressly provided in this Agreement, you may not sell, rent, sublicense, transfer
or distribute the SOFTWARE. For clarity, you may not distribute or sublicense the SOFTWARE as a stand-alone
product."

A limited distribution grant exists (Section 1.1(ii) / 1.2) but only if the model is embedded inside an
application with "material additional functionality" beyond the model itself, and:
- "unpruned"/"trainable"/"train-ready" variants are only distributable after being trained via NVIDIA TAO
  Toolkit (a separate NVIDIA tool)
- "pruned"/"deployable" variants may be distributed as provided by NVIDIA
- You must notify NVIDIA of any known/suspected non-compliant distribution

## Other notable clauses
- Section 2.5: you may not use the SOFTWARE in any way that would cause it to become subject to an open
  source license (no copyleft-triggering use).
- Section 2.1: no reverse engineering, decompiling, or removing proprietary notices.
- Section 6.3(iii): NVIDIA may terminate the agreement "in NVIDIA's sole discretion" if continued use is "no
  longer commercially viable" for NVIDIA.

## Bottom line for AMD
Strictly read, deploying one of these 20 models on AMD hardware falls outside the license grant — the
agreement only licenses use "in systems with NVIDIA GPUs." This is a direct, model-level hardware lock-in,
not merely an SDK/tooling restriction.
