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

# PAVS: Bridging AMD's Softpower Gap

## From the Voice AI Perspective

**Why the best inference silicon doesn't win by itself — Voice AI as the lens, with the same pattern repeating in robotics, industrial & healthcare**

---

<!-- _class: small -->

## The Voice AI: Business, Opportunities & Tech-Stack
### A Massive Inference Market, Being Decided Now, Next is edge-inference
<div class="columns">
<div>

**The opportunity**

| Metric | Value |
|---|---|
| AI voice-agents market, 2034 | **$47.5B** @ **35% CAGR** |
| Cost per call — human vs AI | **$7–12 → ~$0.40** |
| YoY growth, production deploys | **340%** (500+ orgs) |
| Orgs planning voice AI by end-2026 | **80%** |

- A deployed agent is a **steady-state inference machine** — it doesn't train; it **transcribes, reasons & speaks 24×7**
- At scale, its **dominant operating cost is GPU compute**

</div>
<div>

**Why this is AMD's business**

- **MI300X: 34% lower cost-per-token** for 70B-class LLM inference vs H100
- **Single-GPU fit** — 192 GB HBM3 runs a 70B model that needs **two** H100s
- At 1M min/month → **~$84K/month** saved on LLM inference alone
- Self-hosted ROCm TTS removes **$100K–$300K/month** hosted synthesis
- India on-prem: **~50% lower GPU CapEx**

<div class="highlight-box">

The advantage is **real** — yet unrealized, because AMD is absent from the ecosystem surface where compute is **selected**.

</div>

</div>
</div>

---

<!-- _class: tiny -->

## The Voice AI Stack and Its Convergence

<div class="columns">
<div>

**Fig 1 · Five-layer pipeline** — 3 layers are GPU-compute-bearing *(median E2E 680 ms; bar → sub-500 ms)*

<div style="display:flex; flex-direction:column; align-items:center; gap:0; margin-top:4px;">
  <div style="background:#2a2a2a; border:1px solid #666; border-radius:5px; padding:5px 12px; text-align:center; width:88%;"><strong>1. Telephony / Transport</strong> <span style="color:#aaa;">(&lt;50 ms)</span><br><span style="font-size:0.85em; color:#ccc;">SIP / WebRTC routing</span></div>
  <div style="width:0;height:0;border-left:7px solid transparent;border-right:7px solid transparent;border-top:9px solid #3498db;margin:3px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:5px 12px; text-align:center; width:88%;"><strong style="color:#ff8a8a;">2. ASR / STT</strong> <span style="color:#aaa;">(&lt;150 ms)</span> · <em>compute</em><br><span style="font-size:0.85em; color:#ccc;">speech → text</span></div>
  <div style="width:0;height:0;border-left:7px solid transparent;border-right:7px solid transparent;border-top:9px solid #3498db;margin:3px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:5px 12px; text-align:center; width:88%;"><strong style="color:#ff8a8a;">3. LLM / NLU</strong> <span style="color:#aaa;">(&lt;200 ms)</span> · <em>compute</em><br><span style="font-size:0.85em; color:#ccc;">intent → reply text</span></div>
  <div style="width:0;height:0;border-left:7px solid transparent;border-right:7px solid transparent;border-top:9px solid #3498db;margin:3px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:5px 12px; text-align:center; width:88%;"><strong style="color:#ff8a8a;">4. TTS</strong> <span style="color:#aaa;">(&lt;150 ms)</span> · <em>compute</em><br><span style="font-size:0.85em; color:#ccc;">text → audio · hidden budget killer</span></div>
  <div style="width:0;height:0;border-left:7px solid transparent;border-right:7px solid transparent;border-top:9px solid #3498db;margin:3px 0;"></div>
  <div style="background:#2a2a2a; border:1px solid #666; border-radius:5px; padding:5px 12px; text-align:center; width:88%;"><strong>5. Orchestration</strong><br><span style="font-size:0.85em; color:#ccc;">VAD · turn-taking · routing · RAG</span></div>
</div>

<div style="margin-top:6px; font-size:0.92em; color:#ccc;">Shaded <strong style="color:#ff8a8a;">ASR · LLM · TTS</strong> consume GPU cycles — AMD's advantage <em>and</em> its gaps both live here.</div>

</div>
<div>

**Fig 2 · Industry convergence** — every platform sits above one of three frameworks

