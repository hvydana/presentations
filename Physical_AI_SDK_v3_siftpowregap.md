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
    font-size: 28px;
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

# Bridging AMD's Softpower Gap

## Why the best inference silicon doesn't win by itself — and how the Physical AI SDK closes the gap

**Executive Briefing · Voice AI as the lens — the same pattern repeats in robotics, industrial & healthcare**

---

<!-- _class: small -->

## The Stakes — A Market Being Decided Right Now

<div class="columns">
<div>

| Metric | Value |
|---|---|
| AI voice-agents market, 2034 | **$47.5B** @ **35% CAGR** |
| Cost per call — human vs AI | **$7–12 → $0.40** |
| YoY growth in production deployments | **340%** (500+ orgs) |
| Contact-center labor savings, 2026 | **$80B** (Gartner) |
| Orgs planning voice AI by end-2026 | **80%** |

</div>
<div>

**It is a compute market at its core**

- A deployed agent is a **steady-state inference machine** — it doesn't train; it transcribes, reasons & speaks **24×7**
- At scale, its **dominant operating cost is GPU compute**
- **3 of the 5** pipeline layers — **ASR · LLM · TTS** — are GPU-compute-bearing

</div>
</div>

<div class="highlight-box">

The compute substrate for a massive, fast-growing inference market is being **chosen right now** — and whoever owns the default owns the decade.

</div>

---

<!-- _class: smallest -->

## AMD Already Has the Winning Silicon

<div class="columns">
<div>

**LLM inference — MI300X vs H100** *(Llama 3.1 70B, 2026)*

| Dimension | **MI300X** | H100 SXM5 |
|---|---|---|
| VRAM | **192 GB** HBM3 | 80 GB |
| Cloud price | **$1.50–2.50/hr** | $2.90/hr |
| Throughput (tok/s) | ~18,000 | ~19,500 |
| **Cost / 1M tokens** | **$0.027** | $0.041 |
| 70B fits on 1 GPU? | **Yes** | No (needs 2) |

</div>
<div>

**The savings compound at scale**

- **34% lower cost-per-token** → **~$84K/month** saved at 1M min/month
- Self-hosted ROCm TTS removes **$100K–$300K/month** in hosted synthesis
- India on-prem: **~50% lower GPU CapEx**
- MI355X within **single-digit %** of B200 — MLPerf Inference v6.0

</div>
</div>

<div class="highlight-box" style="text-align:center;">

<span style="font-size:1.3em; font-weight:bold; color:#4caf50;">This is <span style="color:#ffffff;">not</span> a hardware problem.</span>

</div>

---

<!-- _class: smallest -->

## Yet AMD Is Absent Where the Decision Is Made

<div class="columns">
<div>

**The real decision isn't "which GPU"**

- Made **upstream and invisibly** — before a developer thinks about silicon
- NVIDIA's edge is **softpower**: a layered ecosystem surface that is the **path of least resistance** at the first touchpoint
- The instrument: the **NIM playbook**

<div class="highlight-box">

*"Follow a Blueprint and you **never consciously select a GPU** — the choice is already made. Every other choice requires active effort."*

</div>

</div>
<div>

**The NIM ecosystem — how the default gets set**

<div style="border:2px solid #76b900; border-radius:6px; padding:8px; background:#202020;">
<div style="text-align:center; font-weight:bold; color:#76b900; margin-bottom:5px;">NVIDIA NIM — Hardware as Platform</div>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:5px; font-size:0.82em;">
<div style="background:#2a2a2a; border-radius:4px; padding:5px;"><strong style="color:#00bcd4;">Software</strong><br>Riva ASR · Maxine · ACE<br>Triton · TensorRT-LLM<br>AI Blueprints</div>
<div style="background:#2a2a2a; border-radius:4px; padding:5px;"><strong style="color:#00bcd4;">Developer</strong><br>28M devs on CUDA<br>VS Code NIM ext.<br>RTX Spark devkit</div>
<div style="background:#2a2a2a; border-radius:4px; padding:5px;"><strong style="color:#00bcd4;">Channel</strong><br>Azure Foundry NIM<br>SI certs: TCS·Infosys<br>Wipro·Accenture</div>
</div>
</div>

