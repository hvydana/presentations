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
  }

  section.tiny {
    font-size: 14px;
  }

  section.tiny li {
    margin-bottom: 0.1em;
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

<!-- _class: lead -->
<!-- _paginate: false -->

# Physical AI SDK - Model Lifecycle & Strategy 2026

*Hari Krishna Vydana*
*PAVS AI*

---

<!-- _class: smallest -->

## Model Lifecycle Overview

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ ENABLEMENT   │ -> │ BENCHMARKING │ -> │  PROFILING   │ -> │ FINE-TUNING  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
    Initial          Validation         Performance        Optimization
    Support          & Metrics          Analysis           & Adaptation
```

<!-- _class: smallest -->

## Phases of Lifecycle

<div class="columns">
<div>

1. **Enablement**
    - Recieve the model from AIG
    - Get the model running
    - Off-the-shelf installtion (solve dependencies)
    - benchmarking (respective metrics w.r.t.model)
    - Identify the right dataset
    - Fill the [docs](https://hvydana.github.io/psdk-model-docs/) with the intial results and expectation
2. **Benchmarking**
    - Measure baseline performance (task-metric, compute-metrics)
    - Competitive analysis, With a right dataset on gpu vs cpu & gpu-npu
    - Work with CI/CD to automate it

</div>
<div>

3. **Profiling**
    - Do compute analysis
    - Find Hotspots and bottlenecks
    - Work with AIG to make profiler as a tool with Physical AI SDK
    - KPI re-assesment & updation
4. **Fine-tuning**
    - Expore oppertunities to fix hotspots
    - Imlement the Model optimizations
    - Benchmark the improvements in [docs](https://hvydana.github.io/psdk-model-docs/)

</div>
</div>


---

<!-- _class: compact -->
## Progressive Model Support Strategy

**Phase 1: Individual Model/Tool Support**
  - Focus on single model enablement and optimization
  - Establish baseline performance for each model
  - Build reusable infrastructure and tooling
    - vLLM, Lemonade,..etc
  - Might get simple as we gain expertise


**Phase 2: Sample Applications**
  - Systems: Pipeline of multiple models working together (More complex)
  - System-level optimization and resource management will be critical
  - End-to-end pipeline integration
  - Will give a real feel of product

---
<!-- _class: compact -->

## Effective Team Collaboration

**Progressive Engagement Model**

```
Internal Team (PAVS)          →    External Teams (SOW/MCW)
    ↓                                       ↓
Enablement + Initial Profiling      Fine-tuning + Optimization
    ↓                                       ↓
Foundation Building                  Advanced Optimization
```

**Strategy:**
**PAVS Team:** Handle goal setting
  - Establish working baseline
  - Identify optimization opportunities
  - Create clear specifications for external teams

**External Partners:** Deliverebles with goals
  - Tangable and measurable outcomes
  - More quality time on Improvements
  - Domain-specific optimizations

**Benefits:**
✓ Better ROI on external resources
✓ Clear handoff criteria
✓ Faster time to production

---

<!-- _class: compact -->

## Model Status Across Lifecycle Stages

| Model Name | Category | Enablement | Profiling | Benchmarking | Fine-tuning |
|------------|----------|------------|-----------|--------------|-------------|
| **MobileSAM** | Vision/Segmentation | <span class="complete">PAVS</span> | <span class="progress">MCW</span> | <span class="progress">MCW</span> | <span class="progress">MCW</span> |
| **YoloV12** | Object Detection | <span class="complete">PAVS</span> | <span class="complete">PAVS</span> | <span class="complete">PAVS</span> | <span class="not-started">MCW</span> |
| **Qwen3-VL** | VLM | <span class="complete">PAVS</span> | <span class="complete">AIG</span> | <span class="progress">AIG</span> | <span class="not-started">AIG</span> |
| **LLaMA3.2-Vision** | VLM | <span class="complete">PAVS</span> | <span class="complete">MCW</span> | <span class="not-started">MCW</span> | <span class="not-started">MCW</span> |
| **Whisper** | ASR | <span class="complete">PAVS</span> | <span class="complete">MCW</span> | <span class="complete">MCW</span> | <span class="complete">MCW</span> |
| **XTTS** | TTS | <span class="complete">PAVS</span> | <span class="complete">PAVS</span> | <span class="complete">PAVS</span> | <span class="not-started">AIG</span> |
| **DeepSeek-R1** | LLM | <span class="complete">PAVS</span> | <span class="progress">MCW</span> | <span class="not-started">MCW</span> | <span class="not-started">MCW</span> |
| **Qwen2.5-VL** | VLM | <span class="complete">PAVS</span> | <span class="complete">AIG</span> | <span class="complete">AIG</span> | <span class="progress">AIG</span> |
| **CrossFormer** | Vision Transformer | <span class="complete">PAVS</span> | <span class="progress">MCW</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |
| **CenterPoint** | 3D Detection | <span class="progress">PAVS</span> | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |
| **OpenVLA** | Vision-Language-Action | <span class="progress">PAVS</span> | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |
| **MedSigLIP** | Medical Classification | <span class="progress">PAVS</span> | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |
| **EfficientNetV2** | Image Classification | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |
| **RAFT Stereo** | Stereo Matching | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> | <span class="not-started">-</span> |

**Legend:** <span class="complete">Complete</span> | <span class="progress">In-Progress</span> | <span class="not-started">Not-Started</span>

**Key Insight:** Start early, execute in parallel across multiple models, 
              Speed Matters - Parallel Execution


---

<!-- _class: smallest -->

## Slide 6: Environment & CI/CD Infrastructure

<div class="columns">

<div>

**Environment Strategy:**
```
physical-ai-sdk/
  ├── models/
  │   ├── mobilesam/
  │   │   ├── gpu/
  │   │   │   ├── scripts/
  │   │   │   ├── inference.py
  │   │   │   ├── Dockerfile
  │   │   │   ├── pyproject.toml (uv)
  │   │   │   └── .venv/
  │   │   ├── npu_gpu/
  │   │   │   ├── scripts/
  │   │   │   ├── inference.py
  │   │   │   ├── Dockerfile
  │   │   │   ├── pyproject.toml (uv)
  │   │   │   └── .venv/
  │   │   └── npu/
  │   │       ├── scripts/
  │   │       ├── inference.py
  │   │       ├── Dockerfile
  │   │       ├── pyproject.toml (uv)
  │   │       └── .venv/
  │   ├── yolov12/
  │   │   ├── gpu/
  │   │   │   ├── scripts/
  │   │   │   ├── inference.py
  │   │   │   ├── Dockerfile
  │   │   │   ├── requirements.txt (pip)
  │   │   │   └── .venv/
  │   │   ├── npu_gpu/
  │   │   │   ├── scripts/
  │   │   │   ├── inference.py
  │   │   │   ├── Dockerfile
  │   │   │   ├── requirements.txt (pip)
  │   │   │   └── .venv/
  │   │   └── npu/
  │   │       ├── scripts/
  │   │       ├── inference.py
  │   │       ├── Dockerfile
  │   │       ├── pyproject.toml (uv)
  │   │       └── .venv/
```

**Benefits:** ✓ Isolated dependencies | ✓ No version conflicts | ✓ Easy exploration

</div>

---

**CI/CD Pipeline:**
```
  ┌──────────────────────────────────────────────────────┐         ┌────────────────────────────────┐
  │              DEVELOPMENT PHASE                       │         │     Release PHASE              │
  ├──────────────────────────────────────────────────────┤         ├────────────────────────────────┤
  │  ┌─────────────────┐      ┌──────────────┐           │         │                                │
  │  │ Developer Branch│ ───> │ Pull Request │           │         │                                │
  │  └─────────────────┘      └──────────────┘           │         │                                │
  │                                  │                   │         │                                │
  │                                  ▼                   │         │  ┌──────────────────┐          │
  │                           ┌─────────────┐            │         │  │ Release Branch   │          │
  │                           │ Auto Tests  │            | ───────>│  └──────────────────┘          │
  │                           │ + Regression│            │         │           │                    │
  │                           │ + Smoke     │            │         │           ▼                    │
  │                           └─────────────┘            │         │   ┌─────────────┐              │
  │                                  │                   │         │   │ Smoke Tests │              │
  │                                  │                   │         │   └─────────────┘              │
  │                                  ▼                   │         │                                │
  │                          ┌─────────────┐             │         │                                │
  │                          │  CI/CD      │             │         │                                │
  │                          │  Testing    │             │         │                                │
  │                          └─────────────┘             │         │                                │
  └──────────────────────────────────────────────────────┘         └────────────────────────────────┘

```

---

**Dev - Release Timelines:**
```
  Sprint Timeline View:

  Sprint N:     Sprint N+1:    Sprint N+2:    Sprint N+3:
  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
  │         │   │         │   │         │   │         │
  │  DEV    │──>│  DEV    │──>│  DEV    │──>│  DEV    │──> (continuous)
  │ v1.1    │   │ v1.2    │   │ v1.3    │   │ v1.4    │
  └─────────┘   └─────────┘   └─────────┘   └─────────┘
      │             │             │             │
      ▼             ▼             ▼             ▼
  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
  │   QA    │   │   QA    │   │   QA    │   │   QA    │
  │ Test    │   │ Test    │   │ Test    │   │ Test    │
  │ v1.0    │   │ v1.1    │   │ v1.2    │   │ v1.3    │
  └─────────┘   └─────────┘   └─────────┘   └─────────┘
      │             │             │             │
      ▼             ▼             ▼             ▼
  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
  │ Release │   │  Release│   | Release │   │  Release│
  │ v1.0    │   │ (same)  │   │ v1.1    │   │ (same)  │
  └─────────┘   └─────────┘   └─────────┘   └─────────┘

```

---

<!-- _class: smaller -->

## Slide 7: Container & Virtual Environment Options

<div class="columns-3">

<div>

**Option 1: Dockerfile**
```dockerfile
FROM rocm/pytorch:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "inference.py"]
```

</div>

<div>

**Option 2: uv + pyproject.toml**
```toml
[project]
name = "mobilesam"
version = "1.0.0"
dependencies = [
    "torch>=2.0.0",
    "onnxruntime-rocm",
]
```

</div>

<div>

**Option 3: pip + requirements**
```
torch==2.0.0
onnxruntime-rocm==1.17.0
opencv-python==4.8.0
```

</div>

</div>

### Model Distribution
    - 📦 **HuggingFace Hub** - Pre-optimized ONNX/TensorRT, Quantized (INT8, FP16), ROCm builds
    - 🔗 **Public Access** - Anyone can download and test
    - ✅ **Verified Benchmarks** - Performance metrics included
    - 📝 **Alternative:** GitHub Releases, Company registry, Cloud storage

---

<!-- _class: small -->

## Expanding Model Portfolio

### Staying Current with Latest Open Source Models

**Emerging Neural Alternatives:**
- 🔄 **End-to-End Neural Pipelines** replacing traditional CV pipelines
    - Example: Neural speech-to-speech model
    - Example: VLA++, pi-0++

- 🆕 **Latest Model Categories to Track:**
    - Multimodal Foundation Models (GPT-4V alternatives)
    - Action-VLMs (RT-2, OpenVLA successors)
    - Neural Rendering (NeRF, Gaussian Splatting for robotics)
    - On-device Edge LLMs (< 3B parameters)

**Strategy:**
  1. Monthly scan of arxiv.org, HuggingFace, GitHub trending
  2. Quick feasibility assessment (2-3 days cycle)
  3. Add to roadmap if aligned with Physical AI use cases
  4. If the model fits in requirements and aligns with out bussiness directions (Robotics, healthcare, Indistrial we can add it)

---

<!-- _class: smaller -->

## Benchmarking & Documentation Strategy

<div class="columns">

<div>

**Documentation with Code:**
```
docs/
├── index.md
├── models/
│   ├── mobilesam.md
│   ├── yolov12.md
│   └── benchmarks/
├── guides/
│   ├── quick-start.md
│   └── deployment.md
├── tools/
│   └── profilers/
│     ├── roc_profilers.md
│     └── Lemonade_profiler.md
└── _config.yml
```

</div>

<div>

**Automated Workflow:**
1. **Code + Benchmarks** → GitHub Repo
2. **CI/CD** → Auto-generate tests, run benchmarks
3. **GitHub Pages** → Publish automatically(Example: [docs](https://hvydana.github.io/psdk-model-docs/)) 

**Benefits:**
  - ✅ Version-controlled documentation
  - ✅ Automated benchmark updates
  - ✅ Professional presentation
  - ✅ Community collaboration

</div>

</div>

---

<!-- _class: smallest -->

## Practical Example - Model Lifecycle

### Case Study: Qwen3-VL Integration

<div class="columns">

<div>

**Enablement:**
- ✅ Model weights download and conversion
- ✅ Basic ONNX-RT integration
- ✅ Simple inference test (single image)
- ✅ Docker environment setup

**Profiling:**
- 📊 Layer-wise performance analysis
- 📊 Memory usage tracking
- 📊 Hotspot identification (Conv3D, GEMM)

</div>

<div>

**Benchmarking:**
- 🎯 Performance on dataset vs leaderboard
- 🎯 KPI testing: Target 30fps @ 1080p
- 🎯 Accuracy validation on VQA datasets
- 🎯 Power consumption measurement
- 🎯 Automate the benchmarking setup

**Fine-tuning:**
- ⚙️ Kernel optimization for GEMM
- ⚙️ INT8 quantization (W8A8)
- ⚙️ Automotive dataset fine-tuning

</div>

</div>

---

<!-- _class: small -->

## Resource Management Strategy

### Balancing Internal & External Resources

**Resource Allocation Matrix:**

| Lifecycle Stage | Internal Team (PAVS) | External Partners | Max.Exptd Duration |
|----------------|---------------------|-------------------|----------|
| Enablement | ███████████ | ░░░ ░░░ ░░░  | 1 weeks |
| Profiling | ████  | ██████████ | 3 days |
| Benchmarking | █████  | ███████████ | 3 days |
| Fine-tuning | ██████████  | ██████████ | 2-3 weeks |

**Handoff Criteria:**
✓ Model runs successfully on target hardware
✓ Profiling report completed
✓ Baseline benchmarks established
✓ Optimization opportunities documented, explored


---

<!-- _class: small -->

## Success Metrics & KPIs

### Measuring Lifecycle Effectiveness

**Model Lifecycle KPIs:**

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Average Time to Enablement | < 2 weeks | 1 weeks | ⬇️ Improving |
| Models in Profiling Stage | 5-8 concurrent | 6 | ➡️ Stable |
| Benchmark Pass Rate (1st try) | > 80% | 75% | ⬆️ Improving |
| Fine-tuning Speedup (avg) | > 2x | 2.3x | ⬆️ Good |
| CI/CD Pipeline Success Rate | > 95% | 97% | ✅ Excellent |

**Portfolio Metrics:**
- Total Models Supported: **20**
- Production-Ready Models: **15**
- Models in Development: **5**
- Experimental/Research: **5**


---

<!-- _class: tiny -->

## Roadmap & Next Steps

<div class="columns">

<div>

**R1 2026 (Current):**
- ✅ Establish lifecycle framework
- 🔄 Complete models lifecycle planing
- 🔄 Streamline Release Logistics
- 🔄 Deploy GitHub Pages documentation

**R2 2026:**
- 📋 Implement SDK Installation 
  - Make it single installer(Like Nvidia, Intel tools)
- 📋 Expand to 8 release-ready models(P0's and P1's)
- 📋 Implement automated benchmarking CI/CD 
- 📋 Implement Quantization - Beta Version
- 📋 Implement Infra - Beta Version (Looks like mostly integration)
  - vLLM, ONNX-RT, Llama.cpp, Lemonade
- 📋 Start sample applications(may need exploration)
  - ChatBot, Obj.detect, opencv/cvml, Gstreamer + Rocm/HIP, robotics simulator
</div>

<div>

**R3 2026:**
- 📋 Improve-SDK Installation 
- 📋 Expand to 8 release-ready models(P0's and P1's)
- 📋 Improve - Quantization
- 📋 Expand - Infra
  - Model Deploy, Perf. Profile, robotics simulator
- 📋 Expand sample applications
  - Gstreamer+ Ryzen-AI
- 📋 Scale fine-tuning operations
- 📋 Add emerging models from (P2)

**R4 2026:**
- 📋 Expand to 2 release-ready models(P0's and P1's)
- 📋 Production deployment for 3 segments
- 📋 Expand Infra
  - Model Training(Drafter)
- <span class="violet">📋 Complete Backlogs</span>
- <span class="violet">📋 2027 strategy planning</span>

</div>

</div>



