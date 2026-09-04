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

## Meet & Greet with AIG-Models Team

### Prateek Prabhanjan's team · [Hyperloom](https://github.com/AMD-AGI/Hyperloom)

**Their work:** Hyperloom — an agentic system that optimizes kernels on AMD HW.
GEAK is the kernel-optimizing part of Hyperloom (other parts create traces, etc.). Today GEAK runs on MI300.

**The two teams are two halves of one pipeline:**

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────┐
│     AIG-Models      │     │        PAVS         │     │    Customers    │
├─────────────────────┤     ├─────────────────────┤     ├─────────────────┤
│ optimize the models │ ──► │ deploy on Edge HW   │ ──► │ edge deployment │
│ kernels,            │     │ GPK, NPU, GPU       │     │ on real robots  │
│ synthetic data      │     │ ROS, robot arm, AMR │     │                 │
└─────────────────────┘     └─────────────────────┘     └─────────────────┘
```

- **AIG-Models~(<span class="violet">AIG-M</span>)** optimize models — Kernel-Optimization, kernel generation, synthetic data Generation, Simulators.
- **PAVS** deployment of platforms & models — Edge HW (GPK, krk2e, PNR), PAI SDK, AMD-ROS, AMD-cUROBO, robot arm, AMR.

**Purpose of this deck:** the topics where the two teams overlap, and how we develop the collaboration.

---

<!-- _class: smallest -->

## Overlap Topics — and How We Develop Each

<div style="font-size:0.8em; margin-bottom:0.4em;"><span class="violet">■ AIG-M (team)</span> &nbsp;&nbsp; <span style="color:#4caf50">■ People on the work</span> &nbsp;&nbsp; <span style="color:#ff9800">■ What AIG-M wants from us</span></div>

<div class="columns">
<div>

**Joint / technical work**

**1. Hyperloom → Edge HW**
- Extend GEAK (today on MI300) to GPK · krk2e · PNR
- Optimize PAI SDK models on GPU + NPU via GEAK
- An optimized NPU model → step toward an NPU-Hyperloom
- <span class="violet">AIG-M</span> to allocate an engineer to on-board us on GEAK
*<span style="color:#4caf50">Amol · Vaibhav · Karthik</span>*

**2. World Action Robotic Models**
- <span class="violet">AIG-M</span> developing & optimizing these now (trending soon)
- PAVS to understand, integrate & benchmark on Edge HW

*<span style="color:#4caf50">Srini · Hari</span>*

**3. Synthetic Data Generation**
- <span class="violet">AIG-M</span> expertise in optimizing Genesis-style simulators
- PAVS robotics / sim-to-real can benefit

*<span style="color:#4caf50">Ravi · Kush · Hari</span>*

**4. Kernel Generation**
- <span class="violet">AIG-M</span> has proposed kernel-generation expertise
- We can explore an MLIR-style optimization library (as in MIGraphX) for NPU

</div>
<div>

**<span style="color:#ff9800">What AIG-M wants from us</span>**

**<span style="color:#ff9800">5. Assets Exchange — schedule a robotics session</span>**
- <span class="violet">AIG-M</span> wants to learn PAVS assets: AMD-ROS pipelines, AMD-cUROBO motion planner
- Set up a walkthrough with the robotics team
- They're interested in latest model development for edge deployment

**<span style="color:#ff9800">6. Customer Gateway — HW access</span>**
- <span class="violet">AIG-M</span> sees PAVS as their gateway to customers
- Share our Edge-HW to benchmark their models
- Run models on our robotic arm & AMR → Exposure feeds into <span class="violet">AIG-M</span>'s R&D.

</div>
</div>
