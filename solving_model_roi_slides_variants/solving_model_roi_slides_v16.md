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

# Solving the Model Gap

## Why does cheaper, better silicon not win by itself?

**AMD-Sourcing the Engineering Cycles to Close NVIDIA's Physical-AI Lead -- A proposal**

---

<!-- _class: small -->

## 1 · The Paradox We Keep Hitting in Sales

### We Win the Spec Sheet and Lose the Deal

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">The customer never disputes the economics — he refuses because the decision was made above the silicon.</div>

<div class="columns">
<div>

**AMD hardware wins on economics**

- **~50% lower capex** and **~30% lower opex** vs the incumbent (on the right criteria)
- Competitive silicon: MI300X **5.3 TB/s** HBM3, Ryzen AI edge, Kria deterministic control

<div class="highlight-box" style="border-left-color:#4caf50;">
On price-performance, we may have/reach a real, quantifiable advantage.
</div>

</div>
<div>

**…yet the application developer still says "no"**

- His product is already built **around NVIDIA's models and pipelines**
- Switching means **re-engineering the whole stack** — a cost *he* has to pay
- The better chip **never gets a fair evaluation**

<div class="highlight-box" style="border-left-color:#e05555;">
We lose the deal <strong>before</strong> hardware economics enter the conversation.
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.2em; font-weight:bold; color:#4aa3ff;">The barrier is not the silicon — it's the <span style="color:#4caf50;">ecosystem the customer has already built on top of NVIDIA.</span></span>
</div>

---

<!-- _class: small -->

## 2 · NVIDIA's Moat Is Software, Not the Chip

### A Decade of Models Turned Into a Vertically Integrated Stack


<div class="columns" style="grid-template-columns: 1.4fr 1fr; align-items:center;">
<div>

![w:560](./model_zoo/Nvidia-model-zoo.png)

<div style="font-size:0.8em; color:#888; text-align:center;">NGC Catalog — years of curated, prepackaged, ready-to-run models</div>

</div>
<div>

**The lock-in is measurable**

- **~80% ecosystem, ~20% hardware** — NVIDIA's own default status
- **2M+ robotics developers**, **4M CUDA developers**, **7+ year** head start
- **Isaac Sim** leads robotics job postings — **50% more** than the closest competitor
- **1,228 VLA papers** at ICLR 2026 → **zero** mention ROCm

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">Models → TensorRT → Isaac ROS → cuRobo → Isaac Sim → Cosmos — <span style="color:#4caf50;"> where each layer locks in the next — and locks AMD out.</span></span>
</div>

---

<!-- _class: small -->

## 3 · The Switching Cost Is the Real Barrier

### The Customer Would Take Cheaper Hardware — but He Pays the Switching Bill

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">Every engineering cycle spent re-hosting on AMD is capex the customer must justify before he saves a cent.</div>

<div class="columns">
<div>

**Why the customer stays put**

- Years of infra, pipelines, and applications built on NVIDIA models
- Rebuilding fleet/deployment infra: **6–18 engineer-months per deployment**
- **5–7 deployment artifacts per model** to re-target hardware
- Even hardware-competitive rivals face a **12–24 month** software catch-up

</div>
<div>

**The burden lands hardest where we want to win**

<div style="display:flex; flex-direction:column; gap:6px; margin-top:4px;">
  <div style="background:#3a1e1e; border:1px solid #e05555; border-radius:6px; padding:8px 12px;"><strong style="color:#ff8a8a;">Small / mid-size robotics companies</strong><br><span style="font-size:0.88em; color:#ccc;">every engineering cycle is capex they cannot spare</span></div>
  <div style="color:#e05555; text-align:center; font-size:1.2em;">&#8595;</div>
  <div style="background:#333; border:1px dashed #888; border-radius:6px; padding:8px 12px; color:#ccc;">They keep buying the more expensive chip — because <strong style="color:#fff;">switching costs more than it saves</strong></div>
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">This is the <span style="color:#4caf50;">soft-power gap</span> — AMD is absent from every on-ramp above the compute layer, and it shows up directly in <span style="color:#4caf50;">sales.</span></span>
</div>

