# PaDiM Optimization GIF Storyboard

## Complete Visual Narrative for Animation

This document describes each frame of the GIF animation in detail. Each paragraph explains what the image should depict, the visual elements to include, and how it connects to the next frame to create a cohesive story about optimizing PaDiM inference from 621ms to 8ms.

---

## Frame 1: Title Card

The opening frame should display a bold title "PaDiM Inference Optimization" centered on a dark background. Below the title, show two boxes side by side: the left box displays "621 ms / 1.6 FPS" in red (representing the slow baseline), and the right box displays "8 ms / 125 FPS" in green (representing the optimized result). An arrow connects them with "77×" written above it. This immediately communicates the magnitude of improvement to the viewer.

---

## Frame 2: The Problem Statement

This frame establishes why optimization was needed. Show a large horizontal progress bar that is completely filled, representing 621ms of inference time. Add a warning icon and text stating "TOO SLOW FOR REAL-TIME". Below, include a brief note: "Goal: Real-time anomaly detection for manufacturing quality control". The visual should convey urgency—the current system cannot meet production requirements.

---

## Frame 3: Time Breakdown Analysis

Display a pie chart or stacked bar showing where the 621ms is spent. The critical insight here is that 95% of the time (approximately 590ms) is consumed by the Mahalanobis distance computation, shown as a massive red segment. The remaining 5% is split between feature extraction (15ms), embedding concatenation (12ms), and post-processing (4ms), shown as tiny segments. A large arrow or spotlight should point to the Mahalanobis segment with text "TARGET: 95% of total time". This frame identifies the bottleneck.

---

## Frame 4: Input Image and ResNet Backbone

Begin explaining the algorithm. Show an input image (224×224 pixels) of a sample object like a bottle on the left side. Draw an arrow pointing into a representation of ResNet18 shown as stacked rectangular layers. The network should be depicted with labeled layers: Conv1, Layer1, Layer2, Layer3. From Layer1, Layer2, and Layer3, draw arrows pointing outward to three feature map boxes labeled f₁ [64, 56, 56], f₂ [128, 28, 28], and f₃ [256, 14, 14]. This visualizes multi-scale feature extraction from the pretrained backbone.

---

## Frame 5: Multi-Scale Feature Concatenation

Show the three feature maps from the previous frame (f₁, f₂, f₃) at the top. Draw upsampling arrows: f₂ gets upsampled 2× to match f₁'s spatial size (56×56), and f₃ gets upsampled 4× to also reach 56×56. All three now have the same spatial dimensions. Show them merging/concatenating into a single large feature map labeled "Embedding E [448, 56, 56]". Add a note: "64 + 128 + 256 = 448 channels". This frame shows how multi-scale information is combined.

---

## Frame 6: Patch Grid Visualization

Display a 56×56 grid representing all spatial positions in the embedding. Highlight a few grid cells and label them as "Position 1", "Position 2", etc., up to "Position 3136". Show that at each position, there is a feature vector of 100 dimensions (after dimension selection from 448). Draw one zoomed-in cell showing a vertical bar representing the 100-dimensional feature vector xᵢ. Text should read: "3,136 spatial positions, each with 100-dimensional feature vector". This establishes the scale of computation needed.

---

## Frame 7: Gaussian Distribution at Each Position

Focus on a single patch position. Show a 2D scatter plot representing the 100-dimensional feature space (simplified to 2D for visualization). Plot multiple dots clustered together representing features from N training images at this position. Draw an ellipse around the cluster representing the Gaussian distribution. Label the center as μᵢ (mean) and the ellipse boundary as defined by Σᵢ (covariance). Add the equations: μᵢ = (1/N)Σxₖᵢ and Σᵢ = covariance + εI. Caption: "Training learns what 'normal' looks like at each position".

---

## Frame 8: Normal vs Anomaly Visualization

Split the frame into two panels. Left panel: Show the Gaussian ellipse with a test point (green dot) inside it, close to the center μ. Label it "Normal: Low Mahalanobis distance, d ≈ 0.5". Right panel: Show the same Gaussian ellipse but with a test point (red star) far outside the ellipse. Label it "Anomaly: High Mahalanobis distance, d ≈ 5.0". This intuitive visualization explains how anomaly detection works—deviations from the learned normal distribution indicate defects.

---

## Frame 9: Mahalanobis Distance Equation

Center the Mahalanobis distance formula prominently: d(x) = √[(x - μ)ᵀ Σ⁻¹ (x - μ)]. Below the equation, provide a legend explaining each term: x is the test feature vector [100], μ is the mean from training [100], and Σ⁻¹ is the inverse covariance matrix [100×100]. Add interpretation text: "Small d → Normal, Large d → Anomaly". This frame establishes the mathematical foundation before showing the computational problem.

---

## Frame 10: Baseline Loop - The Bottleneck

Show a code-like flowchart of the baseline algorithm. Display a large FOR loop box: "FOR i = 1 TO 3136". Inside the loop, show three sequential operations: (1) "Extract xᵢ", (2) "Compute Σᵢ⁻¹ = inverse(Σᵢ)" with a red warning label "O(100³) = 1,000,000 ops", and (3) "Calculate dᵢ using Mahalanobis". Emphasize that step 2 (matrix inversion) happens 3,136 times. Add a timer showing "590 ms" for this loop. Highlight that this is sequential—no parallelism.

