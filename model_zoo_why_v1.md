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

# Why a Model Zoo?

## From a 100 GB Tarball to an Off-the-Shelf Product Experience

**What PAVS needs from a Model Zoo — and what we must not turn it into**

---

<!-- _class: small -->

## 1 · The Off-the-Shelf Promise

<div class="columns">
<div>

**What an application developer actually wants**

- Download a model → **start building the application today**
- No knowledge of layers, kernels, quantization, or backends
- Just a **prepackaged model, best-suited to the task**, ready to run on AMD hardware

<div class="highlight-box">

The developer knows the **inputs and outputs** of the model and builds his product around them — nothing more.

</div>

</div>
<div>

**The experience we are selling**

<div style="display:flex; flex-direction:column; align-items:center; gap:6px; margin-top:8px;">
  <div style="background:#2a2a2a; border:1px solid #00bcd4; border-radius:6px; padding:8px 16px; width:82%; text-align:center;"><strong style="color:#00bcd4;">Pick a task</strong> — detect / classify / segment / LLM</div>
  <div style="color:#3498db; font-size:1.3em;">&#8595;</div>
  <div style="background:#2a2a2a; border:1px solid #00bcd4; border-radius:6px; padding:8px 16px; width:82%; text-align:center;"><strong style="color:#00bcd4;">Download the packaged model</strong> — already optimized</div>
  <div style="color:#3498db; font-size:1.3em;">&#8595;</div>
  <div style="background:#333333; border:1px solid #4caf50; border-radius:6px; padding:8px 16px; width:82%; text-align:center; color:#ffffff;"><strong style="color:#4caf50;">Build the product</strong> — runs on CPU · GPU · NPU</div>
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
A model zoo is what turns <strong>"here are some weights"</strong> into <strong>"here is a product you can ship."</strong>
</div>

---

<!-- _class: small -->

## 2 · NVIDIA's Blueprint: NGC &#8596; Isaac ROS

<div class="columns">
<div>

![w:520](./model_zoo/Nvidia-model-zoo.png)

<div style="font-size:0.8em; color:#888; text-align:center;">NGC Catalog — curated, prepackaged models (PeopleNet, Mistral-7B Int4, …)</div>

</div>
<div>

**The pattern that makes it work**

- **NGC Catalog** hosts the ready-to-run models
- **Isaac ROS** consumes them directly into robotics pipelines
- The developer pulls a model and it *just runs* — no export, no tuning

<div class="highlight-box">

**AMD needs exactly this pairing:**
a **zoo** that hosts optimized models + an **SDK / robotics stack** that consumes them off-the-shelf.

</div>

<div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-top:12px;">
  <div style="background:#2a2a2a; border:1px solid #3498db; border-radius:6px; padding:6px 12px; text-align:center;"><strong style="color:#3498db;">AMD Model Zoo</strong><br><span style="font-size:0.82em; color:#ccc;">hosts weights</span></div>
  <div style="color:#4caf50; font-weight:bold;">&#8596;</div>
  <div style="background:#2a2a2a; border:1px solid #4caf50; border-radius:6px; padding:6px 12px; text-align:center;"><strong style="color:#4caf50;">PAI SDK / AARTS</strong><br><span style="font-size:0.82em; color:#ccc;">consumes them</span></div>
</div>

</div>
</div>

---

<!-- _class: small -->

## 3 · The Tarball Problem

<div class="columns">
<div>

**How we ship today**

- **Every model** is packaged into the release tarball
- Add optimized variants of CNNs **and** LLMs and it balloons fast
- Realistically **100+ GB** — and growing with every new variant

<div class="highlight-box" style="border-left-color:#e05555;">

Every user carries **the entire zoo on their disk** — even if they only ever use a couple of CNNs.

</div>

</div>
<div>

<div style="display:flex; flex-direction:column; align-items:center; gap:8px; margin-top:4px;">
  <div style="width:88%; background:#2a2a2a; border:2px solid #e05555; border-radius:6px; padding:10px;">
    <div style="text-align:center; font-weight:bold; color:#ff8a8a; margin-bottom:6px;">Monolithic Tarball · 100+ GB</div>
    <div style="display:flex; flex-wrap:wrap; gap:4px; justify-content:center; font-size:0.7em;">
      <span style="background:#333; border-radius:3px; padding:2px 6px;">YOLOv12</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">YOLO26 fp16/int8</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">MobileSAM</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">CenterPoint</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">Llama-3 int4</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">SmolVLA</span>
      <span style="background:#333; border-radius:3px; padding:2px 6px;">+ every variant</span>
    </div>
  </div>
  <div style="color:#e05555; font-size:1.3em;">&#8595; forced onto every disk</div>
  <div style="width:88%; background:#333333; border:1px dashed #888; border-radius:6px; padding:8px; text-align:center; font-size:0.82em; color:#ccc;">User who only wanted <strong style="color:#4caf50;">2 CNNs</strong> still pays the full 100+ GB</div>