<div style="display:flex; flex-direction:column; align-items:center; gap:0; margin-top:2px;">
  <div style="background:#2a2a2a; border:1px solid #666; border-radius:6px; padding:5px 12px; text-align:center; width:92%;">
    <strong style="color:#ffffff;">EVERY VOICE AI COMPANY</strong><br>
    <span style="font-size:0.82em; color:#cccccc;">Vapi · Retell · Bolna · Gnani · PolyAI · Synthflow · Ringg.ai</span>
  </div>
  <div style="width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-top:10px solid #3498db;margin:3px 0;"></div>
  <div style="display:flex; gap:8px; width:92%; justify-content:center;">
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:5px; text-align:center;"><strong style="color:#5dade2;">LiveKit</strong><br><span style="font-size:0.75em; color:#ccc;">Apache 2.0</span></div>
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:5px; text-align:center;"><strong style="color:#5dade2;">Pipecat</strong><br><span style="font-size:0.75em; color:#ccc;">BSD-2</span></div>
    <div style="flex:1; background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:5px; text-align:center;"><strong style="color:#5dade2;">TEN</strong><br><span style="font-size:0.75em; color:#ccc;">C++/Go</span></div>
  </div>
  <div style="width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-top:10px solid #3498db;margin:3px 0;"></div>
  <div style="background:#2a2a2a; border:1px solid #666; border-radius:6px; padding:5px 12px; text-align:center; width:92%;">
    <strong>SHARED MODEL LAYER</strong><br>
    <span style="font-size:0.8em; color:#ccc;">STT: Whisper / Sarvam · LLM: Llama / GPT-4o · TTS: Kokoro / ElevenLabs</span>
  </div>
  <div style="width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-top:10px solid #e05555;margin:3px 0;"></div>
  <div style="background:#3a1e1e; border:2px solid #e05555; border-radius:6px; padding:6px 12px; text-align:center; width:60%;">
    <strong style="color:#ffffff;">GPU COMPUTE</strong> &nbsp; NVIDIA / <strong style="color:#4caf50;">AMD</strong>
  </div>
</div>

<div class="highlight-box" style="margin-top:8px;">
Win the <strong>compute layer</strong> — or the <strong>plugin slot just above it</strong> — and the hardware choice is made for <em>every</em> platform above.
</div>

</div>
</div>

---

<!-- _class: tiny -->

## CUDA Gap Closed; AMD Still Lacks a Low-Resistance Path to Its Silicon

<div class="columns-3">
<div>

**Table 1 · ROCm support for voice-AI components (2026)**

| Component | ROCm | Note |
|---|---|---|
| LLM serving (vLLM, Llama 3.1) | Full | 90–95% of H100 tput |
| LLM serving (SGLang) | Full | Within 5–10% of CUDA |
| TTS: Kokoro, Chatterbox | Full | Pure PyTorch, 0 changes |
| TTS: Coqui XTTS-v2 | Partial | Works with effort |
| ASR: Faster-Whisper (batch) | Full | RT mode needs work |
| ASR: streaming containers | **Gap** | CUDA-assumed |
| Embeddings: HF TEI | **Gap** | No ROCm build |

*Two heaviest layers (LLM, TTS) solved; streaming ASR + TEI remain open.*

</div>
<div>

**Table 3 · NIM ecosystem gap: NVIDIA vs AMD required**

| NVIDIA Has | AMD Equivalent | Status |
|---|---|---|
| Riva ASR NIM | AMD ASR container | **Absent** |
| Riva TTS NIM | AMD TTS container | **Absent** |
| AI Blueprint: voice agent | Pipecat on MI300X | **Absent** |
| Pipecat NVIDIA processor | Pipecat AMD processor | **Absent** |
| LiveKit certified backend | LiveKit AMD backend | **Absent** |
| VS Code NIM extension | ROCm / Quark ext. | **Absent** |
| Azure Foundry NIM | Azure AMD endpoint | Partial |
| SI cert (TCS, Infosys) | SI cert program | **Absent** |
| 28M devs default CUDA | AMD dev default | Opt-in |

</div>
<div>

**Table 4 · Framework ecosystem presence**

| Framework | NVIDIA | AMD |
|---|---|---|
| Pipecat | Official processor | Absent |
| LiveKit Agents | Certified backend | Absent |
| LangChain | `langchain-nvidia-ai-endpoints` | Absent |
| LlamaIndex | `llama-index-llms-nvidia` | Absent |
| Haystack | NIM pipeline component | Absent |

<div class="highlight-box">
The gap is <strong>not silicon</strong> — it's the <strong>least-resistant path to silicon</strong>: containers, plugins, blueprints &amp; marketplace slots.
</div>

</div>
</div>

---

<!-- _class: smallest -->

