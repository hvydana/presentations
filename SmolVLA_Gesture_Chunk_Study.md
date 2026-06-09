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

  section::after {
    content: '';
    display: block;
    height: 40px;
  }

  section.small  { font-size: 21px; }
  section.smaller { font-size: 19px; }

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

  table {
    font-size: 0.9em;
    width: 100%;
    background-color: #1a1a1a;
  }
  th, td { padding: 6px 10px; }
  thead { background-color: #3498db !important; }
  thead th { color: #000000 !important; background-color: #3498db !important; }
  tbody tr:nth-child(odd) { background-color: #2a2a2a; }
  tbody tr:nth-child(even) { background-color: #1a1a1a; }
  td, th { color: #ffffff; }

  ul, ol { margin: 0.3em 0; }
  li { margin-bottom: 0.3em; }

  pre {
    font-size: 0.75em;
    padding: 10px;
    background-color: #e8e8e8;
    border-radius: 5px;
    color: #000000 !important;
  }
  pre code { color: #000000 !important; background-color: transparent; }
  code {
    background-color: #2a2a2a;
    color: #00bcd4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
  }

  a { color: #00bcd4; }
  strong { color: #3498db; }

  footer { position: absolute; bottom: 20px; left: auto; right: 40px; width: auto; }
  footer img { height: 50px; }

  .success { color: #4caf50; font-weight: bold; }
  .warning { color: #ff9800; font-weight: bold; }

  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5em;
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
---

<!-- _class: lead -->

# SmolVLA — Gesture Mimic Training
## Chunk-size vs. Accuracy / Throughput Study

Hari Krishna Vydana

---

<!-- _class: small -->

## Setup

### Training & Evaluation Data

**Combined dataset — 3 sources @ 30 fps** (train + held-out test, disjoint)

<table>
  <thead>
    <tr>
      <th rowspan="2">Dataset (human position)</th>
      <th colspan="2" style="text-align:center;">Train set</th>
      <th colspan="2" style="text-align:center;">Test set (held-out)</th>
    </tr>
    <tr>
      <th style="text-align:right;">Episodes</th>
      <th style="text-align:right;">Frames</th>
      <th style="text-align:right;">Episodes</th>
      <th style="text-align:right;">Frames</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>multigesture_mimic</code> — <em>sitting pose</em></td>
      <td style="text-align:right;">39</td>
      <td style="text-align:right;">15,015</td>
      <td style="text-align:right;">10</td>
      <td style="text-align:right;">3,868</td>
    </tr>
    <tr>
      <td><code>extended_gesture_mimic</code> — <em>standing pose</em></td>
      <td style="text-align:right;">35</td>
      <td style="text-align:right;">20,787</td>
      <td style="text-align:right;">9</td>
      <td style="text-align:right;">5,346</td>
    </tr>
    <tr>
      <td><code>Action-per-video-…clean</code> — <em>one action / video</em> (80/20 split, seed 42)</td>
      <td style="text-align:right;">315</td>
      <td style="text-align:right;">75,446</td>
      <td style="text-align:right;">79</td>
      <td style="text-align:right;">18,930</td>
    </tr>
    <tr>
      <td><strong>Total</strong></td>
      <td style="text-align:right;"><strong>389</strong></td>
      <td style="text-align:right;"><strong>111,248</strong></td>
      <td style="text-align:right;"><strong>98</strong></td>
      <td style="text-align:right;"><strong>28,144</strong></td>
    </tr>
  </tbody>
</table>

**Model:** SmolVLA &nbsp;|&nbsp; **Training:** `chunk_size=50`, `n_action_steps=10`, bf16, batch 64, lr 5e-6, 30 k steps, RTC on (`exec_horizon=10`) &nbsp;|&nbsp; Dataset 3: 56 bad episodes removed before split.

**Sweep variable:** parallel actions per inference call *k* ∈ {1, 2, 4, 6, 8, 10, 12, 14} — controls **throughput ↔ accuracy** trade-off.

---

<!-- _class: small -->

## Accuracy vs. Action-Chunk Size

### Mean MAE per test set (lower is better) — checkpoint 030000

| Actions / step (k) | multi-gesture | eep it | action-per-episode |
|:---:|:---:|:---:|:---:|
|  1 | **1.75** | **2.57** | **1.99** |
|  2 | **1.83** | **2.56** | **2.15** |
|  4 | **1.92** | **2.76** | **2.32** |
|  6 | **2.02** | **2.93** | **2.46** |
|  8 | **2.13** | **3.10** | **2.57** |
| 10 | **2.18** | **3.28** | **2.72** |
| 12 | **2.29** | **3.44** | **2.78** |
| 14 | **2.33** | **3.66** | **2.85** |

<div class="highlight-box">

**Observation:** Trained with chunk = **10**, evaluated with smaller *k* → <span class="success">better accuracy</span> (easier task than training).
Larger *k* (12, 14) extrapolates beyond training horizon → <span class="warning">accuracy degrades</span>. Higher *k* still gives better **throughput** (more actions / inference).

</div>


---

<!-- _class: small -->

## Past Delivery vs Current Model — *extended multi-gesture*

### Mean MAE on `extended_gesture_mimic` held-out test set

| Actions / step (k) | Past delivery <br/>`smolvla-multigesture-val` <br/>(ckpt 010000) | Current model <br/>`smolvla-gesture3-trainall-evaltest` <br/>(ckpt 030000) |
|:---:|:---:|:---:|
|  1 | — | **2.57** |
|  2 | — | **2.56** |
|  4 | — | **2.76** |
|  6 | — | **2.93** |
|  8 | — | **3.10** |
| 10 | **5.39** | **3.28** |
| 12 | — | **3.44** |
| 14 | — | **3.66** |

<div class="highlight-box">

**Observation:** Current model (combined training, ckpt 030000) cuts MAE on `extended_gesture_mimic` from **5.39 → 3.28** at *k* = 10 — a <span class="success">~39% reduction</span> over the past delivery.

</div>

---

<!-- _class: small -->

## Possible Next attempt: Train with Larger Chunks

### Why push the training chunk beyond 10?

<div class="columns">
<div>

**Current state (chunk = 10)**

- Eval with *k* < 10 → easy, better accuracy
- Eval with *k* > 10 → unseen horizon, accuracy drops
- Throughput is capped by **k = 10** for safe accuracy

**Hypothesis**

- Train with **larger chunk** (e.g. 16 / 20)
- Then chunk = 10 at inference becomes an **easier** sub-task
- Expect: <span class="success">same-or-better accuracy at k = 10</span> with <span class="success">higher throughput headroom</span>

</div>
<div>

**Throughput math (Strix, bf16)**

| Quantity | Value |
|---|---|
| Inference rate (model)    | **2.3 inf / sec** |
| Actions per inference (k) | **10**           |
| Effective action rate     | **23 actions / sec** |

**Next experiments**

- Retrain with chunk ∈ {16, 20}
- Re-run the k-sweep on all 3 held-out test sets
- Verify: at *k* = 10, accuracy ≥ current chunk-10 model
- Then push *k* higher to trade marginal accuracy for throughput

<div class="highlight-box">
<span class="success">Goal:</span> decouple <strong>training horizon</strong> from <strong>inference chunk</strong> — train hard, infer fast.
</div>

</div>
</div>

---

<!-- _class: small -->

## Take-Home Message

- SmolVLA trained on **combined** (multi-gesture + extended + action-per-episode) data, chunk = 10.
- Held-out evaluation across all 3 sources; **k-sweep** shows the expected pattern: <span class="success">smaller k → better accuracy</span>, <span class="warning">larger k → faster but less accurate</span>.
- **Next step:** train with a **larger chunk** so that *k* = 10 at inference is well inside the training distribution → preserve accuracy while unlocking higher action throughput on Strix (currently 23 actions/sec @ k = 10, bf16).