- `docker pull` → running in **30 seconds**
- `ChatNVIDIA(...)` → routed to NVIDIA **at the call site**
- Prototype on NVIDIA → **default to NVIDIA in production**

</div>
</div>

---

<!-- _class: smaller -->

## The Convergence — One Compute Decision Rules the Whole Market

<div style="display:flex; flex-direction:column; align-items:center; gap:0; margin-top:6px;">

  <div style="background:#2a2a2a; border:1px solid #666; border-radius:6px; padding:8px 14px; text-align:center; width:82%;">
    <strong style="color:#ffffff; font-size:1.05em;">EVERY VOICE AI COMPANY</strong><br>
    <span style="font-size:0.82em; color:#cccccc;">Vapi · Retell · Bolna · ElevenAgents · Caller Digital · Gnani · PolyAI · Synthflow · Ringg.ai</span>
  </div>

  <div style="width:0; height:0; border-left:9px solid transparent; border-right:9px solid transparent; border-top:12px solid #3498db; margin:4px 0;"></div>

  <div style="display:flex; gap:14px; width:82%; justify-content:center;">
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:7px; text-align:center;"><strong style="color:#5dade2;">LiveKit Agents</strong><br><span style="font-size:0.78em; color:#cccccc;">Apache 2.0 · WebRTC</span></div>
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:7px; text-align:center;"><strong style="color:#5dade2;">Pipecat</strong><br><span style="font-size:0.78em; color:#cccccc;">BSD-2 · 60+ connectors</span></div>
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:7px; text-align:center;"><strong style="color:#5dade2;">TEN</strong><br><span style="font-size:0.78em; color:#cccccc;">C++/Go · sub-300ms</span></div>
  </div>

  <div style="width:0; height:0; border-left:9px solid transparent; border-right:9px solid transparent; border-top:12px solid #3498db; margin:4px 0;"></div>

  <div style="background:#2a2a2a; border:1px solid #666; border-radius:6px; padding:7px 14px; text-align:center; width:82%;">
    <strong style="color:#ffffff;">SHARED MODEL LAYER</strong><br>
    <span style="font-size:0.8em; color:#cccccc;">STT: Faster-Whisper / Sarvam · LLM: Llama 3.1 / GPT-4o / Claude · TTS: Kokoro / ElevenLabs</span>
  </div>

  <div style="width:0; height:0; border-left:9px solid transparent; border-right:9px solid transparent; border-top:12px solid #e05555; margin:4px 0;"></div>

  <div style="background:#3a1e1e; border:2px solid #e05555; border-radius:6px; padding:8px 14px; text-align:center; width:50%;">
    <strong style="color:#ffffff; font-size:1.05em;">GPU COMPUTE</strong> &nbsp; NVIDIA / <strong style="color:#4caf50;">AMD</strong>
  </div>

</div>

<div class="highlight-box" style="margin-top:10px;">

Every commercial platform is a business layer above **one of three frameworks**, sharing a common model layer. **Win the compute layer — or the plugin slot just above it — and the hardware choice is made for every platform above.**

</div>

---

<!-- _class: smallest -->

## The Gap, Mapped — Five Downstream Layers, Four Upstream Barriers

<div class="columns">
<div>

**5 downstream layers** — visible & closeable

| Layer | NVIDIA | AMD |
|---|---|---|
| **Framework plugins** | LangChain · LlamaIndex · Pipecat · LiveKit | — |
| **Inference serving** | Triton / Dynamo · TensorRT-LLM | vLLM ROCm only |
| **Voice-domain SDKs** | Riva · Maxine · ACE | — |
| **Edge platform** | Jetson · JetPack · Isaac | Ryzen AI (laptop only) |
| **Cloud marketplace** | Azure · HF · SageMaker · Vertex | absent / limited |

</div>
<div>

**4 upstream barriers** — deeper, durable lock-in

- **Training / fine-tuning** — NeMo + CUDA-primary libs (bitsandbytes, trl, Axolotl, FlashAttention 3)
- **ISV & SI channel** — Genesys, Cisco, Salesforce; TCS/Infosys/Wipro certified on NVIDIA
- **Voice + vision convergence** — Jetson Thor unifies Isaac · Metropolis · Riva · ACE; AMD has no unified edge module
- **Synthetic data** for low-resource languages — no AMD-native pipeline or academic partnership

</div>
</div>

<div class="highlight-box">