## The Five Downstream Ecosystem Layers

<div class="columns">
<div>

**Same logic at every layer:** ship a named package → developers adopt the default → the hardware choice becomes invisible at the call site.

**1 · Framework plugin slots**
`ChatNVIDIA(...)` routes to NVIDIA at the endpoint. AMD doesn't exist at that call site — repeated across millions of pipelines.

**2 · Inference serving infrastructure**
Triton / Dynamo + TensorRT-LLM = the invisible substrate (20–30% edge at batch 1–4). AMD has **vLLM ROCm only** — one tool, not infrastructure.

**3 · Voice-domain SDKs**
Riva (ASR+TTS+MT+diarization) · Maxine (noise suppression) · ACE (digital humans). **AMD has no equivalent for any of the three.**

</div>
<div>

**4 · Edge hardware platform**
Jetson (Nano → Thor) + JetPack ships Riva, vLLM, CUDA. Certified OEMs: Siemens, KUKA, ADLINK. Caterpillar runs Jetson Thor + Riva inside a bulldozer cab. AMD Ryzen AI = **laptop only** — no industrial module.

**5 · Cloud marketplace slots**
NIM native on Azure Foundry; selectable on HF, SageMaker, Vertex. AMD **absent / limited** — TGI ROCm image is production-ready but **not surfaced in the UI**.

<div class="highlight-box">

**"Deploy this model" → MI300X isn't in the GPU dropdown.** Not a silicon gap — a **slot gap**. And a slot gap is **closeable**.

</div>

</div>
</div>

---

<!-- _class: smallest -->

## The Four Upstream Gaps

<div class="columns">
<div>

**Gap 1 · Training & fine-tuning moat**
Voice companies fine-tune weekly (custom ASR/TTS/NLU). **NeMo → Triton export** locks the whole loop to NVIDIA. Key libs are CUDA-primary on AMD:

| Library | Role | ROCm Status |
|---|---|---|
| `bitsandbytes` | 4/8-bit quant | Community fork |
| `trl` (HF) | RLHF / fine-tune | Experimental |
| Axolotl | Most-used tuner | Untested |
| PEFT | LoRA / QLoRA | Works, less tested |
| FlashAttention 3 | Fastest attn kernel | No AMD equiv. |

</div>
<div>

**Gap 2 · ISV & SI sales channel**
GPU chosen implicitly by the ISV. NVIDIA is in **Genesys** (11k+ customers), **Cisco Webex** (Maxine), **Salesforce**, **ServiceNow**. SIs (TCS, Infosys, Wipro, Accenture) are **certified on NVIDIA**. AMD: no presence in any major contact-center ISV.

**Gap 3 · Voice + vision convergence**
Next-gen agents fuse camera + mic. Jetson Thor unifies **Isaac · Metropolis · Riva · ACE** on one substrate. AMD's lines don't converge (MI300X · Ryzen AI · Radeon) — a **missing product category**.

**Gap 4 · Synthetic data for low-resource languages**
No AMD-native speech-data pipeline or academic partnership (e.g. AI4Bharat) → lifecycle dependency predates any inference decision.

</div>
</div>

<div class="highlight-box">
Closing <strong>downstream</strong> puts AMD in contention; closing <strong>upstream</strong> creates <strong>platform momentum</strong>. The chain compounds: fine-tune on NeMo → deploy to Triton → shipped inside Genesys → sold by an NVIDIA-certified SI.
</div>

---

<!-- _class: smallest -->

## The AMD Gateway Strategy

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.3em 0 0.4em;">Run NVIDIA's playbook — targeting the cost wedge its pricing creates. Same Pipecat code, same LiveKit transport, 34% lower per-conversation LLM cost.</div>

<div class="columns-3">
<div>

**Step 1 · Three certified containers**
`docker pull` → validated in 30 s: (a) Pipecat Voice Agent (Whisper + vLLM + Kokoro), (b) LiveKit + SIP, (c) Sarvam India (DPDP-compliant, on-prem).

**Step 2 · AMD Voice AI Blueprints**
Deployable repos, not docs — US/EU contact center, India BFSI, Arabic GCC, edge/offline. Must run on a **~$700 consumer GPU**.

</div>
<div>

**Step 3 · Pipecat ROCm plugin**
`pipecat-ai[amd]` on PyPI — AMD as an official processor alongside Deepgram / ElevenLabs. **~2 weeks.**

**Step 4 · HF TEI on ROCm**
Upstream ROCm into Text-Embeddings-Inference — closes the last RAG software gap.

</div>
<div>

