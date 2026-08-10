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

**Why a competitive silicon doesn't win by itself?**
**Voice AI is the lens -- conclusions Hold**

---

<!-- _class: smaller -->

## The Voice AI: Business, Opportunities & Tech-Stack
### A Massive Inference Market, Being Decided Now — Next is Edge Inference
<div class="columns">
<div>

**Tech Stack**

<div style="display:flex; flex-direction:column; align-items:center; gap:0; margin-top:3px; font-size:0.9em;">
  <div style="background:#2a2a2a; border:1px solid #666; border-radius:5px; padding:4px 12px; text-align:center; width:90%;"><strong>1. Telephony / Transport</strong> <span style="color:#aaa;">(&lt;50 ms)</span></div>
  <div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #3498db;margin:2px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:4px 12px; text-align:center; width:90%;"><strong style="color:#ff8a8a;">2. ASR / STT</strong> <span style="color:#aaa;">(&lt;150 ms)</span> · <em>compute</em></div>
  <div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #3498db;margin:2px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:4px 12px; text-align:center; width:90%;"><strong style="color:#ff8a8a;">3. LLM / NLU</strong> <span style="color:#aaa;">(&lt;200 ms)</span> · <em>compute</em></div>
  <div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #3498db;margin:2px 0;"></div>
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:5px; padding:4px 12px; text-align:center; width:90%;"><strong style="color:#ff8a8a;">4. TTS</strong> <span style="color:#aaa;">(&lt;150 ms)</span> · <em>compute</em></div>
  <div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #3498db;margin:2px 0;"></div>
  <div style="background:#1e3a5f; border:1px solid #3498db; border-radius:5px; padding:4px 12px; text-align:center; width:90%;"><strong style="color:#5dade2;">5. Orchestration</strong> <span style="color:#ccc;">· VAD · routing · RAG</span></div>
</div>

**Fig 1 · 3/5 layers are GPU-compute-bearing**

<div style="margin-top:5px; font-size:0.82em; color:#ff8a8a;"> — AMD's advantage <em>and</em> its gaps both live here. </div>

</div>
<div>

**The opportunity**

| Metric | Value |
|---|---|
| AI voice-agents market, 2034 | **$47.5B** @ **35% CAGR** |
| Cost per call — human vs AI | **$7–12 → ~$0.40** |
| YoY growth, production deploys | **340%** (500+ orgs) |
| Contact-center labor savings, 2026 | **$80B** (Gartner) |
| Orgs planning voice AI by end-2026 | **80%** |


</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">A massive, fast-growing inference market whose <span style="color:#4caf50;">compute default</span> is being chosen right now.</span>
</div>

---

<!-- _class: smallest -->

## It's a Compute Market — AMD Has the Winning Silicon

<div class="columns-3">
<div>

**A deployed agent is a steady-state inference machine**

- It doesn't train — it **transcribes, reasons & speaks 24×7**

- **LLM** is cheapest per minute but **most latency-critical** — first token in **&lt;200 ms**
- **TTS is the hidden budget killer** — premium hosted synthesis is **$0.10–$0.30/min**, often exceeding ASR + LLM combined 
- The next frontier is **on-device / edge inference** — kiosks, vehicles, factory floors, hospitals and public services

</div>
<div>

**The savings compound at scale**

- **34% lower cost-per-token** → **~$84K/month** saved at 1M min/month
- Self-hosted ROCm TTS removes **$100K–$300K/month** in hosted synthesis
- on-prem: **~50% lower GPU CapEx**

</div>
<div style="font-size:0.75em;">


| Dimension | MI300X | H100 SXM5 |
|---|---|---|
| VRAM | **192 GB** HBM3 | 80 GB HBM3e |
| On-demand cloud price | **$1.50–2.50/hr** | $2.90/hr |
| Throughput (tok/s) | ~18,000 | ~19,500 |
| **Cost / 1M tokens** | **$0.027** | $0.041 |
| 70B fits on 1 GPU? | **Yes** | No (needs 2+NVLink) |

**LLM inference — MI300X vs H100 SXM5** *(Llama 3.1 70B, 2026)*
*MI355X (288 GB HBM3e) lands within single-digit % of B200 on MLPerf Inference v6.0.*

<div style="font-size:0.72em; color:#888; margin-top:6px; line-height:1.5;">
  <sup>1</sup> <a href="https://www.spheron.network/blog/rocm-vs-cuda-gpu-cloud-2026/">Spheron: ROCm vs CUDA GPU Cloud 2026</a> — cloud pricing MI300X vs H100<br>
  <sup>2</sup> <a href="https://vllm.ai/blog/2026-02-27-rocm-attention-backend">vLLM Blog: High-Performance Inference on AMD ROCm</a> — throughput benchmarks
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;"> Silicon advantage is yet unrealized in the Market: <span style="color:#4caf50;">This is not a hardware problem.</span></span>
</div>