---

## Frame 11: Optimization 1 - Pre-compute Inverse

Split the frame to show "Before" and "After". On the left (Before): Show the loop with Σ⁻¹ computation inside, highlighted in red. On the right (After): Show the inverse computation moved outside and above the loop, happening only once during training. The loop now only contains the distance calculation using pre-loaded Σ⁻¹. Draw an arrow showing the inverse moving from "Inference Time" to "Training Time". Show time reduction: 621ms → 80ms. Add "8× SPEEDUP" badge. Caption: "3,136 matrix inversions eliminated from inference".

---

## Frame 12: The Problem with Sequential Loops

Visualize the sequential nature of the baseline. Show 3,136 small boxes arranged in a long horizontal line, each representing one loop iteration. Only one box at a time is highlighted (active), while all others wait. Draw a clock or timeline below showing time progressing slowly. Add text: "One position at a time, 3,136 sequential operations". Contrast this with the potential: "But each position is INDEPENDENT—they don't depend on each other!" This sets up the vectorization solution.

---

## Frame 13: Optimization 2 - Vectorization with Einsum

Show the transformation from loop to parallel operation. Top half: The old loop "FOR i = 1 TO 3136: compute dᵢ" with sequential arrows. Bottom half: A single large tensor operation box labeled "einsum('cdi,bdi→bci', Σ⁻¹, diff)" that processes ALL positions simultaneously. Draw 3,136 parallel arrows going through the operation at once. Show time reduction: 80ms → 36ms. Add "2× SPEEDUP (17× cumulative)" badge. Caption: "3,136 sequential operations → 1 tensor operation".

---

## Frame 14: Einsum Parallel Computation Visualization

Illustrate how einsum works in parallel. Show three matrices side by side representing positions 1, 2, and 3136: each has Σᵢ⁻¹ [100×100] multiplied by diffᵢ [100]. All three multiplications happen simultaneously (shown with parallel vertical arrows dropping down at the same time). Below, show the outputs tmp₁, tmp₂, tmp₃₁₃₆ appearing together. Add CPU icons with "SIMD/AVX" labels showing hardware-level parallelism. Caption: "All 3,136 matrix-vector products computed in ONE CPU instruction".

---

## Frame 15: Optimization 3 - ONNX Runtime

Show PyTorch logo on the left with text "Eager Execution: ops run one-by-one" and ONNX logo on the right with text "Graph Optimization: fused operations". Draw an arrow between them labeled "Export". Below ONNX, list optimizations: "Operator fusion", "Memory planning", "Platform-specific kernels". Show the model structure inside ONNX: Input → ResNet18 → Embedding → Output. Show time reduction: 36ms → 16ms. Add "2× SPEEDUP (39× cumulative)" badge. Caption: "Graph-level optimizations reduce overhead".

---

## Frame 16: Optimization 4 - GPU Acceleration

Split frame showing CPU vs GPU. Left side: Single CPU core icon processing sequentially. Right side: GPU with hundreds of small cores processing in parallel. Draw the pipeline: Image → [GPU: ResNet + Embedding, 6ms] → [CPU: Mahalanobis, 2ms] → Score. Show that the heavy computation (feature extraction) runs on GPU while the already-optimized Mahalanobis stays on CPU. Show time reduction: 16ms → 8ms. Add "2× SPEEDUP (77× cumulative)" badge. Caption: "GPU parallelism for feature extraction".

---

## Frame 17: Complete Pipeline Comparison

Show two horizontal pipelines stacked vertically. Top pipeline (Before): Image → ResNet (CPU, 15ms) → Embed (CPU, 12ms) → FOR loop with inv() (590ms) → Score. The FOR loop box is huge and red. Bottom pipeline (After): Image → ONNX on GPU (6ms) → einsum Mahalanobis (2ms) → Score. All boxes are small and green. Draw a dramatic size comparison between the two pipelines. Caption: "From 621ms sequential to 8ms parallel".

---

## Frame 18: Benchmark Results Bar Chart

Display a horizontal bar chart with all configurations ranked by inference time. Bars from top to bottom: Baseline PyTorch (621ms, very long red bar), Hybrid-CPU (36ms), Mahal ONNX-CPU (32ms), Full ONNX-CPU (16ms), Hybrid-GPU (12ms), Mahal ONNX-GPU (11ms), Full ONNX-GPU (8ms, short green bar with star). Add FPS values on the right: 1.6, 27.6, 31.5, 63.1, 83.0, 92.3, 124.8. Highlight the winner with a trophy icon.

---

## Frame 19: Speedup Progression Chart

Show a step chart or bar graph illustrating cumulative speedup at each optimization stage. X-axis: Baseline → Pre-compute → Vectorize → ONNX → GPU. Y-axis: Speedup (1× to 80×). Bars rise progressively: 1× → 8× → 17× → 39× → 77×. Each bar should be a different color, getting progressively more green. Draw cumulative improvement percentages between bars. Caption: "Each optimization compounds on the previous".