**Step 5 · HF Inference Endpoints slot**
TGI ROCm is ready — one **business agreement** makes MI300X selectable. **Zero eng weeks.**

**Step 6 · Ryzen AI NPU on-ramp**
`pipecat create --backend amd-npu` — offline, no GPU, no API key. The dev-laptop demo that mirrors **RTX Spark**.

</div>
</div>

<div class="highlight-box">
<strong>PAVS sits exactly at this intersection</strong> — between AIG model outputs and lighthouse customers. Converting a raw model → production vertical software does <em>organically</em> what NVIDIA's platform teams do <em>intentionally</em>. The pattern generalizes: robotics, industrial, healthcare, automotive.
</div>

---

<!-- _class: tiny -->

## Prioritized Action Roadmap

<div class="columns">
<div>

**Tier 1 — Pure engineering** *(no new silicon, no product decisions)*

| Action | Effort | Horizon | Impact |
|---|---|---|---|
| HF Inference Endpoints slot | Business neg. | 0–4 wks | High |
| Certified ASR + TTS containers | 2 wks each | 1 month | High |
| Pipecat AMD processor (PyPI) | 2 wks | 1 month | Medium |
| LangChain / LlamaIndex / Haystack | 2–4 wks ea. | 1–2 mo | High |
| AMD Voice AI Blueprints (4 targets) | 4 wks each | 2 months | High |
| `bitsandbytes` ROCm official | 4–6 wks | 2 months | High |
| Triton ROCm certified image | 12–16 wks | 4 months | High |
| Ryzen AI NPU voice template | 4 wks | 2 months | Medium |

</div>
<div>

**Tier 2 — Business dev + engineering**

| Action | Effort | Horizon | Impact |
|---|---|---|---|
| Genesys ISV integration | Business dev | 6–12 mo | Very high |
| SI cert program (TCS, Infosys) | Program build | 6–12 mo | Very high |
| FlashAttention 3 / CDNA3 equiv. | 16–24 wks | 6 months | Medium |

**Tier 3 — Strategic HW commitments**

| Action | Effort | Horizon | Impact |
|---|---|---|---|
| AMD voice data initiative (India) | $5–13M, 2 yr | 18–24 mo | Strategic |
| Jetson-equiv. industrial edge module | HW roadmap | 2–3 yrs | Very high |

<div class="highlight-box">
<strong>First 12–16 weeks:</strong> Steps 1–4 with 6–8 engineers make AMD visible to every Pipecat & LiveKit developer at first contact. <strong>India BFSI under DPDP</strong> is the natural beachhead — on-prem mandatory, ~50% lower CapEx.
</div>

</div>
</div>

---

<!-- _class: small -->

## How the Bridge Is Being Closed

<div class="columns">
<div>

**The gap can't be closed by a new chip**

- It's a **software & ecosystem** problem — containers, plugins, blueprints, marketplace slots
- Which is **exactly** the problem a **vertical-software team** solves

**PAVS produces the closing assets organically**

- Each lighthouse deployment → a **reusable pipeline** = a step toward an AMD-native ecosystem
- Each model the Physical AI SDK supports → **one less** requiring NVIDIA tooling on AMD HW
- Each robotics pipeline on Ryzen AI APU → a **reference design** for an OEM / SI / ISV

</div>
<div>

<div style="border:1px solid #3498db; border-radius:6px; padding:9px; background:#202020; text-align:center; font-size:0.9em;">
<div style="color:#aaaaaa;">AMD AI Group (AIG)</div>
<div style="color:#3498db;">↓ models + research &nbsp;&nbsp; ↑ deployment feedback</div>
<div style="background:#3498db; color:#fff; font-weight:bold; border-radius:4px; padding:4px 0; margin:5px 0;">PAVS</div>
<div style="color:#3498db;">↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↑</div>
<div style="display:flex; gap:6px; margin-top:4px;">
<div style="flex:1; background:#2a2a2a; border-radius:4px; padding:5px; font-size:0.85em;"><strong style="color:#00bcd4;">Physical AI SDK</strong><br>inference substrate</div>
<div style="flex:1; background:#2a2a2a; border-radius:4px; padding:5px; font-size:0.85em;"><strong style="color:#00bcd4;">Multi-modal pipelines</strong><br>+ Jetson-class devkit</div>
</div>
</div>

<div class="highlight-box">
The window is open — but NVIDIA's Jetson ecosystem, NIM integrations & SI certs deepen every quarter. <strong>Make AMD the path of least resistance at the first touchpoint, and the rest of the stack follows adoption.</strong>
</div>

</div>
</div>