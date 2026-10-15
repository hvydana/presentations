# NVIDIA NGC Physical AI Models — Full List & Open-Source Gap Analysis

Source: NVIDIA NGC Catalog (catalog.ngc.nvidia.com), public model search API, filtered to
Physical AI / Computer Vision / Robotics / Metropolis / DeepStream / Video Analytics tags.
120 models scraped; flagship Cosmos / Isaac GR00T models added separately (not exposed via
guest-level catalog search).

## 1. Full Model List

1. actionrecognitionnet — action recognition (5 classes) from video
2. afno_dx_fi-v1-era5 — weather: forecast time-step interpolation *(off-topic, tag overlap)*
3. afno_dx_sr-v1-era5 — weather: solar irradiance forecast *(off-topic)*
4. afno_dx_tp-v1-era5 — weather: precipitation forecast *(off-topic)*
5. afno_dx_wg-v1-era5 — weather: wind gust forecast *(off-topic)*
6. bevfusion — 3D object detection from lidar + RGB (BEV fusion)
7. bi3d_proximity_segmentation — binary depth/proximity classification
8. bodypose3dnet — 3D human pose, 34 keypoints
9. bodyposenet — 2D body pose detection
10. centerpose — retail object pose detection
11. centerpose_ros — retail object pose detection (ROS packaged)
12. citysemsegformer — person semantic segmentation
13. cosmos-embed1 — video-text embedding foundation model for physical AI
14. cradiov2 — C-RADIOv2 vision foundation backbone
15. cwip — camera-to-world-pose contrastive pretraining
16. dino_with_fm_backbone — DINO detector w/ foundation-model backbone
17. dlesym-v1-era5 — global earth-system forecast model *(off-topic)*
18. dlpp — video post-processing / RTX Video Super Resolution
19. dnn_stereo_disparity (ESS) — stereo depth estimation
20. efficientnet_tf2_savedmodel_nohead_b0_amp_cosine — EfficientNet-B0 backbone
21. emotionnet — facial emotion classification
22. facedetectir — IR/thermal face detection
23. facenet — RGB face detection
24. foundationpose — 6-DoF object pose estimation & tracking
25. fourcastnet3 — global weather modeling *(off-topic)*
26. fpenet — facial landmark (fiducial point) detection
27. gazenet — eye gaze estimation
28. gesturenet — hand gesture classification
29. grounding_dino — open-vocabulary object detection
30. heartratenet — remote heart-rate (rPPG) estimation
31. imagenet_nv_dinov2 — NV-DINOv2 ImageNet weights
32. latent_landmarks_bbc_fgbg_fixedcovariance — (no description provided)
33. lpdnet — license plate detection
34. lprnet — license plate character recognition
35. mask2former — instance segmentation (COCO)
36. mask_auto_label — auto-generates semantic segmentation labels
37. mask_grounding_dino — open-vocab instance segmentation
38. maskrcnn_tf1_amp_ckpt — Mask R-CNN checkpoint
39. mixnet — text detection (OCR)
40. monai_brats_mri_segmentation — brain tumor MRI segmentation *(off-topic, medical)*
41. monai_endoscopic_tool_segmentation — endoscopic tool segmentation *(off-topic, medical)*
42. monai_lung_nodule_ct_detection — lung lesion CT detection *(off-topic)*
43. monai_pancreas_ct_dints_segmentation — pancreas CT segmentation *(off-topic)*
44. monai_pathology_nuclei_segmentation_classification — histology nuclei segmentation *(off-topic)*
45. monai_pathology_tumor_detection — histopathology tumor detection *(off-topic)*
46. monai_spleen_ct_segmentation — spleen CT segmentation *(off-topic)*
47. monai_swin_unetr_btcv_segmentation — multi-organ CT segmentation *(off-topic)*
48. monai_vista2d — cell segmentation *(off-topic)*
49. monai_vista3d — 3D medical imaging foundation model *(off-topic)*
50. monai_wholebody_ct_segmentation — whole-body CT segmentation *(off-topic)*
51. multiclass_3d_centerpose — category-level 3D object pose estimation
52. nnunet_pyt_ckpt_2d_fold2_amp — medical segmentation checkpoint *(off-topic)*
53. nnunet_pyt_ckpt_3d_fold2_amp — medical segmentation checkpoint *(off-topic)*
54. nv_dinov2_classification_model — NV-DINOv2 classifier
55. nvclip4str — scene-text recognition (OCR)
56. nvdinov2_vitg — NV-DINOv2 ViT-G backbone
57. nvof — hardware-accelerated optical flow / stereo matching
58. nvsalienc — saliency-driven video encoding optimization
59. ocdnet — text/character detection
60. ocrnet — character recognition
61. odise — open-vocabulary panoptic segmentation
62. oneformer — unified segmentation (semantic/instance/panoptic)
63. oneformer_its_pretrained_commercial — OneFormer, commercial-licensed
64. optical_inspection — PCB solder defect detection
65. optimized-peoplesemseg-amr — person segmentation, tuned for robot AMR + Nvblox
66. optimized_peoplenet_amr — person detection, tuned for multi-camera robot AMR
67. pcb_classification — PCB defect classification
68. peoplenet — person/face/bag detection
69. peoplenet_amr — PeopleNet, AMR-tuned
70. peoplenet_transformer_v2 — PeopleNet, transformer-based
71. peoplesemsegformer — person segmentation (SegFormer-based)
72. peoplesemsegnet — person semantic segmentation
73. peoplesemsegnet_amr — person segmentation, AMR-tuned
74. pix2pixhd — high-res image-to-image translation
75. pointpillarnet — 3D object detection from lidar point clouds
76. polyp_detection_rt_detr_model — colonoscopy polyp detection *(off-topic, medical)*
77. poseclassificationnet — skeleton-based pose classification
78. pretrained_classification — TAO transfer-learning base weights
79. pretrained_deformable_detr_coco — Deformable DETR, COCO-trained
80. pretrained_deformable_detr_imagenet — Deformable DETR, ImageNet weights
81. pretrained_deformable_detr_nvimagenet — Deformable DETR, NvImageNet weights
82. pretrained_detectnet_v2 — DetectNet_v2 base weights
83. pretrained_dino_coco — DINO detector, COCO-trained
84. pretrained_dino_imagenet — DINO detector, ImageNet weights
85. pretrained_dino_nvimagenet — DINO detector, NvImageNet weights
86. pretrained_efficientdet — EfficientDet base weights
87. pretrained_efficientdet_tf2_coco — EfficientDet, COCO-trained
88. pretrained_efficientdet_tf2_nvimagenet — EfficientNet backbone, NvImageNet
89. pretrained_fan_classification_imagenet — FAN classifier, ImageNet
90. pretrained_fan_classification_nvimagenet — FAN classifier, NvImageNet
91. pretrained_gcvit_classification_imagenet — GCViT classifier, ImageNet
92. pretrained_gcvit_classification_nvimagenet — GCViT classifier, NvImageNet
93. pretrained_instance_segmentation — instance seg base weights
94. pretrained_mask_grounding_dino_v2 — Mask Grounding DINO base weights
95. pretrained_segformer_cityscapes — SegFormer, Cityscapes-trained
96. pretrained_segformer_imagenet — SegFormer, ImageNet weights
97. pretrained_segformer_nvimagenet — SegFormer, NvImageNet weights
98. pretrained_semantic_segmentation — semantic seg base weights
99. reidentificationnet — person re-identification embeddings
100. reidentificationnet_transformer — person re-ID, Swin Transformer-based
101. resnet_50_pyt_ckpt — ResNet-50 ImageNet weights
102. retail_object_detection — checkout-counter object detection
103. retail_object_recognition — checkout-counter object recognition embeddings
104. rtdetr_2d_warehouse — RT-DETR for warehouse robotics
105. segic — in-context segmentation
106. sparse4d_rn101 — Sparse4D 3D detection, ResNet-101
107. sparse4d_rn50 — Sparse4D 3D detection, ResNet-50
108. synthetica_detr — real-time detector trained purely in simulation
109. trafficcamnet — vehicle detection (4 classes)
110. transfusion — 3D object detection, lidar + RGB fusion
111. unetmedical_tf2_ckpt_amp — medical U-Net checkpoint *(off-topic)*
112. unetmedical_tf2_savedmodel_amp — medical U-Net SavedModel *(off-topic)*
113. unetmedical_tf2_tftrt_amp — medical U-Net TF-TRT *(off-topic)*
114. vehiclemakenet — vehicle make classification
115. vehicletypenet — vehicle type classification
116. visual_changenet_classification — change detection (classification)
117. visual_changenet_segmentation_landsatscd — satellite change segmentation
118. visual_changenet_segmentation_levircd — change segmentation (research-only)
119. visual_changenet_segmentation_mvtec — industrial change/defect segmentation
120. vss-vlm-prebuilt-engine — prebuilt TensorRT VLM engines for Video Search & Summarization