Closing the **downstream** layers puts AMD in contention; closing the **upstream** barriers creates **platform momentum**. The chain compounds: fine-tune on NeMo → deploy to Triton → shipped inside Genesys → sold by an SI certified on NIM.

</div>

---

<!-- _class: small -->

## The Sharpest Illustration — "Not a Silicon Gap, a Slot Gap"

<div class="columns">
<div>

**HuggingFace Inference Endpoints**

- AMD has a **formal hardware partnership** with HuggingFace
- The TGI ROCm image is **production-ready** — validated on MI210, MI250, MI300X (Flash Attention 2, AWQ, DeepSpeed)
- **The engineering is done.**

</div>
<div>

**But at the point of decision…**

- Open the "deploy this model" UI → the GPU dropdown lists **T4 → H100**
- **MI300X does not appear.**
- The developer picks NVIDIA — **not because AMD can't run the model, but because AMD isn't on the menu**

</div>
</div>

<div class="highlight-box" style="text-align:center;">

<span style="font-size:1.25em; font-weight:bold; color:#4caf50;">The gap in its simplest form: <span style="color:#ffffff;">not a silicon gap — a slot gap.</span> And a slot gap is <span style="color:#4aa3ff;">closeable.</span></span>

</div>

---

<!-- _class: small -->

## The Bridge Is Already Being Built

<div class="columns">
<div>

**The gap can't be closed by a new chip**

- It's a **software & ecosystem** problem — containers, plugins, blueprints, marketplace slots
- Which is **exactly** the kind of problem a **vertical-software team** solves

**PAVS sits at the intersection**

- Between **AIG model outputs** and **lighthouse customers** who validate & deploy in real environments
- Every conversion of a raw model → production vertical software does **organically** what NVIDIA's platform teams do **intentionally**

</div>
<div>

<div style="border:1px solid #3498db; border-radius:6px; padding:9px; background:#202020; text-align:center; font-size:0.9em;">
<div style="color:#aaaaaa;">AMD AI Group (AIG)</div>
<div style="color:#3498db;">↓ models + research &nbsp;&nbsp; ↑ deployment feedback</div>
<div style="background:#3498db; color:#fff; font-weight:bold; border-radius:4px; padding:4px 0; margin:5px 0;">PAVS</div>
<div style="color:#3498db;">↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↑</div>
<div style="display:flex; gap:6px; margin-top:4px;">
<div style="flex:1; background:#2a2a2a; border-radius:4px; padding:5px; font-size:0.85em;"><strong style="color:#00bcd4;">Physical AI SDK</strong><br>inference substrate</div>
<div style="flex:1; background:#2a2a2a; border-radius:4px; padding:5px; font-size:0.85em;"><strong style="color:#00bcd4;">Robotics pipelines</strong><br>+ devkit</div>
</div>
</div>

**The assets it produces map 1:1 to the gap:**
- Unified inference SDK → plugin + serving layers
- Multi-modal pipelines → voice + vision
- Jetson-class devkit → edge landing zone

</div>
</div>

---

<!-- _class: smallest -->

## PAVS DevKit — AMD's Jetson Moment

<div class="columns">
<div>

| Capability | NVIDIA Jetson | **AMD PAVS DevKit** |
|---|---|---|
| **Form factor** | Module (Nano→Thor) | Ryzen AI embedded APU |
| **OS + SDK** | JetPack (CUDA+Riva+Isaac) | **Physical AI SDK** (ROCm+Ryzen AI) |
| **Model supply** | NIM containers | AIG zoo → PAVS vertical SW |
| **Runtime** | TensorRT + Triton | vLLM · MIGraphX · llama.cpp · ONNX |
| **Voice** | Riva | Whisper + Kokoro + pipeline |
| **Multi-modal** | Isaac + Riva + ACE | VLM + VLA on one NPU/GPU |

</div>
<div>

**The architectural edge**

- Ryzen AI APUs put **x86 CPU + RDNA GPU + XDNA NPU on one die** with **unified memory** — no CPU↔GPU copy overhead
- For **VLA models** (visual + language → robot action), NPU+GPU may beat Jetson's ARM+CUDA

<div class="highlight-box">

The technical foundation — unified SDK, heterogeneous inference, robotics + voice pipelines, VLM/VLA support — is **being assembled by PAVS now**. What remains is the ISV/SI certification ecosystem.

