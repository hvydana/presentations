# NGC Physical AI Models — Can AMD Use Them Commercially?

For each model's *actual stated license* (from its own NGC catalog page, or from the upstream repository where the NGC page pointed there), whether AMD (or any non-NVIDIA vendor) can (a) use the model commercially and (b) redistribute it commercially — plus whether the license ties usage to NVIDIA hardware/software.

See also: [license_terms_summary.md](license_terms_summary.md) (bullet-point narrative), [ngc_model_licenses_table.md](ngc_model_licenses_table.md) (per-model exact license text), [license_references/](license_references/) (full source documents).

## Verdict by license type

| License | # Models | AMD: Commercial Use | AMD: Redistribute | HW/SW Tie to NVIDIA | Note |
|---|---|---|---|---|---|
| NVIDIA Open Model License | 26 | YES | YES (attribution required) | None | Full commercial use + redistribution for anyone, incl. AMD. Must keep 'Licensed by NVIDIA Corporation under the NVIDIA Open Model License' notice. |
| CC-BY-4.0 | 4 | YES | YES (attribution required) | None | Fully permissive. |
| Apache-2.0 | 12 | YES | YES | None | Fully permissive; includes 2 nnUNet checkpoints verified directly against github.com/NVIDIA/DeepLearningExamples PyTorch/Segmentation/nnUNet/LICENSE. |
| MIT | 1 | YES | YES | None | Fully permissive. |
| OpenMDW-1.1 | 1 | YES | YES (must retain license + notices) | None | MIT-like model-weights license; no restriction on outputs. |
| BSD-3-Clause | 5 | YES | YES | None | Fully permissive; includes 3 UNet_Medical + 1 ResNet50 checkpoints verified against github.com/NVIDIA/DeepLearningExamples LICENSE files, plus pix2pixHD (license was on the page all along in a '**License:**' bold field the original extraction missed). |
| NVIDIA Community Model License | 5 | CONDITIONAL | YES (with license copy attached) | YES | Production commercial use requires NVIDIA NIM via an NVIDIA AI Enterprise subscription, OR the model must run on NVIDIA RTX/GeForce RTX GPU (single-user only). Also bars using the model to develop/improve competing AI models without NVIDIA's written approval. |
| Model EULA (TAO Toolkit) | 20 | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit | Actual document = 'Deep Learning Models License Agreement'. States verbatim: 'The SOFTWARE is licensed for you to develop applications only for use in systems with NVIDIA GPUs.' Deploying on AMD hardware is outside the license grant. |
| TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | 20 | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') | No formal EULA is named on the page, but the page itself states the model 'needs to be used with NVIDIA Hardware and Software', 'can only be used with TAO Toolkit, DeepStream SDK or TensorRT', and ships with a DRM 'Model load key' (tlt_encode/nvidia_tlt/nvidia_tao). 4 of 20 directly re-verified (LPRNet, PeopleSemSegNet, PointPillarNet, VehicleMakeNet); remaining 16 inferred from identical team/template/page structure. |
| NVIDIA AI Enterprise EULA | 3 | YES, but scope-limited | Restricted (Enterprise licensing terms) | YES (narrower) | Section 8.15 'NVIDIA Platform Requirement' ties enterprise deployment to NVIDIA-certified SDKs/drivers/Omniverse stack. |
| CC-BY-NC-SA-4.0 | 15 | NO | NO (noncommercial only) | N/A | Blocks ALL commercial use for everyone, including NVIDIA itself — not an AMD-specific lock, just unavailable for commercial use by any vendor. |
| NVIDIA One-Way Noncommercial License (NSCLv1) | 3 | NO for AMD | NO for AMD | N/A | ASYMMETRIC: 'NVIDIA Corporation and its affiliates may use the Work and any derivative works commercially' — NVIDIA gets a commercial carve-out that AMD/everyone else does not. This is a genuine NVIDIA-only lock, not a generic non-commercial license. |
| UNLICENSED (no LICENSE file found anywhere upstream) | 1 | NO (no license granted at all) | NO | N/A | Confirmed via direct inspection of github.com/NVIDIA/DeepLearningExamples: no LICENSE file exists in the TensorFlow/Segmentation/MaskRCNN path or any parent folder. Legal default is all-rights-reserved — cannot be used commercially by anyone without a separate grant from NVIDIA. |
| NOT STATED (page has no license info) | 2 | UNVERIFIED | UNVERIFIED | Unknown | No license shown on the model's own NGC page. Do not assume permissive — verify with NVIDIA before any commercial use. |
| NOT FOUND (no NGC catalog page located) | 7 | UNVERIFIED | UNVERIFIED | Unknown | Could not locate a catalog page for this model at all; likely an SDK feature, blueprint component, or NGC 'resource' rather than a standalone model page. |

## Per-model detail (125 models)