---

<!-- _class: small -->

## 4 · The Internal Problem: ROI Can't Be Justified Overnight

### The Gap Is Known and Winnable — But ROI can not be defended

<!--<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">A multi-year, iterative gap cannot be booked as near-term ROI — so every business unit is rational to pass.</div>-->

<div class="columns">
<div>

**How AMD is structured**

- Many business units — each funded by its **own sales / engineering output**
- Every unit must **defend the returns** on what it takes on

**Why no single unit picks this up**

- Model training is **iterative and continual** — not a one-shot deliverable
- A **multi-year ecosystem gap** cannot be closed overnight
- ROI in a fixed window is **hard to measure and harder to justify**

</div>
<div>

<div style="border:2px solid #ff9800; border-radius:8px; padding:14px; background:#202020;">
  <div style="text-align:center; font-weight:bold; color:#ff9800; margin-bottom:10px;">The Deadlock</div>
  <div style="display:flex; flex-direction:column; gap:8px; font-size:0.9em;">
    <div style="background:#2a2a2a; border-radius:5px; padding:8px 10px;">Gap is <strong style="color:#fff;">large</strong> &amp; the payoff is <strong style="color:#fff;">long-horizon</strong></div>
    <div style="text-align:center; color:#ff9800;">&#8595;</div>
    <div style="background:#2a2a2a; border-radius:5px; padding:8px 10px;">No BU can <strong style="color:#fff;">book near-term ROI</strong></div>
    <div style="text-align:center; color:#ff9800;">&#8595;</div>
    <div style="background:#2a2a2a; border-radius:5px; padding:8px 10px;">So <strong style="color:#fff;">nobody starts</strong> — and the gap widens</div>
  </div>
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">A multi-year, iterative gap cannot be booked as near-term ROI — so every business unit is rational to pass.</span>
</div>

---

<!-- _class: small -->

## 5 · The Insight: The Target Is Already Known

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">When the models and target numbers are published, closing the gap becomes bounded, measurable work.</div>

<div class="columns">
<div>

**Unlike open-ended research, we are not searching**

- The **models are named** and mostly **open** (NGC is a public map)
- The **target performance is published** — we know exactly what "done" looks like
- This is a **replication problem**, not an invention problem
- The **replication problem**, can be solved at scale

<div class="highlight-box" style="border-left-color:#4caf50;">
Producing a replica of a known target is <strong>bounded, measurable work</strong> — the ROI objection shrinks.
</div>

</div>
<div>

**Only two pieces are missing**

<div style="display:flex; flex-direction:column; gap:8px; margin-top:4px;">
  <div style="background:#1e3a2a; border:1px solid #4caf50; border-radius:6px; padding:10px 12px;"><strong style="color:#4caf50;">Compute — we already have it</strong><br><span style="font-size:0.88em; color:#ccc;">AMD-wide clusters (ALOLA &amp; others); PAVS can broker access</span></div>
  <div style="background:#3a2f1e; border:1px solid #ff9800; border-radius:6px; padding:10px 12px;"><strong style="color:#ff9800;">Data — the real problem to solve</strong><br><span style="font-size:0.88em; color:#ccc;">the "1M open episodes vs trillions of tokens" gap in physical AI</span><br><span style="font-size:0.85em; color:#aaa;">Close it with <strong style="color:#fff;">synthetic generation</strong> · <strong style="color:#fff;">pooled + curated open data</strong> · <strong style="color:#fff;">semi-supervised for the task</strong> · <strong style="color:#fff;">pseudo-labels from large OSS models</strong> · &amp; more</span></div>
</div>

<div class="highlight-box">
Known target + available compute → the task collapses to <strong>solving the data problem at scale</strong>.
</div>

</div>
</div>


---

<!-- _class: small -->

## 6 · The Proposal: An AMD-Wide Model Training Challenge

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">Convert one multi-year bill into a cohort of motivated engineers, pointed at a scored target.</div>