</div>

</div>
</div>

---

<!-- _class: small -->

## How Physical AI SDK Maps to the Gap

| NVIDIA ecosystem asset | Physical AI SDK answer |
|---|---|
| **NIM certified containers** — one `docker pull` | **OOB + Docker** — ROCm + RyzenAI pre-installed, reproducible |
| **Framework plugin slots** — endpoint-level default | **Unified inference engine** — one interface, CPU · GPU · NPU, every language |
| **Domain SDKs / AI Blueprints** (Riva, ACE) | **Co-engineered vertical software** — healthcare · automotive · industrial |
| **Jetson + JetPack** edge platform | **Ryzen AI + ROCm edge enablement** — HW patches, Yocto / LTS |
| **NeMo** fine-tuning lock-in | **AIG generic → task-specific** operationalization + feedback loop |

<div class="highlight-box" style="text-align:center;">

<span style="font-size:1.15em; font-weight:bold; color:#4caf50;">Here's what that SDK actually is →</span>

</div>

---

<!-- _class: lead -->

# Physical AI SDK

## The Low-Resistance Path to AMD Silicon

**One Interface · Every Language · CPU · GPU · NPU**

---

<!-- _class: compact -->

## What is Physical AI SDK?

- **Physical AI SDK (PAI SDK)** is a **unified inference engine** that catalyses your product development on AMD hardware.

- It does this by creating a **"Low-Resistance Path"** to AMD silicon.

- A single **unified interface** to run AI workloads across **CPU, GPU, and NPU** on AMD edge hardware.

<div class="highlight-box">

**Learn one interface — deploy across every AMD compute device**, from edge CPU to iGPU to NPU.

</div>

---

<!-- _class: tiny -->

## Physical AI SDK — The Pitch

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin-top:-0.4em; margin-bottom:0.5em;">From Camera to Product — in 4 NMTS</div>

<div class="columns">
<div>

<div style="display:flex; flex-direction:column; align-items:center; gap:0;">
  <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
    <div style="width:90px;"></div>
    <div style="background:#2a2a2a; border:1px solid #4caf50; border-radius:5px; padding:6px 16px; text-align:center; color:#ffffff; width:190px;"><strong style="color:#4caf50;">App · logic / UI</strong><br><span style="font-size:0.85em; color:#cccccc;">decisions · action</span></div>
    <div style="width:90px; color:#3498db; font-weight:bold; font-size:0.82em; line-height:1.15;">2 NMTS<br>postprocess</div>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; margin:3px 0;">
    <div style="width:0; height:0; border-left:9px solid transparent; border-right:9px solid transparent; border-bottom:13px solid #3498db;"></div>
    <div style="width:4px; height:16px; background:#3498db;"></div>
  </div>
  <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
    <div style="width:90px;"></div>
    <div style="background:#3498db; border-radius:5px; padding:8px 18px; text-align:center; color:#ffffff; width:190px;"><strong style="color:#ffffff;">Physical AI SDK</strong><br><span style="font-size:0.85em;">Inference Engine</span></div>
    <div style="width:90px; color:#4caf50; font-weight:bold; font-size:0.82em; line-height:1.15;">0 NMTS<br>you write none</div>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; margin:3px 0;">
    <div style="width:0; height:0; border-left:9px solid transparent; border-right:9px solid transparent; border-bottom:13px solid #3498db;"></div>
    <div style="width:4px; height:16px; background:#3498db;"></div>
  </div>
  <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
    <div style="width:90px;"></div>
    <div style="background:#2a2a2a; border:1px solid #666; border-radius:5px; padding:6px 16px; text-align:center; color:#ffffff; width:190px;"><strong style="color:#00bcd4;">Camera / Sensor</strong><br><span style="font-size:0.85em; color:#cccccc;">raw frames</span></div>
    <div style="width:90px; color:#3498db; font-weight:bold; font-size:0.82em; line-height:1.15;">2 NMTS<br>preprocess</div>
  </div>
</div>

- **2 NMTS in** — capture, hand to the SDK
- **0 NMTS middle** — the SDK *is* the engine
- **2 NMTS out** — act on the results

<span class="success">Total effort: 4 NMTS → a working edge app</span>

</div>
<div>