| # | Model | License | AMD Commercial Use | AMD Redistribute | HW/SW Tie |
|---|---|---|---|---|---|
| 1 | BEVFusion for 3D Object Detection | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 2 | CenterPose | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 3 | CenterPose - ISAAC Ros | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 4 | Cosmos-Embed1 | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 5 | Cosmos-Predict2.5-2B | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 6 | Cosmos-Reason1-7B (closest available release to "Cosmos Reason 2 / Cosmos 3") | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 7 | Cosmos-Transfer2.5-2B | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 8 | Grounding DINO | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 9 | Isaac GR00T N1.7 (nvidia/GR00T-N1.7-3B) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 10 | Mask Auto Label (MAL) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 11 | Mask Grounding DINO CC | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 12 | Mask2Former | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 13 | MixNet | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 14 | Multiple 3D CenterPose | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 15 | NV-DINOv2 Classification Model | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 16 | NVOneFormer Commercial | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 17 | PeopleNet | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 18 | PeopleNet Transformer v2.0 | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 19 | Pre-trained SegFormer NvImageNet weights | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 20 | RT-DETR 2D Warehouse | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 21 | SegIC (Segment-In-Context) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 22 | Sparse4D (ResNet-101) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 23 | Sparse4D (ResNet-50) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 24 | TAO Commercial Pretrained C-RADIOv2 Model | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 25 | TAO Commercial Pretrained NV-Dinov2 Model (ViT-G backbone) | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 26 | nvCLIP4STR | NVIDIA Open Model License | YES | YES (attribution required) | None |
| 27 | BodyPose3DNet | CC-BY-4.0 | YES | YES (attribution required) | None |
| 28 | Pre-trained EfficientDet NvImageNet Backbones | CC-BY-4.0 | YES | YES (attribution required) | None |
| 29 | TAO Pretrained Classification-TF2 (efficientnet_tf2_savedmodel_nohead_b0_amp_cosine) | CC-BY-4.0 | YES | YES (attribution required) | None |
| 30 | Visual ChangeNet - Segmentation (LandSat-SCD) | CC-BY-4.0 | YES | YES (attribution required) | None |
| 31 | Earth-2 FourCastNet 3 | Apache-2.0 | YES | YES | None |
| 32 | MONAI BraTS MRI Segmentation Model | Apache-2.0 | YES | YES | None |
| 33 | MONAI Endoscopic Tool Segmentation Model | Apache-2.0 | YES | YES | None |
| 34 | MONAI Lung Nodule CT Detection Model | Apache-2.0 | YES | YES | None |
| 35 | MONAI Pancreas CT DiNTS Segmentation Model | Apache-2.0 | YES | YES | None |
| 36 | MONAI Pathology Nuclei Segmentation Classification Model | Apache-2.0 | YES | YES | None |
| 37 | MONAI Pathology Tumor Detection Model | Apache-2.0 | YES | YES | None |
| 38 | MONAI Spleen CT Segmentation Model | Apache-2.0 | YES | YES | None |
| 39 | MONAI Swin UNETR BTCV Segmentation Model | Apache-2.0 | YES | YES | None |
| 40 | MONAI Whole Body CT Segmentation Model | Apache-2.0 | YES | YES | None |
| 41 | nnUNet PyTorch checkpoint 2D AMP | Apache-2.0 | YES | YES | None |
| 42 | nnUNet PyTorch checkpoint 3D AMP | Apache-2.0 | YES | YES | None |
| 43 | OneFormer Research | MIT | YES | YES | None |
| 44 | CWIP (Contrastive World-Image Pre-training) | OpenMDW-1.1 | YES | YES (must retain license + notices) | None |
| 45 | ResNet50 pretrained weights (PyTorch, AMP, ImageNet) | BSD-3-Clause | YES | YES | None |
| 46 | UNet_Medical TensorFlow2 SavedModel (AMP) | BSD-3-Clause | YES | YES | None |
| 47 | UNet_Medical TensorFlow2 TF-TRT model (AMP) | BSD-3-Clause | YES | YES | None |
| 48 | UNet_Medical TensorFlow2 checkpoint (AMP) | BSD-3-Clause | YES | YES | None |
| 49 | pix2pixHD | BSD-3-Clause | YES | YES | None |
| 50 | PhysicsNeMo Checkpoints: AFNO_DX_FI-V1-ERA5 | NVIDIA Community Model License | CONDITIONAL | YES (with license copy attached) | YES |
| 51 | PhysicsNeMo Checkpoints: AFNO_DX_SR-V1-ERA5 | NVIDIA Community Model License | CONDITIONAL | YES (with license copy attached) | YES |
| 52 | PhysicsNeMo Checkpoints: AFNO_DX_TP-V1-ERA5 | NVIDIA Community Model License | CONDITIONAL | YES (with license copy attached) | YES |
| 53 | PhysicsNeMo Checkpoints: AFNO_DX_WG-V1-ERA5 | NVIDIA Community Model License | CONDITIONAL | YES (with license copy attached) | YES |
| 54 | PhysicsNeMo Checkpoints: DLESyM-V1-ERA5 | NVIDIA Community Model License | CONDITIONAL | YES (with license copy attached) | YES |
| 55 | Bi3D Proximity Segmentation | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 56 | ESS DNN Stereo Disparity Model Card | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 57 | EmotionNet | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 58 | FaceDetectIR | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 59 | FaceNet | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 60 | Facial Landmark Estimator (FPENet) | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 61 | FoundationPose | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 62 | GazeNet (Gaze Estimation) | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 63 | GestureNet | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 64 | HeartRateNet | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 65 | NVIDIA Optical Inspection Model | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 66 | Optical Character Detection (OCDNet) | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 67 | Optical Character Recognition (OCRNet) | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 68 | Pre-trained Deformable DETR NvImageNet Weights | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 69 | Pre-trained FAN based NVImageNet Classification Weights | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 70 | Pre-trained GCViT NVImageNet Classification Weights | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 71 | Re-Identification Transformer (ReIdentificationNet Transformer) | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 72 | Retail Object Recognition | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 73 | Transfusion for 3D Object Detection | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 74 | Visual ChangeNet Classification | Model EULA (TAO Toolkit) | YES, but scope-limited | Restricted (no stand-alone distribution; only embedded in an app with material added functionality) | YES - explicit |
| 75 | Action Recognition Net | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 76 | BodyPoseNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 77 | CitySemSegFormer | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 78 | LPDNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 79 | License Plate Recognition (LPRNet) | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 80 | PeopleNet - AMR Model Card | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 81 | PeopleSemSegNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 82 | PeopleSemSegNet AMR | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 83 | PointPillarNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 84 | Pose Classification Model (PoseClassificationNet) | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 85 | ReIdentificationNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 86 | Retail Object Detection | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 87 | TAO Pretrained Classification | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 88 | TAO Pretrained DetectNet V2 | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 89 | TAO Pretrained EfficientDet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 90 | TAO Pretrained Instance Segmentation | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 91 | TAO Pretrained Semantic Segmentation | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 92 | TrafficCamNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 93 | VehicleMakeNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 94 | VehicleTypeNet | TAO Purpose-Built Model (no formal EULA cited; DRM-locked + explicit NVIDIA HW/SW requirement) | YES, but scope-limited | Restricted (no stand-alone distribution per general TAO model terms) | YES - explicit (page itself states 'needs to be used with NVIDIA Hardware and Software') |
| 95 | PCB Defect Classification Model | NVIDIA AI Enterprise EULA | YES, but scope-limited | Restricted (Enterprise licensing terms) | YES (narrower) |
| 96 | PeopleSemSegFormer Model Card | NVIDIA AI Enterprise EULA | YES, but scope-limited | Restricted (Enterprise licensing terms) | YES (narrower) |
| 97 | Pre-trained DINO NvImageNet Weights | NVIDIA AI Enterprise EULA | YES, but scope-limited | Restricted (Enterprise licensing terms) | YES (narrower) |
| 98 | DINO Model Card (Pretrained DINO COCO) | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 99 | Deformable DETR (TAO Pretrained Deformable DETR) | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 100 | ImageNet NV-DINOv2 | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 101 | MONAI VISTA2D Model | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 102 | Pre-trained DINO ImageNet Weights | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 103 | Pre-trained Deformable DETR ImageNet Weights | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 104 | Pre-trained EfficientDet Model trained on COCO | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 105 | Pre-trained FAN based ImageNet Classification Weights | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 106 | Pre-trained GCViT ImageNet Classification Weights | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 107 | Pre-trained SegFormer ImageNet weights | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 108 | Pre-trained Segformer - CityScapes | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 109 | TAO Pretrained DINO with Foundational Model Backbone | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 110 | TAO Toolkit ODISE 1.1 | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 111 | Visual ChangeNet Segmentation - MvTEC | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 112 | Visual ChangeNet-Segmentation (Research-only) - LEVIR-CD | CC-BY-NC-SA-4.0 | NO | NO (noncommercial only) | N/A |
| 113 | Cosmos-Policy-ALOHA-Predict2-2B (representative of the "Cosmos Policy" family; "Cosmos-H-Dreams" not found) | NVIDIA One-Way Noncommercial License (NSCLv1) | NO for AMD | NO for AMD | N/A |
| 114 | MONAI VISTA3D Model | NVIDIA One-Way Noncommercial License (NSCLv1) | NO for AMD | NO for AMD | N/A |
| 115 | Mask Grounding DINO Research | NVIDIA One-Way Noncommercial License (NSCLv1) | NO for AMD | NO for AMD | N/A |
| 116 | Mask R-CNN TensorFlow Checkpoint (AMP) | UNLICENSED (no LICENSE file found anywhere upstream) | NO (no license granted at all) | NO | N/A |
| 117 | SyntheticaDETR | NOT STATED (page has no license info) | UNVERIFIED | UNVERIFIED | Unknown |
| 118 | Unsupervised Latent Landmarks BBC Fixed Covariance | NOT STATED (page has no license info) | UNVERIFIED | UNVERIFIED | Unknown |
| 119 | Polyp Detection RT-DETR Model | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 120 | dlpp | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 121 | nvof | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 122 | nvsalienc | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 123 | optimized-peoplesemseg-amr | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 124 | optimized_peoplenet_amr | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
| 125 | vss-vlm-prebuilt-engine | NOT FOUND (no NGC catalog page located) | UNVERIFIED | UNVERIFIED | Unknown |