**Flagship models not exposed in guest catalog search** (confirmed via NVIDIA/HF/GitHub, added separately):
121. Cosmos Predict 2 / 2.5 — world foundation model, video prediction/generation
122. Cosmos Transfer 2.5 — sim-to-real domain transfer
123. Cosmos Reason 2 / Cosmos 3 — embodied/physical reasoning VLM
124. Cosmos Policy / Cosmos-H-Dreams — world-model-based robot control
125. Isaac GR00T N1.7 (+ DROID/LIBERO/SimplerEnv-Bridge/SimplerEnv-Fractal finetunes) — humanoid VLA policy

*(off-topic)* = swept in only via a shared generic tag (medical imaging / weather forecasting), not actually Physical AI / robotics.

## 2. Models With No Good Open-Source Pin-to-Pin Replacement

| # | Model | Comment |
|---|---|---|
| 1 | Cosmos Predict 2 / 2.5 | No open world-foundation-model matches its scale, photorealism, and action-conditioning together (Wan 2.2, HunyuanVideo, Open-Sora are open video-gen but not action-conditioned world models) |
| 2 | Cosmos Transfer 2.5 | No open sim-to-real domain-transfer model operates at this scale/quality |
| 3 | Cosmos Policy / Cosmos-H-Dreams | No open world-model-based robot-control system at comparable scale (DreamerV3 is open but far smaller/less photoreal) |
| 4 | Cosmos Reason 2 / Cosmos 3 | Strong open general VLMs exist (Qwen2.5-VL, InternVL3) but none benchmark-tuned specifically for embodied/physical-commonsense reasoning |
| 5 | nvof (NVIDIA Optical Flow) | Backed by a dedicated GPU hardware block; AMD has no equivalent silicon. Software OSS (RAFT, FlowFormer) covers the capability but not the hardware acceleration — a silicon-level gap, not a model gap |
| 6 | facedetectir | IR/thermal-specific face detectors are thin to absent in open source; nearly all mature OSS face detectors (RetinaFace, YOLO-face) are RGB-only |
| 7 | heartratenet | Only academic/research-grade rPPG toolkits exist (e.g. rPPG-Toolbox); nothing production-packaged |
| 8 | cwip | Could not confirm any open equivalent for camera-to-world-pose consistency scoring + per-patch object presence/type — flagged as unverified rather than a guessed alternative |
| 9 | gesturenet | No turnkey open hand-gesture-from-crop classifier; would require custom training on top of MediaPipe/hand-landmark output |
| 10 | gazenet | Open gaze-estimation research exists (L2CS-Net, ETH-XGaze models) but is less mature/production-ready than this |
| 11 | bodypose3dnet | Open real-time 3D human pose options (MotionBERT, VideoPose3D via MMPose) are less mature/real-time than this |
| 12 | synthetica_detr | No public open checkpoint trained purely in simulation with matching zero-shot sim-to-real robustness; would need to reproduce via Isaac Sim/Replicator or BlenderProc from scratch |
| 13 | retail_object_detection / retail_object_recognition | No open pretrained checkpoint specific to retail checkout SKUs; open detectors/embeddings (Grounding DINO, CLIP, DINOv2) are strong building blocks but not a drop-in replacement |
| 14 | optimized_peoplenet_amr / optimized-peoplesemseg-amr | No public open finetune tuned for robot AMR multi-camera geometry / Nvblox integration; base architectures (YOLO, RT-DETR) are open but the specific finetune isn't |
| 15 | rtdetr_2d_warehouse | RT-DETR itself is open, but no public warehouse-specific finetuned checkpoint exists |
| 16 | dlpp (RTX Video Super Resolution) | No open real-time video super-resolution model integrated at the driver/pipeline level the same way |
| 17 | nvsalienc | Open saliency-prediction models exist (e.g. TranSalNet) but none integrated into an NVENC-style real-time encode pipeline |
| 18 | vss-vlm-prebuilt-engine | Distributed only as prebuilt TensorRT engines; no vendor-neutral open equivalent packaged the same way |

Everything else in the list above (PeopleNet, Grounding DINO, BEVFusion, TransFusion, PointPillars, Sparse4D, FoundationPose, Bi3D, ESS, OneFormer, Mask2Former, ODISE, SegFormer, DINO/Deformable DETR, OCR models, C-RADIOv2/DINOv2, Isaac GR00T) already has a good open-source equivalent — in most cases because NVIDIA's NGC version *is* a repackaged/TAO-optimized retrain of an already-open academic model. For those, the real gap is CUDA/TensorRT-only tooling (a ROCm-portability problem), not missing model capability.

## 3. Open-Source Alternative Per Model (all 120 NGC-scraped models)