<div style="font-size:0.82em; color:#ffffff; margin-bottom:5px;"><strong style="color:#3498db;">NMTS</strong> = "Not More Than Ten (lines of code)" — one unit of developer effort.</div>

**The whole application — in Python**

<pre style="background:#f6f8fa; color:#24292e; font-family:'Courier New',monospace; font-size:0.62em; padding:9px 11px; border-radius:5px; line-height:1.4; white-space:pre; margin:0;"><span style="color:#6a737d;"># NMTS 1 · set up the SDK</span>
<span style="color:#d73a49;">from</span> physical_ai_sdk.inference_engine <span style="color:#d73a49;">import</span> <span style="color:#6f42c1;">InferenceEngine</span>
engine = <span style="color:#6f42c1;">InferenceEngine</span>(<span style="color:#032f62;">"physical-ai-sdk.local"</span>)
yolo   = engine.model(<span style="color:#032f62;">"yolov12"</span>)
<span style="color:#6a737d;"># NMTS 2 · read the camera</span>
frame = Camera.open(<span style="color:#005cc5;">0</span>).read()
<span style="color:#6a737d;"># NMTS 3 · inference — SDK does everything</span>
dets = yolo.predict(frame)
<span style="color:#6a737d;"># NMTS 4 · act on the results</span>
<span style="color:#d73a49;">for</span> d <span style="color:#d73a49;">in</span> dets:
    <span style="color:#6f42c1;">draw_box</span>(frame, d.box, d.label)</pre>

<div style="margin-top:6px; font-size:0.72em; color:#cccccc;">Same call, every language: <span style="display:inline-block; background:#2a2a2a; border:1px solid #3498db; color:#00bcd4; border-radius:10px; padding:1px 8px; margin:0 1px; font-weight:bold;">Python</span> <span style="display:inline-block; background:#2a2a2a; border:1px solid #3498db; color:#00bcd4; border-radius:10px; padding:1px 8px; margin:0 1px; font-weight:bold;">C++</span> <span style="display:inline-block; background:#2a2a2a; border:1px solid #3498db; color:#00bcd4; border-radius:10px; padding:1px 8px; margin:0 1px; font-weight:bold;">Kotlin</span> <span style="display:inline-block; background:#2a2a2a; border:1px solid #3498db; color:#00bcd4; border-radius:10px; padding:1px 8px; margin:0 1px; font-weight:bold;">JS</span></div>

<div style="border:2px solid #3498db; border-radius:6px; padding:7px; background:#202020; margin-top:6px;">
  <div style="text-align:center; font-weight:bold; color:#ffffff; margin-bottom:4px; font-size:0.88em;">Physical AI SDK</div>
  <div style="background:#3498db; color:#ffffff; text-align:center; font-weight:bold; border-radius:4px; padding:3px 0; margin-bottom:5px; font-size:0.76em;">Inference Engine · one interface, seamless access</div>
  <div style="display:flex; gap:4px; margin-bottom:5px;">
    <div style="flex:1; background:#2a2a2a; border:1px solid #666; border-radius:4px; padding:4px 1px; text-align:center; font-size:0.66em;"><strong style="color:#00bcd4;">YOLOv12</strong><br>detect</div>
    <div style="flex:1; background:#2a2a2a; border:1px solid #666; border-radius:4px; padding:4px 1px; text-align:center; font-size:0.66em;"><strong style="color:#00bcd4;">MobileNetV3</strong><br>classify</div>
    <div style="flex:1; background:#2a2a2a; border:1px solid #666; border-radius:4px; padding:4px 1px; text-align:center; font-size:0.66em;"><strong style="color:#00bcd4;">MobileSAM</strong><br>segment</div>
    <div style="flex:1; background:#2a2a2a; border:1px solid #666; border-radius:4px; padding:4px 1px; text-align:center; font-size:0.66em;"><strong style="color:#00bcd4;">Llama-3</strong><br>LLM</div>
  </div>
  <div style="text-align:center; color:#4caf50; font-size:0.66em; font-weight:bold; margin:3px 0;">one call runs seamlessly on any AMD compute</div>
  <div style="display:flex; gap:4px;">
    <div style="flex:1; background:#333333; border:1px solid #4caf50; border-radius:4px; padding:3px 1px; text-align:center; font-size:0.66em; color:#ffffff;"><strong style="color:#4caf50;">AMD CPU</strong></div>
    <div style="flex:1; background:#333333; border:1px solid #4caf50; border-radius:4px; padding:3px 1px; text-align:center; font-size:0.66em; color:#ffffff;"><strong style="color:#4caf50;">AMD GPU</strong></div>
    <div style="flex:1; background:#333333; border:1px solid #4caf50; border-radius:4px; padding:3px 1px; text-align:center; font-size:0.66em; color:#ffffff;"><strong style="color:#4caf50;">AMD NPU</strong></div>
  </div>
