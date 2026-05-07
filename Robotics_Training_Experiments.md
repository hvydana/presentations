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

  section.small {
    font-size: 21px;
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

  ul, ol {
    margin: 0.3em 0;
  }

  li {
    margin-bottom: 0.3em;
  }

  code {
    background-color: #2a2a2a;
    color: #00bcd4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
  }

  a {
    color: #00bcd4;
  }

  strong {
    color: #3498db;
  }

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

  .success {
    color: #4caf50;
    font-weight: bold;
  }

  .warning {
    color: #ff9800;
    font-weight: bold;
  }

  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5em;
  }

  .highlight-box {
    background-color: #2a2a2a;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 10px 0;
  }

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

  .video-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .video-cell {
    text-align: center;
  }

  .video-cell video {
    border: 2px solid #3498db;
    border-radius: 4px;
  }

  .video-label {
    font-size: 0.85em;
    color: #aaaaaa;
    margin-top: 4px;
  }

---

<!-- _class: smallest -->

## Joint Trajectories — GT vs Predicted

### Episode 60 | SO-101 Red Cube Green Cloth (3 Cams) | MAE = 1.9988

<div class="columns">
<div>

**All Joints — Overlay**

![w:540](./vedios/episode_60.png)

All 6 joints (shoulder, elbow, wrist, gripper) plotted together — solid = GT, dashed = predicted

</div>
<div>

**Per-Joint Breakdown**

![w:480](./vedios/episode_60_detailed.png)

Individual MAE per joint — shoulder_pan: 1.68, shoulder_lift: 3.01, elbow_flex: 2.76, wrist_flex: 1.20, wrist_roll: 1.80, gripper: 1.55

</div>
</div>

<div class="highlight-box">

<span class="success">Predicted trajectories closely track ground truth across all joints</span> — largest error on shoulder_lift (MAE 3.01), tightest on wrist_flex (MAE 1.20)

</div>

---

<!-- _class: smallest -->

## Training Progress — Policy Improvement Over Time

### SO-101 Task Execution: April 28 → May 2, 2026

<div class="video-grid">
<div class="video-cell">

<video src="./vedios/28_04_2026.mp4" width="440" controls></video>

<div class="video-label"><strong>April 28</strong> — Baseline</div>

</div>
<div class="video-cell">

<video src="./vedios/29_04_2026.mp4" width="440" controls></video>

<div class="video-label"><strong>April 29</strong> — Day 2</div>

</div>
<div class="video-cell">

<video src="./vedios/30_04_2026.mp4" width="440" controls></video>

<div class="video-label"><strong>April 30</strong> — Day 3</div>

</div>
<div class="video-cell">

<video src="./vedios/02_05_2026.mp4" width="440" controls></video>

<div class="video-label"><strong>May 2</strong> — Latest</div>

</div>
</div>

<div class="highlight-box">

<span class="success">Progressive improvement visible across iterations</span> — from initial baseline (Apr 28) to refined policy execution (May 2)

</div>