<div style="display:flex; align-items:stretch; justify-content:center; gap:8px; margin:10px 0;">
  <div style="background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:10px 14px; text-align:center; width:150px;"><strong style="color:#5dade2;">Pick a target model</strong><br><span style="font-size:0.82em; color:#ccc;">from the known NGC-parallel set</span></div>
  <div style="display:flex; align-items:center; color:#3498db; font-weight:bold;">&#8594;</div>
  <div style="background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:10px 14px; text-align:center; width:150px;"><strong style="color:#5dade2;">Train on AMD compute</strong><br><span style="font-size:0.82em; color:#ccc;">clusters PAVS brokers</span></div>
  <div style="display:flex; align-items:center; color:#3498db; font-weight:bold;">&#8594;</div>
  <div style="background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:10px 14px; text-align:center; width:150px;"><strong style="color:#5dade2;">Climb the leaderboard</strong><br><span style="font-size:0.82em; color:#ccc;">per-model webpage</span></div>
  <div style="display:flex; align-items:center; color:#4caf50; font-weight:bold;">&#8594;</div>
  <div style="background:#1e3a2a; border:1px solid #4caf50; border-radius:6px; padding:10px 14px; text-align:center; width:160px; color:#fff;"><strong style="color:#4caf50;">PAVS validates &amp; publishes</strong><br><span style="font-size:0.82em; color:#ccc;">top 3–4 teams per model</span></div>
</div>

<div class="columns">
<div>

**The mechanics**

- A **leaderboard per model** (grouped: perception · manipulation · VLA · SLAM …)
- A **webpage** tracking the top teams and their models
- Each **new #1 notifies every participant** — winner + solution shared — keeping the field competitive
- **Top 3–4 teams** get to **publish their work** under AMD
- PAVS **reproduces and certifies** the model + performance

</div>
<div>

**Why a challenge, not a hire**

- Taps **latent enthusiast engineering** across all of AMD
- Converts a **multi-year gap** into **many parallel short sprints**
- No single BU carries the bill — the org **contributes cycles**

</div>
</div>

</div>

---

<!-- _class: smallest -->

## 7 · Challenges Have Closed Big Capability Gaps Before

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">We're not guessing this works — a scored, public target has repeatedly closed gaps no single roadmap could.</div>

<div class="columns-3">
<div>

<div style="background:#2a2a2a; border:1px solid #3498db; border-radius:8px; padding:12px; height:100%;">
<div style="color:#5dade2; font-weight:bold; font-size:1.1em;">ImageNet Challenge</div>

- A **public leaderboard** on a known target
- Sparked **AlexNet** and the deep-learning era
- A benchmark did what no single lab's roadmap could

</div>

</div>
<div>


<div style="background:#2a2a2a; border:1px solid #4caf50; border-radius:8px; padding:12px; height:100%;">
<div style="color:#4caf50; font-weight:bold; font-size:1.1em;">DARPA Grand Challenge</div>

- A **prize + leaderboard** for autonomous driving
- Year 1: nobody finished. Year 2: **multiple teams did**
- Seeded the entire self-driving industry

</div>

</div>
<div>

<div style="background:#2a2a2a; border:1px solid #9b59b6; border-radius:8px; padding:12px; height:100%;">
<div style="color:#b07cc6; font-weight:bold; font-size:1.1em;">Kaggle / Netflix Prize</div>

- **Crowdsourced** solutions to a fixed, scored target
- Outperformed in-house teams at a **fraction of the cost**
- Recognition — not salary — drove the effort

</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.1em; font-weight:bold; color:#ffffff;"><em>"The right challenge stimulates the right engineer."</em> — a scored, public target <span style="color:#4caf50;">closes gaps faster than any single funded roadmap.</span></span>
</div>

---

<!-- _class: small -->

## 8 · The Target Set Is Open — and Achievable

### The Models Are Open, the Datasets Exist, the Data Scales Cheaply

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">One AMD alternative per NGC model — the perception + manipulation set Isaac ROS consumes — each with an open replica to train.</div>

<div class="columns">
<div>

**One replica per NGC / Isaac ROS model**