</div>

</div>
</div>

<div style="display:flex; align-items:stretch; gap:10px; margin-top:22px;">
  <div style="flex:1; background:#2a2a2a; border-left:4px solid #e05555; border-radius:5px; padding:7px 12px; font-size:0.85em;"><strong style="color:#ff8a8a;">Without PAI SDK</strong> — Triton + ROCm + gRPC setup, per-language rewrites, <strong style="color:#ff8a8a;">weeks</strong> to first inference</div>
  <div style="display:flex; align-items:center;"><div style="width:0; height:0; border-top:11px solid transparent; border-bottom:11px solid transparent; border-left:18px solid #3498db;"></div></div>
  <div style="flex:1; background:#2a2a2a; border-left:4px solid #4caf50; border-radius:5px; padding:7px 12px; font-size:0.85em;"><strong style="color:#4caf50;">With PAI SDK</strong> — one call, <strong style="color:#4caf50;">4 NMTS</strong>, 2 engineers, <strong style="color:#4caf50;">half a week</strong> to a stable app on AMD</div>
</div>

<div class="highlight-box" style="margin-top:12px; text-align:center;">
<span style="font-size:1.5em; font-weight:bold; color:#4caf50;"><span style="color:#ffffff;">The Pitch:</span> Physical AI SDK accelerates AI development on AMD Edge-HW — <span style="color:#4aa3ff;">from a quarter to a week</span></span>
</div>

---

<!-- _class: small -->

## Same Inference Call — Every Language

<div class="columns">
<div>

**Python**

```python
from physical_ai_sdk.inference_engine \
    import InferenceEngine
engine = InferenceEngine(
    endpoint="physical-ai-sdk.local")
yolo = engine.model("yolov12")
dets = yolo.predict(frame)
```

**C++**

```cpp
#include <physical_ai_sdk/inference_engine.hpp>
auto engine = InferenceEngine(
    "physical-ai-sdk.local");
auto yolo = engine.model("yolov12");
auto dets = yolo.predict(frame);
```

</div>
<div>

**Android (Kotlin)**

```kotlin
import com.amd.physical_ai_sdk.InferenceEngine
val engine = InferenceEngine(
    endpoint = "physical-ai-sdk.local")
val yolo = engine.model("yolov12")
val dets = yolo.predict(frame)
```

**JavaScript / TypeScript**

```javascript
import { InferenceEngine }
    from "@amd/physical-ai-sdk";
const engine = new InferenceEngine({
  endpoint: "http://physical-ai-sdk.local:8000" });
const yolo = await engine.model("yolov12");
const dets = await yolo.predict(frame);
```

</div>
</div>

<div class="highlight-box">

**One mental model, four ecosystems.** Same `Detection {label, score, box}` output everywhere.

</div>

---

<!-- _class: smallest -->

## What Am I Getting in This SDK?

<div class="columns">
<div>

<div style="color:#00bcd4; font-weight:bold; font-size:1.08em; margin-bottom:2px;">The Engine</div>

- **Unified inference engine** — one interface across **CPU · GPU · NPU**, every language (Python · C++ · Android · JS) and transport (in-place · gRPC · HTTP), **zero-copy on edge**

<div style="color:#00bcd4; font-weight:bold; font-size:1.08em; margin:8px 0 2px;">The Models</div>

- **Optimized model zoo** — AMD-tuned models per task
- **Add a model = drop a config**; parallel · sequential · batched pipelines, all by config

</div>
<div>

<div style="color:#00bcd4; font-weight:bold; font-size:1.08em; margin-bottom:2px;">The performance</div>

- **Accuracy, throughput & PnP benchmarks** on edge for every model

<div style="color:#00bcd4; font-weight:bold; font-size:1.08em; margin:8px 0 2px;">The Delivery</div>