---

## Frame 20: FPS Improvement Visualization

Show a speedometer or gauge visualization. Left gauge shows 1.6 FPS with needle in the red zone (too slow). Right gauge shows 124.8 FPS with needle in the green zone (real-time ready). Alternatively, show an animation-style comparison: a slow-motion camera icon (1.6 FPS) transforming into a high-speed camera icon (125 FPS). Add context: "Real-time threshold: 30 FPS" with a line showing both values relative to it. The optimized version is 4× above real-time requirements.

---

## Frame 21: CPU vs GPU Comparison Table

Display a table with three rows (Hybrid, Full ONNX, Mahalanobis ONNX) and columns for CPU time, GPU time, and GPU speedup. Include mini bar charts within cells for visual comparison. Show that GPU provides 2-3× speedup over CPU for each variant. Add a key insight box: "Algorithm optimization: 40× improvement. GPU acceleration: 2× improvement. GPU alone without algorithm fix: only 1.1×". This emphasizes that algorithmic optimization was more important than hardware acceleration.

---

## Frame 22: Accuracy Verification

Show two identical accuracy displays side by side. Left (Before): "Image AUROC: 90.54%, Pixel AUROC: 96.52%". Right (After): "Image AUROC: 90.54%, Pixel AUROC: 96.52%". Draw an equals sign between them with a green checkmark. Add text: "Numerical difference < 0.00001". Below, show a badge: "77× FASTER + ZERO ACCURACY LOSS = PRODUCTION READY". This critical frame proves that speed improvements didn't sacrifice detection quality.

---

## Frame 23: Key Equations Summary

Display all three key equations in a clean layout. Equation 1 (Training): μᵢ = (1/N)Σxₖᵢ and Σᵢ = covariance + εI. Equation 2 (Inference): d(x) = √[(x-μ)ᵀ Σ⁻¹ (x-μ)]. Equation 3 (Vectorized): D = einsum('cdi,bdi→bci', Σ⁻¹, X-μ). Label each equation with its purpose: "Learn Normal", "Detect Anomaly", "Parallel Computation". This provides a mathematical summary of the entire system.

---

## Frame 24: Final Summary Card

Create a clean summary card with three columns. Column 1 (Metric): Time, FPS, Speedup, Accuracy. Column 2 (Before): 621ms, 1.6, 1×, 90.5%. Column 3 (After): 8ms, 125, 77×, 90.5%. Use red for "Before" values and green for "After" values. Below the table, display three achievement badges: "77× FASTER", "REAL-TIME READY", "ZERO ACCURACY LOSS". End with "PRODUCTION READY" in a prominent banner. This final frame leaves viewers with the key takeaways.

---

## Animation Timing Recommendations

| Frame | Duration | Transition |
|-------|----------|------------|
| 1. Title | 4 sec | Fade in |
| 2. Problem | 3 sec | Slide right |
| 3. Time Breakdown | 4 sec | Fade |
| 4. ResNet | 4 sec | Slide right |
| 5. Concatenation | 3 sec | Slide right |
| 6. Patch Grid | 3 sec | Zoom |
| 7. Gaussian Training | 4 sec | Fade |
| 8. Normal vs Anomaly | 4 sec | Split |
| 9. Mahalanobis Equation | 4 sec | Fade |
| 10. Baseline Loop | 4 sec | Fade |
| 11. Opt 1: Pre-compute | 4 sec | Slide down |
| 12. Sequential Problem | 3 sec | Fade |
| 13. Opt 2: Vectorize | 4 sec | Slide down |
| 14. Einsum Visual | 3 sec | Fade |
| 15. Opt 3: ONNX | 3 sec | Slide down |
| 16. Opt 4: GPU | 4 sec | Slide down |
| 17. Pipeline Compare | 4 sec | Split |
| 18. Benchmark Bars | 4 sec | Grow bars |
| 19. Speedup Chart | 4 sec | Grow bars |
| 20. FPS Gauges | 3 sec | Animate needle |
| 21. CPU vs GPU | 3 sec | Fade |
| 22. Accuracy | 3 sec | Checkmark pop |
| 23. Equations | 4 sec | Fade |
| 24. Summary | 5 sec | Fade + hold |

**Total Duration: ~90 seconds**

---

## Color Scheme

- **Background**: Dark (#1a1a1a)
- **Text**: White (#ffffff)
- **Baseline/Slow/Problem**: Red (#ED1C24)
- **Optimized/Fast/Success**: Green (#4CAF50)
- **Intermediate steps**: Orange (#FF9800)
- **Equations/Math**: Cyan (#00BCD4)
- **Arrows/Flow**: Light gray (#888888)

---

## Visual Style Notes

1. Keep each frame clean and focused on ONE concept
2. Use consistent iconography throughout (CPU, GPU, clock, checkmark)
3. Progress bars and charts should use the red-to-green gradient to show improvement
4. Equations should be large and centered when they are the focus
5. Use animation to show transformation (before → after)
6. Keep text minimal—let visuals tell the story
7. End each optimization frame with the cumulative speedup badge