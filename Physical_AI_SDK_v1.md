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

<!-- _class: smallest -->

## Physical AI SDK - Structure & Workflow

### Three Paths — Pick the One That Fits Your Workflow

<div class="columns-3">
<div>

**Option 1: Zero Steps**

Every example ships with a pre-generated `METRICS_TABLE.md`

```
examples/yolov12/METRICS_TABLE.md
```

- CPU, GPU, NPU throughput & latency
- Cross-device comparison table
- Auto-generated from benchmark runs
- **Plan:** expose as a web dashboard

<div class="highlight-box">

<span class="success">Just open the file — numbers are already there</span>

</div>

</div>
<div>

**Option 2: Docker (One Command)**

Pre-installed ROCm + RyzenAI environment

```bash
# Pull & run the container
docker run physical-ai-sdk

# Inside the container:
make benchmark-all-devices metrics
```

- No local installs needed
- Reproducible environment
- Generates `METRICS_TABLE.md` automatically

<div class="highlight-box">

<span class="success">One command to fresh numbers</span>

</div>

</div>
<div>

**Option 3: Manual Setup**

Full local installation — 4 steps:

```bash
# 1. Install ROCm and raizen-ai
./install.sh

# 2. Navigate to example
cd examples/yolov12

# 3. Run benchmarks
make benchmark-all-devices metrics
```

Output: `METRICS_TABLE.md`

<div class="highlight-box">

<span class="warning">Most control, most setup</span>

</div>

</div>
</div>

---

<!-- _class: small -->

## Easy to Use

### Uniform Interface Across Every Example

<div class="columns">
<div>

**Make-Based Uniformity**

Same commands work in **every** example directory:

```bash
make benchmark-all-devices metric   # all devices
make benchmark-gpu                  # GPU only
make benchmark-cpu                  # CPU only
make benchmark-npu                  # NPU only
make eval                           # evaluation pipeline
```

- Learn once, use everywhere
- No per-model setup surprises
- Consistent output format (`METRICS_TABLE.md`)

</div>
<div>

**Every Example Includes:**

| Feature | Description |
|---------|-------------|
| **CPU / GPU / NPU flows** | Benchmark each compute device for throughput & latency |
| **Eval pipeline** | Sample inputs → sample outputs to visually verify correctness |
| **Guiding documentation** | Per-example tutorial to walk you from setup to results |

<div class="highlight-box">

**Principle:** If you can run one example, you can run them all — same commands, same structure, same outputs.

</div>

</div>
</div>

---

<!-- _class: smallest -->

## Contributions — Research Desk → Vertical Software

### 1. PAVS transforms raw researcher code into production-ready vertical software

<div class="columns-3">
<div>

**What we receive: Research Repo**

![w:250](./images/AIG_Model_delovery_cropped.png)

*Flat list of scripts — no structure, no device flows, no Make targets*

</div>
<div>

**What we receive: Research Code**

```python
# rocm-scripts/test/pytorch/yolo12n.py
#........
# .......
# .......
#........
# .......
# .......
recalled = gt_labels & detected_classes
recall = len(recalled) / len(gt_labels)
sanity_pass = recall >= RECALL_THRESHOLD
assert sanity_pass, (
  f"recall {recall:.0%} < {RECALL_THRESHOLD:.0%}")

return lats, {
  "architecture": "CNN",
  "task": "object_detection",
  "num_detections": num_detections,
  "recall": round(recall, 4),
}
if __name__ == "__main__":
  sys.exit(run(run_benchmark))
```

*Single script, no structure, no device flows*

</div>
<div>

**What we deliver: Vertical Software**

```
examples/yolov12/
├── Makefile
├── METRICS_TABLE.md
├── README.md
├── app/
│   ├── routes/
│   ├── services/
│   ├── main.py & config.py
├── scripts/
│   ├── benchmark.py
│   ├── export_onnx.py
│   ├── profile_model.py
│   ├── run_val.py
│   └── update_metrics_table.py
├── tests/
│   ├── test_api.py
│   ├── test_docker.py
│   ├── test_migraphx.py
│   └── test_yolo_workflow.py
├── weights/
├── datasets/
├── requirements.txt
├── requirements_cpu.txt
└── requirements_npu.txt
```

*App, scripts, tests, per-device requirements — production-ready*

</div>
</div>

<div class="highlight-box">

**Physical AI & Vertical Software:** Researcher's Desk → Vertical Software — same commands, every device, production-ready.

</div>

---

<!-- _class: smallest -->

## Contributions(contd.) — Building the AMD AI Ecosystem

<div class="columns">
<div>

**2. AIG vs PAVS — Functional Correctness over Operator Validation**

| | **AIG** | **PAVS** |
|---|---------|----------|
| **Approach** | Operator validation | Functional correctness |
| **Inputs** | Dummy / synthetic tensors | Real input datasets |
| **Measures** | Throughput on isolated ops | End-to-end accuracy + throughput + latency |
| **Pipeline** | Op-level checks | Full inference pipeline (pre → infer → post) |

<div class="highlight-box">

PAVS implements the **end-to-end working pipeline** and ensures the model produces **expected outputs from real input datasets** — not just numbers from dummy inputs.

</div>

</div>
<div>

**3. Developer-Friendly Inference Tools & LLM Infra**

Profilers + LLM serving stacks — with tutorials for ease of adoption:

| Category | Tools |
|----------|-------|
| **Profilers** | Lemonade, NPU AI Analyzer, ROCProfiler |
| **LLM Infra** | vLLM (high-throughput serving), Llama.cpp (edge inference), FastFlowLM (LLMs on NPU) |

Bridging the **open-source ecosystem** ↔ **AMD HW ecosystem** — making these tools easy to use across the AMD stack.

**4. Vertical Application Platform**

A platform that **evolves with the client** — solving, fixing, and growing together in targeted domains:

| Domain | Focus |
|--------|-------|
| **Healthcare** | Medical imaging, diagnostics |
| **Automotive** | Perception, safety systems |
| **Industrial** | Inspection, anomaly detection |



</div>
</div>

---

<!-- _class: small -->

## Pain Points

### Current Challenges on Edge Devices

<div class="columns">
<div>

**ROCm Installation Stability**

- ROCm install on edge devices is **not yet stable**
- Driver/firmware mismatches on some hardware revisions
- Workaround: pinned ROCm versions in install scripts

**Reboot During Installation**

- ROCm installation requires a **system reboot** mid-process
- Breaks unattended / CI-driven installs
- Users unfamiliar with the flow find this unexpected

</div>
<div>

**Sudo / Root Access Required**

- Both ROCm and RyzenAI installers need **sudo privileges**
- Containers mitigate this

</div>
</div>

<div class="highlight-box">

**Docker path sidesteps all three issues** — pre-built image with ROCm + RyzenAI already configured, no reboot, no sudo on host.

</div>

---

<!-- _class: lead -->

# SW Stack (For Reference)

![w:800](./images/SW_stack.png)