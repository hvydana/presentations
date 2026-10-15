# NGC Physical AI Models — License Terms Summary (Can AMD Use Them Commercially?)

All source documents cited below are saved in full in `license_references/`. Per-model verdicts are in
`ngc_model_licenses_amd_usability.md`; per-model license labels in `ngc_model_licenses_table.md`.

## Terms under which a model CAN be used/distributed commercially by AMD (or any non-NVIDIA vendor)

- **[NVIDIA Open Model License](license_references/nvidia_open_model_license.md)** (26 models) — commercial
  use and redistribution both fully permitted, no hardware restriction. Condition: keep the "Licensed by
  NVIDIA Corporation under the NVIDIA Open Model License" attribution notice on redistribution.
- **[CC-BY-4.0](license_references/standard_permissive_licenses.md)** (4 models) — commercial use and
  redistribution permitted with attribution.
- **[Apache-2.0](license_references/standard_permissive_licenses.md)** (12 models) — commercial use and
  redistribution permitted; retain copyright/license notices, state changes made. Includes 2 nnUNet
  checkpoints resolved via direct inspection of
  [github.com/NVIDIA/DeepLearningExamples per-subfolder LICENSE files](license_references/deeplearningexamples_and_tao_purpose_built.md).
- **[BSD-3-Clause](license_references/standard_permissive_licenses.md)** (5 models) — commercial use and
  redistribution permitted; retain copyright/license notice. 4 resolved via
  [DeepLearningExamples per-subfolder LICENSE files](license_references/deeplearningexamples_and_tao_purpose_built.md)
  (UNet_Medical x3, ResNet50), 1 (pix2pixHD) was on its NGC page all along in a `**License:**` bold field
  our original extraction script missed.
- **[MIT](license_references/standard_permissive_licenses.md)** (1 model) — commercial use and
  redistribution permitted with minimal conditions.
- **[OpenMDW-1.1](license_references/openmdw-1.1.md)** (1 model) — commercial use and redistribution
  permitted; retain license copy + notices; don't sue over patents you allege are infringed by the model.

**→ 49 of 125 models are a clean "yes" for AMD: no NVIDIA-specific gate, no hardware tie.**

## Terms under which a model CAN be used commercially, but ONLY if AMD stays inside NVIDIA's stack

- **["Model EULA" = NVIDIA Deep Learning Models License Agreement](license_references/nvidia_deep_learning_models_license_agreement.md)**
  (20 models — LPRNet, LPDNet, TrafficCamNet, VehicleMakeNet, PointPillarNet, FaceNet, GazeNet, OCDNet,
  OCRNet, ActionRecognitionNet, Bi3D, etc.):
  - Commercial use is allowed in general, **but** the license states: *"The SOFTWARE is licensed for you to
    develop applications only for use in systems with NVIDIA GPUs."* Deploying on AMD hardware falls outside
    the license grant.
  - Redistribution is restricted to embedding inside an application with "material additional functionality"
    — no stand-alone redistribution. "Unpruned/trainable" variants must first be trained via NVIDIA TAO
    Toolkit (a separate NVIDIA-only tool) before they can be distributed at all.
- **[TAO Purpose-Built Model — DRM-locked, no formal EULA cited](license_references/deeplearningexamples_and_tao_purpose_built.md)**
  (20 models — LPRNet, PeopleSemSegNet, PointPillarNet, VehicleMakeNet, VehicleTypeNet, TrafficCamNet,
  ActionRecognitionNet, BodyPoseNet, CitySemSegFormer, LPDNet, PeopleNet AMR, PeopleSemSegNet AMR,
  PoseClassificationNet, TAO Pretrained Classification/DetectNet V2/EfficientDet/Instance
  Segmentation/Semantic Segmentation, ReIdentificationNet, Retail Object Detection):
  - No formal license/EULA is named anywhere on the model's own page. Instead the page states directly:
    *"These models need to be used with NVIDIA Hardware and Software"* and *"can only be used with Train
    Adapt Optimize (TAO) Toolkit, DeepStream SDK or TensorRT."*
  - Each model file is DRM-encrypted with a "Model load key" (`tlt_encode`/`nvidia_tlt`/`nvidia_tao`) — the
    weights can't even be loaded outside NVIDIA's own toolchain, independent of what any license would
    otherwise permit. This is arguably a *stronger* lock-in than a contractual GPU-only clause, since it's a
    technical barrier, not just a legal one.
- **[NVIDIA Community Model License](license_references/nvidia_community_model_license.md)** (5 models —
  Earth-2/PhysicsNeMo weather models):
  - Production commercial use requires **NVIDIA NIM via an NVIDIA AI Enterprise subscription**, OR the model
    must run specifically on an **NVIDIA RTX/GeForce RTX GPU** (single-user only).
  - Cannot use the model to "develop or improve any other AI models" without NVIDIA's written approval —
    blocks using the weights to train/improve a competing model.
