---
marp: true
paginate: true
footer: '![h:50](./themes/pavs-logo.png)'
style: |
  @import url('status-styles.css');

  section {
    font-family: 'Helvetica', 'Arial', sans-serif;
    padding: 40px 50px 70px 50px;
    overflow: hidden;
    background-color: #1a1a1a;
    color: #ffffff;
  }

  section.small { font-size: 21px; }
  section.smaller { font-size: 19px; }

  section.smallest {
    font-size: 17px;
    padding: 25px 50px 70px 50px;
  }
  section.smallest li { margin-bottom: 0.05em; }
  section.smallest h2 { font-size: 1.35em; margin-bottom: 0.3em; margin-top: 0; }
  section.smallest h3 { font-size: 1.08em; margin-top: 0.2em; margin-bottom: 0.25em; }
  section.smallest ul, section.smallest ol { margin: 0.2em 0; }

  section.compact { font-size: 18px; }

  h1, h2, h3, h4, h5, h6 { color: #ffffff; }

  h1 {
    font-size: 1.8em;
    font-weight: bold;
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.2em;
    margin-bottom: 0.5em;
  }

  h2 { font-size: 1.4em; margin-top: 0; }
  h3 { font-size: 1.1em; color: #aaaaaa; margin-top: 0; }

  table { font-size: 0.85em; width: 100%; background-color: #1a1a1a; }
  th, td { padding: 6px 10px; }
  thead { background-color: #3498db !important; }
  thead th { color: white !important; background-color: #3498db !important; }
  tbody tr:nth-child(odd) { background-color: #2a2a2a; }
  tbody tr:nth-child(even) { background-color: #1a1a1a; }
  td, th { color: #ffffff; }

  ul, ol { margin: 0.3em 0; }
  li { margin-bottom: 0.3em; }

  pre {
    font-size: 0.7em; padding: 10px;
    background-color: #e8e8e8; border-radius: 5px; color: #000000 !important;
  }
  pre code { color: #000000 !important; background-color: transparent; }
  code { background-color: #2a2a2a; color: #00bcd4; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }

  a { color: #00bcd4; }
  strong { color: #3498db; }

  footer { position: absolute; bottom: 20px; left: auto; right: 40px; width: auto; }
  footer img { height: 50px; }

  .success { color: #4caf50; font-weight: bold; }
  .warning { color: #ff9800; font-weight: bold; }
  .violet { color: #9b59b6 !important; }

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

  section.lead {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.lead h1 { border-bottom: none; font-size: 2.2em; }

  .highlight-box {
    background-color: #2a2a2a;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 10px 0;
  }

  .metric-large { font-size: 2.5em; font-weight: bold; color: #4caf50; }
  .metric-label { font-size: 0.9em; color: #888888; }
---

<!-- _class: small -->

## AIG-Models × PAVS — Collaboration Landscape

### Meet & Greet · Prateek Prabhanjan's team · [Hyperloom](https://github.com/AMD-AGI/Hyperloom) — agentic kernel optimization on AMD HW

<div class="columns">
<div>

**What AIG-Models brings**

- **Hyperloom** — automated kernel optimization pipeline on AMD silicon
- **Kernel Generation** expertise (Kush, Ravi)
- **Synthetic Data Generation** — Genesis-style simulators for training
- **World Action Robotic Models** — being developed & optimized now; trending next few months

<div class="highlight-box" style="border-left-color:#9b59b6;">

Deep expertise in model internals: layers, kernels, quantization — and the tooling to automate it.

</div>

</div>
<div>

**What PAVS brings**

- **Edge HW coverage** — GPK, krk2e, PNR (Strix, Krackan, Panther Lake)
- **PAI SDK** — models already packaged and ready for optimization
- **AMD-ROS pipelines** — robotics middleware stack on AMD HW
- **AMD-cUROBO** — motion planning (cuRobo ported to ROCm)
- **AARTS / Vertical Software** — research → production-grade SDK

<div class="highlight-box" style="border-left-color:#4caf50;">

The deployment end: Edge HW, robotics pipelines, and the SDK that ships models to customers.

</div>

</div>
</div>

<div class="highlight-box" style="text-align:center;">
AIG optimizes models. PAVS deploys them. <strong>The two teams are the two halves of the same pipeline.</strong>
</div>

---

<!-- _class: smallest -->

## Four Collaboration Tracks

### Where the teams overlap and what moves next

<div style="display:grid; grid-template-columns:1fr 1fr; gap:1em; margin-top:0.5em;">

<div style="background:#2a2a2a; border:1px solid #3498db; border-radius:8px; padding:12px;">
  <div style="color:#3498db; font-weight:bold; font-size:1.1em; margin-bottom:6px;">① Hyperloom → Edge HW</div>
  <ul style="margin:0; padding-left:1.2em; color:#eee;">
    <li>Extend Hyperloom to <strong style="color:#fff;">GPK · krk2e · PNR</strong></li>
    <li>Start from GEEK system; optimize <strong style="color:#fff;">PAI SDK models</strong> on NPU + GPU</li>
    <li style="color:#aaa; font-size:0.9em;">Amol · Vaibhav · Karthik leading</li>
  </ul>
</div>

<div style="background:#2a2a2a; border:1px solid #4caf50; border-radius:8px; padding:12px;">
  <div style="color:#4caf50; font-weight:bold; font-size:1.1em; margin-bottom:6px;">② World Action Robotic Models</div>
  <ul style="margin:0; padding-left:1.2em; color:#eee;">
    <li>AIG developing & optimizing <strong style="color:#fff;">World Action models</strong> now</li>
    <li>Integrate and <strong style="color:#fff;">benchmark on Edge HW</strong> (GPU · NPU)</li>
    <li style="color:#aaa; font-size:0.9em;">Srini leading integration from PAVS side</li>
  </ul>
</div>

<div style="background:#2a2a2a; border:1px solid #ff9800; border-radius:8px; padding:12px;">
  <div style="color:#ff9800; font-weight:bold; font-size:1.1em; margin-bottom:6px;">③ Synthetic Data & Kernel Gen</div>
  <ul style="margin:0; padding-left:1.2em; color:#eee;">
    <li>AIG running <strong style="color:#fff;">Genesis-style simulators</strong> for synthetic data</li>
    <li>PAVS robotics / sim-to-real work can <strong style="color:#fff;">directly benefit</strong></li>
    <li style="color:#aaa; font-size:0.9em;">Kush · Ravi (AIG) — connect with PAVS sim team</li>
  </ul>
</div>

<div style="background:#2a2a2a; border:1px solid #9b59b6; border-radius:8px; padding:12px;">
  <div style="color:#9b59b6; font-weight:bold; font-size:1.1em; margin-bottom:6px;">④ Assets Exchange — Kick-off Session</div>
  <ul style="margin:0; padding-left:1.2em; color:#eee;">
    <li>AIG wants to learn: <strong style="color:#fff;">AMD-ROS</strong> pipelines, <strong style="color:#fff;">AMD-cUROBO</strong> motion planner</li>
    <li>PAVS assets from <strong style="color:#fff;">PAVS model zoo</strong> for AIG model dev</li>
    <li style="color:#aaa; font-size:0.9em;">Action: schedule robotics kick-off session</li>
  </ul>
</div>

</div>

<div class="highlight-box" style="text-align:center; margin-top:0.8em;">
<strong>Near-term action:</strong> Amol/Vaibhav/Karthik start Hyperloom on GPK · Srini aligns on World Action models · Schedule robotics assets session with AIG
</div>
