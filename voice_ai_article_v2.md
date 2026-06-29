# Voice AI: The $47 Billion Revolution Reshaping Business — and What AMD Can Do About It

*A Techno-Business Analysis | June 2026*

---

## Article Direction Map

| # | Direction | One-line Question |
|---|-----------|-------------------|
| 1 | **Market Landscape** | How big is it, who's in it, what's the growth story? |
| 2 | **Application Verticals** | Where is voice AI being used and which sectors benefit most? |
| 3 | **Business Impact & ROI** | How does it save money — with real numbers? |
| 4 | **Tech Stack Deep Dive** | What are all the layers and how do they connect? |
| 5 | **Cost Anatomy** | Where does the money go — which layer is the most expensive? |
| 6 | **Open-Source Stack** | What can you build for free — and what are the real trade-offs? |

---

## 1. The Market Landscape: From Whisper to Commotion

Voice AI crossed the threshold from novelty to critical infrastructure. The numbers make this plain:

| Metric | Value |
|--------|-------|
| Global voice recognition market (2025) | **$18.39 billion** |
| Global voice recognition market (2031) | **$61.71 billion** at 22% CAGR |
| AI voice agents market (2024) | $2.4 billion |
| AI voice agents market (2034) | **$47.5 billion** at 35% CAGR |
| VC funding into voice AI (2025) | **$2.1 billion** — 8× the 2022 level |
| VC funding already in 2026 | **$559 million** — 68% above 2025 pace |
| YoY growth in production deployments | **340%** across 500+ organizations |
| Median end-to-end response latency (2026) | **680ms** (was 1,200ms in 2024) |
| Builders actively building agents (not just researching) | **87.5%** |
| Businesses planning voice AI in customer service by 2026 | **80%** |


---

## 2. Application Verticals: Where Voice AI Is Being Deployed

### 2.1 Banking, Financial Services & Insurance (BFSI) — 32.9% Market Share

BFSI is the largest adopter globally. Key use cases:

- **Multilingual IVR**: natural conversation replacing touch-tone menus
- **Lead qualification**: India case — cost dropped from ₹800 to ₹120 per lead (85% reduction)
- **Loan processing**: voice-guided applications in regional languages
- **Fraud detection**: voice biometrics to verify caller identity in real time
- **Policy renewals & KYC**: automated reminders at scale
- **Debt collection**: AI calling restricted 8 AM–7 PM, with grievance redressal built in

**Real deployments (India):** HDFC, ICICI, Bank of Baroda, IDFC First (via Gnani.ai). Gnani processes **30M+ daily voice AI conversations** for Indian financial enterprises. Gnani.ai's voice foundation model (14B parameters) handles **10 million daily interactions** for Indian banks with speech-to-speech capability.

57% of Indian BFSI institutions use voice analytics to track interaction patterns.

### 2.2 Healthcare — Fastest Growing at 37.79% CAGR

- Appointment scheduling (reducing no-shows 30–40%)
- Post-discharge follow-ups at scale
- Clinical documentation — physicians speak, notes write themselves
- Patient triage and multilingual intake before routing
- Pharmacy refill reminders

70% of healthcare organizations credit voice AI with measurable operational improvements.

### 2.3 Contact Centers & Customer Service

The economic disruption is most visible here. Gartner predicts voice AI will reduce contact center labor costs by **$80 billion in 2026**.

| Metric | Human Agent | Voice AI |
|--------|------------|---------|
| Cost per call | $7–$12 | $0.40 |
| Simultaneous calls | 1 | Unlimited |
| Availability | 8 hrs/day | 24/7/365 |
| Languages | 1–2 | 45–70+ |
| QA call review coverage | 1–2% | 100% (automated) |
| Call deflection rate | — | 60–80% |

Retell AI alone processes **40 million+ AI phone calls per month**. PolyAI customers report **391% ROI** and $10.3M average annual savings.

### 2.4 Outbound Sales & Lead Qualification

Outbound voice agents are the fastest-growing segment projected through 2033:
- Appointment reminders and confirmations
- Payment follow-ups (collections)
- Lead qualification before human handoff
- Re-engagement campaigns (abandoned cart, renewal)

In India, SquadStack and Caller Digital handle tens of millions of outbound calls monthly for D2C brands, NBFCs, and insurers.

### 2.5 Education & E-Learning

- Language learning: accent coaching, pronunciation feedback, conversation practice
- Accessibility for visually impaired or low-literacy learners
- Voice-based tutoring, quiz delivery, adaptive learning
- Lecture summarization and Q&A

### 2.6 Agriculture & Micro-Enterprise (India-Specific)

- Mandi (wholesale market) price queries by voice in Bhojpuri, Haryanvi, Rajasthani
- Weather-based crop advisory in local dialect
- Government scheme eligibility checks (PM-KISAN, Ayushman Bharat)
- GST filing assistance by voice
- UPI transaction alerts and confirmations
- Kirana store inventory management via spoken commands

### 2.7 Hospitality & Field Operations

- Hotel concierge agents (multilingual, 24/7)
- Field worker guided instructions (hands-free, voice-driven)
- Maintenance ticket creation via spoken reports
- In-store voice assistants for retail

---

## 3. Business Impact: Real ROI Numbers

| Metric | Value | Source |
|--------|-------|--------|
| 3-year ROI | 331–391% | Forrester Consulting |
| ROI breakeven | 3.2 months median | Industry data |
| Cost reduction per call | 90–95% | $0.40 vs $7–$12 |
| Contact center labor savings (2026) | $80 billion | Gartner |
| Small business annual savings (vs receptionist) | $23,000–$42,000 | Industry |
| Per-call cost reduction at contact centers | 60–80% | Industry |
| Response latency improvement 2024→2026 | 1,200ms → 680ms | 2026 Voice Agent Report |
| Voice AI funding surge 2022→2025 | 7× ($315M → $2.1B) | Crunchbase |

**Productivity prediction:** Gartner expects Agentic AI to autonomously resolve 80% of common customer service issues by 2029, cutting operational costs by 30%. By end of 2026, 40% of enterprise applications will integrate task-specific AI agents — up from <5% in 2025.

---

## 4. The Tech Stack: Five Layers Every Builder Must Understand

A voice AI system is a **pipeline** — five distinct layers, each with its own latency budget, cost structure, and vendor ecosystem.

```
┌──────────────────────────────────────────────────┐
│  User speaks (phone / browser / mic / WhatsApp)  │
└──────────────────────┬───────────────────────────┘
                       │ raw audio
                       ▼
┌──────────────────────────────────────────────────┐
│  LAYER 1: Telephony / Transport                  │
│  Routes audio to the stack; handles SIP, WebRTC  │
│  Twilio · Telnyx · LiveKit · Plivo · SignalWire  │
└──────────────────────┬───────────────────────────┘
                       │ PCM audio stream
                       ▼
┌──────────────────────────────────────────────────┐
│  LAYER 2: ASR / STT  (The "Ears")                │
│  Converts speech → text in < 150ms              │
│  Deepgram · AssemblyAI · Whisper · Sarvam AI     │
└──────────────────────┬───────────────────────────┘
                       │ transcript text
                       ▼
┌──────────────────────────────────────────────────┐
│  LAYER 3: LLM / NLU  (The "Brain")               │
│  Understands intent, generates reply text        │
│  GPT-4o · Claude · Gemini · Llama 3 · Mistral   │
└──────────────────────┬───────────────────────────┘
                       │ response text
                       ▼
┌──────────────────────────────────────────────────┐
│  LAYER 4: TTS        (The "Voice")               │
│  Converts text → natural-sounding audio          │
│  ElevenLabs · Cartesia · Kokoro · Coqui XTTS-v2 │
└──────────────────────┬───────────────────────────┘
                       │ audio stream
                       ▼
┌──────────────────────────────────────────────────┐
│  LAYER 5: Orchestration  (The "Conductor")       │
│  VAD · turn-taking · context · routing           │
│  Vapi · Retell AI · Pipecat · LiveKit Agents     │
└──────────────────────────────────────────────────┘
```

**End-to-end latency budget for a natural conversation:**

| Layer | Target latency | Notes |
|-------|---------------|-------|
| Telephony | <50ms | Network round-trip |
| ASR | <150ms | From end-of-speech to transcript |
| LLM (first token) | <200ms | Time-to-first-token |
| TTS (first audio chunk) | <150ms | Streaming synthesis |
| **Total** | **<680ms** | Industry median 2026; target is <500ms |

Sub-500ms end-to-end is now the new production bar for Indian deployments, where cellular latency adds ~50ms overhead over fiber.

### Layer 1: Telephony / Transport

**Costs:**
- US local DID (phone number): $0.50–$1.15/month
- Per-minute call charge: $0.0035–$0.014/min
- At 1M minutes/month: $3,500–$14,000 in telephony alone

**Indian specifics:** SIP trunks via Plivo, Tata Tele, or Jio provide INR-priced telephony. Audio quality on Indian cellular is 8 kHz narrowband — this significantly degrades ASR accuracy (see Section 7).

### Layer 2: ASR / STT (The "Ears")

**Key players & 2026 pricing:**

| Provider | Price/min | Real-world English WER | Indian Language Notes |
|----------|-----------|------------------------|----------------------|
| Deepgram Nova-3 | $0.0043 | ~5.26% (batch) | Good Hindi; limited regional |
| OpenAI gpt-4o-transcribe | $0.006 | Lower than Whisper v3 | No Indian specialization |
| AssemblyAI Universal-2 | $0.015 | ~8.4% | Limited Indian |
| Google Chirp 2/3 | $0.024 | Unverified | Good multilingual |
| Whisper Large-v3 (self-hosted) | GPU cost only | ~10.6% (independent) | Hindi "good"; Bengali 25%+ |
| Faster-Whisper (self-hosted) | GPU cost only | Same as Whisper | 4× faster throughput |
| Sarvam AI Saarika | INR pricing | Indian-optimized | 22 Indian languages, telephony-trained |
| NVIDIA Parakeet TDT 0.6B | ~$0.0015/min (cloud) | Competitive | English-primary |


### Layer 3: LLM / NLU (The "Brain")

Counterintuitively, **LLM inference is the cheapest layer per minute** for most voice AI systems. A system running 10,000 minutes/month spends under $200 on the LLM.

**What matters is latency, not cost:** LLMs must return first tokens in <200ms for the conversation to feel natural. Smaller, faster models (Llama 3.1 8B, Mistral 7B) are often preferred over larger ones for voice specifically.