**License-bucket legend** (added after verifying actual license text, not assuming from "open" labeling):
- **A** — Permissive (MIT/Apache/BSD): free for anyone, commercial use included, no NVIDIA carve-out
- **B** — NVIDIA Source Code License (NC): non-commercial only for everyone *except* NVIDIA/affiliates, who retain a commercial-use exception. Confirmed on every native NVlabs research repo checked (Bi3D, CenterPose, FoundationPose, RADIO, GCViT, FAN, ODISE, SegFormer). This is not an AMD-specific block — it blocks all non-NVIDIA commercial use, on any hardware. Real commercial deployment of these models requires going back to NVIDIA for the packaged/licensed NGC version.
- **C** — NVIDIA Open Model License: fully commercial-usable by anyone, no hardware restriction (confirmed for PeopleNet, Cosmos, GR00T-class NGC releases)
- **?** — Not independently verified this pass (base project isn't NVIDIA-authored, so bucket B likely doesn't apply, but license text wasn't fetched)

| # | Model | Open-Source Alternative | License Bucket | Why It Matches | Where It Doesn't Match |
|---|---|---|---|---|---|
| 1 | actionrecognitionnet | MMAction2 (SlowFast, TSN, PoseC3D) | A | Mature open action-recognition models, Kinetics-pretrained, comparable/broader class coverage | NGC version is a fixed 5-class model wired into DeepStream/TAO deployment; OSS needs its own inference pipeline |
| 2 | afno_dx_fi-v1-era5 | NVlabs/FourCastNet (open), GraphCast, Pangu-Weather | B? | AFNO architecture itself is open-sourced by NVIDIA; general open weather models cover forecasting | Exact fine-tuned task (6h→1h temporal interpolation) has no released open checkpoint |
| 3 | afno_dx_sr-v1-era5 | Same as above | B? | Same | Same — specific solar-irradiance fine-tune not public |
| 4 | afno_dx_tp-v1-era5 | Same as above | B? | Same | Same — specific precipitation fine-tune not public |
| 5 | afno_dx_wg-v1-era5 | Same as above | B? | Same | Same — specific wind-gust fine-tune not public |
| 6 | bevfusion | mit-han-lab/bevfusion (open, MIT) | A | NGC model is a retrain of this exact open repo — same architecture/performance | NVIDIA's TAO/TensorRT export tooling isn't in the original repo (need to build your own for non-NVIDIA HW) |
| 7 | bi3d_proximity_segmentation | NVlabs/Bi3D (open) | B | Same authors' open release, identical method | Productionized DeepStream data loaders not included in the open repo |
| 8 | bodypose3dnet | MMPose 3D (MotionBERT, VideoPose3D) | A | Comparable 3D pose estimation capability | Less real-time-optimized; no turnkey 34-keypoint schema match |
| 9 | bodyposenet | OpenPose, MediaPipe Pose, RTMPose (MMPose) | A | Mature, arguably better accuracy/speed than NGC model | Keypoint schema differs; needs remapping |
| 10 | centerpose | NVlabs/CenterPose (open) | B | Same base method | Retail-object-specific fine-tune not in the public release (open version mostly demoed on YCB objects) |
| 11 | centerpose_ros | NVlabs/CenterPose (open) + own ROS wrapper | B | Same core model | ROS packaging/integration not provided upstream |
| 12 | citysemsegformer | NVlabs/SegFormer (open) fine-tuned on Cityscapes | B | Identical architecture, Cityscapes checkpoints public | Person-only-class head may need retraining |
| 13 | cosmos-embed1 | InternVideo2, ViCLIP, LanguageBind | A | Comparable joint video-text embedding capability | Not benchmarked/tuned for "physical AI" retrieval tasks specifically |
| 14 | cradiov2 | NVlabs/RADIO (open) | B | Same agglomerative distillation approach (CLIP+DINOv2+SAM), open checkpoints exist | "Commercial Pretrained" version may include extra proprietary data/licensing |
| 15 | cwip | None confirmed | N/A | — | No open project found replicating camera-to-world-pose consistency scoring; flagged as unverified rather than guessed |
| 16 | dino_with_fm_backbone | IDEA-Research/DINO + DINOv2 backbone (both open) | A | Can be assembled directly from open components | NVIDIA's specific combined checkpoint not public |
| 17 | dlesym-v1-era5 | NeuralGCM (Google, open), GraphCast, Pangu-Weather | A | Comparable coupled earth-system forecasting | Exact atmosphere+ocean variable set not replicated |
| 18 | dlpp (RTX VSR) | Real-ESRGAN, BasicVSR++ | A | Video super-resolution capability covered | Not integrated at driver/codec level; slower without RTX-specific acceleration |
| 19 | dnn_stereo_disparity (ESS) | RAFT-Stereo, IGEV-Stereo, CREStereo | A | Open, often SOTA-or-better stereo depth accuracy, full training code | Not pre-optimized for Isaac ROS/Jetson TensorRT deployment |
| 20 | efficientnet_tf2_savedmodel_nohead_b0_amp_cosine | timm (pytorch-image-models) EfficientNet-B0 | A | Identical architecture/weights freely available | TF2 SavedModel-without-head export format needs manual conversion |
| 21 | emotionnet | HSEmotion, DeepFace, FER+ | A | Comparable facial emotion classification | Class taxonomy may differ from NGC's set |
| 22 | facedetectir | None strong | N/A | Retrainable from RetinaFace/YOLO-face on open thermal datasets (Tufts Face, SCFace) | No pretrained open IR/thermal face detector exists off-the-shelf |
| 23 | facenet | RetinaFace, YOLOv8-face, MediaPipe Face Detector | A | Mature, excellent open alternatives | None significant |
| 24 | foundationpose | NVlabs/FoundationPose (open) | B | This is literally the open-source release | Some CUDA-specific ops (custom rasterizer) need porting for ROCm |
| 25 | fourcastnet3 | NVlabs/FourCastNet (open), GraphCast, Pangu-Weather | B? | Same underlying open approach available | FourCastNet 3-specific improvements/checkpoint may not be open yet |
| 26 | fpenet | MediaPipe Face Mesh, dlib 68-point, 3DDFA-v2 | A | Comparable facial landmark detection | Exact fiducial point count/definition differs |
| 27 | gazenet | L2CS-Net, ETH-XGaze models | A | Gaze vector estimation capability exists in open form | Less mature/production-hardened than NGC model |
| 28 | gesturenet | MediaPipe Hands + custom classifier | A | Hand landmark extraction is open and strong | No turnkey open hand-gesture-from-crop classifier; requires custom training |
| 29 | grounding_dino | IDEA-Research/Grounding DINO (open, Apache-2.0) | A | Exact same model; NGC version is a commercial-license retrain | None substantive — original is equally capable, fewer license restrictions |
| 30 | heartratenet | rPPG-Toolbox (academic) | A | Only research-grade rPPG implementations available | Nothing production-packaged |
| 31 | imagenet_nv_dinov2 | DINOv2 (Meta, open) ImageNet-pretrained | A | Same self-supervised approach, open checkpoints available | NV-specific retraining/robustness improvements not replicated |
| 32 | latent_landmarks_bbc_fgbg_fixedcovariance | Unknown | N/A | — | No description provided by NGC; insufficient information to assess |
| 33 | lpdnet | OpenALPR, YOLO-based plate detectors | A | Mature, widely available open alternatives | None major |
| 34 | lprnet | OpenALPR OCR, PaddleOCR fine-tuned, CRNN plate readers | A | Comparable capability | Region/format-specific plate layouts need retraining either way |
| 35 | mask2former | Facebook Research/Mask2Former (open) | A | Identical, open original | None |
| 36 | mask_auto_label | Meta/Segment Anything (SAM, SAM2) | A | Comparable or superior auto-labeling capability | Prompt-based workflow differs from NGC's automatic class-aware labeling |
| 37 | mask_grounding_dino | Grounded-SAM (Grounding DINO + SAM, open) | A | Functionally equivalent, popular open combo | Two-stage pipeline vs. NVIDIA's single unified model |
| 38 | maskrcnn_tf1_amp_ckpt | Detectron2 Mask R-CNN (open) | A | Identical capability | PyTorch vs. TF1 framework difference only |
| 39 | mixnet | CRAFT, DBNet++, PaddleOCR detection | A | Comparable text detection accuracy | None major |
| 40 | monai_brats_mri_segmentation | Project MONAI (open) | A | This literally *is* a MONAI Model Zoo bundle, mirrored on NGC | None — already open source |
| 41 | monai_endoscopic_tool_segmentation | Project MONAI (open) | A | Same | None |
| 42 | monai_lung_nodule_ct_detection | Project MONAI (open) | A | Same | None |
| 43 | monai_pancreas_ct_dints_segmentation | Project MONAI (open) | A | Same | None |
| 44 | monai_pathology_nuclei_segmentation_classification | Project MONAI (open) | A | Same | None |
| 45 | monai_pathology_tumor_detection | Project MONAI (open) | A | Same | None |
| 46 | monai_spleen_ct_segmentation | Project MONAI (open) | A | Same | None |
| 47 | monai_swin_unetr_btcv_segmentation | Project MONAI (open) | A | Same | None |
| 48 | monai_vista2d | Project MONAI (open) | A | Same | None |
| 49 | monai_vista3d | Project MONAI (open) | A | Same | None |
| 50 | monai_wholebody_ct_segmentation | Project MONAI (open) | A | Same | None |
| 51 | multiclass_3d_centerpose | NVlabs/CenterPose (open) | B | Same base method extended to multiclass | Multiclass category-level extension/checkpoint not in the original open repo |
| 52 | nnunet_pyt_ckpt_2d_fold2_amp | MIC-DKFZ/nnUNet (open) | A | Identical, nnU-Net is fully open source | None |
| 53 | nnunet_pyt_ckpt_3d_fold2_amp | MIC-DKFZ/nnUNet (open) | A | Identical | None |
| 54 | nv_dinov2_classification_model | DINOv2 (Meta, open) + finetuned head | A | Same backbone | NV-specific data curation not replicated |
| 55 | nvclip4str | Original CLIP4STR (open, academic release) | A | Literally the open academic model NGC repackaged | None substantive |
| 56 | nvdinov2_vitg | DINOv2 ViT-g/14 (Meta, open) | A | Same architecture/size available open | TAO-commercial retraining/optimization not replicated |
| 57 | nvof | RAFT, FlowFormer (software-only) | A | Covers optical-flow/stereo-matching capability | Backed by dedicated GPU silicon; no AMD-equivalent hardware block — software OSS is slower, not a drop-in |
| 58 | nvsalienc | TranSalNet (open saliency model) | A | Saliency prediction capability covered | No NVENC-integrated real-time encode pipeline equivalent |
| 59 | ocdnet | CRAFT, DBNet++, PaddleOCR detection | A | Comparable text detection | None major |
| 60 | ocrnet | PaddleOCR, docTR, EasyOCR, CRNN/attention recognizers | A | Comparable recognition accuracy | None major |
| 61 | odise | Original ODISE (NVIDIA Research + UT Austin, open) | B | Identical, open academic release | None |
| 62 | oneformer | SHI-Labs/OneFormer (open) | A | Identical | None |
| 63 | oneformer_its_pretrained_commercial | SHI-Labs/OneFormer (open) | A | Identical architecture | Commercial-data retrain not replicated (license nuance, not capability) |
| 64 | optical_inspection | Anomalib (Intel, open) | A | Comparable/superior defect detection, broader algorithm choice (PatchCore, PaDiM) | None major — OSS arguably ahead |
| 65 | optimized-peoplesemseg-amr | SegFormer/Mask2Former fine-tuned yourself | A | Base architecture open | No public finetune for robot-AMR camera geometry / Nvblox integration |
| 66 | optimized_peoplenet_amr | YOLO/RT-DETR fine-tuned yourself | A | Base architecture open | No public finetune for multi-camera RealSense/AMR setups |
| 67 | pcb_classification | Anomalib, general open classifiers | A | Comparable capability/tooling | PCB-specific pretrained checkpoint not public; needs your own fine-tune |
| 68 | peoplenet | YOLOv11, RT-DETR (person class) | A | Strong open alternatives, often equal/better COCO-person accuracy | NVIDIA's specific edge-optimized/quantized checkpoint not replicated 1:1 |
| 69 | peoplenet_amr | Same as above, self-finetuned | A | Same | AMR-tuned variant not public |
| 70 | peoplenet_transformer_v2 | RT-DETR, DINO detector (open) | A | Comparable transformer-based detection | Exact checkpoint not replicated |
| 71 | peoplesemsegformer | SegFormer (open) | B | Same architecture | Person-only fine-tune not public as-is |
| 72 | peoplesemsegnet | Mask2Former/SegFormer fine-tuned | A | Comparable capability | Specific checkpoint not public |
| 73 | peoplesemsegnet_amr | Same, self-finetuned | A | Same | AMR-tuned variant not public |
| 74 | pix2pixhd | NVIDIA/pix2pixHD (open) | A | This is literally the open NVIDIA Research release | None |
| 75 | pointpillarnet | OpenPCDet PointPillars (open) | A | Identical algorithm, actively maintained open implementation | None major |
| 76 | polyp_detection_rt_detr_model | RT-DETR (open) fine-tuned on Kvasir-SEG (open dataset) | A | Architecture and dataset both open | Exact fine-tuned checkpoint not public |
| 77 | poseclassificationnet | ST-GCN, PoseC3D (MMAction2, open) | A | Comparable skeleton-based classification | Exact pose taxonomy/class set differs |
| 78 | pretrained_classification | timm/torchvision ImageNet weights | A | Standard open pretrained weights | None major |
| 79 | pretrained_deformable_detr_coco | fundamentalvision/Deformable-DETR (open) | A | Identical, COCO checkpoints public | None |
| 80 | pretrained_deformable_detr_imagenet | Deformable DETR (open) + ImageNet backbone | A | Standard open backbone weights available | None major |
| 81 | pretrained_deformable_detr_nvimagenet | Deformable DETR (open) | A | Architecture open | NvImageNet is NVIDIA's proprietary dataset — not reproducible; ImageNet-pretrained version is the closest open substitute |
| 82 | pretrained_detectnet_v2 | Any open single-shot detector (YOLO) as base | A | Comparable transfer-learning starting point | DetectNet_v2 architecture itself isn't a widely-used open standard |
| 83 | pretrained_dino_coco | IDEA-Research/DINO (open) | A | Identical, COCO checkpoints public | None |
| 84 | pretrained_dino_imagenet | DINO (open) + ImageNet backbone | A | Standard open weights available | None major |
| 85 | pretrained_dino_nvimagenet | DINO (open) | A | Architecture open | NvImageNet proprietary dataset not reproducible |
| 86 | pretrained_efficientdet | google/automl EfficientDet (open) | A | Identical architecture | None major |
| 87 | pretrained_efficientdet_tf2_coco | google/automl EfficientDet (open) | A | Identical, COCO checkpoints public | None |
| 88 | pretrained_efficientdet_tf2_nvimagenet | EfficientNet backbone (open) | A | Architecture open | NvImageNet proprietary dataset not reproducible |
| 89 | pretrained_fan_classification_imagenet | NVlabs/FAN (open) | B | Same NVIDIA Research open release | None |
| 90 | pretrained_fan_classification_nvimagenet | NVlabs/FAN (open) | B | Architecture open | NvImageNet proprietary dataset not reproducible |
| 91 | pretrained_gcvit_classification_imagenet | NVlabs/GCViT (open) | B | Same NVIDIA Research open release | None |
| 92 | pretrained_gcvit_classification_nvimagenet | NVlabs/GCViT (open) | B | Architecture open | NvImageNet proprietary dataset not reproducible |
| 93 | pretrained_instance_segmentation | Mask2Former/Mask R-CNN (open) | A | Comparable starting weights | Specific TAO base checkpoint not identical |
| 94 | pretrained_mask_grounding_dino_v2 | Grounded-SAM (open) | A | Comparable open-vocab instance segmentation | Not the same unified single-model checkpoint |
| 95 | pretrained_segformer_cityscapes | NVlabs/SegFormer (open) | B | Identical, Cityscapes checkpoints public | None |
| 96 | pretrained_segformer_imagenet | SegFormer (open) + ImageNet backbone | B | Standard open weights available | None major |
| 97 | pretrained_segformer_nvimagenet | SegFormer (open) | B | Architecture open | NvImageNet proprietary dataset not reproducible |
| 98 | pretrained_semantic_segmentation | Any open segmentation backbone (SegFormer, DeepLab) | A | Comparable starting point | Specific TAO checkpoint not identical |
| 99 | reidentificationnet | JDAI-CV/FastReID (open) | A | Comparable accuracy, mature open ecosystem | None major |
| 100 | reidentificationnet_transformer | TransReID (open) | A | Comparable Swin/ViT-based re-ID | None major |
| 101 | resnet_50_pyt_ckpt | torchvision ResNet-50 (open) | A | Identical standard weights | None |
| 102 | retail_object_detection | Grounding DINO / open detectors, self-finetuned | A | Strong open building blocks | No open pretrained checkpoint specific to retail checkout SKUs |
| 103 | retail_object_recognition | CLIP, DINOv2 embeddings, self-finetuned | A | Strong open embedding building blocks | No open checkpoint specific to checkout-counter retail objects |
| 104 | rtdetr_2d_warehouse | Ultralytics/RT-DETR (open) | A | Base architecture fully open | No public warehouse-specific finetuned checkpoint |
| 105 | segic | Original SEGIC academic release (if published) | A | Comparable to SEEM/SegGPT (open) in-context segmentation | Exact one-shot/few-shot performance parity unverified |
| 106 | sparse4d_rn101 | HorizonRobotics/Sparse4D (open) | A | Identical algorithm, open release | None major |
| 107 | sparse4d_rn50 | HorizonRobotics/Sparse4D (open) | A | Identical algorithm, open release | None major |
| 108 | synthetica_detr | Isaac Sim/Replicator or BlenderProc + open detector (self-trained) | A | Simulation-based training pipeline itself is open | No public checkpoint matching its zero-shot sim-to-real robustness |
| 109 | trafficcamnet | YOLO-based vehicle detectors (COCO car/truck/bus) | A | Comparable detection capability | Specific 4-class edge-optimized checkpoint not replicated |
| 110 | transfusion | XuyangBai/TransFusion (open) | A | Identical, open academic release | None major |
| 111 | unetmedical_tf2_ckpt_amp | Project MONAI / open U-Net implementations | A | Same architecture family, open | TF2-specific checkpoint format differs |
| 112 | unetmedical_tf2_savedmodel_amp | Project MONAI / open U-Net | A | Same | Same |
| 113 | unetmedical_tf2_tftrt_amp | Project MONAI / open U-Net | A | Same | TF-TRT optimized export not replicated in open form |
| 114 | vehiclemakenet | Self-trained ResNet18 on Stanford Cars / CompCars (open datasets) | A | Architecture trivial to replicate with open data | No turnkey pretrained open "car brand classifier" as mature/maintained |
| 115 | vehicletypenet | Self-trained classifier on open vehicle datasets | A | Same | Same; taxonomy differs by region |
| 116 | visual_changenet_classification | wgcban/ChangeFormer (open) | A | Comparable change-detection capability | Different backbone/architecture than NVIDIA's ChangeNet |
| 117 | visual_changenet_segmentation_landsatscd | ChangeFormer (open) on open LEVIR-CD/Landsat-SCD data | A | Comparable capability, open datasets available | Exact architecture/checkpoint differs |
| 118 | visual_changenet_segmentation_levircd | ChangeFormer (open) | A | Comparable capability | Exact architecture/checkpoint differs |
| 119 | visual_changenet_segmentation_mvtec | Anomalib (open) | A | Comparable industrial change/defect segmentation | Different underlying method (anomaly detection vs. change detection) |
| 120 | vss-vlm-prebuilt-engine | Open VLMs (Qwen2.5-VL, InternVL3) + your own inference server | A | Underlying VLM capability is open | Distributed only as prebuilt TensorRT engines; no vendor-neutral open equivalent packaged the same way |

Confidence note: rows for `cwip`, `latent_landmarks_bbc_fgbg_fixedcovariance`, and `segic` are lower-confidence — no authoritative open-source match could be confirmed for the first two, and `segic`'s exact original-paper openness wasn't independently re-verified in this pass.

## 3.5 The Real Hardware Lock-In: SDK License vs. Model License vs. AI Enterprise EULA

Section 3's bucket column describes the license on *model weights/code*. That turns out not to be where the hardware tie lives. There are three separate real NVIDIA license documents in play, each doing a different job — verified by fetching each one directly, and by checking actual NGC catalog model pages (not inferring from the model list alone):

**1. NVIDIA Open Model License** — the model-weights license on newer/flagship NGC catalog entries. Confirmed on PeopleNet, BEVFusion, CenterPose, Mask2Former, Cosmos, GR00T-class releases. Fully commercial-usable, **no hardware restriction** — silent on GPU vendor.

**2. NVIDIA AI Enterprise Software License Agreement** — confirmed as the license actually bound to the *model download itself* for a specific set of older TAO purpose-built models, either via an explicit "License to use this model is covered by the Model EULA" clause on the catalog page, or via a "Licensing:" metadata field:

| Model | License on NGC page |
|---|---|
| ActionRecognitionNet | AI Enterprise EULA |
| LPRNet | AI Enterprise EULA |
| LPDNet | AI Enterprise EULA |
| TrafficCamNet | AI Enterprise EULA |
| VehicleMakeNet | AI Enterprise EULA |
| PointPillarNet | AI Enterprise EULA |
| FaceNet | AI Enterprise EULA (explicit license clause on page) |
| GazeNet | AI Enterprise EULA (explicit license clause on page) |
| OCDNet | AI Enterprise EULA (explicit license clause on page) |
| OCRNet | AI Enterprise EULA (explicit license clause on page) |

This EULA (`nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/`) does contain a hardware clause — **Section 8.15, "NVIDIA Platform Requirement"** — but it's scoped to "software development kits (CUDA toolkit, TensorRT, cuDNN), drivers, and Omniverse," not to model weights/checkpoints in general. So this is a real, GPU-restrictive document these ten models are contractually bound to, but it does not unambiguously state the downloaded model itself only runs on NVIDIA hardware — the restriction bites once you pair the model with NVIDIA's SDK/driver stack, which is the NVIDIA-blessed way to deploy it.

By contrast, BodyPoseNet on the same catalog uses **CC-BY-4.0** — fully open, no NVIDIA-specific terms of any kind.

**3. NVIDIA Software License Agreement / TensorRT SDK Supplement** — the license for the *deployment tooling itself* (TAO Toolkit, TensorRT), not any model's weights. This is the one with the unambiguous hardware clause:

- TAO Toolkit SLA (`developer.download.nvidia.com/licenses/tao_toolkit_21-08.pdf`), Section 1 "License Grant":
  > "...license to install and use the SOFTWARE **in conjunction with your use of NVIDIA GPUs** including to deploy a service to external users, provided that the SOFTWARE is not distributed."
- TensorRT SDK Supplement (`docs.nvidia.com/deeplearning/tensorrt/sla/`), Section 1 "License Scope":
  > "The SDK is licensed for you to develop applications **only for use in systems with NVIDIA GPUs**."

**No NGC catalog model page (checked: ActionRecognitionNet, LPRNet, LPDNet, TrafficCamNet, VehicleMakeNet, BodyPoseNet, FaceNet, GazeNet, OCDNet, OCRNet, BEVFusion, CenterPose, PointPillarNet, Mask2Former, PeopleNet) cites the TAO Toolkit SLA or TensorRT SLA by name.** That clause governs the SDK you download separately to train/export/deploy the model, not the model itself — so it's real, unambiguous, and NVIDIA-GPU-only, but it's one layer removed from any specific model's own license terms.

**Net picture:** no single model in the catalog carries a license that says, in so many words, "these weights only run on NVIDIA hardware." The closest things are (a) the ~10-model AI Enterprise EULA list above, whose hardware clause is scoped to the SDK/driver stack rather than the weights, and (b) the TAO Toolkit/TensorRT SDK license, which is unambiguous but attaches to the tooling, not to any model. Running the same weights via ROCm or an open runtime (ONNX Runtime, PyTorch native, TVM) sidesteps both — the lock-in is in NVIDIA's *recommended production path*, not in the model artifact.

I did not find a document literally titled "NVIDIA Deep Learning License Agreement" — the closest real names are the **NVIDIA Software License Agreement** (TAO Toolkit / TensorRT / DeepStream) and the **NVIDIA AI Enterprise EULA**.

## 4. Models With NO True Pin-to-Pin Replacement (input, output, training data, or NVIDIA-license mismatch)

A "pin-to-pin" replacement means: same input modality, same output format/taxonomy, comparable training data, and freely available (not gated behind an NVIDIA-only license or NVIDIA-only silicon). Any row below fails on at least one of those axes, even where a *capability-level* open alternative exists (noted in Section 3).

| # | Model | Mismatch Type | Why It's Not Pin-to-Pin |
|---|---|---|---|
| 1 | afno_dx_fi-v1-era5 | Data | Task-specific fine-tune (6h→1h interpolation) has no released open checkpoint |
| 2 | afno_dx_sr-v1-era5 | Data | Solar-irradiance fine-tune not public |
| 3 | afno_dx_tp-v1-era5 | Data | Precipitation fine-tune not public |
| 4 | afno_dx_wg-v1-era5 | Data | Wind-gust fine-tune not public |
| 5 | bodypose3dnet | Output | No open checkpoint matches its exact 34-keypoint 3D schema |
| 6 | centerpose | Data | Retail-object-specific fine-tune not in the open CenterPose release |
| 7 | centerpose_ros | Data + Output | Same fine-tune gap, plus ROS packaging not provided upstream |
| 8 | citysemsegformer | Data | Person-only-class fine-tune not public as-is |
| 9 | cosmos-embed1 | Data | Not tuned/benchmarked for "physical AI" retrieval tasks specifically |
| 10 | cradiov2 | NVIDIA license | "Commercial Pretrained" variant trained on additional NVIDIA-licensed data |
| 11 | cwip | Unresolved | No open project replicates camera-to-world-pose consistency scoring at all |
| 12 | dino_with_fm_backbone | Data | Specific backbone+detector combination checkpoint not public |
| 13 | dlesym-v1-era5 | Data | Exact coupled atmosphere+ocean variable set not replicated |
| 14 | dlpp (RTX VSR) | Output | Not integrated at driver/codec level; no equivalent real-time pipeline output |
| 15 | emotionnet | Output | Emotion class taxonomy differs from open alternatives |
| 16 | facedetectir | Input | No open detector trained on IR/thermal input — all mature options are RGB-only |
| 17 | fourcastnet3 | Data | FourCastNet-3-specific checkpoint/improvements not released open |
| 18 | fpenet | Output | Fiducial landmark point count/definition differs from open alternatives |
| 19 | gazenet | Output | Open gaze models estimate differently-defined gaze vectors, less production-ready |
| 20 | gesturenet | Data | No open checkpoint for this exact gesture taxonomy; needs custom training |
| 21 | heartratenet | Data | Only academic rPPG code exists, no matching production checkpoint |
| 22 | imagenet_nv_dinov2 | Data | NV-specific retraining/curation not replicated in open DINOv2 |
| 23 | latent_landmarks_bbc_fgbg_fixedcovariance | Unresolved | No description available; cannot assess |
| 24 | lprnet | Data | Region/plate-format-specific training data differs |
| 25 | mask_auto_label | Input | SAM is prompt-driven; NGC model's automatic class-aware workflow differs |
| 26 | mask_grounding_dino | Output | Grounded-SAM is a two-stage pipeline, not NVIDIA's single unified model output |
| 27 | multiclass_3d_centerpose | Data | Multiclass category-level extension/checkpoint not in the open release |
| 28 | nv_dinov2_classification_model | Data | NV-specific data curation not replicated |
| 29 | nvdinov2_vitg | NVIDIA license | TAO-commercial retraining/optimization not in the open RADIO/DINOv2 release |
| 30 | nvof | NVIDIA license (hardware) | Backed by dedicated GPU silicon block; no AMD-equivalent hardware exists at all |
| 31 | nvsalienc | Output | No open model integrated into an NVENC-style real-time encode pipeline |
| 32 | oneformer_its_pretrained_commercial | NVIDIA license | Retrained on NVIDIA-commercial-licensed data, not reproducible with open data |
| 33 | optimized-peoplesemseg-amr | Data | AMR-specific finetune + Nvblox integration not public |
| 34 | optimized_peoplenet_amr | Data | AMR/multi-camera-RealSense finetune not public |
| 35 | pcb_classification | Data | PCB-defect-specific checkpoint not public |
| 36 | peoplenet | Data | Edge-optimized/quantized checkpoint not replicated 1:1 |
| 37 | peoplenet_amr | Data | AMR-tuned variant not public |
| 38 | peoplenet_transformer_v2 | Data | Exact checkpoint not replicated |
| 39 | peoplesemsegformer | Data | Person-only fine-tune not public as-is |
| 40 | peoplesemsegnet | Data | Specific checkpoint not public |
| 41 | peoplesemsegnet_amr | Data | AMR-tuned variant not public |
| 42 | polyp_detection_rt_detr_model | Data | Fine-tuned checkpoint on this exact task not public |
| 43 | poseclassificationnet | Output | Pose/class taxonomy differs from open alternatives |
| 44 | pretrained_deformable_detr_nvimagenet | Data + NVIDIA license | Pretrained on NvImageNet, a proprietary NVIDIA-internal dataset never released |
| 45 | pretrained_detectnet_v2 | Data | DetectNet_v2 architecture itself isn't a widely-adopted open standard |
| 46 | pretrained_dino_nvimagenet | Data + NVIDIA license | NvImageNet dataset not public |
| 47 | pretrained_efficientdet_tf2_nvimagenet | Data + NVIDIA license | NvImageNet dataset not public |
| 48 | pretrained_fan_classification_nvimagenet | Data + NVIDIA license | NvImageNet dataset not public |
| 49 | pretrained_gcvit_classification_nvimagenet | Data + NVIDIA license | NvImageNet dataset not public |
| 50 | pretrained_instance_segmentation | Data | TAO base checkpoint not identical to open alternatives |
| 51 | pretrained_mask_grounding_dino_v2 | Output | Not a single unified model like the open combo (Grounded-SAM) |
| 52 | pretrained_segformer_nvimagenet | Data + NVIDIA license | NvImageNet dataset not public |
| 53 | pretrained_semantic_segmentation | Data | TAO base checkpoint not identical to open alternatives |
| 54 | retail_object_detection | Data | No open checkpoint trained on retail-checkout-specific SKUs |
| 55 | retail_object_recognition | Data | No open checkpoint trained on retail-checkout-specific SKUs |
| 56 | rtdetr_2d_warehouse | Data | No public warehouse-specific finetuned checkpoint |
| 57 | segic | Data (unverified) | Exact in-context segmentation performance parity with open alternatives unverified |
| 58 | synthetica_detr | Data | No public checkpoint trained purely in simulation with matching zero-shot robustness |
| 59 | trafficcamnet | Data | Specific 4-class edge-optimized checkpoint not replicated |
| 60 | vehiclemakenet | Data | No turnkey pretrained open checkpoint for this exact brand taxonomy |
| 61 | vehicletypenet | Data | No turnkey pretrained open checkpoint for this exact type taxonomy |
| 62 | visual_changenet_classification | Output | Different backbone/architecture than open ChangeFormer |
| 63 | visual_changenet_segmentation_landsatscd | Output | Different backbone/architecture than open alternatives |
| 64 | visual_changenet_segmentation_levircd | Output | Different backbone/architecture than open alternatives |
| 65 | visual_changenet_segmentation_mvtec | Input | Different underlying method (change detection vs. Anomalib's anomaly detection) |
| 66 | vss-vlm-prebuilt-engine | NVIDIA license | Distributed only as prebuilt TensorRT engines; no open/vendor-neutral packaging |
| 67 | Cosmos Predict 2 / 2.5 | Data | No open world-model reproduces its scale/action-conditioning/photorealism |
| 68 | Cosmos Transfer 2.5 | Data | No open sim-to-real domain-transfer model at comparable scale |
| 69 | Cosmos Reason 2 / Cosmos 3 | Output | Open VLMs aren't benchmark-tuned for embodied/physical-commonsense reasoning |
| 70 | Cosmos Policy / Cosmos-H-Dreams | Data | No open world-model-based robot-control system at comparable scale |

Rows not listed here (e.g. Grounding DINO, BEVFusion, TransFusion, PointPillars, FoundationPose, Mask2Former, OneFormer, ODISE, SegFormer, MONAI/nnU-Net models, ResNet-50, Isaac GR00T) have a genuine pin-to-pin open equivalent — usually because NVIDIA's version *is* the same open model repackaged, or because the open ecosystem (LeRobot/OpenVLA/π0 for GR00T) already covers the same input/output/training-data profile.
## 5. License Actually Stated on Each Model's NGC Catalog Page

Extracted directly from the saved per-model NGC catalog pages in `ngc_model_pages/` (125 models). This is the license shown **on that specific model's own catalog page** — not inferred, not assumed from the model family. Where a model splits code vs. weights licensing, both are shown.

| # | Model | License (as stated on NGC page) | Code/Weights split (if any) |
|---|---|---|---|
| 1 | bevfusion | NVIDIA Open Model License | - |
| 2 | centerpose | NVIDIA Open Model License | - |
| 3 | centerpose_ros | NVIDIA Open Model License | - |
| 4 | cosmos-embed1 | NVIDIA Open Model License | - |
| 5 | cosmos_predict_2 | NVIDIA Open Model License | - |
| 6 | cosmos_reason_2 | NVIDIA Open Model License | - |
| 7 | cosmos_transfer_2.5 | NVIDIA Open Model License | - |
| 8 | cradiov2 | NVIDIA Open Model License | - |
| 9 | grounding_dino | NVIDIA Open Model License | - |
| 10 | isaac_gr00t_n1.7 | NVIDIA Open Model License | - |
| 11 | mask2former | NVIDIA Open Model License | - |
| 12 | mask_auto_label | NVIDIA Open Model License | - |
| 13 | mask_grounding_dino | NVIDIA Open Model License | - |
| 14 | mixnet | NVIDIA Open Model License | - |
| 15 | multiclass_3d_centerpose | NVIDIA Open Model License | - |
| 16 | nv_dinov2_classification_model | NVIDIA Open Model License | - |
| 17 | nvclip4str | NVIDIA Open Model License | - |
| 18 | nvdinov2_vitg | NVIDIA Open Model License | - |
| 19 | oneformer_its_pretrained_commercial | NVIDIA Open Model License | - |
| 20 | peoplenet | NVIDIA Open Model License | - |
| 21 | peoplenet_transformer_v2 | NVIDIA Open Model License | - |
| 22 | pretrained_segformer_nvimagenet | NVIDIA Open Model License | - |
| 23 | rtdetr_2d_warehouse | NVIDIA Open Model License | - |
| 24 | segic | NVIDIA Open Model License | - |
| 25 | sparse4d_rn101 | NVIDIA Open Model License | - |
| 26 | sparse4d_rn50 | NVIDIA Open Model License | - |
| 27 | afno_dx_fi-v1-era5 | NVIDIA Community Model License | - |
| 28 | afno_dx_sr-v1-era5 | NVIDIA Community Model License | - |
| 29 | afno_dx_tp-v1-era5 | NVIDIA Community Model License | - |
| 30 | afno_dx_wg-v1-era5 | NVIDIA Community Model License | - |
| 31 | dlesym-v1-era5 | NVIDIA Community Model License | - |
| 32 | bodypose3dnet | CC-BY-4.0 | - |
| 33 | efficientnet_tf2_savedmodel_nohead_b0_amp_cosine | CC-BY-4.0 | - |
| 34 | pretrained_efficientdet_tf2_nvimagenet | CC-BY-4.0 | - |
| 35 | visual_changenet_segmentation_landsatscd | CC-BY-4.0 | - |
| 36 | fourcastnet3 | Apache-2.0 | - |
| 37 | monai_brats_mri_segmentation | Apache-2.0 | - |
| 38 | monai_endoscopic_tool_segmentation | Apache-2.0 | - |
| 39 | monai_lung_nodule_ct_detection | Apache-2.0 | - |
| 40 | monai_pancreas_ct_dints_segmentation | Apache-2.0 | - |
| 41 | monai_pathology_nuclei_segmentation_classification | Apache-2.0 | - |
| 42 | monai_pathology_tumor_detection | Apache-2.0 | - |
| 43 | monai_spleen_ct_segmentation | Apache-2.0 | - |
| 44 | monai_swin_unetr_btcv_segmentation | Apache-2.0 | - |
| 45 | monai_wholebody_ct_segmentation | Apache-2.0 | - |
| 46 | oneformer | MIT | - |
| 47 | cwip | OpenMDW-1.1 | - |
| 48 | bi3d_proximity_segmentation | Model EULA (TAO Toolkit) | - |
| 49 | dnn_stereo_disparity | Model EULA (TAO Toolkit) | - |
| 50 | emotionnet | Model EULA (TAO Toolkit) | - |
| 51 | facedetectir | Model EULA (TAO Toolkit) | - |
| 52 | facenet | Model EULA (TAO Toolkit) | - |
| 53 | foundationpose | Model EULA (TAO Toolkit) | - |
| 54 | fpenet | Model EULA (TAO Toolkit) | - |
| 55 | gazenet | Model EULA (TAO Toolkit) | - |
| 56 | gesturenet | Model EULA (TAO Toolkit) | - |
| 57 | heartratenet | Model EULA (TAO Toolkit) | - |
| 58 | ocdnet | Model EULA (TAO Toolkit) | - |
| 59 | ocrnet | Model EULA (TAO Toolkit) | - |
| 60 | optical_inspection | Model EULA (TAO Toolkit) | - |
| 61 | pretrained_deformable_detr_nvimagenet | Model EULA (TAO Toolkit) | - |
| 62 | pretrained_fan_classification_nvimagenet | Model EULA (TAO Toolkit) | - |
| 63 | pretrained_gcvit_classification_nvimagenet | Model EULA (TAO Toolkit) | - |
| 64 | reidentificationnet_transformer | Model EULA (TAO Toolkit) | - |
| 65 | retail_object_recognition | Model EULA (TAO Toolkit) | - |
| 66 | transfusion | Model EULA (TAO Toolkit) | - |
| 67 | visual_changenet_classification | Model EULA (TAO Toolkit) | - |
| 68 | pcb_classification | NVIDIA AI Enterprise EULA | - |
| 69 | peoplesemsegformer | NVIDIA AI Enterprise EULA | - |
| 70 | pretrained_dino_nvimagenet | NVIDIA AI Enterprise EULA | - |
| 71 | dino_with_fm_backbone | CC-BY-NC-SA-4.0 | - |
| 72 | imagenet_nv_dinov2 | CC-BY-NC-SA-4.0 | - |
| 73 | monai_vista2d | CC-BY-NC-SA-4.0 | Code: Apache 2.0 | Weights: CC-BY-NC-SA-4.0 |
| 74 | odise | CC-BY-NC-SA-4.0 | - |
| 75 | pretrained_deformable_detr_coco | CC-BY-NC-SA-4.0 | - |
| 76 | pretrained_deformable_detr_imagenet | CC-BY-NC-SA-4.0 | - |
| 77 | pretrained_dino_coco | CC-BY-NC-SA-4.0 | - |
| 78 | pretrained_dino_imagenet | CC-BY-NC-SA-4.0 | - |
| 79 | pretrained_efficientdet_tf2_coco | CC-BY-NC-SA-4.0 | - |
| 80 | pretrained_fan_classification_imagenet | CC-BY-NC-SA-4.0 | - |
| 81 | pretrained_gcvit_classification_imagenet | CC-BY-NC-SA-4.0 | - |
| 82 | pretrained_segformer_cityscapes | CC-BY-NC-SA-4.0 | - |
| 83 | pretrained_segformer_imagenet | CC-BY-NC-SA-4.0 | - |
| 84 | visual_changenet_segmentation_levircd | CC-BY-NC-SA-4.0 | - |
| 85 | visual_changenet_segmentation_mvtec | CC-BY-NC-SA-4.0 | - |
| 86 | cosmos_policy | NVIDIA One-Way Noncommercial License (NSCLv1) | - |
| 87 | monai_vista3d | NVIDIA One-Way Noncommercial License (NSCLv1) | Code: Apache License 2.0" - accessible at http://www.apache.org/licenses/LICENSE-2.0 | Weights: NCLS v1 License |
| 88 | pretrained_mask_grounding_dino_v2 | NVIDIA One-Way Noncommercial License (NSCLv1) | - |
| 89 | maskrcnn_tf1_amp_ckpt | Refer to upstream (DeepLearningExamples) license | - |
| 90 | nnunet_pyt_ckpt_2d_fold2_amp | Refer to upstream (DeepLearningExamples) license | - |
| 91 | nnunet_pyt_ckpt_3d_fold2_amp | Refer to upstream (DeepLearningExamples) license | - |
| 92 | resnet_50_pyt_ckpt | Refer to upstream (DeepLearningExamples) license | - |
| 93 | unetmedical_tf2_ckpt_amp | Refer to upstream (DeepLearningExamples) license | - |
| 94 | unetmedical_tf2_tftrt_amp | Refer to upstream (DeepLearningExamples) license | - |
| 95 | lprnet | NOT STATED (no License section on page) | - |
| 96 | pix2pixhd | NOT STATED (no License section on page) | - |
| 97 | pretrained_detectnet_v2 | NOT STATED (no License section on page) | - |
| 98 | actionrecognitionnet | NOT STATED (page has no license info) | - |
| 99 | bodyposenet | NOT STATED (page has no license info) | - |
| 100 | citysemsegformer | NOT STATED (page has no license info) | - |
| 101 | latent_landmarks_bbc_fgbg_fixedcovariance | NOT STATED (page has no license info) | - |
| 102 | lpdnet | NOT STATED (page has no license info) | - |
| 103 | peoplenet_amr | NOT STATED (page has no license info) | - |
| 104 | peoplesemsegnet | NOT STATED (page has no license info) | - |
| 105 | peoplesemsegnet_amr | NOT STATED (page has no license info) | - |
| 106 | pointpillarnet | NOT STATED (page has no license info) | - |
| 107 | poseclassificationnet | NOT STATED (page has no license info) | - |
| 108 | pretrained_classification | NOT STATED (page has no license info) | - |
| 109 | pretrained_efficientdet | NOT STATED (page has no license info) | - |
| 110 | pretrained_instance_segmentation | NOT STATED (page has no license info) | - |
| 111 | pretrained_semantic_segmentation | NOT STATED (page has no license info) | - |
| 112 | reidentificationnet | NOT STATED (page has no license info) | - |
| 113 | retail_object_detection | NOT STATED (page has no license info) | - |
| 114 | synthetica_detr | NOT STATED (page has no license info) | - |
| 115 | trafficcamnet | NOT STATED (page has no license info) | - |
| 116 | unetmedical_tf2_savedmodel_amp | NOT STATED (page has no license info) | - |
| 117 | vehiclemakenet | NOT STATED (page has no license info) | - |
| 118 | vehicletypenet | NOT STATED (page has no license info) | - |
| 119 | dlpp | NOT FOUND (no NGC catalog page located) | - |
| 120 | nvof | NOT FOUND (no NGC catalog page located) | - |
| 121 | nvsalienc | NOT FOUND (no NGC catalog page located) | - |
| 122 | optimized-peoplesemseg-amr | NOT FOUND (no NGC catalog page located) | - |
| 123 | optimized_peoplenet_amr | NOT FOUND (no NGC catalog page located) | - |
| 124 | polyp_detection_rt_detr_model | NOT FOUND (no NGC catalog page located) | - |
| 125 | vss-vlm-prebuilt-engine | NOT FOUND (no NGC catalog page located) | - |

**Summary counts:**

- 26 — NVIDIA Open Model License
- 5 — NVIDIA Community Model License
- 4 — CC-BY-4.0
- 10 — Apache-2.0
- 1 — MIT
- 1 — OpenMDW-1.1
- 20 — Model EULA (TAO Toolkit)
- 3 — NVIDIA AI Enterprise EULA
- 15 — CC-BY-NC-SA-4.0
- 3 — NVIDIA One-Way Noncommercial License (NSCLv1)
- 6 — Refer to upstream (DeepLearningExamples) license
- 3 — NOT STATED (no License section on page)
- 21 — NOT STATED (page has no license info)
- 7 — NOT FOUND (no NGC catalog page located)
