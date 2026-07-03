I have worked in reducing algoritmic latency of padim model,  the repo is here and there a code in whyc refelctes these changes. Look at the repo search on internet to get some citations about some work related that. I have a presentation about the things i have don in this works and 


- github repo look at code at `~/Workspace/physical_ai_sdk/models/padim`, and `~/Workspace/physical_ai_sdk/models/padim/scripts/archive/research`; 
- summary of the work done: 
    `I have recently worked on the PaDiM model for releasing with the Kraken2e setup. The model from AIG is not yet ready, so I have attempted to implemented it.
    I started with a very popular repo: https://github.com/xiahaifeng1995/PaDiM-Anomaly-Detection-Localization-master.git - though this has 100+ forks and 470+ stars, the model has compute issues  moving it to production on edge devices. The initial model runs at 1.7 FPS on GPU.
 
      The Problem:
              This model takes an input image and extracts a (100 × 56 × 56) patch embedding using ResNet18. To generate an anomaly probability map, it computes Mahalanobis distance at each of the 3,136 spatial positions (56 × 56 grid).
 
    The baseline implementation spent 95% of inference time (~590 ms out of 621 ms) in this Mahalanobis computation because:
                                           - It runs  a  loop over 3,136 positions
                                          -  At each position, it computes a 100×100 matrix inverse - O(n³) operation
                                           - Uses scipy function calls with significant overhead
                                           - No GPU parallelism - everything runs on CPU
 
    The Solution:
              The key insight is that the covariance matrix is constant after training - it doesn't change between images. So instead of computing 3,136 inversions per image at runtime:
                             1. Pre-compute the inverse of covariance once after training for all spatial positions and save it (~31 MB)
                             2. Replace the Python loop with vectorized NumPy einsum operations, Now the models is ONNX compatible
                             3. Export the backbone to ONNX for GPU acceleration
 
    With these optimizations, the entire Mahalanobis computation happens in a single tensor operation, and the model runs end-to-end on GPU in ONNX format.
 
    Results:
            Metric      original      Optimized
            ─────────────────────────────────
              GPU                    1.7 FPS     125 FPS
              CPU                    1.6 FPS     64 FPS
              Speedup           -           77x
              Accuracy           90.5%       90.5% (preserved)
 
    I am attaching the complete slides for this work(). Please have a look.
    I have also provided a training pipeline for this model so users can add newer image classes and extend the model.
`