---
marp: true
paginate: true
footer: '![h:50](./themes/pavs-logo.png)'
style: |
  @import url('status-styles.css');

  /* Dark theme with auto-scaling */
  section {
    font-family: 'Helvetica', 'Arial', sans-serif;
    padding: 40px 50px 70px 50px;
    overflow: hidden;
    background-color: #1a1a1a;
    color: #ffffff;
  }

  /* Ensure footer doesn't overlap content */
  section::after {
    content: '';
    display: block;
    height: 40px;
  }

  /* Auto-scale content to fit - use these classes on dense slides */
  section.small {
    font-size: 21px;
  }

  section.smaller {
    font-size: 19px;
  }

  section.smallest {
    font-size: 17px;
    padding: 25px 50px 70px 50px;
  }

  section.smallest li {
    margin-bottom: 0.05em;
  }

  section.smallest h2 {
    font-size: 1.35em;
    margin-bottom: 0.3em;
    margin-top: 0;
  }

  section.smallest h3 {
    font-size: 1.08em;
    margin-top: 0.2em;
    margin-bottom: 0.25em;
  }

  section.smallest pre {
    font-size: 0.68em;
    padding: 8px;
    margin: 0.25em 0;
  }

  section.smallest ul, section.smallest ol {
    margin: 0.2em 0;
  }

  section.tiny {
    font-size: 14px;
    padding: 30px 50px 70px 50px;
  }

  section.tiny li {
    margin-bottom: 0.05em;
  }

  section.tiny h2 {
    font-size: 1.3em;
    margin-bottom: 0.3em;
  }

  section.tiny h3 {
    font-size: 1.05em;
    margin-top: 0.2em;
    margin-bottom: 0.2em;
  }

  section.tiny pre {
    font-size: 0.65em;
    padding: 8px;
    margin: 0.3em 0;
  }

  /* Optimized size - maximum readability without clipping */
  section.optimized {
    font-size: 15.5px;
    padding: 22px 50px 70px 50px;
  }

  section.optimized li {
    margin-bottom: 0.03em;
    line-height: 1.3;
  }

  section.optimized h2 {
    font-size: 1.32em;
    margin-bottom: 0.25em;
    margin-top: 0;
    line-height: 1.2;
  }

  section.optimized h3 {
    font-size: 1.06em;
    margin-top: 0.15em;
    margin-bottom: 0.2em;
    line-height: 1.2;
  }

  section.optimized pre {
    font-size: 0.67em;
    padding: 7px;
    margin: 0.2em 0;
    line-height: 1.3;
  }

  section.optimized ul, section.optimized ol {
    margin: 0.15em 0;
  }

  section.optimized strong {
    line-height: 1.3;
  }

  section.compact {
    font-size: 18px;
  }

  h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
  }

  h1 {
    font-size: 1.8em;
    font-weight: bold;
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.2em;
    margin-bottom: 0.5em;
  }

  h2 {
    font-size: 1.4em;
    margin-top: 0;
  }

  h3 {
    font-size: 1.1em;
    color: #aaaaaa;
    margin-top: 0;
  }

  /* Tables - compact */
  table {
    font-size: 0.85em;
    width: 100%;
    background-color: #1a1a1a;
  }

  th, td {
    padding: 6px 10px;
  }

  thead {
    background-color: #3498db !important;
  }

  thead th {
    color: white !important;
    background-color: #3498db !important;
  }

  tbody tr:nth-child(odd) {
    background-color: #2a2a2a;
  }

  tbody tr:nth-child(even) {
    background-color: #1a1a1a;
  }

  td, th {
    color: #ffffff;
  }

  /* Lists - tighter spacing */
  ul, ol {
    margin: 0.3em 0;
  }

  li {
    margin-bottom: 0.3em;
  }

  /* Code blocks - compact, dark text, light background */
  pre {
    font-size: 0.7em;
    padding: 10px;
    background-color: #e8e8e8;
    border-radius: 5px;
    color: #000000 !important;
  }

  pre code {
    color: #000000 !important;
    background-color: transparent;
  }

  code {
    background-color: #2a2a2a;
    color: #00bcd4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
  }

  .code-large pre {
    font-size: 1.1em;
  }

  /* Links */
  a {
    color: #00bcd4;
  }

  /* Strong/bold text */
  strong {
    color: #3498db;
  }

  /* Footer - logo on right */
  footer {
    position: absolute;
    bottom: 20px;
    left: auto;
    right: 40px;
    width: auto;
  }

  footer img {
    height: 50px;
  }

  /* Success/warning colors */
  .success {
    color: #4caf50;
    font-weight: bold;
  }

  .warning {
    color: #ff9800;
    font-weight: bold;
  }

  .violet {
    color: #9b59b6 !important;
  }

  /* Grid layout helper */
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5em;
  }

  .columns-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1em;
  }

  .columns-wide {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1em;
  }

  /* Lead slide styling */
  section.lead {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.lead h1 {
    border-bottom: none;
    font-size: 2.2em;
  }

  /* Highlight box */
  .highlight-box {
    background-color: #2a2a2a;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 10px 0;
  }

  .metric-large {
    font-size: 2.5em;
    font-weight: bold;
    color: #4caf50;
  }

  .metric-label {
    font-size: 0.9em;
    color: #888888;
  }

---

<!-- _class: lead -->

# PaDiM Model Optimization

### From Research Code to Production-Ready Inference

**77x Performance Improvement**

March 2026

---

<!-- _class: small -->

## What is PaDiM & Why Does It Matter?

### Patch Distribution Modeling for Anomaly Detection

<div class="columns">
<div>

**How It Works:**
1. **Learn "Normal"**: Extract features from +ve examples using CNN backbone
2. **Build Statistical Model**: Fit Gaussian distribution per patch location
3. **Detect Anomalies**: Measure deviation using Mahalanobis distance

**Why PaDiM is Important:**
- Zero-shot anomaly detection: - no -ve samples needed
- Defect localization: - pinpoints exact anomaly location
- State-of-the-art: - 96%+ AUROC on MVTec AD benchmark

</div>
<div>

**The Challenge:**
- Implementation taken from a popular open-source repository
- **Not production-ready** out of the box
- **Not designed for edge compute**
- Sequential processing, heavy Python overhead

![w:400](./images/Padim_repo_v2.png)

**Industry Applications:**
- Manufacturing quality control
- PCB inspection
- Surface anomaly detection

</div>
</div>

---

<!-- _class: tiny -->

## PaDiM Pipeline: Gaussian Scanning Process

<div class="columns-wide">
<div>

![w:700 h:480](./gif_gen/gaussian_frames/frame_031.png)

</div>
<div class="code-large">

*Each patch compared against learned Gaussian distribution*

**Pipeline Steps:**
1. Feature Extraction (ResNet18)
2. Embedding Concat (448D)
3. Dimension Reduction (→100D)
4. Gaussian Scan - Compare each patch to learned distribution
5. Anomaly Map - Mahalanobis distance per spatial location

**The Bottleneck:**
- 3,136 spatial positions
- Each needs distance computation
- Python loop with SciPy calls

</div>
</div>

---

<!-- _class: small -->

## Key Optimization Insight

### Inverse Covariance Can Be Pre-computed

<div class="columns">
<div>

**Original Approach (Per-Inference):**
```
For each of 3,136 positions:
    1. Get covariance matrix Σ
    2. Compute inverse Σ⁻¹  ← SLOW!
    3. Calculate Mahalanobis distance
```

**Problem:** Computing Σ⁻¹ is O(n³) = O(100³)

**Solution:**
- Σ⁻¹ is **constant** after training
- Compute once, save to disk (~31 MB)
- Load and reuse during inference

**Impact:** Eliminates 3,136 matrix inversions at runtime

</div>
<div>

**Optimized Pipeline:**

With `inv_cov` and `mean` pre-computed and loaded:

```python
# Pre-loaded from training
mean = load("mean.pkl")        # [100, 56, 56]
inv_cov = load("inv_cov.pkl")  # [100, 100, 56, 56]

# Inference - no matrix inverse needed!
diff = embedding - mean
dist = mahalanobis(diff, inv_cov)
```

**Result:** The expensive operations are moved to training time. Rest of the loop can be **parallelized** and **converted to ONNX**.

</div>
</div>

---

<!-- _class: tiny -->

## Vectorized Mahalanobis Distance

<div class="columns-wide">
<div>

![w:700 h:480](./gif_gen/gaussian_frames/frame_090.png)

</div>
<div class="code-large">

**Implementation (Einstein Summation):**
```python
left = np.einsum('ci,cdij->di', diff, inv_cov)
dist = np.sqrt(np.einsum('di,di->i', diff, left))
```
- **Mahalanobis:** $d(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}$
- **Vectorized:** $\text{dist}[i] = \sqrt{\sum_{c,d} \text{diff}[c,i] \cdot \Sigma^{-1}[c,d,i] \cdot \text{diff}[d,i]}$
- **Key Insight:** 
  - No Python loops
  - BLAS/LAPACK optimized, CPU SIMD (AVX2)
  - **ONNX convertible**
  - All 3,136 distances in ONE op
</div>
</div>




---

## Performance Results

### Speed Gains from Baseline to Full ONNX GPU

| Configuration | Time (ms) | FPS | vs Baseline |
|---------------|-----------|-----|-------------|
| Baseline PyTorch (scipy loop) | 621.51 | 1.6 | 1.0x |
| Pre-computed Σ⁻¹ | ~80 | ~12 | ~8x |
| + Vectorized einsum (CPU) | 36.22 | 27.6 | 17.2x |
| + ONNX Runtime (CPU) | 15.86 | 63.1 | 39.2x |
| **+ GPU (MIGraphX)** | **8.01** | **124.8** | **77.6x** |

<div class="highlight-box">

**Key Achievement:** From 621 ms to 8 ms — **77x speedup** with zero accuracy loss

</div>

---

<!-- _class: small -->

## Future Optimization Opportunities

### What Could Be Done Next

<div class="columns">
<div>

**NPU Acceleration:**
- Running CNN backbone on **NPU** could improve performance
- AMD XDNA / Intel NPU support via ONNX Runtime
- Offload ResNet18 feature extraction
- Free up GPU for other tasks

**Mahalanobis Distance Optimization:**
- Explore more optimal versions of `Mahalanobis Distance` compatible for **NPU/GPU**
- Custom kernels for einsum operations
- Fused operations to reduce memory bandwidth

</div>
<div>

**Other Opportunities:**

| Technique | Potential | Complexity |
|-----------|-----------|------------|
| NPU backbone | 1.5-2x | Medium |
| INT8 quantization | 1.5-2x | Medium |
| Batch inference | Nx for N images | Low |
| Custom HIP kernel | 1.2x | High |

**Current Status:**
- 125 FPS already exceeds real-time requirements
- Further optimization for edge deployment scenarios

</div>
</div>

---

<!-- _class: lead -->

# Summary

### 77x Faster | 8ms Inference | 125 FPS

<div style="margin-top: 40px;">

| Metric | Baseline | Optimized |
|--------|----------|-----------|
| Time | 621 ms | **8 ms** |
| FPS | 1.6 | **125** |
| Speedup | - | **77x** |
| Accuracy | 90.5% | **90.5%** |

</div>

**Key Takeaways:**
- Pre-compute inverse covariance at training time
- Vectorize with einsum for parallel computation
- ONNX + GPU acceleration for production deployment

**Questions?**
