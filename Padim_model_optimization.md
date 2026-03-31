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

  .center-table table {
    width: auto;
    margin: 0 auto;
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
    align-items: center;
  }

  section.lead h1 {
    border-bottom: none;
    font-size: 2.2em;
  }

  section.lead table {
    width: auto;
    margin: 0 auto;
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

**549x Performance Improvement**

March 2026

---

<!-- _class: smallest -->

## What is PaDiM & Why Does It Matter?

<div class="columns">
<div>

**How It Works:**
1. **Learn "Normal"**: Extract features from +ve examples using CNN backbone
2. **Build Statistical Model**: Fit Gaussian distribution per patch location
3. **Detect Anomalies**: Measure deviation using Mahalanobis distance

**Why PaDiM is Important:**
- **Zero-shot anomaly detection** - no -ve samples needed
- **Used in** Manufacturing QC, PCB inspection, Surface anomaly detection
- State-of-the-art - 96%+ AUROC on MVTec AD benchmark

</div>
<div>

**The Challenge:**
- Implementation from popular open-source repo
- **Not production-ready** out of the box
- **Not designed for edge compute**
- Sequential processing, Python overhead

![w:580](./images/Padim_repo_v2.png)

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

## The Bottleneck: Where Was Time Being Spent?

<div class="columns">
<div>

### Baseline Time Breakdown

| Component | Time | % of Total |
|-----------|------|------------|
| Feature Extraction | 15 ms | 2.4% |
| Embedding Concat | 12 ms | 1.9% |
| **Mahalanobis Loop** | **590 ms** | **95%** |
| Post-processing | 4 ms | 0.6% |
| **Total** | **621 ms** | 100% |

</div>
<div>

### Root Cause Analysis

**The Problem:**
- 3,136 spatial positions to compute
- Each requires 100×100 matrix inverse
- Python loop with SciPy calls

**Complexity:**
- Matrix inverse: O(n³) = O(100³)
- Total: 3,136 × O(100³) operations
- Sequential, non-parallelized

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
- Compute once, save to disk
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
tmp = np.einsum('cdi,bdi->bci', inv_cov, diff)
dist = np.sqrt(np.einsum('bci,bci->bi', diff, tmp))
```
- **Mahalanobis:**  $d(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}$
- **Vectorized:**  $\text{dist}[i] = \sqrt{\sum_{c} \sum_{d} \text{diff}[c,i] \cdot \Sigma^{-1}[c,d,i] \cdot \text{diff}[d,i]}$
- **Key Insight:** 
  - No Python loops
  - BLAS/LAPACK optimized, CPU SIMD (AVX2)
  - **ONNX convertible**
  - All 3,136 distances in ONE op
</div>
</div>




---

## Performance Results

### Speed Gains from Baseline to BF16 + Diagonal Covariance

| Configuration | Time (ms) | FPS | vs Baseline |
|---------------|-----------|-----|-------------|
| Baseline PyTorch CPU (scipy loop) | 621.51 | 1.6 | 1.0x |
| + Pre-computed Σ⁻¹ | ~80 | ~12 | ~8x |
| + Vectorized einsum (CPU) | ~36 | ~28 | ~17x |
| + ONNX Runtime (CPU) | ~15 | ~67 | ~41x |
| + GPU MIGraphX (FP32 + Full Cov) | 7.43 | 135 | 84x |
| + GPU BF16 (Full Cov) | 6.79 | 147 | 92x |
| **+ GPU BF16 + Diagonal Cov** | **1.14** | **878** | **549x** |

<div class="highlight-box">

**Key Achievement:** From 621 ms to 1.14 ms — **549x speedup** with no accuracy loss

</div>

---

<!-- _class: small -->

## Diagonal vs Full Covariance Comparison

### The Final Optimization: 6x Additional Speedup

<div class="columns">
<div>

**Full Covariance:**
- Mahalanobis: $d(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}$
- Matrix: [100 × 100] per position
- Time: 6.27 ms (Mahalanobis only)

**Diagonal Covariance:**
- Mahalanobis: $d(x) = \sqrt{\sum_i (x_i - \mu_i)^2 / \sigma_i^2}$
- Vector: [100] per position
- Time: 0.62 ms (10x faster)

</div>
<div>

| Mode | Total Time | FPS |  AUROC |
|------|------------|-----|-------|
| **Diagonal** | **1.14 ms** | **878**  | 98.14 |
| Full | 6.79 ms | 147 | 98.14 |

**Key Finding:**
- **No accuracy loss**
- **6x faster** total pipeline

</div>
</div>

---

<!-- _class: small -->

## Future Optimization Opportunities

### What Could Be Done Next

<div class="columns">
<div>

**NPU Acceleration:**

- Offload ResNet18 feature extraction
- Running CNN backbone on **NPU** to free up GPU

**Batch Inference:**

- Process multiple images in parallel
- N× throughput for batch size N

</div>
<div>

**Current Status:**

- **878 FPS** far exceeds real-time requirements
- Ready for edge deployment

</div>
</div>

---

<!-- _class: lead -->

# Summary

### 549x Faster | 1.14ms Inference | 878 FPS

<div class="center-table" style="margin-top: 40px;">

| Metric | Baseline | Optimized |
|--------|----------|-----------|
| Time | 621 ms | **1.14 ms** |
| FPS | 1.6 | **878** |
| Speedup | - | **549x** |
| Accuracy | 98.14% | **98.14%** |

</div>