### Layer 4: TTS (The "Voice")

**The hidden budget killer.** TTS is often more expensive per-minute than ASR and LLM combined when using premium providers.

| Provider | Price/min | Quality | AMD ROCm |
|----------|-----------|---------|----------|
| ElevenLabs | $0.10–$0.30 | Best-in-class | Cloud only |
| Cartesia Sonic-3 | $0.05–$0.10 | Excellent, low latency | Cloud only |
| Amazon Nova Sonic | ~$0.02 | Good | Cloud only |
| Gnani Vachana TTS | INR pricing | Best Indian voices, 12 langs | On-premise |
| Sarvam Bulbul | INR pricing | 10 Indian languages | On-premise |
| Kokoro 82M (self-hosted) | GPU compute | Very good, Apache 2.0 | ✅ ROCm works |
| Chatterbox (self-hosted) | GPU compute | Excellent | ✅ ROCm works |
| Coqui XTTS-v2 (self-hosted) | GPU compute | Good, 17 langs, non-commercial | ⚠️ Partial |


### Layer 5: Orchestration (The "Conductor")

Manages conversation state, VAD (knowing when user stops speaking), turn-taking, interruption handling, and component routing.

| Platform | Type | Pricing | India Compliance |
|----------|------|---------|-----------------|
| Vapi | Managed, API-first | USD/min | Developer-managed |
| Retell AI | Managed | USD/min | Developer-managed |
| Bolna.ai | Managed, Indian | ~₹5.52/min | Developer-managed |
| Caller Digital | Managed, Indian | INR per-outcome | Built-in TRAI + DPDP |
| Pipecat | Open-source framework | GPU compute | Self-managed |
| LiveKit Agents | Open-source/cloud | Compute cost | Self-managed |

---

## 5. Cost Anatomy: Where the Money Goes

### Full Stack Cost Per 10,000 Minutes/Month

| Layer | DIY / Self-hosted | Managed Cloud |
|-------|------------------|---------------|
| Telephony | $35–$140 | $35–$140 |
| ASR/STT | $15–$50 (GPU) | $43–$240 |
| LLM | $20–$150 | $20–$150 |
| TTS | $20–$50 (GPU) | $200–$3,000 |
| Infrastructure (GPU/cloud) | $200–$800 | Included |
| **Total** | **$290–$1,190/month** | **$298–$3,530/month** |

### Platform Pricing (All-in-One)

| Platform | Cost/min | Trade-off |
|----------|----------|-----------|
| Vapi / Retell (global) | $0.25–$0.50 USD | Fast to deploy; USD pricing hurts India unit economics |
| Bolna.ai (India) | ~₹5.52 (~$0.066) | Developer-built; 3–4× cheaper than global for India |
| Caller Digital (India) | ₹8–25 per outcome | Per-outcome pricing; compliant; fast deploy |
| Gnani.ai (enterprise India) | Custom INR | Best for Tier-1 BFSI, biometrics; slow procurement |

**The INR vs USD gap matters enormously in India.** A 3-minute customer call costs:
- USD-priced platform: ~$0.75–$1.50 (~₹63–₹125)
- INR-priced platform: ₹16–₹45

At 1 million calls/month, this is a cost difference of **₹2–8 crore per month**.

### Build Cost by Complexity

| System Type | Build Cost | Monthly Ops |
|-------------|-----------|-------------|
| Basic IVR replacement | $15,000–$35,000 | $1,500–$3,000 |
| Multi-intent customer service agent | $35,000–$80,000 | $3,000–$6,000 |
| Enterprise voice platform (CRM + multilang + analytics) | $80,000–$150,000+ | $6,000–$8,000+ |
| India-compliant BFSI deployment (DPDP + TRAI + RBI) | Add 30–50% for compliance scaffolding | Add ₹50K–₹2L/month for audit + storage |

---

## 6. The Open-Source Stack: Build It for the Cost of GPU Compute

A fully capable voice AI system can be assembled from open-source components — no API bills, no data leaving your infrastructure. This is especially relevant for India (DPDP compliance) and AMD (on-premise GPU cost advantage).

### Canonical Open-Source Pipeline (2026)

```
Faster-Whisper or Sarvam Saarika (STT)
        ↓
Llama 3.1 8B/70B via Ollama (LLM)
        ↓
Kokoro 82M / Chatterbox / Coqui XTTS-v2 (TTS)
        ↓
LiveKit Agents / Pipecat (Orchestration)
        ↓
Plivo / Telnyx SIP trunk (Telephony)
```

### STT Options

| Model | WER (English) | Speed | License | AMD ROCm |
|-------|--------------|-------|---------|----------|
| Whisper Large-v3 | ~10.6% real-world | 1× | MIT | ✅ Works |
| Faster-Whisper | Same as Whisper | **4×** | MIT | ✅ Works |
| distil-whisper | Within 1% of Whisper | **6×** | Apache 2.0 | ✅ Works |
| WhisperX | Same + diarization | 4× | MIT | ✅ Works |

**Critical gap:** All Whisper variants are **batch-only** — not streaming. For real-time voice agents, you need to pair with a Voice Activity Detection (VAD) model (Silero VAD is standard) and chunk audio aggressively. Commercial streaming ASR (Deepgram, AssemblyAI) is still the easier path for sub-300ms latency.

### TTS Options

| Model | Params | License | Languages | AMD ROCm | Notes |
|-------|--------|---------|-----------|----------|-------|
| Kokoro | 82M | **Apache 2.0** | English | ✅ | Fastest, near-instant |
| Chatterbox | ~500M | Open | English | ✅ | Excellent quality |
| Coqui XTTS-v2 | ~1.5B | Non-commercial | 17 languages | ⚠️ | Voice cloning with 6s audio |
| Higgs Audio V2 | 5.8B | **Apache 2.0** | Multilingual | Untested | 10M+ training hours |
| Fish Audio S2 Pro | — | Commercial | Multilingual | Unknown | 81.88% win rate benchmark |

### Orchestration Frameworks

| Framework | Type | Best for |
|-----------|------|---------|
| Pipecat | Python, 50+ service connectors | Flexible multi-modal pipelines |
| LiveKit Agents | WebRTC-native, enterprise | Low-latency browser/phone |
| TEN | Multi-agent, real-time | Complex routing |
| Bolna (open-core) | India-focused | Indian language deployments |

### What's Missing in Open Source

1. **Sub-100ms streaming ASR** — batch Whisper cannot hit this alone
2. **Indian language models with telephony training** — Sarvam is open-weight but not fully open-source
3. **Telephony integration** — no OSS equivalent to Twilio; requires SIP stack expertise
4. **Emotion and prosody control** — commercial TTS still superior
5. **DPDP-compliant audit logging** — must be built from scratch
6. **Voice Activity Detection for 8 kHz phone audio** — Silero VAD helps but noise is brutal

---

## 7. ASR Accuracy: The Language Reality Check

This section matters most for India and AMD's opportunity. The headline WER numbers sound great. The reality for Indian-language, phone-quality audio is harder.

### Whisper Benchmark vs Real-World

| Condition | WER | Notes |
|-----------|-----|-------|
| LibriSpeech test-clean (benchmark) | **~2.7%** | Ideal — audiobook, one speaker |
| Clean studio podcast | 3–6% | Still controlled |
| Conference call, 2 speakers | 7–12% | Business baseline |
| Zoom/Teams call, 3+ speakers | 10–15% | Common reality |
| Phone audio (8 kHz telephony) | Significantly higher | Bandwidth-limited — exact delta unverified but material |
| Strong accents | +5–10% over baseline | Documented in JASA Express Letters 2024 |
| Heavy background noise | +5–15% | Cafés, traffic, construction |
| Overlapping speakers | Significant degradation | Whisper has no native diarization |

**Independent real-world English WER (2025 benchmarks):**
- Whisper Large-v3: ~10.6%
- Deepgram Nova-3: ~5.26%
- AssemblyAI Universal-2: ~8.4%


---

## 8. AMD's Opportunity in the Voice AI Stack

### The Hardware Picture

Every voice AI conversation costs GPU cycles — for ASR inference, TTS synthesis, and LLM response generation. At scale (millions of calls/month), compute cost is the primary operating variable. This is where hardware choices become multimillion-dollar decisions.

### AMD vs NVIDIA in 2026: Current State

| Dimension | AMD MI300X | AMD MI355X | NVIDIA H100 SXM5 |
|-----------|-----------|-----------|------------------|
| VRAM | **192GB HBM3** | **288GB HBM3e** | 80GB HBM3e |
| On-demand cloud price | $1.50–$2.50/hr | Est. higher | **$2.90/hr** |
| Llama 3.1 70B throughput | ~18,000 tok/sec | ~22,000+ tok/sec | ~19,500 tok/sec |
| Cost per million tokens | **~$0.027** | ~$0.025 | ~$0.041 |
| PyTorch + vLLM | ✅ Full support | ✅ Full support | ✅ Full support |
| TensorRT-LLM | ❌ Not supported | ❌ Not supported | ✅ Native |
| FlashAttention 3 | ❌ Not available | ❌ Not available | ✅ (Hopper+) |
| HuggingFace TEI | ❌ No support | ❌ No support | ✅ Full support |
| TTS (Kokoro/Chatterbox) | ✅ Works | ✅ Works | ✅ Works |
| AMD-Meta production deal | ✅ 6 GW commitment | — | — |

**MLPerf Inference 6.0 (April 2026):** MI355X results were within single-digit percentage points of B200 on server inference workloads — the most direct like-for-like benchmark available.

### AMD's Roadmap

- **MI450 (H2 2026):** Improved CDNA architecture, better FP8/FP4 throughput. Cloud availability 3–6 months after hardware release (early 2027).
- **AMD Helios rack-scale platform:** 72 MI455X accelerators + EPYC Venice CPUs + Pensando networking + UALink interconnect delivering 260 TB/s scale-up bandwidth per rack. Designed for large-scale training at data-center scale.
- **ROCm 7.x roadmap:** Active work on closing the attention kernel gap, better Triton AMD backend, improved `torch.compile()` on ROCm.

### Where AMD Wins in Voice AI

**1. LLM Inference — 25–40% Cost Advantage**

For Llama 3.1 70B at 1M tokens:
- H100 SXM5 ($2.90/hr, ~19,500 tok/sec): **~$0.041 per million tokens**
- MI300X ($1.75/hr, ~18,000 tok/sec): **~$0.027 per million tokens**

