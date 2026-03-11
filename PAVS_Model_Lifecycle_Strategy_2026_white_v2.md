---
marp: true
paginate: true
footer: '![h:50](./themes/pavs-logo.png)'
style: |
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

  /* Auto-scale content to fit - Marp shrink-to-fit */
  section.small {
    font-size: 21px;
  }

  section.smaller {
    font-size: 19px;
  }

  section.smallest {
    font-size: 17px;
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
  }

  th, td {
    padding: 6px 10px;
  }

  table {
    background-color: #1a1a1a;
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

  /* Code blocks - compact */
  pre {
    font-size: 0.75em;
    padding: 10px;
    background-color: #2a2a2a;
    border-radius: 5px;
    color: #ffffff;
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

# Physical AI SDK - Model Lifecycle & Strategy

## 2026

**Zhaohui Yan**
AECG/PAVS AI SW

---

# Model Lifecycle Overview
### The Four-Stage Model Lifecycle

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ ENABLEMENT   │ -> │  PROFILING   │ -> │ BENCHMARKING │ -> │ FINE-TUNING  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
   Initial            Performance         Validation         Optimization
   Support            Analysis            & Metrics          & Adaptation
```

**Key Phases:**

1. **Enablement** - Initial model support, integration, basic functionality
2. **Profiling** - Performance analysis, bottleneck identification, hotspot analysis
3. **Benchmarking** - KPI validation, performance metrics, competitive analysis
4. **Fine-tuning** - Model optimization, domain-specific adaptation, deployment ready

---

# Progressive Model Support Strategy
### From Individual Models to System Orchestration

<div class="columns">

<div>

**Phase 1: Individual Model Support**
- Focus on single model enablement and optimization
- Establish baseline performance for each model
- Build reusable infrastructure and tooling

</div>

<div>

**Phase 2: Multi-Model Orchestration**
- Coordinate multiple models working together
- System-level optimization and resource management
- End-to-end pipeline integration

</div>

</div>

**Example Pipeline:** Vision → VLM → LLM → TTS

---

# Effective Team Collaboration
### Progressive Engagement Model

```
Internal Team (PAVS)          →    External Teams (SOW/MCW)
    ↓                                       ↓
Enablement + Initial Profiling      Fine-tuning + Optimization
    ↓                                       ↓
Foundation Building                  Advanced Optimization
```

**Strategy:**
- **PAVS Team:** Handle enablement and initial profiling - establish working baseline, identify optimization opportunities
- **External Partners:** Focus on fine-tuning and advanced optimization - domain-specific optimization, large-scale benchmarking

**Benefits:** ✓ Better ROI ✓ Clear handoff criteria ✓ Faster time to production

---

<!-- _class: smaller -->

# Speed Matters - Parallel Execution
### Current Model Status Across Lifecycle Stages

| Model Name | Category | Enablement | Profiling | Benchmarking | Fine-tuning |
|------------|----------|:----------:|:---------:|:------------:|:-----------:|
| **MobileSAM** | Vision/Segmentation | ✅ | ✅ | ✅ | 🔄 |
| **YoloV12** | Object Detection | ✅ | ✅ | ✅ | ⏸️ |
| **Qwen3-VL** | VLM | ✅ | ✅ | 🔄 | ⏸️ |
| **LLaMA3.2-Vision** | VLM | ✅ | ✅ | ⏸️ | ⏸️ |
| **Whisper** | ASR | ✅ | ✅ | ✅ | ✅ |
| **XTTS** | TTS | ✅ | ✅ | ✅ | ⏸️ |
| **DeepSeek-R1** | LLM | ✅ | 🔄 | ⏸️ | ⏸️ |
| **Qwen2.5-VL** | VLM | ✅ | ✅ | ✅ | 🔄 |
| **CrossFormer** | Vision Transformer | ✅ | 🔄 | ⏸️ | ⏸️ |
| **CenterPoint** | 3D Detection | ✅ | ⏸️ | ⏸️ | ⏸️ |
| **OpenVLA** | Vision-Language-Action | ✅ | ⏸️ | ⏸️ | ⏸️ |
| **EfficientNetV2** | Image Classification | ✅ | ✅ | ✅ | ⏸️ |

**Legend:** ✅ Complete | 🔄 In Progress | ⏸️ Not Started

---

<!-- _class: small -->

# Environment & CI/CD Infrastructure
### Isolated Environments for Each Model/System

<div class="columns">

<div>

**Environment Strategy:**
```bash
physical-ai-sdk/
├── models/
│   ├── mobilesam/
│   │   ├── Dockerfile
│   │   ├── pyproject.toml (uv)
│   │   └── .venv/
│   ├── yolov12/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── .venv/
```

**Benefits:** ✓ Isolated dependencies ✓ No version conflicts ✓ Easy model-specific exploration

</div>

<div>

**Branch Strategy:**
- `feature/*` → Developer branches
- `dev` → **Continuous work branch**
- `prod` → **Stable release branch**

**Model Deployment Flow:**
1. Developer → Push to `dev`
2. CI/CD runs automated tests
3. Validated → Pull to `prod`
4. Final validation suite
5. Deploy to customers

</div>

</div>

---

<!-- _class: smaller -->

# Container & Virtual Environment Options
### Deployment Flexibility

<div class="columns-3">

<div>

**Option 1: Dockerfile**
```dockerfile
FROM rocm/pytorch:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r \
    requirements.txt
COPY . .
CMD ["python", \
     "inference.py"]
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

---

<!-- _class: small -->

# Expanding Model Portfolio
### Staying Current with Latest Open Source Models

**Emerging Neural Alternatives:**
- 🔄 **End-to-End Neural Pipelines** replacing traditional CV pipelines
  - Example: Neural SLAM replacing traditional SLAM
  - Example: Neural 3D reconstruction replacing classical methods

- 🆕 **Latest Model Categories to Track:**
  - Multimodal Foundation Models (GPT-4V alternatives)
  - Action-VLMs (RT-2, OpenVLA successors)
  - Neural Rendering (NeRF, Gaussian Splatting for robotics)
  - On-device Edge LLMs (< 3B parameters)

**Strategy:**
1. Monthly scan of arxiv.org, HuggingFace, GitHub trending
2. Quick feasibility assessment (30-day cycle)
3. Add to roadmap if aligned with Physical AI use cases

---

<!-- _class: small -->

# Benchmarking & Documentation Strategy
### GitHub Pages Integration

<div class="columns">

<div>

**Documentation as Code:**
```
docs/
├── index.md
├── models/
│   ├── mobilesam.md
│   ├── yolov12.md
│   └── benchmarks/
│       ├── robotics.md
│       └── industrial.md
├── guides/
│   ├── quick-start.md
│   └── deployment.md
└── _config.yml
```

</div>

<div>

**Automated Workflow:**
1. **Code + Benchmarks** → GitHub Repo
2. **CI/CD** → Auto-generate docs, run benchmarks
3. **GitHub Pages** → Publish results automatically

**Benefits:**
- ✓ Version-controlled documentation
- ✓ Automated benchmark updates
- ✓ Professional presentation
- ✓ Community collaboration

</div>

</div>

---

<!-- _class: small -->

# Comprehensive Benchmarking Strategy
### Dual-Mode Benchmarking & Regression Testing

<div class="columns">

<div>

**1. NPU-Disabled Mode** (Competitive Comparison)
- **Purpose:** Fair comparison with NVIDIA/Intel
- **Hardware:** NPU disabled, iGPU + CPU execution
- **Use Case:** Match industry-standard metrics

</div>

<div>

**2. NPU-Enabled Mode** (AMD Advantage)
- **Purpose:** Demonstrate AMD's hybrid execution
- **Hardware:** NPU + iGPU + CPU (full APU)
- **Use Case:** Showcase AMD performance gains

</div>

</div>

**Performance Comparison:**

| Model | NPU-Off (vs Competitors) | NPU-On (AMD Advantage) | Gain |
|-------|--------------------------|------------------------|------|
| MobileSAM | 180 fps (iGPU) | 240 fps (NPU) | <span class="success">+33%</span> |
| YoloV12 | 200 fps (iGPU) | 240 fps (NPU) | <span class="success">+20%</span> |
| Whisper | 85 tok/s (CPU) | 100 tok/s (NPU) | <span class="success">+18%</span> |
| Qwen3-VL | 25 fps (iGPU) | 35 fps (NPU+iGPU) | <span class="success">+40%</span> |

---

<!-- _class: smaller -->

# CI/CD Pipeline Detail
### Preventing Regressions

```
┌─────────────┐
│  Git Push   │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Trigger CI/CD      │
│  (GitHub Actions)   │
└──────┬──────────────┘
       │
       ├─────────────────────────────┐
       │                             │
       ▼                             ▼
┌──────────────┐              ┌──────────────┐
│ Build Tests  │              │ Model Tests  │
│ - Lint       │              │ - Accuracy   │
│ - Unit tests │              │ - Performance│
└──────┬───────┘              └──────┬───────┘
       │                             │
       └──────────┬──────────────────┘
                  │
                  ▼
           ┌──────────────┐         ┌─────────┐      ┌──────────┐
           │   All Pass?  │ ──Yes──>│ Merge   │  No──>│ Block PR │
           └──────────────┘         │ to Dev  │      │ + Notify │
                                    └─────────┘      └──────────┘
```

---

<!-- _class: smaller -->

# Practical Example - Model Lifecycle
### Case Study: Qwen3-VL Integration

<div class="columns">

<div>

**Week 1-2: Enablement**
- ✅ Model weights download and conversion
- ✅ Basic ONNX-RT integration
- ✅ Simple inference test (single image)
- ✅ Docker environment setup

**Week 3-4: Profiling**
- 📊 Layer-wise performance analysis (AMD Profiler)
- 📊 Memory usage tracking
- 📊 Hotspot identification (Conv3D, GEMM)

</div>

<div>

**Week 5-6: Benchmarking**
- 🎯 KPI testing: Target 30fps @ 1080p
- 🎯 Accuracy validation on VQA datasets
- 🎯 Power consumption measurement

**Week 7-8: Fine-tuning**
- ⚙️ Triton kernel optimization for GEMM
- ⚙️ INT8 quantization (W8A8)
- ⚙️ Model-specific automotive dataset fine-tuning

</div>

</div>

<span class="success">**Result:** 2.5x speedup, 92% accuracy maintained</span>

---

<!-- _class: small -->

# Resource Management Strategy
### Balancing Internal & External Resources

**Resource Allocation Matrix:**

| Lifecycle Stage | Internal Team (PAVS) | External Partners | Duration |
|----------------|---------------------|-------------------|----------|
| Enablement | Primary | Support | 2-3 weeks |
| Profiling | Lead | Assist | 2-4 weeks |
| Benchmarking | Guide | Execute | 3-4 weeks |
| Fine-tuning | Review | Primary | 4-8 weeks |

**Handoff Criteria:**
- ✓ Model runs successfully on target hardware
- ✓ Profiling report completed
- ✓ Baseline benchmarks established
- ✓ Optimization opportunities documented

---

<!-- _class: small -->

# Technology Watchlist 2026
### Emerging Models & Technologies

<div class="columns">

<div>

**High Priority:**
1. **Qwen3-VL 32B** - Latest multimodal foundation model
2. **RT-X** - Robotics transformer with broader action space
3. **Neural SLAM** - End-to-end learned SLAM systems
4. **Depth Anything V2** - Improved monocular depth

**Medium Priority:**
5. **SAM 2** - Segment Anything with video support
6. **Florence-2** - Microsoft's vision foundation model
7. **Stable Diffusion 3** - For synthetic data generation
8. **Phi-3 Vision** - Compact VLM (< 4B params)

</div>

<div>

**Evaluation Criteria:**
- ✓ Open source availability
- ✓ Relevance to Physical AI use cases
- ✓ Hardware compatibility (ROCm/NPU)
- ✓ Community adoption & maintenance

</div>

</div>

---

<!-- _class: small -->

# Success Metrics & KPIs
### Measuring Lifecycle Effectiveness

**Model Lifecycle KPIs:**

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Average Time to Enablement | < 2 weeks | 2.5 weeks | ⬇️ Improving |
| Models in Profiling Stage | 5-8 concurrent | 6 | ➡️ Stable |
| Benchmark Pass Rate (1st try) | > 80% | 75% | ⬆️ Improving |
| Fine-tuning Speedup (avg) | > 2x | 2.3x | ⬆️ Good |
| CI/CD Pipeline Success Rate | > 95% | 97% | ✅ Excellent |

**Portfolio Metrics:** Total: **45+** | Production-Ready: **28** | In Development: **12** | Experimental: **5**

---

<!-- _class: small -->

# Roadmap & Next Steps
### 2026 Execution Plan

<div class="columns">

<div>

**Q1 2026 (Current):**
- ✅ Establish lifecycle framework
- 🔄 Complete 8 models through full lifecycle
- 🔄 Deploy GitHub Pages documentation

**Q2 2026:**
- 📋 Expand to 15 production-ready models
- 📋 Implement automated benchmarking CI/CD
- 📋 Onboard 2 external partner teams (MCW/SOW)

</div>

<div>

**Q3 2026:**
- 📋 Multi-model orchestration (5 system pipelines)
- 📋 Add 10 emerging models from watchlist
- 📋 Scale fine-tuning operations

**Q4 2026:**
- 📋 Full production deployment for 3 customer segments
- 📋 Documentation portal v2.0
- 📋 2027 strategy planning

</div>

</div>

---

<!-- _class: lead -->

# Call to Action
### Building the Future of Physical AI

**Our Commitment:**
🎯 **Systematic** approach to model support | 🎯 **Efficient** collaboration with partners
🎯 **Rapid** adaptation to emerging technologies | 🎯 **Quality** focus through CI/CD

**Get Involved:**
📧 zhaohui.yan@amd.com | 💬 Slack: #pavs-ai-sdk

---

**Together, we enable Physical AI at scale.**
