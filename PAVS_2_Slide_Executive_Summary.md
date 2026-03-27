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
    border-bottom: 3px solid #ED1C24;
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
    background-color: #ED1C24 !important;
  }

  thead th {
    color: white !important;
    background-color: #ED1C24 !important;
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

  /* Links */
  a {
    color: #00bcd4;
  }

  /* Strong/bold text */
  strong {
    color: #ED1C24;
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

---

<!-- _class: optimized -->

## PAVS Model Lifecycle & Delivery Strategy 2026

<div class="columns">
<div>

### **4-Phase Model Lifecycle**
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ ENABLEMENT   │ -> │ PROFILING    │ -> │ BENCHMARKING │ -> │ FINE-TUNING  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
  Initial Setup    Performance         Validation         Optimization
  (1 week)      Analysis (3 days)   & Metrics (3 days)  (2-3 weeks)
```

**Team Core Capabilities:**
- **Model Enablement**: Off-the-shelf installation, dependency resolution, initial benchmarking
- **Performance Profiling**: Compute analysis, hotspot identification, bottleneck detection
- **Benchmarking & Validation**: Task metrics,Identify/suggest right model per domain/client,competitive analysis (GPU vs CPU vs NPU), CI/CD automation
- **Model Optimization**: Quantization (INT8, FP16), kernel optimization
- **Training Infrastructure**: Custom model training, domain-specific adaptation, fine-tuning on custom datasets
- **Deployment & Release**: Docker containerization, HuggingFace distribution, automated documentation

</div>

<div>

### **2026 Release Timeline**

**R1 2026 (Q1-Q3):** Foundation
- Complete lifecycle framework for all models
- Streamline release logistics & CI/CD
- Deploy automated docs ([GitHub Pages](https://hvydana.github.io/psdk-model-docs/))

**R2 2026 (Q4-Q6):** Scale
- Single SDK installer (Nvidia/Intel style)
- 8 production-ready models (P0/P1)
- Automated benchmarking pipeline
- Quantization & Infra Beta (vLLM, ONNX-RT, Llama.cpp, Lemonade)
- Sample apps (ChatBot, Object Detection, GStreamer+ROCm)

**R3 2026 (Q7-Q9):** Expand
- 8 more release-ready models
- Enhanced quantization & infrastructure
- Model deployment & robotics simulator
- Scale fine-tuning operations

**R4 2026 (Q10-Q12):** Production
- 2 additional production models (20 total)
- Multi-segment deployment (Robotics, Healthcare, Industrial)
- Model training infrastructure
- 2027 strategy planning

</div>
</div>

---

<!-- _class: optimized -->

## Open Source Release & Distribution Strategy

<div class="columns">
<div>

### **GitHub-Based Development & Release**

**Repository Structure:**
```
physical-ai-sdk/
├── models/
│   ├── mobilesam/
│   │   ├── gpu/          (Dockerfile, pyproject.toml, .venv)
│   │   ├── npu_gpu/      (hybrid environment)
│   │   └── npu/          (NPU-optimized)
│   ├── yolov12/
│   ├── whisper/
│   └── [20 models...]
├── benchmarks/           (automated CI/CD tests)
├── docs/                 (auto-generated)
└── tools/
    ├── profilers/        (Lemonade, ROCm profilers)
    └── optimizers/       (quantization, training)
```

**CI/CD Automation Pipeline:**
```
Developer Branch → Pull Request → Auto Tests
     ↓                ↓                ↓
  Regression      Smoke Tests    Benchmarking
     ↓                ↓                ↓
Release Branch → QA Validation → GitHub Release
     ↓                                 ↓
Documentation Update          HuggingFace/tipp Push
```

**Release Workflow:**
```
Model Complete → Benchmarking → Optimization
     ↓               ↓               ↓
  Package      Verify Metrics    Test Deploy
     ↓               ↓               ↓
GitHub Release → HuggingFace Push → Docs Update
     ↓                                ↓
Community Access             Analytics & Feedback
```

</div>

<div>

### **HuggingFace Hub Distribution**

**What We Publish:**
- 🤗 **Pre-optimized Model Weights**: ONNX, TensorRT, ROCm-ready
- 📦 **Quantized Variants**: INT8, FP16 for edge deployment
- 🐳 **Docker Images**: GPU/NPU/Hybrid ready-to-run containers
- 📊 **Benchmark Results**: Verified performance metrics included
- 📝 **Model Cards**: Documentation, usage examples, hardware requirements

**HuggingFace Advantages:**
- ✅ **Public Discovery**: Searchable by AI/robotics community
- ✅ **Version Control**: Track model iterations & improvements
- ✅ **Direct Download**: `pip install` or one-click deployment
- ✅ **Community Engagement**: Issues, feedback, contributions
- ✅ **Ecosystem Integration**: Works with Transformers, ONNX-RT, vLLM

**Infrastructure Tools (Open Source Ready):**
- **vLLM**: Efficient LLM serving & inference
- **Llama.cpp**: Optimized CPU/GPU inference
- **ONNX Runtime**: Cross-platform model deployment
- **Lemonade Profiler**: Performance analysis tool

</div>
</div>
