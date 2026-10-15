# NVIDIA Software License Agreement (TAO Toolkit) + TensorRT SDK Supplement

These two documents license the **deployment tooling itself** (TAO Toolkit, TensorRT) — not any model's
weights. They are not cited by name on any checked NGC catalog model page (checked: ActionRecognitionNet,
LPRNet, LPDNet, TrafficCamNet, VehicleMakeNet, BodyPoseNet, FaceNet, GazeNet, OCDNet, OCRNet, BEVFusion,
CenterPose, PointPillarNet, Mask2Former, PeopleNet). They apply once you use NVIDIA's SDK to
train/export/deploy a model, regardless of which model.

## TAO Toolkit SLA
Source: https://developer.download.nvidia.com/licenses/tao_toolkit_21-08.pdf — Section 1, "License Grant":
> "...license to install and use the SOFTWARE **in conjunction with your use of NVIDIA GPUs** including to
deploy a service to external users, provided that the SOFTWARE is not distributed."

## TensorRT SDK Supplement
Source: https://docs.nvidia.com/deeplearning/tensorrt/sla/ — Section 1, "License Scope":
> "The SDK is licensed for you to develop applications **only for use in systems with NVIDIA GPUs**."

## Bottom line
Unambiguous, blanket NVIDIA-GPU-only language — but it attaches to the tooling you use to train/export/
deploy a model, not to the model artifact itself. Running the same weights via ROCm or an open runtime
(ONNX Runtime, PyTorch native, TVM) sidesteps this specific clause; the lock-in here is in NVIDIA's
recommended production path, not in the model file.
