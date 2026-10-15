# Standard Permissive Licenses (referenced, not NVIDIA-authored)

Used across the NGC physical-AI list where the model/weights are licensed under a well-known open license
rather than an NVIDIA-specific one.

## CC-BY-4.0 (4 models, e.g. BodyPose3DNet)
Source: https://creativecommons.org/licenses/by/4.0/legalcode
Commercial use and redistribution both permitted; attribution to the original author required.

## Apache-2.0 (10 models, e.g. most MONAI bundles' code license, mit-han-lab/bevfusion)
Source: https://www.apache.org/licenses/LICENSE-2.0
Commercial use and redistribution both permitted; must retain copyright/license notices and state changes;
includes an express patent grant.

## MIT (1 model)
Source: https://opensource.org/license/mit/
Commercial use and redistribution both permitted with minimal conditions (retain copyright + license text).

## Note on MONAI dual-licensing
Two MONAI bundles (`monai_vista2d`, `monai_vista3d`) split licensing: Apache-2.0 for the code, but the
**model weights** are under CC-BY-NC-SA-4.0 (noncommercial) — see `cc-by-nc-sa-4.0.md`. Always check whether
"Apache-2.0" on an NGC page refers to the code, the weights, or both.
