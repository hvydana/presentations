# NVIDIA AI Enterprise Software License Agreement

Source: https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/

Used by 3 models in the current per-model table's "NVIDIA AI Enterprise EULA" bucket; previously verified
(session history) as the license bound to ~10 older TAO purpose-built models on NGC (ActionRecognitionNet,
LPRNet, LPDNet, TrafficCamNet, VehicleMakeNet, PointPillarNet, FaceNet, GazeNet, OCDNet, OCRNet) — either via
an explicit "License to use this model is covered by the Model EULA" clause or a "Licensing:" metadata field
on the catalog page.

## Hardware Restriction — Section 8.15, "NVIDIA Platform Requirement"
Ties usage to NVIDIA's certified stack — scoped to "software development kits (CUDA toolkit, TensorRT,
cuDNN), drivers, and Omniverse," not to the model weights/checkpoints in general. The restriction bites once
the model is paired with NVIDIA's SDK/driver stack for production deployment — which is NVIDIA's
recommended/blessed deployment path for these models — but the clause does not unambiguously state that the
downloaded model artifact itself can only run on NVIDIA GPUs.

## Contrast
BodyPoseNet, on the same NGC catalog, uses CC-BY-4.0 instead — fully open, no NVIDIA-specific terms at all —
showing the EULA choice is model-specific, not catalog-wide.