- **OOB & Docker** — reproducible, ready-to-ship packaging

- **Co-engineering** with lighthouse customers — cut latency, tune accuracy

</div>
</div>

<div class="highlight-box">

A **low-resistance path** to a **co-engineered, benchmarked, containerized** product on AMD edge hardware.

</div>

---

<!-- _class: lead -->

# Relation with AIG & Value Add

### How PAI SDK builds on — and feeds back into — the AMD AI ecosystem

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

<!-- _class: smallest -->

## Contributions(contd.) — AIG Model → Task-Specific

### 5. Operationalizing AIG Models for Real Applications

<div class="columns">
<div>

**From Generic to Task-Specific**

Took generic AIG Hub models and extended them with operation enablement, hyperparameter tuning, and backend exploration to reach application-level performance:

| Backend | Role |
|---------|------|
| **PyTorch** | Fallback path — handles missing/broken operators |
| **torch.compile** | Additional optimization on top of PyTorch |
| **ONNX** | Stable cross-device flow (CPU ↔ GPU ↔ NPU) |
| **MIGraphX** | **2× improvement** over torch+ROCm |

<div class="highlight-box">

**MobileSAM · CenterPoint · YOLOv12 · YOLO26** — integrated into AARTS robotics pipelines, consumed by the robotics team today.

</div>

</div>
<div>

**SmolVLA: Tuned for the Task**

| | **AIG Generic** | **PAVS Task-Specific** |
|---|---|---|
| **Latency** | 48 ms | **30 ms** |
| **ROCm version** | — | **7.2.4** |
| **Customized to task** | ✗ | ✓ |

**37% latency reduction through algorithmic tuning alone** — on ROCm 7.2.4, without the edge-optimized kernels in ROCm 7.13 that give **2× speedup** on other models.

The gains here are purely from **task-specific model and algorithm optimization** — not from a newer ROCm stack.

<div class="highlight-box">

**Headroom remains:** upgrading to ROCm 7.13 on top of these algorithmic gains is expected to push latency even lower.

</div>

</div>
</div>

---

<!-- _class: small -->

## Contributions(contd.) — Ecosystem & Co-Engineering

### 6. Closing the Loop: Generic Model → Application Pipeline

<div class="columns">
<div>

**The Full Journey**

Continuing from the previous point — we don't stop at model operationalization:

1. Pick generic model from AIG Hub
2. Make it **task-specific** (tune, operationalize)
3. **Compute accuracy** on real inputs — surface gaps
4. **Communicate gaps back to AIG** for model improvement
5. Wire model into **inference pipelines** — connecting to real applications

<div class="highlight-box">

Taking the generic model all the way to working applications — not just benchmarks.

</div>

</div>
<div>

**Co-Engineering Opportunities**

**PAVS × Audio SDK**
- Started discussions to explore co-engineering across SDK verticals
- Shared infrastructure, tooling, and pipeline patterns

**Rivian (RVT) — Automotive Stack**
- Using PAI SDK models to build an **in-car monitoring system** and **voice assistant** on AMD hardware

**Google — Gemma on LiteRT**
- Running the **Gemma** model on **LiteRT** on AMD hardware

</div>
</div>

---

<!-- _class: small -->

## Contributions(contd.) — PAI SDK Platform & Edge Enablement

### Infrastructure: Installer, Edge HW, and LLM Stack

<div class="columns">
<div>

**Installation & Edge Hardware**

- **Single installer/uninstaller** for ROCm + RyzenAI in PAI SDK — one command to set up or tear down the full stack
- Extended and maintained ROCm + RAI support for **edge HW** — required targeted patches for hardware-specific gaps
- **Yocto & LTS support** — enabling model deployment on embedded edge devices

</div>
<div>

**LLM Infrastructure on AMD Stack**

- Integrated **stable vLLM** — high-throughput serving with quantized LLM variants on iGPU
- Integrating **FLM framework** — running LLMs on NPU
- Bridging the open-source LLM ecosystem onto the AMD edge stack

<div class="highlight-box">

Full-stack edge enablement: installer → hardware patches → quantized LLM serving → NPU inference → Yocto deployment.

</div>

</div>
</div>

---

<!-- _class: lead -->

# SW Stack (For Reference)

![w:800](./images/SW_stack.png)