The 34% cost advantage on LLM inference is real and compounds at scale. A voice AI system doing 1M minutes/month generates ~6B tokens/month — the AMD savings are **~$84,000/month**.

**2. Large Model VRAM Fit**

A model that requires 2× H100s (160GB combined) fits on a **single MI300X (192GB)**. This halves node cost, eliminates NVLink/interconnect complexity, and simplifies serving architecture. For 70B+ parameter LLMs — which are common for high-quality enterprise voice agents — this is a structural advantage.

**3. TTS Inference — Pure PyTorch Models Work**

Kokoro, Chatterbox, and Coqui XTTS-v2 are pure PyTorch. They run correctly on AMD ROCm with no modification. For companies building self-hosted TTS to avoid ElevenLabs costs ($0.10–$0.30/min), AMD provides cost-competitive inference infrastructure.

**4. Price-Sensitive On-Premise Markets**

India's DPDP compliance often mandates audio and transcripts stay within India. On-premise GPU deployment is frequently the only compliant option for BFSI. AMD's hardware cost (~half of NVIDIA's list price for equivalent capability) is a direct competitive advantage in this procurement context.

### Where AMD Is Behind

**1. Streaming ASR Ecosystem**

Most streaming ASR systems are built assuming NVIDIA CUDA. Deepgram and AssemblyAI run their cloud infrastructure on NVIDIA. HuggingFace inference containers default to CUDA. Self-hosted streaming ASR (e.g., Faster-Whisper real-time mode) on AMD requires additional integration work.

*What AMD can do:* Publish certified ROCm builds for Faster-Whisper + Silero VAD + streaming pipeline. Partner with Sarvam AI to validate their Saarika ASR on AMD hardware — a high-value, India-specific contribution.

**2. HuggingFace TEI (Text Embeddings Inference)**

TEI — used for knowledge-base retrieval in RAG-augmented voice agents — has no AMD support. This is a real gap for enterprise voice agents that use product catalogues, policy documents, or FAQs as context.

*What AMD can do:* Upstream ROCm support into HuggingFace TEI. This is a bounded engineering project with high ecosystem multiplier.

**3. FlashAttention 3 and TensorRT-LLM**

NVIDIA's FlashAttention 3 (Hopper-specific) and TensorRT-LLM provide throughput optimizations that AMD cannot match for latency-critical workloads at batch size 1–4.

*What AMD can do:* This is a silicon and compiler problem, not purely software. The ROCm 7.x attention kernel improvements help, but FA3 parity will require sustained investment. In the interim, AMD's advantage is throughput (batch 64–128), not ultra-low-latency single-user inference.

### The ROCm Migration Path for Voice AI

```bash
# Step 1: Start from AMD's official image
docker pull rocm/pytorch:rocm6.2_ubuntu22.04_py3.10_pytorch_2.4.0

# Step 2: Install ROCm-compatible vLLM
pip install vllm --extra-index-url https://download.pytorch.org/whl/rocm6.2

# Step 3: Serve your LLM (API-identical to CUDA version)
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.1-70B-Instruct --dtype float16

# Step 4: Run TTS (Kokoro — works out of the box)
# No changes needed — pure PyTorch, ROCm routes CUDA calls via HIP
```

**ROCm compatibility summary for voice AI workloads:**

| Component | AMD ROCm | Notes |
|-----------|----------|-------|
| LLM serving (vLLM + Llama 3.1) | ✅ Full | 90–95% of H100 throughput |
| LLM serving (SGLang) | ✅ Full | Within 5–10% of CUDA |
| TTS: Kokoro, Chatterbox | ✅ Full | Pure PyTorch |
| TTS: Coqui XTTS-v2 | ⚠️ Partial | Works with effort |
| ASR: Faster-Whisper (batch) | ✅ Full | Real-time needs extra work |
| ASR: HuggingFace containers | ❌ | NVIDIA-assumed |
| Embeddings: HuggingFace TEI | ❌ | No ROCm support |
| Streaming ASR | ❌ | Needs community work |

### AMD's Positioning Statement for Voice AI

> "Run your LLM and TTS layers on AMD MI300X. Pay 25–40% less per conversation than on H100. A voice AI system handling 1 million minutes/month can save $50,000–$100,000 per year on LLM inference alone. For India BFSI deployments requiring on-premise data residency, AMD's hardware cost advantage — roughly 50% lower GPU list price — translates directly to lower CapEx. One MI300X (192GB) replaces two H100s for 70B-parameter models."

**The AMD strategic opportunity is not to win training workloads from NVIDIA.** It is to own the inference layer of the voice AI stack at the cost-optimized, compliance-sensitive end of the market — which is exactly where India sits.

---

---

## Sources

Primary research and data sourced from:

- [AssemblyAI: Voice AI in 2026 — Companies and Investments](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1)
- [AssemblyAI: Voice AI Stack for Building Agents](https://www.assemblyai.com/blog/the-voice-ai-stack-for-building-agents)
- [AssemblyAI: Top 8 Open-Source STT Options 2026](https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications)
- [Spheron: ROCm vs CUDA GPU Cloud 2026](https://www.spheron.network/blog/rocm-vs-cuda-gpu-cloud-2026/)
- [vLLM Blog: High-Performance Inference on AMD ROCm](https://vllm.ai/blog/2026-02-27-rocm-attention-backend)
- [AMD ROCm: Voice Pipeline RAG Ollama Tutorial](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/voice_pipeline_rag_ollama.html)
- [AMD: On-Device ASR with Whisper on Ryzen AI NPU](https://www.amd.com/en/developer/resources/technical-articles/2025/unlocking-on-device-asr-with-whisper-on-ryzen-ai-npus.html)
- [CallerDigital: Top 10 Voice AI Agents India 2026](https://caller.digital/blog/top-10-voice-ai-agents-india-2026)
- [CallerDigital: Voice AI India 2026 Complete Guide](https://caller.digital/blog/voice-ai-india-2026-complete-guide)
- [CallerDigital: DPDP Compliance Checklist for Voice AI](https://caller.digital/blog/dpdp-act-compliance-checklist-voice-ai-india)
- [Slator: Sarvam Raises $234M for Sovereign Multilingual AI](https://slator.com/sarvam-raises-234m-sovereign-multilingual-ai/)
- [Vexascribe: Whisper Accuracy WER Benchmarks 2026](https://vexascribe.com/how-accurate-is-whisper)
- [BentoML: Best Open-Source TTS Models 2026](https://bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models)
- [Resemble AI: Best Open-Source Voice Cloning Tools 2026](https://www.resemble.ai/resources/best-open-source-ai-voice-cloning-tools)
- [LocalAI Master: Coqui TTS XTTS-v2 Guide](https://localaimaster.com/models/coqui-tts)
- [RaftLabs: Voice AI Development Cost Breakdown](https://www.raftlabs.com/blog/voice-ai-development-cost)
- [Aircall: AI Voice Agent Cost 2026](https://aircall.io/blog/best-practices/ai-voice-agent-cost/)
- [Vomyra: Future of Voice AI in India](https://vomyra.com/blogs/the-future-of-voice-ai-in-india-trends-growth)
- [Shunyalabs: Speech AI in 2026](https://www.shunyalabs.ai/blog/speech-ai-in-2026)
- [arXiv: ASR Benchmarks for Indian Languages](https://arxiv.org/html/2602.03868v1)
- [Sarvam AI: Evaluating Indian Language ASR](https://www.sarvam.ai/blogs/evaluating-indian-language-asr)
- [TechCrunch: Vapi $500M Valuation](https://techcrunch.com/2026/05/12/vapi-hits-500m-valuation-as-amazon-ring-chose-its-ai-platform-over-40-rivals/)
- [Business Standard: Voice AI India Inclusion](https://www.business-standard.com/amp/technology/artificial-intelligence/voice-ai-could-bridge-the-gap-between-india-s-ai-haves-and-have-nots-126061501393_1.html)
- [ConversAI Labs: Voice AI Compliance in India](https://www.conversailabs.com/blog/voice-ai-compliance-in-india)
- [AInora: 50+ Voice AI Statistics 2026](https://ainora.lt/blog/voice-ai-statistics-market-data-2026)
- [NextLevel.ai: Voice AI Enterprise Adoption & ROI](https://nextlevel.ai/voice-ai-trends-enterprise-adoption-roi/)
- [Grand View Research: AI Voice Agents Market 2026–2033](https://www.grandviewresearch.com/industry-analysis/ai-voice-agents-market-report)

---
---

## 14. The Three Frameworks That Rule Everything — and How AMD Becomes the Gateway

### The Convergence No One Talks About

Here is the uncomfortable truth beneath the voice AI hype: despite hundreds of companies, thousands of GitHub repos, and billions in funding, the entire industry's production code converges on **two or three open-source orchestration frameworks**. Everything else — Vapi, Retell, Bolna, Caller Digital, Gnani — is a business layer sitting on top of one of these three:

```
┌─────────────────────────────────────────────────────────────┐
│                    EVERY VOICE AI COMPANY                   │
│   Vapi · Retell · Bolna · ElevenAgents · Caller Digital    │
│   Gnani · Sarvam Agents · PolyAI · Synthflow · Ringg.ai   │
└────────────────────┬──────────────┬───────────────┬────────┘
                     │              │               │
            ┌────────▼──────┐ ┌────▼─────┐ ┌─────▼──────┐
            │  LiveKit      │ │ Pipecat  │ │    TEN     │
            │  Agents       │ │          │ │ Framework  │
            │  (Apache 2.0) │ │ (BSD-2)  │ │  (C++/Go)  │
            └───────────────┘ └──────────┘ └────────────┘
                     │              │               │
         ┌───────────▼──────────────▼───────────────▼───────┐
         │              SHARED MODEL LAYER                   │
         │  STT: Faster-Whisper / Deepgram / Sarvam Saarika  │
         │  LLM: Llama 3.1 / Mistral / Claude / GPT-4o       │
         │  TTS: Kokoro / ElevenLabs / Coqui / Vachana       │
         └───────────────────────────┬───────────────────────┘
                                     │
                         ┌───────────▼──────────┐
                         │   GPU COMPUTE LAYER  │
                         │  NVIDIA / AMD        │
                         └──────────────────────┘
```

Win at the framework layer or the compute layer — everything above is margin compression.

---

### The Three Frameworks Dissected

#### LiveKit Agents (Apache 2.0) — The WebRTC Backbone

LiveKit is the open-source WebRTC stack that **OpenAI's ChatGPT Voice Mode runs on**. Character.ai, Meta, and thousands of production voice products use it. LiveKit Agents 1.0 shipped April 2025; 1.5.x is current as of April 2026.

**Architecture:** A LiveKit agent joins a "room" as a headless participant — the same way a human would dial in. It subscribes to the caller's audio track, runs it through STT, feeds text to an LLM with tool-calling, and publishes synthesized speech back on its own audio track. Real-time, bi-directional, parallel.

**Why it dominates:**
- Native SIP and phone numbers shipped 2025 — no Twilio bridge needed
- Multi-participant native: group calls, video + voice, screen sharing built-in
- Model Context Protocol (MCP) tool support built in
- The entire media server, Agents SDK, and SIP bridge are Apache 2.0 — you can run the whole stack yourself

**The GPU bottleneck:** LiveKit handles network. The GPU is needed for the model layer — STT, LLM, TTS. If those models run on AMD GPUs, AMD becomes the compute substrate for every LiveKit deployment.

---

#### Pipecat (BSD-2) — The Model Integration Layer

Pipecat is a Python framework from Daily.ai that reached v1.0 in April 2026. It is **the framework with the largest integration library** — 60+ service connectors covering every STT, LLM, TTS, and transport combination commercially available.

**Architecture:** Left-to-right frame pipeline. Every audio frame flows through:
```
VAD (silence detection) → STT (speech to text) → LLM (response) → TTS (synthesis) → output
```
Each stage is a swappable component. Change Deepgram to Faster-Whisper. Change ElevenLabs to Kokoro. Change GPT-4o to Llama 3.1. No code rewrite — just swap the processor.

**Why it matters for AMD:**
- Pipecat is transport-agnostic — works with LiveKit, WebRTC, telephony, or raw audio
- It's pure Python, pure PyTorch under the hood — **ROCm compatibility is direct**
- Its self-hosted model support (Ollama, vLLM, local Whisper) is exactly the AMD deployment scenario
- `pipecat create` scaffolds a working agent in under 60 seconds — AMD needs to be the compute target when that command runs

**Key tools shipping with Pipecat:** Whisker (real-time pipeline debugging), Tail (live monitoring), OpenTelemetry integration — a full production observability stack.

---

#### TEN Framework (C++ / Go / Python) — The Performance Core

TEN (Transformative Extensions Network) is the highest-performance framework because its core is C++, not Python. Extensions can be written in C++, Go, or Python. It includes proprietary VAD and turn-detection models optimized for sub-300ms response.

**Why it matters:** TEN is where **avatar + voice** combinations run — lip-sync integrations with Trulience, HeyGen, Tavus. The TMAN Designer visual editor means non-engineers can wire together voice agents. It requires Docker + Agora account to run, making it heavier than LiveKit or Pipecat.

**AMD angle:** TEN's C++ compute core means its GPU calls go directly to the driver level. An AMD ROCm-certified TEN container would validate AMD for the highest-performance tier.

---

### How NVIDIA Became the Hardware Gateway — The NIM Playbook

NVIDIA did not win voice AI by making better silicon (though that helped). They won by making their silicon the **path of least resistance** for every developer. The NIM (NVIDIA Inference Microservices) strategy is the clearest example of hardware-as-platform executed correctly.

```
NVIDIA's Gateway Strategy:
┌─────────────────────────────────────────────────────────────┐
│                    NVIDIA NIM ECOSYSTEM                      │
├──────────────────┬──────────────────┬────────────────────────┤
│  Compute Layer   │  Software Layer  │  Developer Layer       │
│                  │                  │                        │
│  RTX 50 Series   │  NIM containers  │  28M developers on NIM │
│  FP4 support     │  (TensorRT-LLM   │  AI Blueprints         │
│  32GB VRAM       │   vLLM, SGLang)  │  VS Code NIM extension │
│  RTX Spark       │                  │  Azure AI Foundry NIM  │
│  (Grace+Blackwell│  Riva ASR        │  (from July 2026)      │
│   128GB shared)  │  Maxine TTS      │                        │
│                  │                  │  Global SI certs:      │
│  DGX / Certified │  AI Blueprints   │  TCS, Infosys, Wipro   │
│  Systems         │  for voice       │  Accenture, Deloitte   │
└──────────────────┴──────────────────┴────────────────────────┘
```

**What NIM actually does for voice AI:**
1. **Pre-packages Riva ASR** (Parakeet TDT model) as a production-ready container — one Docker pull, CUDA-optimized, benchmarked, supported
2. **Pre-packages Maxine Studio Voice TTS** — same one-pull model
3. **AI Blueprints** are reference implementations for complete voice workflows — developers don't design the stack, they clone it
4. **RTX Spark** (Grace CPU + Blackwell GPU, 128GB shared memory) eliminates the CPU/GPU memory bottleneck — entire large models live in shared memory
5. **VS Code NIM extension** means the developer tool every programmer uses defaults to NVIDIA compute targets
6. **Azure AI Foundry** native NIM support from July 2026 — deploy to cloud from VS Code with one click, NVIDIA GPU underneath
7. **28 million developers** who downloaded NIM effectively opted into the NVIDIA ecosystem by default

The result: when a developer runs `docker pull nvidia/riva-asr` or follows an AI Blueprint for a voice agent, they never think about GPU choice — it's already made for them. NVIDIA is the default. Everything else requires active choice.

---

### What AMD Has — and What It's Missing

**What AMD has today:**
- MI300X: 192GB HBM3, 25–40% cheaper per inference token than H100
- ROCm 7.2: PyTorch, vLLM, Ollama, llama.cpp all work natively
- HIP compatibility: CUDA calls route to AMD automatically — most PyTorch code needs zero changes
- vLLM ROCm wheel: `pip install vllm --extra-index-url https://download.pytorch.org/whl/rocm6.2`
- Ryzen AI NPU: runs Whisper on-device with BFP16 precision
- AMD-Meta 6GW production commitment — ecosystem credibility signal

**What AMD is missing — the NIM gap:**

| NVIDIA Has | AMD Equivalent | Status |
|-----------|---------------|--------|
| `nvidia/riva-asr` NIM container | AMD-certified ASR container | ❌ Does not exist |
| `nvidia/riva-tts` NIM container | AMD-certified TTS container | ❌ Does not exist |
| AI Blueprint: Voice Agent | AMD voice AI Blueprint | ❌ Does not exist |
| Pipecat validated on RTX | Pipecat validated on MI300X | ❌ No official validation |
| LiveKit + Riva reference stack | LiveKit + AMD ROCm reference | ❌ No official reference |
| VS Code NIM extension (NVIDIA target) | VS Code AMD target | ❌ Does not exist |
| Azure Foundry NIM (July 2026) | AMD cloud inference on Azure | ❌ Partial only |
| 28M developers defaulting to CUDA | AMD developer default | ❌ Developers must opt in |

**The gap is not silicon.** AMD's MI300X is competitive with H100 for inference. The gap is **three missing Docker containers and two missing documentation pages.**

---

### The AMD Gateway Strategy: Match NIM, Beat It on Cost

AMD's path to becoming the gateway for voice AI requires executing the same playbook NVIDIA ran — but targeting the specific wedge NVIDIA's pricing creates:

#### Step 1 — The Three Certified Containers (Do This First)

```bash
# Container 1: AMD Pipecat Voice Agent (generic, global)
docker pull amd/rocm-pipecat-voice:latest
# Inside: Faster-Whisper + vLLM (Llama 3.1 8B) + Kokoro TTS
#         + Pipecat 1.0 + Silero VAD + LiveKit transport
#         + ROCm 7.2 base image
#         AMD-certified on MI300X, MI355X, RX 7900 XTX

# Container 2: AMD LiveKit Voice Agent (WebRTC-first)
docker pull amd/rocm-livekit-voice:latest
# Inside: Same model stack with LiveKit Agents 1.5
#         + native SIP bridge
#         + AMD ROCm-optimized vLLM serving

# Container 3: AMD Sarvam India Voice Agent (India-specific)
docker pull amd/rocm-sarvam-india-voice:latest
# Inside: Sarvam Saarika ASR + Sarvam Bulbul TTS
#         + Llama 3.1 or Sarvam-30B LLM
#         + Pipecat + Hinglish VAD tuning
#         + DPDP-compliant audit logging layer
#         AMD-certified, runs entirely on-premise in India
```

**Why three containers?** Because every developer evaluating voice AI asks "does this run on AMD?" If the answer is `docker pull amd/rocm-pipecat-voice` — it takes 30 seconds to validate. If the answer is "install ROCm, configure HIP, port the Whisper container..." — they choose NVIDIA.

#### Step 2 — AMD Voice AI Blueprints

Mirror NVIDIA's AI Blueprints concept. Each Blueprint is a complete, working voice agent application — not documentation, not a tutorial, an actual deployable repo.

| Blueprint | Stack | Target Market |
|-----------|-------|--------------|
| `amd-voice-contact-center` | Pipecat + Faster-Whisper + Llama 3.1 70B + Kokoro | US/EU enterprise |
| `amd-voice-india-bfsi` | LiveKit + Sarvam Saarika + Sarvam-30B + Vachana TTS | Indian BFSI |
| `amd-voice-arabic-banking` | Pipecat + Arabic-tuned ASR + Llama 3.1 + Gulf Arabic TTS | GCC banking |
| `amd-voice-edge-offline` | Ryzen AI NPU + Whisper Small + Llama 3.2 3B + Kokoro | Edge/offline India |
| `amd-voice-multilingual-latam` | Pipecat + Whisper + Llama 3.1 + Brazil Portuguese TTS | LatAm telecom |

Each Blueprint ships as: one `docker-compose.yml`, one `README.md`, one Python entry point. It works on MI300X and — critically — also on the RX 7900 XTX (consumer GPU, ~$700) to reach the developer who can't expense a data center GPU.

#### Step 3 — ROCm Plugin Certification for Pipecat

Pipecat's architecture is built around pluggable processors. AMD needs:
- An official `pipecat-amd` package on PyPI: `pip install pipecat-ai[amd]`
- Registers AMD-optimized Faster-Whisper, AMD-optimized Kokoro, AMD-optimized vLLM serving as first-class Pipecat processors
- Shows up in Pipecat's official documentation as a supported compute backend

This is **two weeks of engineering work** and positions AMD alongside Deepgram, ElevenLabs, and OpenAI as an official Pipecat integration partner.

#### Step 4 — HuggingFace TEI on ROCm (Closes the Biggest Gap)

The one missing piece that genuinely blocks enterprise voice AI on AMD: HuggingFace Text Embeddings Inference (TEI) has no ROCm support. Voice agents using RAG (retrieval-augmented generation) — product catalogues, policy documents, FAQ databases — need TEI for embeddings. Without it, AMD cannot serve the RAG-augmented enterprise voice agent market.

Fund the ROCm TEI port. It is bounded engineering. Once it ships, AMD closes the last meaningful software gap vs NVIDIA for the voice AI stack.

#### Step 5 — The Ryzen AI NPU as the Developer On-Ramp

NVIDIA's RTX AI PC strategy (RTX Spark, AI PCs with GeForce RTX 50 Series) reaches developers through consumer hardware. AMD has the same play with **Ryzen AI NPU**:

```
NVIDIA RTX AI PC Strategy        AMD Ryzen AI Strategy
─────────────────────────         ────────────────────────────
RTX 50 Series GPU               ← Ryzen AI 300 NPU
NIM local containers            ← AMD ROCm Pipecat Blueprint
CUDA default in VS Code         ← AMD Quark + ROCm extension
32GB VRAM                       ← NPU (dedicated, no GPU needed)
$1,500+ laptop                  ← $800 Ryzen AI laptop
```

AMD already publishes Whisper-on-NPU documentation. The next step: ship a `pipecat create --backend amd-npu` template that scaffolds a complete voice agent running on Ryzen AI — Whisper Tiny on NPU, Llama 3.2 3B via Ollama, Kokoro TTS on CPU. No GPU required. No cloud required. No API key required. Runs offline. DPDP-compliant.

This is the developer laptop demo that converts engineers into AMD advocates.

---

### Side-by-Side: NVIDIA NIM vs AMD's Required Response

| NVIDIA (Current) | AMD (Required) | Effort |
|-----------------|---------------|--------|
| `docker pull nvidia/riva-asr` | `docker pull amd/rocm-faster-whisper` | 2 weeks |
| `docker pull nvidia/riva-tts` | `docker pull amd/rocm-kokoro-tts` | 2 weeks |
| AI Blueprint: voice agent | AMD Blueprint: Pipecat on MI300X | 4 weeks |
| AI Blueprint: India voice | AMD Blueprint: Sarvam on MI300X | 4 weeks |
| VS Code NIM extension | VS Code ROCm / AMD Quark extension | 8 weeks |
| Pipecat docs show NVIDIA | Pipecat official AMD processor | 2 weeks |
| Azure Foundry NIM (July 2026) | Azure AMD inference endpoint | 12 weeks |
| Riva ASR (NVIDIA's own model) | Partner with Sarvam (AMD-Sarvam deal) | 8 weeks |
| RTX Spark (Grace+Blackwell) | Ryzen AI NPU voice template | 4 weeks |
| SI certification (TCS, Infosys) | India SI certification (TCS, Infosys, HCL) | 16 weeks |

**Total engineering investment for steps 1–4: approximately 12–16 weeks for a focused team of 6–8 engineers.**

The ROI: AMD positions itself as the compute substrate for every Pipecat and LiveKit voice agent deployment targeting on-premise, India, Middle East, or cost-optimized serving. At AMD's current cost advantage ($0.027 vs $0.041 per million tokens), the pitch to every voice AI company is:

> "Same Pipecat code. Same LiveKit transport. Replace `nvidia/riva-asr` with `amd/rocm-faster-whisper`. Pay 34% less per conversation. For a platform doing 10M minutes/month, that's $600,000/year."

---

### The Strategic Summary

The voice AI market has converged on three frameworks. The GPU market has converged on NVIDIA through software, not just silicon. AMD has a real silicon advantage in the deployment workload that matters — inference. The missing piece is not hardware. It is **three Docker containers, two Blueprints, one PyPI package, and one TEI port.**

That is the entire gap between "AMD is an alternative" and "AMD is the gateway."

```
AMD Voice AI Gateway — Target State

Developer types:
  pipecat create --backend amd

Gets:
  ✅ Faster-Whisper (STT)  — AMD ROCm certified
  ✅ Llama 3.1 via vLLM    — AMD ROCm certified
  ✅ Kokoro TTS             — AMD ROCm certified
  ✅ LiveKit transport      — AMD ROCm certified
  ✅ DPDP audit logging     — India-compliant
  ✅ Sarvam plugin option   — 22 Indian languages
  ✅ Works on MI300X        — 34% cheaper than H100
  ✅ Works on Ryzen AI NPU  — offline, no cloud

Result:
  Every Pipecat developer who chooses AMD gets a complete,
  working, production-grade voice agent in 60 seconds.
  NVIDIA requires the same 60 seconds.
  AMD costs 34% less per conversation at scale.
  In India, AMD costs 50% less in CapEx.

That is the gateway.
```

---

## 15. The Five Ecosystem Layers — Where NVIDIA Lives and AMD Does Not

Beyond the three orchestration frameworks (§14), NVIDIA has staked out positions across five distinct ecosystem layers. Each layer operates on the same logic: ship a named package, container, or SDK; let developers adopt it as the default; AMD silicon becomes invisible at the call site. The following is a complete map.

---

### Layer 1 — Framework Plugin Slots (the Pipecat pattern, repeated)

| Framework | NVIDIA presence | AMD presence |
|---|---|---|
| **Pipecat** | Official processor plugin, docs, examples | None |
| **LiveKit Agents** | Certified GPU backend | None |
| **LangChain** | `langchain-nvidia-ai-endpoints` — chat, embeddings, reranking, tool calling, LangGraph parallel execution | None |
| **LlamaIndex** | `llama-index-llms-nvidia` — NIM-backed LLM + embeddings | None |
| **Haystack** | NIM integration as a native pipeline component | None |

Every LangChain or LlamaIndex voice agent that uses NIM routes to NVIDIA hardware at the endpoint level. The developer writes `ChatNVIDIA(model="...")` — done. AMD does not exist in that call. The same call, repeated across millions of agent pipelines, is the mechanism by which NVIDIA becomes the default GPU substrate for every voice AI application built in 2025–2026.

---

### Layer 2 — Inference Serving Infrastructure (the deepest lock-in)

**NVIDIA Triton / Dynamo-Triton** is the invisible substrate beneath every production voice pipeline. ASR model served from Triton. LLM served from Triton. TTS served from Triton. Users include Microsoft, American Express, Salesforce, Naver, and Hugging Face. It runs inside AWS SageMaker, Azure Machine Learning, Google Vertex AI, and Oracle Cloud. In March 2025 NVIDIA folded it into the **NVIDIA Dynamo** platform, adding disaggregated LLM serving (prefix caching, KV offload to storage), making it the only inference server that handles both traditional ML models and large-scale LLM serving in a single orchestration layer.

**TensorRT-LLM** sits on top of Triton — hand-tuned CUDA kernels for LLM inference. At batch size 1–4 (real-time voice, latency-critical), TensorRT-LLM holds a 20–30% throughput advantage over vLLM ROCm. This is the latency gap that matters for voice: a 50ms difference in LLM token generation is audible to a human ear.

AMD's position: **vLLM ROCm became officially first-class in January 2026** (CI pass rate jumped from 37% in November 2025 to 93% in six weeks; first pre-built Docker image shipped). This is genuine progress. But vLLM is one serving tool. Triton is infrastructure. There is no AMD model serving standard, no AMD inference server with multi-model ensemble orchestration, no AMD equivalent of Dynamo's disaggregated serving.

---

### Layer 3 — Voice-Domain SDKs (vertically integrated stacks)

NVIDIA ships three domain-specific SDKs for voice AI. Each one pulls Triton and TensorRT as dependencies, creating a complete vertical stack from model to microservice that a developer cannot easily swap hardware under.

**NVIDIA Riva** — full conversational AI SDK: ASR + TTS + neural machine translation + speaker diarization + speaker identification + voice activity detection, served as gRPC microservices. Enterprise-licensed with SLA. Fine-tunable via NVIDIA NeMo on custom speech data. Supports English plus 11 languages including Hindi, Arabic, Mandarin, and Spanish. Real-world deployment: Caterpillar's Cat AI Assistant runs Riva on Jetson Thor inside heavy construction machinery — offline, no cloud dependency, full operator voice interaction.

AMD alternative: stitch Whisper + Coqui TTS + pyannote-audio together manually. No enterprise support. No unified gRPC API. No SLA. No fine-tuning pipeline.

**NVIDIA Maxine** — audio and video enhancement SDK: real-time noise suppression, acoustic echo cancellation, room reverb removal, background replacement, video super-resolution. Used in Cisco and Zoom integrations. For voice AI in call centers, noise suppression before ASR is not optional — it is the difference between 10% WER and 25% WER in a noisy environment.

AMD alternative: none.

**NVIDIA ACE (Avatar Cloud Engine)** — digital human platform: Riva (voice) + Audio2Face (lip sync and facial animation from audio signal) + Nemotron LLM (dialogue) + P-Flow voice cloning from 30 minutes of audio, all packaged as NIM microservices. Partners: Convai, Inworld, UneeQ, SoftServe. Deployed in customer service kiosks, retail concierges, healthcare reception, and gaming NPCs rendered in Unreal Engine 5.

AMD alternative: none.

The three form a natural progression: Riva for the voice backend, Maxine for audio quality on the wire, ACE for animated avatar frontend. A hospital reception kiosk or bank branch digital concierge built on ACE is locked to NVIDIA at every layer of the stack — not by contract, but by the absence of any AMD-equivalent component at any layer.

---

### Layer 4 — Edge Hardware and SDK (Jetson versus nothing)

**NVIDIA Jetson** is the dominant embedded AI compute platform: hardware modules from Jetson Nano (entry-level, ~$100) to Jetson AGX Orin (64GB, 275 TOPS) to Jetson Thor (next-gen, 241 TOPS with MIG). JetPack OS ships with Riva, vLLM, NemoClaw agentic framework, and full CUDA stack. Certified OEM hardware partners include ADLINK, Siemens, and KUKA. Industries served: retail kiosks, smart factory floor copilots, autonomous mobile robots, agricultural drones, in-vehicle assistants.

The Caterpillar case study is the clearest signal of where this is heading: Jetson Thor + Riva ASR (Nemotron speech models) + Qwen3 4B via vLLM, running entirely on-device inside a bulldozer cab. No cloud, no latency, full privacy. This is the template for embedded voice AI across heavy industry, healthcare, and automotive.

AMD's answer: **Ryzen AI NPU** runs Whisper BFP16 locally on a laptop. It works. But there is no industrial edge module, no JetPack-equivalent OS image, no certified hardware partners for robotics or kiosk deployment, no AMD reference design for an offline factory floor voice copilot.

Ryzen AI NPU addresses the developer laptop. Jetson addresses every physical deployment at the edge. These are different markets with different buyer profiles — and only NVIDIA is present in the physical deployment market.

---

### Layer 5 — Cloud Marketplace Slots

| Platform | NVIDIA | AMD |
|---|---|---|
| **Azure AI Foundry** | NIM native integration (July 2026) | Not present |
| **HuggingFace Inference Endpoints** | T4, A10G, A100, H100 selectable | Not selectable — despite formal AMD–HF partnership |
| **AWS SageMaker** | Triton available, NIM containers supported | Limited |
| **Google Vertex AI** | Triton available | Limited |
| **Oracle Cloud AI** | Triton available | Not present |

The Hugging Face Inference Endpoints gap is the sharpest example of the pattern. AMD has a formal hardware partnership with Hugging Face. The TGI ROCm Docker image is production-ready and supports MI210, MI250, and MI300X. Flash Attention 2, AWQ quantization, and DeepSpeed are all validated on AMD. The engineering work is done. But when a developer opens the HF Inference Endpoints UI and clicks "deploy this Whisper model" or "deploy this Llama model," MI300X does not appear in the GPU dropdown. NVIDIA T4 through H100 does. The developer selects NVIDIA — not because AMD cannot run the model, but because AMD is not on the menu.

That is the ecosystem gap in its simplest form. It is not a silicon gap. It is a slot gap.

---

### The complete gap map

```
                         NVIDIA                           AMD
                         ──────                           ───

Framework plugins        LangChain · LlamaIndex           ──
                         Haystack · Pipecat · LiveKit

Serving infra            Triton/Dynamo-Triton             vLLM ROCm (Jan 2026,
                         TensorRT-LLM                     first-class)
                                                          TRT-LLM equivalent: none

Voice domain SDKs        Riva · Maxine · ACE              ──

Edge platform            Jetson (Nano → AGX Orin → Thor)  Ryzen AI NPU (laptops only)
                         JetPack OS · NemoClaw
                         Certified OEM partners

Cloud marketplace        Azure AI Foundry                  ──
                         HF Inference Endpoints
                         AWS SageMaker · GCP Vertex
```

---

### Where AMD can move fast — ranked by effort versus impact

Three of the five layers have low engineering cost because the underlying capability already exists:

**1. HuggingFace Inference Endpoints — 0 engineering weeks, 1 business conversation.**
TGI ROCm is production-ready. AMD needs one commercial agreement with Hugging Face to make MI300X appear as a selectable GPU option. This is the highest-leverage action available: every model deployment that flows through HF Inference Endpoints — voice, LLM, embedding — would immediately have an AMD option. The developer does not need to know anything about ROCm.

**2. LangChain / LlamaIndex / Haystack packages — 2–4 engineering weeks each.**
AMD ROCm already serves OpenAI-compatible endpoints via vLLM. A `langchain-amd` package is a thin wrapper that registers AMD NIM-equivalent endpoints with documented model names, authentication, and examples. The LangChain integration architecture is public. LlamaIndex and Haystack follow the same pattern. Three packages, six to eight weeks total, covering the entire agentic AI framework layer.

**3. Pipecat AMD processor PyPI plugin — 2 weeks (already identified in §14).**

**4. Triton adoption for ROCm — 12–16 weeks.**
Triton is open-source (BSD-3). AMD could certify and ship a `triton-rocm` Docker image — Triton backend running on MI300X with ROCm runtime. This is bounded engineering work, not a rewrite. It closes the model-serving infrastructure gap and gives enterprises a path to run their existing Triton-based pipelines on AMD hardware without rewriting serving logic.

**5. Jetson-equivalent edge platform — 2–3 years.**
This requires hardware: a compact, industrial-grade AMD module with fixed power envelope, certified thermal design, and software stack. Not a laptop chip. This is a product strategy decision, not an engineering sprint. The window is open because Jetson is still scaling — but the longer AMD waits, the deeper the OEM certification moats become.

---

### What closes the voice AI gap specifically

A voice AI developer building on LangChain + Pipecat + HuggingFace today touches NVIDIA at five points before writing a single line of business logic:

1. `ChatNVIDIA` endpoint in LangChain
2. NVIDIA processor in Pipecat
3. NVIDIA GPU in HF Inference Endpoints
4. NVIDIA Triton serving the ASR and TTS models
5. NVIDIA Riva if they want enterprise support

Close points 1, 2, and 3 — the three lowest-effort items above — and AMD becomes visible to that developer at the moment of first contact. Points 4 and 5 can follow once the developer is already building on AMD hardware. The same snowball logic that made NVIDIA the default runs in both directions: make AMD the path of least resistance at the first touchpoint, and the rest of the stack follows adoption.

---

## 16. The Four Upstream Gaps — What §14 and §15 Did Not Cover

Sections 14 and 15 map the downstream gaps: the framework plugins, serving containers, cloud marketplace slots, and edge hardware that AMD is absent from. Those are real and closeable. But there are four upstream gaps that operate at a different layer — they happen before a model is ever deployed, before a developer picks a framework, and before an enterprise issues a purchase order. Closing only the downstream gaps puts AMD in the running for inference workloads. Closing the upstream gaps is what creates platform momentum.

---

### Gap 1 — The Training and Fine-Tuning Moat

Everything in §14 and §15 assumes AMD competes at inference time. The implicit assumption is that a model already exists and a developer just needs to serve it. That is the smaller half of the problem.

Voice AI companies do not just serve pre-trained models. They fine-tune on proprietary data continuously: custom ASR acoustic models trained on their customers' speech (medical transcription, legal dictation, financial advisory), custom TTS voice clones trained to sound like a brand's specific voice persona, custom NLU models trained on domain-specific intents. This fine-tuning loop runs weekly or monthly in production. The toolchain it runs through is entirely NVIDIA-anchored:

**NVIDIA NeMo** is the training and fine-tuning framework purpose-built for speech and language models. It provides recipes for ASR fine-tuning (Conformer, Parakeet), TTS voice cloning (FastPitch, HiFi-GAN), and LLM instruction tuning — all with Triton export as the final step. A company that fine-tunes a Riva ASR model using NeMo gets a TensorRT-optimized artifact that deploys directly to Triton. The entire pipeline from raw audio to production microservice is one command.

**Critical library gaps on AMD:**

| Library | Role | AMD ROCm status |
|---|---|---|
| `bitsandbytes` | Most-used quantization lib (4-bit, 8-bit) | No official support — community fork only |
| `trl` (HuggingFace) | RLHF and fine-tuning framework | CUDA-primary; ROCm experimental |
| `Axolotl` | Most popular open-source fine-tuning tool | CUDA-primary; ROCm untested |
| `PEFT` | LoRA, QLoRA adapters | Works but less tested on AMD |
| FlashAttention 3 | Fastest attention kernel (Hopper-only) | No AMD equivalent — FA2 exists, not FA3 |
| NVIDIA CUTLASS | High-performance CUDA matrix kernel templates | AMD CK (Composable Kernel) exists, far smaller ecosystem |

The consequence is direct: a voice AI company that fine-tunes its ASR model using NeMo is not going to switch GPU vendors for inference. The training moat creates inference lock-in. The model's artifact, optimization flags, quantization format, and deployment recipe are all NVIDIA-native. Re-running fine-tuning on AMD requires porting the recipe, validating outputs, and re-benchmarking — cost with no revenue upside. Companies do not do this.

**What AMD needs here:** Official ROCm support in `bitsandbytes` (the engineering work exists in the community fork — needs AMD to adopt and maintain it); a NeMo-equivalent speech training framework or a certified NeMo-ROCm Docker image; FlashAttention 3 port or a competitive replacement kernel for CDNA3 architecture.

---

### Gap 2 — The ISV and SI Sales Channel Moat

The article focuses on developers choosing frameworks. Enterprises do not choose GPU vendors directly. They buy software from independent software vendors (ISVs) and deploy through systems integrators (SIs). The GPU is chosen implicitly by the ISV's architecture decision, made years before the enterprise procurement conversation.

**ISV integrations NVIDIA has in voice AI:**

- **Genesys** (largest global contact center platform, 11,000+ enterprise customers) — NVIDIA GPU-backed real-time agent assist and post-call analytics
- **Salesforce Einstein Voice** — NVIDIA inference backend for voice-to-CRM transcription and intent extraction
- **Cisco Webex** — NVIDIA Maxine noise suppression and transcription baked into the product; not a feature toggle, it is the product
- **ServiceNow Now Assist** — NVIDIA NIM backend for voice-triggered workflow automation
- **Five9, NICE CXone, Avaya** — contact center platforms with NVIDIA integrations

When an enterprise's procurement team selects Genesys or Cisco Webex, AMD is not in the conversation. The GPU vendor was selected when Genesys chose its AI stack. AMD has no presence in any of the major contact center ISV platforms.

**SI certification moat:** NVIDIA has formally certified TCS, Infosys, Wipro, Accenture, and Capgemini as NVIDIA NIM implementation partners. These SIs now sell NVIDIA-based voice AI to their Fortune 500 clients as a packaged offering. An SI's certified practice is built around NVIDIA tooling — their engineers are trained on it, their delivery playbooks reference it, their pre-sales demos run on it. A client asking for AMD would require the SI to rebuild its practice from scratch. SIs do not do this unless a client specifically mandates it — and no client mandates AMD because no client has been sold AMD.

**What AMD needs here:** Three to five direct ISV integration partnerships (Genesys is the highest leverage — it reaches more enterprise contact center seats than any other platform). An SI certification program equivalent to NVIDIA's NIM partner program. Without SI certification, AMD hardware will not appear in enterprise voice AI bids regardless of technical merit.

---

### Gap 3 — Voice Plus Vision Convergence

The article treats voice AI in isolation. That is accurate for 2024 deployments but increasingly wrong for 2026 and beyond. The next generation of deployed voice AI agents — retail kiosks, factory floor copilots, healthcare reception desks, in-vehicle assistants, delivery robots — combine voice with vision. A camera observes the environment or the person; a microphone captures speech; the system integrates both to respond appropriately.

**NVIDIA's unified multi-modal story:**

```
Jetson Thor (edge compute)
    ├── Isaac (robotics vision + manipulation)
    ├── Metropolis (retail + industrial video analytics)
    ├── Riva (voice ASR + TTS)
    ├── ACE (avatar + face animation)
    └── Cosmos (world model for synthetic training data)

All on one CUDA substrate. One SDK. One vendor relationship.
```

Real-world example: the Caterpillar Cat AI Assistant on Jetson Thor combines obstacle detection (vision via Isaac), operator voice commands (Riva ASR), response generation (Qwen3 4B via vLLM), and spoken response (Riva TTS) — all on a single embedded module inside a bulldozer cab. A Siemens factory copilot combines machine vision (anomaly detection) with natural language operator guidance using the same stack.

When voice AI companies grow their product to include a camera — and they will, because vision context dramatically improves voice agent responses — they stay on NVIDIA because AMD has no landing zone for them. AMD has:

- **Instinct MI300X** — data center inference (no vision pipeline)
- **Ryzen AI NPU** — laptop on-device inference (no industrial form factor)
- **Radeon GPUs** — graphics and gaming (separate driver stack, not integrated with ROCm)

No unified edge module. No certified hardware for industrial deployment. No multi-modal SDK that bridges voice and vision on a single AMD device. The product gap here is not a missing library — it is a missing product category.

**What AMD needs here:** A Jetson-equivalent embedded AI module — compact, fixed power envelope, thermally certified for industrial environments — with a unified SDK that runs ROCm-based voice and vision pipelines on the same device. This is a 2–3 year hardware roadmap decision, not an engineering sprint. Every quarter AMD waits, Jetson OEM certifications deepen.

---

### Gap 4 — Synthetic Data Pipeline for Low-Resource Languages

Training high-quality ASR for low-resource languages requires synthetic speech data. Real transcribed audio in Hindi, Bengali, Tamil, Telugu, Swahili, or Filipino is scarce — not because the languages are rare, but because the recording and transcription infrastructure to produce training-grade data has never been systematically built for these markets.

NVIDIA's answer is the **Nemotron synthetic data pipeline** — a system that generates diverse, high-quality synthetic speech from text, including varied accents, speaking rates, background conditions, and speaker demographics. This is what enables training ASR at scale for languages where real data is thin. Sarvam AI, Gnani.ai, and AI4Bharat (IIT Madras) — the three organizations building India's language model foundation — all trained on NVIDIA DGX clusters, using NVIDIA-native pipelines.

The consequence compounds: even if AMD wins an inference contract for a Sarvam-based voice agent, the Sarvam model was trained on NVIDIA. Its fine-tuning requires NVIDIA-compatible tooling. Its next version will be trained on NVIDIA. The model's entire lifecycle is anchored to NVIDIA before it reaches a production AMD server.

**The data flywheel:** NVIDIA's synthetic data pipeline feeds training, which produces better models, which attract more voice AI companies, which generate more fine-tuning data, which trains better models. AMD is not in this loop at any point. AMD has no synthetic speech data generation capability, no partnership with AI4Bharat or Sarvam for training compute, no AMD-sponsored voice dataset for Indian or African or Southeast Asian languages.

For the India opportunity specifically (§10), this matters enormously. India's 22 official languages represent a 1.4-billion-person market where the quality of language models determines which company wins. Every model trained on NVIDIA infrastructure creates a training-data dependency that outlasts the initial compute decision.

**What AMD needs here:** An AMD-sponsored voice data initiative for high-priority markets — a partnership with AI4Bharat or a similar academic institution to fund transcription and annotation of 10,000+ hours of speech per language, with AMD compute provided for training. Cost: approximately $2–5M in compute credits and $3–8M in data collection over two years. Return: model ecosystem that is AMD-native from inception, not ported from NVIDIA as an afterthought.

---

### The complete gap map — all layers

```
Layer                    NVIDIA                           AMD
─────────────────────────────────────────────────────────────────────
Synthetic data           Nemotron pipeline                ──
(upstream of training)   Cosmos world models

Training / fine-tuning   NeMo · TensorRT-LLM              vLLM ROCm (inference)
                         bitsandbytes · FA3               bitsandbytes: community fork
                         CUTLASS kernels                  CK: smaller ecosystem

Framework plugins        LangChain · LlamaIndex           ──
(§15 Layer 1)            Haystack · Pipecat · LiveKit

Serving infra            Triton/Dynamo-Triton             vLLM ROCm (Jan 2026)
(§15 Layer 2)            TensorRT-LLM                     Triton ROCm: not shipped

Voice domain SDKs        Riva · Maxine · ACE              ──
(§15 Layer 3)

Edge platform            Jetson (Nano→Thor)                Ryzen AI NPU (laptops only)
(§15 Layer 4)            JetPack · Isaac · Metropolis      No industrial module

Cloud marketplace        Azure AI Foundry                  ──
(§15 Layer 5)            HF Inference Endpoints
                         AWS SageMaker · GCP Vertex

ISV integrations         Genesys · Salesforce             ──
(§16 Gap 2)              Cisco · ServiceNow
                         Five9 · NICE CXone

SI certification         TCS · Infosys · Wipro             ──
(§16 Gap 2)              Accenture · Capgemini

Multi-modal              Isaac · Metropolis · Cosmos       ──
(§16 Gap 3)              ACE · Jetson unified stack
```

---

### 17  Prioritized AMD action roadmap across all layers

| Action | Effort | Time horizon | Impact |
|---|---|---|---|
| HF Inference Endpoints slot | Business negotiation | 0–4 weeks | High — immediate developer visibility |
| LangChain / LlamaIndex / Haystack packages | 2–4 weeks each | 1–2 months | High — agentic AI framework layer |
| Pipecat AMD processor (PyPI) | 2 weeks | 1 month | Medium — voice AI developer niche |
| Official `bitsandbytes` ROCm support | 4–6 weeks | 2 months | High — unlocks fine-tuning ecosystem |
| Triton ROCm certified image | 12–16 weeks | 4 months | High — closes serving infra gap |
| Genesys ISV integration | Business development | 6–12 months | Very high — enterprise channel access |
| SI certification program (TCS/Infosys/Wipro) | Program build | 6–12 months | Very high — enterprise sales channel |
| AMD voice data initiative (India 22 languages) | $5–13M, 2 years | 18–24 months | Strategic — model ecosystem ownership |
| FlashAttention 3 port or CDNA3 equivalent | 16–24 weeks | 6 months | Medium — fine-tuning performance |
| Jetson-equivalent industrial edge module | Hardware roadmap | 2–3 years | Very high — physical deployment market |

The first four items require no new silicon, no new partnerships, and no new product categories. They are software and business development actions that close the most visible gaps — the ones a developer or enterprise architect encounters on day one. The remaining items require progressively more strategic commitment but address progressively more durable lock-in. The window on the ISV integrations and SI certification program is closing: every year NVIDIA's enterprise relationships deepen, and the cost of displacing them rises.



## 18. Softpower: The Ecosystem Moat NVIDIA Built and How PAVS Delivers the AMD Answer

*Proposed title for chapter_14_15_16.tex:*
**"Softpower: AMD’s Ecosystem Deficit Across Frameworks, Serving, and Edge — and the PAVS Response"**

---

### What Softpower Means in This Context

Sections 14, 15, and 16 document a specific category of competitive disadvantage: not a silicon gap, not a raw performance gap, but a **software ecosystem gap** — the gap between AMD being present as hardware and AMD being present as the **default choice** when a developer types a package name, clicks a deploy button, or scaffolds a new agent project.

NVIDIA’s dominance is not primarily about CUDA performance. It is about **softpower**: the accumulation of named packages, certified containers, framework plugins, cloud marketplace slots, ISV integrations, and SI certification programs that make NVIDIA the path of least resistance at every decision point in the developer journey. The developer who types `langchain-nvidia-ai-endpoints`, `docker pull nvcr.io/nvidia/tritonserver`, or opens the Hugging Face Inference Endpoints UI is not making a GPU decision — they are following the defaults. AMD is absent from the defaults.

This is what softpower means: the ability to win workloads before the hardware decision is ever explicitly made.

The gap map from §15 summarizes it starkly:

```
Framework plugins      NVIDIA: LangChain · LlamaIndex · Haystack · Pipecat · LiveKit
                       AMD:    ——

Inference serving      NVIDIA: Triton/Dynamo · TensorRT-LLM
                       AMD:    vLLM ROCm (Jan 2026, first-class) · Triton ROCm: not shipped

Voice-domain SDKs      NVIDIA: Riva · Maxine · ACE
                       AMD:    ——

Edge platform          NVIDIA: Jetson (Nano→Thor) · JetPack · Isaac · Metropolis
                       AMD:    Ryzen AI NPU (laptops only) · no industrial module

Cloud marketplace      NVIDIA: HF Endpoints · Azure AI Foundry · SageMaker · Vertex AI
                       AMD:    not selectable despite formal HF partnership
```

The training and fine-tuning moat (§16 Gap 1), the ISV/SI sales channel (§16 Gap 2), the voice+vision convergence gap (§16 Gap 3), and the synthetic data deficit (§16 Gap 4) compound on top of this. Each layer reinforces the others. A developer who fine-tunes on NeMo gets a TensorRT artifact; the TensorRT artifact deploys to Triton; Triton is the substrate inside Genesys; Genesys was sold by a TCS SI practice certified on NIM. AMD is absent from every link in that chain.

---

### PAVS: AMD’s Organizational Answer to the Softpower Gap

AMD created the **Physical AI and Vertical Software (PAVS)** team to directly address this gap. PAVS is not a marketing team — it is an engineering team that takes raw researcher output from AMD’s AI Group (AIG) and converts it into production-grade vertical software that developers and enterprise customers can actually use.

The organizational logic is precise:

- **AIG** produces models and research artifacts — scripts, weights, benchmark results
- **PAVS** takes those artifacts and converts them into structured, deployable, ecosystem-ready software
- **Robotics pipelines** sit on top of PAVS outputs, building accelerated multi-model pipelines for physical deployment
- **Developer kits** package the full stack — hardware + SDK + certified pipelines — into a form factor that competes with Jetson

This is the missing layer. NVIDIA’s softpower is not just CUDA — it is the team that turned CUDA into Triton, Triton into NIM, NIM into ISV integrations, and ISV integrations into enterprise sales. PAVS is AMD’s equivalent: the organizational unit that closes the distance between raw silicon capability and developer adoption.

---

### Layer 1: Physical AI SDK — The Model and Inference Supply Layer

At the foundation of the PAVS stack sits the **Physical AI SDK**: a unified software platform that integrates AMD’s ROCm and Ryzen AI software stacks on embedded x86 APUs.

The SDK’s core capability is **concurrent heterogeneous inference** — the ability to run multiple model types simultaneously across CPU, GPU, and NPU, each assigned to the compute resource that fits it:

```
Physical AI SDK — Inference Substrate
├── CNN / ViT models          → GPU (MIGraphX, ONNX Runtime)
├── LLM / VLM models          → GPU + CPU (vLLM, llama.cpp)
├── VLA models                → NPU + GPU (Ryzen AI + ROCm)
└── Real-time CV pipelines    → NPU (Ryzen AI, <10ms latency)

Supported frameworks: ONNX · PyTorch · vLLM · llama.cpp
```

This is what NVIDIA’s JetPack does on Jetson: a unified runtime that routes inference workloads to the right compute unit without the developer managing it manually. The Physical AI SDK is AMD’s equivalent for embedded x86 APUs.

The developer experience is deliberately Jetson-like: one-click installation, a Make-based uniform interface that works identically across every example (`make benchmark-gpu`, `make benchmark-npu`, `make benchmark-all-devices`), pre-generated `METRICS_TABLE.md` with CPU/GPU/NPU throughput and latency numbers, and a Docker path that bypasses installation complexity entirely.

PAVS converts raw AIG researcher code — a single script with no structure, no device flows, no test suite — into production-ready vertical software:

```
AIG Research Output          PAVS Vertical Software Output
────────────────────         ─────────────────────────────
rocm-scripts/test/           examples/yolov12/
  pytorch/yolo12n.py    →      Makefile
                               METRICS_TABLE.md
                               app/ (routes, services, main.py)
                               scripts/ (benchmark, export, profile)
                               tests/ (API, Docker, device-specific)
                               requirements_{cpu,gpu,npu}.txt
```

Same model. Production-grade structure. Every device. The difference between a proof-of-concept that lives in a researcher’s laptop and a software asset that an enterprise can deploy.

---

### Layer 2: Robotics Pipelines — Accelerated Multi-Model Inference on Physical AI SDK

On top of the Physical AI SDK, **robotics pipelines** build the next abstraction layer: accelerated, real-time, multi-model pipelines designed for physical deployment scenarios — factory floor, warehouse, autonomous vehicle, drone, kiosk.

A robotics pipeline is not a single model. It is a **graph of models executing concurrently**, each model consuming the output of the previous stage:

```
Robotics Pipeline (example: factory floor copilot)
────────────────────────────────────────────────────
Camera feed
    └── [NPU] Obstacle detection (YOLOv12) → spatial map
                └── [GPU] VLM scene understanding (LLaVA) → context
                            └── [GPU] LLM response (Llama 3.1 8B) → text
                                        └── [CPU] TTS synthesis (Kokoro) → audio
                                                    └── Speaker output

All stages run on a single AMD Ryzen AI APU.
Pipeline latency target: <300ms end-to-end.
```

The Physical AI SDK provides the heterogeneous inference substrate that makes this pipeline possible — each stage is dispatched to the appropriate compute unit without inter-process serialization overhead. The robotics pipeline layer adds the **domain-specific orchestration**: the voice interaction loop, the vision context injection, the action policy inference for VLA models.

This is the architectural pattern NVIDIA has productized with Isaac (robotics), Metropolis (video analytics), and Riva (voice), all running on JetPack. PAVS’s robotics pipelines are AMD’s equivalent — not yet unified under a single brand name, but functionally composing the same layers from AMD’s stack.

---

### Layer 3: The Developer Kit — AMD’s Jetson Moment

The output of PAVS — Physical AI SDK + robotics pipelines + certified model zoo — combines with AMD’s embedded Ryzen AI APU hardware into a **developer kit** that addresses the same market Jetson addresses: embedded AI compute for physical deployment.

The Jetson comparison is direct:

| Capability | NVIDIA Jetson | AMD PAVS DevKit |
|---|---|---|
| **Form factor** | Compact module (Nano→Thor) | Ryzen AI embedded APU module |
| **OS + SDK** | JetPack (Ubuntu + CUDA + Riva + Isaac) | Physical AI SDK (ROCm + Ryzen AI + pipeline library) |
| **Model supply** | NVIDIA NIM containers | AIG model zoo → PAVS vertical software |
| **Inference runtime** | TensorRT + Triton | vLLM + MIGraphX + llama.cpp + ONNX |
| **Robotics support** | Isaac (vision + manipulation) | Robotics pipelines (accelerated multi-model) |
| **Voice support** | Riva (ASR + TTS + NMT) | Whisper + Kokoro + PAVS pipeline |
| **Multi-modal** | Isaac + Riva + ACE unified | VLM + VLA on same NPU/GPU |
| **Target markets** | Industrial, healthcare, automotive, robotics | Industrial, healthcare, automotive, robotics |

The critical distinction from Jetson is the compute architecture: Ryzen AI APUs combine x86 CPU, RDNA GPU, and XDNA NPU on a single die, with a unified memory architecture that eliminates the CPU↔GPU memory copy overhead that limits Jetson for workloads that mix heavy LLM inference (GPU) with low-latency vision (NPU). For VLA models — the emerging class of models that output robot actions directly from visual + language inputs — the NPU+GPU architecture may prove more efficient than Jetson’s ARM+CUDA stack.

The developer kit is not yet shipping with the full ISV certification ecosystem that JetPack carries. That is the gap §16 Gap 2 describes. But the technical foundation — unified SDK, heterogeneous inference, robotics pipelines, voice pipeline, multi-modal VLM/VLA support — is being assembled by PAVS now.

---

### The Softpower Roadmap: From SDK to Ecosystem

Closing the softpower gap described in §14–§16 requires PAVS to operate at all three layers simultaneously:

```
Softpower Layer          PAVS Action
────────────────         ────────────────────────────────────────────────
Framework plugins        Pipecat AMD processor · LangChain/LlamaIndex packages
(§14, §15 Layer 1)       → developer picks AMD at pip install time

Inference serving        vLLM ROCm (done) · Triton ROCm certified image
(§15 Layer 2)            → operator picks AMD at docker pull time

Voice + vision SDK       Physical AI SDK pipelines for ASR + TTS + CV
(§15 Layer 3)            → enterprise picks AMD at architecture review time

Edge platform            PAVS DevKit = Physical AI SDK + robotics pipelines
(§15 Layer 4)            → OEM picks AMD at hardware design-in time

Training ecosystem       NeMo-ROCm certified image · bitsandbytes ROCm
(§16 Gap 1)              → model developer picks AMD at training time

ISV / SI channel         PAVS-led SI certification program
(§16 Gap 2)              → enterprise never has to explicitly pick — AMD is the default
```

Each layer of the PAVS platform closes a specific slot in the gap map. The Physical AI SDK closes the serving layer and edge platform layer. The robotics pipelines close the multi-modal convergence gap. The developer kit closes the Jetson gap. The framework plugins and SI certification program close the softpower layer where NVIDIA currently wins without the customer ever making a GPU decision.

The window is not closed. The framework slots are closeable in weeks. The serving infrastructure is closeable in months. The edge platform and robotics pipelines are being built now. The ISV and SI relationships are the longest lead time — but they are the ones that create durable lock-in, for AMD rather than against it.

PAVS is the organizational structure AMD needed to execute this. Physical AI SDK is the foundation. The robotics pipelines and developer kit are the product. The ecosystem integrations are the moat.

---

## Paper Title

**"Bridging AMD's Softpower Gap: Physical AI Vertical Software Through the Voice AI Lens"**

---

## 19. The Chance to Bridge: Why PAVS Is Positioned to Deliver AMD's Softpower

PAVS was not created to close AMD's ecosystem gap. Its founding mission is specific: take model outputs from AMD's AI Group and bring them to lighthouse customers — early adopters who work closely with AMD to validate and deploy these models in real environments. That is the job. Customer delivery, not platform strategy.

But that job creates an unusual structural position. PAVS sits exactly at the intersection where AMD's softpower gap is most visible and most closeable:

```
AMD AI Group (AIG)              Lighthouse Customers
  ↓ models + research              ↑ deployment feedback
         ↓                        ↑
              [ PAVS ]
         ↓                        ↑
  Physical AI SDK          Robotics pipelines + devkit
  (inference substrate)    (vertical software layer)
```

Every time PAVS converts a raw AIG model into production-ready vertical software for a lighthouse customer, it is doing — unintentionally, organically — exactly what NVIDIA's platform teams do intentionally: it is turning hardware capability into software that developers and customers can adopt without understanding the hardware beneath it.

That is the chance.

The Voice AI analysis in §14–§16 makes the gap visible through a specific domain. But the pattern is not specific to voice. The same softpower deficit shows up in robotics (no Isaac equivalent), in industrial inspection (no Metropolis equivalent), in healthcare imaging (no certified clinical inference pipeline), in automotive (no JetPack for embedded x86). Every domain where PAVS is working with a lighthouse customer is a domain where AMD's softpower gap is real and where PAVS's vertical software work directly addresses it.

PAVS does not need to change its mission to bridge the gap. The bridge is already being built — through Physical AI SDK, through robotics pipelines, through the devkit that emerges from lighthouse deployments. What changes is recognizing that this customer delivery work is also ecosystem building, and treating it as such:

- Each lighthouse deployment that produces a reusable pipeline is a step toward an AMD-native software ecosystem
- Each model the Physical AI SDK supports is a model that no longer requires NVIDIA tooling to deploy on AMD hardware
- Each robotics pipeline that runs on Ryzen AI APU is a reference design that an OEM, SI, or ISV can build on

The window to build this is open. NVIDIA's Jetson ecosystem deepens every quarter. Its NIM integrations expand. Its SI certifications multiply. The cost of displacing those relationships rises with each passing quarter. But the softpower gap is not a hardware problem — it cannot be closed by a new chip. It is a software and ecosystem problem, which means it is exactly the kind of problem that an engineering team doing vertical software delivery is positioned to solve.

PAVS is that team. The lighthouse customer work is the method. The chance to bridge AMD's softpower gap is now.