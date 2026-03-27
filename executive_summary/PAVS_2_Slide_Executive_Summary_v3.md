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

  section.exec {
    font-size: 16px;
    padding: 25px 50px 70px 50px;
  }

  section.exec li {
    margin-bottom: 0.08em;
    line-height: 1.35;
  }

  section.exec h2 {
    font-size: 1.4em;
    margin-bottom: 0.3em;
    margin-top: 0;
  }

  section.exec h3 {
    font-size: 1.1em;
    margin-top: 0.15em;
    margin-bottom: 0.2em;
  }

  section.exec pre {
    font-size: 0.7em;
    padding: 8px;
    margin: 0.25em 0;
  }

  section.exec ul, section.exec ol {
    margin: 0.2em 0;
  }

  section.exec table {
    font-size: 0.78em;
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
    padding: 5px 8px;
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
    gap: 1.2em;
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

<!-- _class: exec -->

## Physical AI SDK: 2026 Model Lifecycle & Delivery Strategy

<div class="columns">
<div>

### **What We're Delivering**

**Structured 4-Phase Model Lifecycle:**
```
ENABLEMENT → BENCHMARKING → PROFILING → FINE-TUNING
  (1 wk)      (3 days)      (3 days)    (2-3 wk)
```

**2026 Portfolio Targets:**
- **20 production-ready models** across 6 categories
- **3 market segments:** Robotics, Healthcare, Industrial
- Unified SDK installer with integrated tooling

**Model Categories:**
| Category | Models | Status |
|----------|--------|--------|
| Vision/Detection | YoloV12, MobileSAM, CrossFormer | Active |
| VLMs | Qwen2.5-VL, Qwen3-VL, LLaMA3.2-Vision | Active |
| LLMs | DeepSeek-R1 | In Progress |
| Speech | Whisper (ASR), XTTS (TTS) | Active |
| 3D/Robotics | CenterPoint, OpenVLA | In Progress |
| Medical | MedSigLIP | In Progress |

</div>

<div>

### **2026 Release Roadmap**

**R1:** Foundation
- Lifecycle framework operational
- CI/CD automation & GitHub Pages/AMD docs
- Release logistics streamlined

**R2:** Scale
- **8 production-ready models** (P0/P1)
- Single SDK installer
- Quantization & Infra Beta (vLLM, ONNX-RT, Llama.cpp)
- Sample apps: ChatBot, Object Detection, GStreamer+ROCm

**R3:** Expand
- **8 additional models** (16 total)
- Enhanced quantization & profiling tools
- Robotics simulator integration
- Model deployment infrastructure

**R4:** Complete 1<sup>st</sup> cycle
- **20 total production models**
- Multi-segment deployment ready
- Model training infrastructure (Drafter)
- 2027 strategy planning

</div>
</div>

---

<!-- _class: exec -->

## Open Source Distribution & Team Collaboration Model

<div class="columns">
<div>

### **GitHub + HuggingFace Release Strategy**

**What We Publish:**
- Pre-optimized model weights (ONNX, TensorRT, ROCm)
- Quantized variants (INT8, FP16) for edge deployment
- Docker containers (GPU/NPU/Hybrid ready)
- Verified benchmark results & model cards

**CI/CD Pipeline:**
```
Dev Branch → PR → Auto Tests → Release Branch
                      ↓
              Benchmarking + Validation
                      ↓
GitHub Release → HuggingFace Push → Docs Update
```

**Infrastructure Tools:**
- **vLLM** - LLM serving & inference
- **Llama.cpp** - Optimized CPU/GPU inference
- **ONNX Runtime** - Cross-platform deployment
- **Lemonade** - Performance profiling

</div>

<div>

### **Team Collaboration Model**

**PAVS (Internal) vs External Partners:**

| Stage | PAVS Team | External (MCW/AIG) |
|-------|-----------|-------------------|
| Enablement | Lead | Support |
| Profiling | Initial | Deep Analysis |
| Benchmarking | Setup | Automation |
| Fine-tuning | Goals+Lead | Execution |

**Handoff Criteria:**
- Model runs on target hardware
- Profiling report complete
- Baseline benchmarks established
- Optimization opportunities explored

**Key Benefits:**
- Better ROI on external resources
- Clear deliverables with measurable outcomes
- Faster time to production
- PAVS Lead on goal-setting, partners focus on execution

</div>
</div>