---

<!-- _class: small -->

## Voice AI Stack Convergence & One Compute Decision

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.6em; text-align:center;">Despite hundreds of companies and billions in funding, production code sits above just <strong>three open-source frameworks</strong> — sharing one model layer and one compute decision.</div>

<div style="max-width:660px; margin:0 auto;">

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

</div>

<div class="highlight-box" style="margin-top:10px; text-align:center;">
<span style="font-size:1.25em; font-weight:bold; color:#4aa3ff;">Owning the compute isn't enough — <span style="color:#4caf50;"> you win by owning the on-ramps just above it:
<span style="color:#4aa3ff;">HW choice is made before you reach the compute layer.</span></span></span>
</div>

---

<!-- _class: smallest -->

## How NVIDIA Became the Gateway — The NIM Playbook

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.3em 0 0.4em;">Dominance wasn't silicon alone. The instrument was <strong>NIM</strong> — pre-packaged containers that make NVIDIA the path of least resistance at the first developer touchpoint.</div>

<div class="columns">
<div>

**Ready-to-run microservices**

- **Riva ASR NIM** — streaming ASR (Parakeet) in one `docker pull`; no config, no VAD tuning
- **Maxine Studio Voice NIM** — real-time noise suppression / echo cancellation → directly lowers ASR word-error-rate

**Complete applications**

- **AI Blueprints** — deployable voice-agent repos, not docs. The GPU choice is already encoded inside.

</div>
<div>

**Developer & cloud on-ramps**

- **RTX Spark** — Grace+Blackwell devkit, 128 GB shared memory; prototype on NVIDIA → default to NVIDIA in production
- **Azure AI Foundry NIM** (July 2026) — deploy from VS Code in one click, NVIDIA GPU underneath
- **SI certification** — TCS, Infosys, Wipro, Accenture, Capgemini trained & certified on NIM

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#4aa3ff;">You never consciously select a GPU — Choice is already made.
- <span style="color:#4caf50;">NVIDIA is the default;</span> every other choice requires active effort. <span style="color:#4caf50;">That is softpower.</span></span>
</div>

---

<!-- _class: tiny -->

## CUDA Gap Closed; Ecosystem gap exists
<div class="columns-3">
<div>

**ROCm support for voice-AI components (2026)**

| Component | ROCm | Note |
|---|---|---|
| LLM serving (vLLM, Llama 3.1) | Full | 90–95% of H100 tput |
| LLM serving (SGLang) | Full | Within 5–10% of CUDA |
| TTS: Kokoro, Chatterbox | Full | Pure PyTorch, 0 changes |
| TTS: Coqui XTTS-v2 | Partial | Works with effort |
| ASR: Faster-Whisper (batch) | Full | RT mode needs work |
| ASR: streaming containers | **Gap** | CUDA-assumed |
| Embeddings: HF TEI | **Gap** | No ROCm build |

</div>
<div>

**NIM ecosystem gap: NVIDIA vs AMD required**

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

**Framework ecosystem presence**

| Framework | NVIDIA | AMD |
|---|---|---|
| Pipecat | Official processor | **Absent** |
| LiveKit Agents | Certified backend | **Absent** |
| LangChain | `langchain-nvidia-ai-endpoints` | **Absent** |
| LlamaIndex | `llama-index-llms-nvidia` | **Absent** |
| Haystack | NIM pipeline component |**Absent** |

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#4aa3ff;">The gap is <span style="color:#4aa3ff;">not silicon</span> — it's the <span style="color:#4caf50;">least-resistant path to silicon</span>: containers, plugins, blueprints &amp; marketplace slots.</span>
</div>

---

<!-- _class: smallest -->

## The Five Downstream Ecosystem Layers

<div class="columns">
<div>

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.3em 0 0.4em;"> Same logic at every layer: ship a named package → developers adopt the default → the hardware choice becomes invisible at the call site.</div>

**1 · Framework plugin slots**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">`ChatNVIDIA(...)` routes to NVIDIA at the endpoint. AMD doesn't exist at that call site — repeated across millions of pipelines.</div>

**2 · Inference serving infrastructure**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Triton / Dynamo + TensorRT-LLM = the invisible substrate (20–30% edge at batch 1–4). AMD has **vLLM ROCm only** — one tool, not infrastructure.</div>

**3 · Voice-domain SDKs**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Riva (ASR+TTS+MT+diarization) · Maxine (noise suppression) · ACE (digital humans). **AMD has no equivalent for any of the three.**</div>

</div>
<div>