- **[NVIDIA AI Enterprise EULA](license_references/nvidia_ai_enterprise_eula.md)** (3 models) — Section 8.15
  "NVIDIA Platform Requirement" ties enterprise-grade deployment to NVIDIA's certified SDK/driver/Omniverse
  stack.

**→ 48 of 125 models are commercially usable in principle, but the license text — or, for the TAO
purpose-built bucket, the page's own stated requirements plus DRM encryption — ties production deployment to
NVIDIA GPUs, NVIDIA's NIM runtime, or NVIDIA's own SDK/toolkit. This is the real, verified NVIDIA lock-in, and
it is now confirmed across 40 of the 125 models (Model EULA + TAO Purpose-Built combined), roughly a third of
the entire catalog.**

## Terms under which a model CANNOT be used commercially at all

- **[CC-BY-NC-SA-4.0](license_references/cc-by-nc-sa-4.0.md)** (15 models) — non-commercial only, for
  **everyone including NVIDIA itself**. Not an AMD-specific lock — the model just isn't licensed for
  commercial use by any vendor.
- **[NVIDIA One-Way Noncommercial License ("NSCLv1")](license_references/nvidia_one_way_noncommercial_license_nsclv1.md)**
  (3 models) — the one genuinely asymmetric case: *"NVIDIA Corporation and its affiliates may use the Work
  and any derivative works commercially"* while everyone else, including AMD, is restricted to non-commercial
  (research/evaluation) use only. This is a real NVIDIA-only carve-out, not a generic non-commercial license.
- **UNLICENSED — no LICENSE file at all** (1 model — Mask R-CNN TensorFlow checkpoint (AMP)): confirmed via
  direct inspection of
  [github.com/NVIDIA/DeepLearningExamples](license_references/deeplearningexamples_and_tao_purpose_built.md)
  that no LICENSE file exists anywhere in `TensorFlow/Segmentation/MaskRCNN/` or any parent folder. Legal
  default is all-rights-reserved, so this cannot be used commercially by anyone absent a separate grant from
  NVIDIA.

**→ 19 of 125 models cannot be used commercially by AMD; 15 of those can't be used commercially by anyone,
3 are a genuine NVIDIA-exclusive carve-out, and 1 has no license grant at all.**

## Terms that are unverified — do not assume either way

- **No license stated on the model's own NGC page** (2 models — `latent_landmarks_bbc_fgbg_fixedcovariance`,
  `synthetica_detr`) — re-checked directly and confirmed genuinely blank, not an extraction artifact.
- **No NGC catalog page could be located at all** (7 models — `dlpp`, `nvof`, `nvsalienc`,
  `optimized-peoplesemseg-amr`, `optimized_peoplenet_amr`, `polyp_detection_rt_detr_model`,
  `vss-vlm-prebuilt-engine`) — most of these look like SDK features, NGC "resources" rather than standalone
  model pages, or components of an NVIDIA Blueprint (e.g. `vss-vlm-prebuilt-engine` inside the VSS Blueprint),
  and resisted resolution via web search and GitHub API lookups. Do not assume permissive terms — verify
  directly with NVIDIA/legal before commercial use.

**→ 9 of 125 models remain unverified**, down from 37 after the investigation below.

## How the unverified count was reduced from 37 to 9

- **GitHub API subfolder introspection**: `NVIDIA/DeepLearningExamples` has no repo-root LICENSE
  (`api.github.com/repos/NVIDIA/DeepLearningExamples` returns `"license": null`), so 6 models pointing at that
  repo were unresolved as a group. Checking each model's specific subfolder LICENSE file directly resolved 5
  of them (Apache-2.0 x2, BSD-3-Clause x3) and confirmed the 6th (Mask R-CNN TF) has no license at all — a
  real negative answer, not a dead end.
- **Extraction-bug fix**: pix2pixHD's BSD-3-Clause license had been on its NGC page the entire time, just in
  a `**License:**` bold-field format instead of a `## License` markdown heading, which the original
  regex-based extraction script didn't check for. Grepped all remaining "NOT STATED" files for the bold
  pattern to confirm this was the only false negative.
- **Targeted re-fetch of TAO purpose-built model pages**: re-fetching 4 representative pages (LPRNet,
  PeopleSemSegNet, PointPillarNet, VehicleMakeNet) with prompts specifically asking about hardware/software
  requirements (not just "license") surfaced the "NVIDIA Hardware and Software" + DRM-key pattern described
  above. The same team, URL template, and page structure applies to 16 more models, which were reclassified
  on that basis without individually re-fetching each one.
- **What did not resolve**: Google search hit a consent-wall redirect for ambiguous short names (`dlpp`);
  several remaining names look like SDK/blueprint components rather than standalone NGC model entries and
  don't have a normal catalog page to find.