</div>

<div class="highlight-box" style="border-left-color:#4caf50;">
A zoo fixes this: <strong>pull only the model you need</strong>, keep the SDK lean.
</div>

</div>
</div>

---

<!-- _class: smallest -->

## 4 · Save the Optimization Stages — Don't Ship Them Raw

### AIG hands us a PyTorch model — the zoo stores every optimized artifact so the customer never has to

<div style="display:flex; align-items:stretch; justify-content:center; gap:8px; margin:6px 0;">
  <div style="background:#2a2a2a; border:1px solid #9b59b6; border-radius:6px; padding:8px 12px; text-align:center; width:130px;"><strong style="color:#b07cc6;">AIG PyTorch model</strong><br><span style="font-size:0.8em; color:#ccc;">research checkpoint</span></div>
  <div style="display:flex; align-items:center; color:#3498db; font-weight:bold;">&#8594;</div>
  <div style="background:#2a2a2a; border:1px solid #00bcd4; border-radius:6px; padding:8px 12px; text-align:center; width:130px;"><strong style="color:#00bcd4;">Export to ONNX</strong><br><span style="font-size:0.8em; color:#ccc;">MIGraphX · Vitis-AI</span></div>
  <div style="display:flex; align-items:center; color:#3498db; font-weight:bold;">&#8594;</div>
  <div style="background:#2a2a2a; border:1px solid #00bcd4; border-radius:6px; padding:8px 12px; text-align:center; width:150px;"><strong style="color:#00bcd4;">Quantize</strong><br><span style="font-size:0.8em; color:#ccc;">AWQ · INT4 + calibration</span></div>
  <div style="display:flex; align-items:center; color:#3498db; font-weight:bold;">&#8594;</div>
  <div style="background:#2a2a2a; border:1px solid #00bcd4; border-radius:6px; padding:8px 12px; text-align:center; width:130px;"><strong style="color:#00bcd4;">NPU flow</strong><br><span style="font-size:0.8em; color:#ccc;">kernel-level opt</span></div>
  <div style="display:flex; align-items:center; color:#4caf50; font-weight:bold;">&#8594;</div>
  <div style="background:#333333; border:1px solid #4caf50; border-radius:6px; padding:8px 12px; text-align:center; width:120px; color:#fff;"><strong style="color:#4caf50;">Customer usage</strong><br><span style="font-size:0.8em; color:#ccc;">just downloads</span></div>
</div>

<div class="columns">
<div>

**The zoo stores every stage as a downloadable artifact**

- PyTorch → ONNX → MIGraphX / Vitis-AI graphs
- AWQ-quantized ONNX · INT4 + calibration data
- Kernel-level optimized NPU builds

<div class="highlight-box" style="border-left-color:#e05555;">

**If we don't save these stages,** the end customer has to run PyTorch &#8594; ONNX &#8594; INT4 **on his own disk at usage time** — slow toolchains, calibration data, hours of work. **Poor user experience.**

</div>

</div>
<div>

**This is why NVIDIA & Qualcomm pre-bake artifacts**

- NVIDIA NGC — ready-to-run per target
- **Qualcomm AI Hub** — per-backend precompiled models
- We are building a zoo **close to the Qualcomm model** — graphics not there yet, but the structure is live:

![w:340](./model_zoo/AMD_PAVS_MODEL_ZOO.png)

<div style="font-size:0.78em; color:#888; text-align:center;">AMD-PAVS-AI on Hugging Face — 49 models, per-task</div>

</div>
</div>

---

<!-- _class: small -->

## 5 · How the Zoo Delivers a Great User Experience

![w:1000](./model_zoo/user_exprience.png)

<div class="highlight-box" style="text-align:center;">
Model cards reference companion scripts · downloadable preprocessed ONNX checkpoints · <strong>ready-to-run for MIGraphX / Vitis-AI</strong> — and a <strong style="color:#4caf50;">lean SDK</strong> because weights live in the zoo, not the tarball.
</div>

---

<!-- _class: small -->

## 6 · Two Kinds of Users — Two Kinds of Products

<div class="columns">
<div>