**4 · Edge hardware platform**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Jetson (Nano → Thor) + JetPack ships Riva, vLLM, CUDA. Certified OEMs: Siemens, KUKA, ADLINK. Caterpillar runs Jetson Thor + Riva inside a bulldozer cab. AMD — <span class="warning">partial</span>: Kria (latest) launched but not ecosystem-certified for industrial voice pipelines.</div>

**5 · Cloud marketplace slots**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">NIM native on Azure Foundry; selectable on HF, SageMaker, Vertex. AMD <span class="warning">partial</span>: [`huggingface/testing-rocm7.0-preview`](https://hub.docker.com/r/huggingface/testing-rocm7.0-preview) exists — preview only, **not surfaced in the UI**.</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.25em; font-weight:bold; color:#ffffff;">The pattern: <span style="color:#4aa3ff;">ship the default package, and the hardware choice disappears at the call site.</span> <span style="color:#4caf50;">AMD is not present above Compute layers
.</span></span>
</div>

---

<!-- _class: smallest -->

## The Four Upstream Gaps

<div class="columns">
<div>

**Gap 1 · Training & fine-tuning moat**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Voice companies fine-tune weekly (custom ASR/TTS/NLU). **NeMo → Triton export** locks the whole loop to NVIDIA.</div>

**Gap 2 · ISV & SI sales channel**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">GPU chosen implicitly by the ISV. NVIDIA is in **Genesys** (11k+ customers), **Cisco Webex** (Maxine), **Salesforce**, **ServiceNow**. SIs (TCS, Infosys, Wipro, Accenture) are **certified on NVIDIA**. AMD: no presence in any major contact-center ISV.</div>

</div>
<div>

**Gap 3 · Voice + vision convergence**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Next-gen agents fuse camera + mic. Jetson Thor unifies **Isaac · Metropolis · Riva · ACE** on one substrate. AMD's lines still converging <span style="color:#4caf50;"> AMD-PAVS AI Pipelines </span> — a **converging but early stage**.</div>

**Gap 4 · Synthetic data for low-resource languages**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">No AMD-native syntheitc-data pipeline's or minimal academic partnership's → lifecycle dependency predates any inference decision.</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#4aa3ff;">Closing downstream <span style="color:#4caf50;"> puts AMD in contention;</span> 
closing upstream  <span style="color:#4caf50;">creates platform momentum</span>.</span>
</div>

---

<!-- _class: smallest -->

## The AMD Gateway Strategy

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.3em 0 0.4em;">Run NVIDIA's playbook — targeting the cost wedge its pricing creates. Same Pipecat code, same LiveKit transport, 34% lower per-conversation LLM cost.</div>

<div class="columns-3">
<div>

**Step 1 · Three certified containers**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">`docker pull` → validated in 30 s: (a) Pipecat Voice Agent (Whisper + vLLM + Kokoro), (b) LiveKit + SIP, (c) DPDP-compliant, on-prem setup.</div>

**Step 2 · AMD Voice AI Blueprints**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Deployable repos, not docs — US/EU contact center, India BFSI, Arabic GCC, edge/offline. Must run on a **~$700 consumer GPU**.</div>

</div>
<div>

**Step 3 · Pipecat ROCm plugin**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">`pipecat-ai[amd]` on PyPI — AMD as an official processor alongside Deepgram / ElevenLabs.</div>

**Step 4 · HF TEI on ROCm**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">Upstream ROCm into Text-Embeddings-Inference — closes the last RAG software gap.</div>

</div>
<div>

**Step 5 · HF Inference Endpoints slot**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">TGI ROCm is ready — one **business agreement** makes MI300X selectable. **Zero eng weeks.**</div>

**Step 6 · Ryzen AI NPU on-ramp**
<div style="font-size:0.82em; margin:0.1em 0 0.5em;">`pipecat create --backend amd-npu` — offline, no GPU, no API key. The dev-laptop demo that mirrors **RTX Spark**.</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#ffffff;"><span style="color:#4caf50;">PAVS sits exactly at this intersection</span> — <span style="color:#4aa3ff;">between AIG model outputs and lighthouse customers. It does <span style="color:#4caf50;">Implicitly</span> what NVIDIA's platform teams do intentionally</span></span>
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

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#ffffff;"><span style="color:#4caf50;">First 12–16 weeks:</span> Steps 1–4 with 6–8 engineers make AMD visible at first contact. <span style="color:#4aa3ff;">India BFSI under DPDP is the natural beachhead</span> — on-prem mandatory, ~50% lower CapEx.</span>
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

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.2em; font-weight:bold; color:#4caf50;">Make AMD the path of least resistance at the first touchpoint, and the rest of the stack follows.</span>
</div>