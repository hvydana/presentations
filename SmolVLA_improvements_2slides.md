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

<!-- _class: small -->

## Optimization Sequence — Throughput & Accuracy Journey

### Step-by-step changes on SmolVLA + LeRobot (GPU / Strix)

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Step</th>
      <th>What changed</th>
      <th>Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><strong>Diffusion steps ↓</strong></td>
      <td>Reduced denoising steps <strong>30 → 2</strong> (extra steps shown unnecessary)</td>
      <td>2 → <span class="success">4.5–5 inf/s</span></td>
    </tr>
    <tr>
      <td>2</td>
      <td><strong>torch.compile</strong></td>
      <td>Rewrote LeRobot SmolVLA modules so the full flow forms a single graph → optimized GPU kernels</td>
      <td>→ <span class="success">8.5 inf/s</span></td>
    </tr>
    <tr>
      <td>3</td>
      <td><strong>fp32 → fp16</strong></td>
      <td>Cast weights to fp16 <em>before</em> compile so the graph has no up/down-scale ops around each layer</td>
      <td>→ <span class="success">13–15 inf/s</span></td>
    </tr>
    <tr>
      <td>4</td>
      <td><strong>RTC on (Real-Time Chunking)</strong></td>
      <td>Camera pipeline + model run on parallel threads sharing the GPU → reactive end-to-end pipeline</td>
      <td>Reactivity ↑</td>
    </tr>
    <tr>
      <td>5</td>
      <td><strong>chunk_size_threshold ↓</strong></td>
      <td>Next inference triggered after only <strong>5</strong> consumed actions → fresher images drive predictions</td>
      <td>Reactivity ↑</td>
    </tr>
    <tr>
      <td>6</td>
      <td><strong>Action smoothing</strong></td>
      <td>Post-processing removes jitter/shake in continuous-action output</td>
      <td>Smoothness ↑</td>
    </tr>
    <tr>
      <td>7</td>
      <td><strong>More data + fine-tune</strong></td>
      <td>Scaled training data and fine-tuned model</td>
      <td>MAE <span class="success">6 → ~3</span></td>
    </tr>
  </tbody>
</table>

<div class="highlight-box">
<strong>Bottom line:</strong> <span class="success">~7× throughput</span> (2 → 13–15 inf/s) and <span class="success">~50% lower MAE</span> (6 → ~3, usable limit ~3.5) — model is now usable for live gesture mimic on Strix.
</div>

---

<!-- _class: small -->

## Throughput → Accuracy Coupling

### Faster model = more accurate, more responsive robot

<div class="columns">
<div>

**Why a slow model hurts accuracy**

- **Drops camera frames** → operator ↔ robot sync is lost.
- Forced to predict **far into the future** from stale observations — long-horizon predictions are inherently unreliable.
- Lag accumulates → robot mimics what the operator did *seconds ago*.

</div>
<div>

**Why a fast model is more accurate**

- Consumes **every fresh frame** from the camera stream.
- New predictions **overwrite** old ones, always grounded in current state → less guessing.
- Short, reliable horizons → tighter operator ↔ robot sync.

</div>
</div>

<div class="highlight-box">
<strong>Key insight for leadership:</strong> throughput is not just speed — it directly raises <strong>behavioral accuracy</strong> by keeping predictions grounded in the latest observation.
</div>