| Isaac ROS model (NGC) | Open replica to train on AMD |
|---|---|
| Detection — PeopleNet / DetectNet | **YOLOv12 · RT-DETR** |
| Segmentation — PeopleSemSegNet | **SegFormer · U-Net** |
| Stereo depth — ESS | **RAFT-Stereo · HITNet** |
| 6-DoF pose — FoundationPose / DOPE | **FoundationPose · MegaPose** |
| Visual SLAM — cuVSLAM | **ORB-SLAM3** |
| Manipulation / VLA — GR00T / pi0 | **OpenVLA · SmolVLA** |

<div class="highlight-box" style="border-left-color:#4caf50;">
Each replica drops into **AMD-ROS / AARTS** — our Isaac ROS-equivalent consumption layer.
</div>

</div>
<div>

**The models are reachable, the data exists**

- **OpenVLA** fine-tunes on **1× A100 in <24h**; **SmolVLA** needs **50× less** compute
- **Perception** — COCO · KITTI · nuScenes public benchmarks
- **Manipulation** — Open X-Embodiment (1.4M episodes) · LeRobot (58k datasets)
- Synthetic data is **50–70× cheaper** than real-world capture
- The challenge lets **many teams attack the data problem in parallel**

<div class="highlight-box" style="border-left-color:#4caf50;">
Each NGC model has a <strong>concrete, scored finish line</strong> — replicate it, hit the target on AMD.
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">The pieces already exist — what's missing is <span style="color:#4caf50;">organized, incentivized effort pointed at AMD silicon.</span></span>
</div>

---

<!-- _class: smallest -->

## 9 · Incentive Design — Everyone Wins

### A Challenge Only Works if Every Party Wins by Playing — Here, Three Do

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">The engineer, PAVS, and AMD each get something they want — which is why the mechanism sustains itself.</div>

<div class="columns-3">
<div>

<div style="background:#1e3a2a; border:1px solid #4caf50; border-radius:8px; padding:12px; height:100%;">
<div style="color:#4caf50; font-weight:bold; font-size:1.15em; margin-bottom:6px;">Participant (Engineer)</div>

- **Recognition** — publish work, top-team webpage
- A **countable contribution to AMD** for their record
- An **extra purpose &amp; goal** alongside the day job
- Enthusiast hours become **productive output**

</div>

</div>
<div>

<div style="background:#1e3a5f; border:1px solid #3498db; border-radius:8px; padding:12px; height:100%;">
<div style="color:#5dade2; font-weight:bold; font-size:1.15em; margin-bottom:6px;">Organizer (PAVS)</div>

- Becomes the **customer gateway** to physical AI across AMD
- Reproducing models **builds working ties** across many teams
- A **niche — but the lead player** in that niche
- **Bridges the islands** of physical AI at AMD

</div>

</div>
<div>

<div style="background:#3a2f1e; border:1px solid #ff9800; border-radius:8px; padding:12px; height:100%;">
<div style="color:#ff9800; font-weight:bold; font-size:1.15em; margin-bottom:6px;">AMD (Org)</div>

- The **ecosystem gap closes fast** — target is known
- A growing **pool of curated datasets** — one team's data &amp; models **catalyze the next**
- **Idle compute** (ALOLA &amp; others) gets **popularized**
- A pipeline of **market-ready, AMD-native models**
- Engagement without a **single-BU budget line**

</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">One mechanism, three winners — which is why a crowdsourced challenge is <span style="color:#4caf50;">self-sustaining, not a one-off spend.</span></span>
</div>

---

<!-- _class: small -->

## 10 · PAVS as the Customer Gateway to Physical AI

### Organizing the Challenge Isn't Overhead — It's How PAVS Earns Its Position

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">Reproducing and routing every winning model is exactly what makes PAVS the gateway physical AI flows through.</div>

<div class="columns">
<div>

**What PAVS commits to**

- Send an **org-wide call** for the right technical solutions
- The right solution that reaches us → **we help take it to market**
- **Reproduce, evaluate, and certify** each model + its performance
- Curate the leaderboard and the **model webpage**