<div style="color:#9b59b6; font-weight:bold; font-size:1.15em;">AIG Git + Model Zoo serves…</div>

**The Research Engineer**

- Knows the **nitty-gritty** of the model internals
- Rewires layers, swaps operators, debugs graphs
- Cares *which layer breaks*, *which workflow is GPU-heavy*, *which lighter variant to substitute*
- Works **inside** the model

<div class="highlight-box" style="border-left-color:#9b59b6;">
Audience: people who build and modify models.
</div>

</div>
<div>

<div style="color:#4caf50; font-weight:bold; font-size:1.15em;">PAVS serves…</div>

**The Application Engineer**

- Uses AI models as **black boxes**
- Knows only the **inputs and outputs**
- Does **not** need to know which layer breaks or which variant is lighter
- Builds the **application around** the model

<div class="highlight-box" style="border-left-color:#4caf50;">
Audience: people who ship products using models.
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
Our zoo brings a <strong>different kind of user</strong> onto AMD silicon — and needs to be shaped for <strong>them</strong>, not for the researcher.
</div>

---

<!-- _class: small -->

## 7 · What PAVS Expects From a Model Zoo

<div class="columns">
<div>

**Just a storage space — like Hugging Face**

- We **don't care who owns or maintains it** — could be AMD central-wide infrastructure
- One requirement: it **hosts weights and serves them to customers**

**What we do need: operational flexibility**

- Freedom to **create directories** / structure as our workflows demand
- **Store the weights** for every optimization stage
- **Make them public** for customer consumption on our schedule

</div>
<div>

<div style="border:2px solid #3498db; border-radius:8px; padding:12px; background:#202020;">
  <div style="text-align:center; font-weight:bold; color:#3498db; margin-bottom:8px;">Model Zoo = Storage + Freedom</div>
  <div style="display:flex; flex-direction:column; gap:6px; font-size:0.85em;">
    <div style="background:#2a2a2a; border-radius:5px; padding:6px 10px;">&#128193; Create our own directory structure</div>
    <div style="background:#2a2a2a; border-radius:5px; padding:6px 10px;">&#128190; Store weights for every stage</div>
    <div style="background:#2a2a2a; border-radius:5px; padding:6px 10px;">&#127760; Publish for customers directly</div>
    <div style="background:#2a2a2a; border-radius:5px; padding:6px 10px;">&#128274; Control what is public, and when</div>
  </div>
</div>

<div class="highlight-box">
Think <strong>Hugging Face for AMD</strong>: a backing store we operate freely — not a system we must conform to.
</div>

</div>
</div>

---

<!-- _class: smallest -->

## 8 · What We Should NOT Do

### The initial promise: convert research code into **vertical software** — a zoo must not reverse that

<div class="columns">
<div>

**The anti-pattern**

If AIG **hosts** the zoo and mandates we place our models in it:

1. To appear on **their dashboard**, we must write research code that **fits their git repo**
2. We end up rebuilding a **research setup** — **not vertical software**
3. This turns our SDK into a mirror of **their repo and dashboard**

<div class="highlight-box" style="border-left-color:#e05555;">

This direction **nullifies the value-add** that Physical AI & Vertical Software brings — the exact opposite of our founding promise.

</div>

</div>
<div>

**The right shape**

- Our job (per the SW-stack promise) is **Research Desk → Vertical Software**
- Fitting AIG's repo/dashboard is **book-keeping**, not a **customer-facing** deliverable

<div style="display:flex; flex-direction:column; align-items:center; gap:4px; margin:6px 0;">
  <div style="background:#2a2a2a; border:1px solid #4caf50; border-radius:6px; padding:6px 12px; text-align:center; width:88%;"><strong style="color:#4caf50;">Vertical software</strong> — customer-facing, product-grade</div>
  <div style="color:#3498db;">&#9650; keep on top</div>
  <div style="background:#333; border:1px dashed #888; border-radius:6px; padding:6px 12px; text-align:center; width:88%; color:#ccc;"><strong style="color:#aaa;">AIG repo / dashboard sync</strong> — do it as <em>book-keeping</em>, if at all</div>
</div>

<div class="highlight-box" style="border-left-color:#4caf50;">

**If it must be done, do it as book-keeping** — never let it turn the SDK into a customer-facing clone of the research repo.

</div>

</div>
</div>

---

<!-- _class: lead -->

# The Ask

## A model zoo that is **storage + operational freedom** — so PAVS ships an **off-the-shelf, product-grade** experience on AMD silicon

**Host the optimized artifacts · keep the SDK lean · serve the application engineer · stay vertical software**