</div>
<div>

**What that makes PAVS**

<div style="display:flex; flex-direction:column; align-items:center; gap:6px; margin-top:4px;">
  <div style="background:#1e3a2a; border:1px solid #4caf50; border-radius:6px; padding:8px 14px; width:92%; text-align:center;"><strong style="color:#4caf50;">The gateway</strong> — every physical-AI solution enters through PAVS</div>
  <div style="color:#3498db; font-size:1.2em;">&#8595;</div>
  <div style="background:#1e3a5f; border:1px solid #3498db; border-radius:6px; padding:8px 14px; width:92%; text-align:center;"><strong style="color:#5dade2;">The bridge</strong> — connecting the islands of physical AI across AMD</div>
  <div style="color:#3498db; font-size:1.2em;">&#8595;</div>
  <div style="background:#1e3a2a; border:1px solid #4caf50; border-radius:6px; padding:8px 14px; width:92%; text-align:center; color:#fff;"><strong style="color:#4caf50;">The lead player</strong> in a well-defined niche</div>
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">The organizing work is not overhead — it's how PAVS <span style="color:#4caf50;">earns the relationships and the position to route physical AI to market on AMD.</span></span>
</div>

---

<!-- _class: small -->

## 11 · An Enormous Market — The Prize Is Worth the Effort

<div style="font-size:0.95em; color:#00bcd4; font-style:italic; margin:-0.2em 0 0.5em;">A drop-in AMD replica per NGC model turns a costly migration into a seamless switch — and unlocks the customers already locked in.</div>

<div class="columns-3">
<div>

<div style="text-align:center;">
<div class="metric-large">$200B</div>
<div class="metric-label">AMD's own projection for the physical-AI silicon market by 2035</div>
</div>

</div>
<div>

<div style="text-align:center;">
<div class="metric-large">$22.2B</div>
<div class="metric-label">robotics startup funding in 2025 — up 69% YoY; the buyers of tomorrow are forming now</div>
</div>

</div>
<div>

<div style="text-align:center;">
<div class="metric-large">0</div>
<div class="metric-label">of 1,228 VLA papers at ICLR 2026 mention ROCm — the on-ramp is wide open to claim</div>
</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
<span style="font-size:1.15em; font-weight:bold; color:#4aa3ff;">Make the transfer seamless and AMD's price-performance is finally evaluated — <span style="color:#4caf50;">the cheaper stack wins the deals it loses today.</span></span>
</div>

---

<!-- _class: smallest -->

# The Ask

### The plan is already staffed — we only need the mandate to start

<div class="columns" style="grid-template-columns: 1fr 1.15fr; align-items:start;">
<div>

**What we need from leadership**

<div class="highlight-box" style="border-left-color:#4caf50;">
An <strong>org-wide email</strong> endorsing the challenge — the signal that gives the effort <strong>traction</strong>.
</div>

![w:260](./contibutors/Upperlevel_management.png)

<div style="font-size:0.82em; color:#888;">The push </div>

</div>
<div>

**Already staffed &amp; committed — <span style="color:#4caf50;">execution is ready</span>**

<div style="font-size:0.92em; color:#5dade2; font-weight:bold; margin-bottom:2px;">Compute — grants cluster access (ALOLA &amp; AMD-wide)</div>

![w:320](./contibutors/mathew.png)

<div style="font-size:0.92em; color:#5dade2; font-weight:bold; margin:5px 0 2px;">Per-model GitHub — creates the per-model repos</div>

![w:320](./contibutors/Bharat.png)

<div style="font-size:0.92em; color:#5dade2; font-weight:bold; margin:5px 0 2px;">Team to drive the work </div>

![w:270](./contibutors/Team_participation.png)

</div>
</div>

<div class="highlight-box" style="text-align:center; margin-top:6px;">
<span style="font-size:1.1em; font-weight:bold; color:#4aa3ff;">Known target · staffed team · available compute — <span style="color:#4caf50;">all that's missing is the go-ahead.</span></span>
</div>