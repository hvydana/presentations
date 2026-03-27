#!/usr/bin/env python3
"""Convert Marp markdown to editable PPTX - Clean version."""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

LOGO_PATH = "/home/amd/Work/presentations/themes/pavs-logo.png"

def add_footer(slide, page_num, total_pages):
    """Add footer with logo and page number."""
    # Add logo in bottom right
    logo = slide.shapes.add_picture(LOGO_PATH, Inches(11.5), Inches(6.85), height=Inches(0.45))

    # Add page number
    page_box = slide.shapes.add_textbox(Inches(12.6), Inches(6.95), Inches(0.5), Inches(0.3))
    p = page_box.text_frame.paragraphs[0]
    p.text = str(page_num)
    p.font.size = Pt(12)
    p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

def create_pptx(output_file):
    """Create a clean, editable PPTX."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Colors
    BG_DARK = RGBColor(0x1a, 0x1a, 0x1a)
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)
    RED = RGBColor(0xED, 0x1C, 0x24)
    GRAY = RGBColor(0xAA, 0xAA, 0xAA)

    blank_layout = prs.slide_layouts[6]

    # ==================== SLIDE 1 ====================
    slide1 = prs.slides.add_slide(blank_layout)
    slide1.background.fill.solid()
    slide1.background.fill.fore_color.rgb = BG_DARK

    # Title
    title = slide1.shapes.add_textbox(Inches(0.4), Inches(0.25), Inches(12.5), Inches(0.5))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Physical AI SDK: 2026 Model Lifecycle & Delivery Strategy"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Red line under title
    line = slide1.shapes.add_shape(1, Inches(0.4), Inches(0.75), Inches(12.5), Pt(3))
    line.fill.solid()
    line.fill.fore_color.rgb = RED
    line.line.fill.background()

    # LEFT COLUMN - What We're Delivering
    left_title = slide1.shapes.add_textbox(Inches(0.4), Inches(1.0), Inches(6), Inches(0.4))
    p = left_title.text_frame.paragraphs[0]
    p.text = "What We're Delivering"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Lifecycle diagram
    lifecycle = slide1.shapes.add_textbox(Inches(0.4), Inches(1.45), Inches(6), Inches(0.7))
    tf = lifecycle.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ENABLEMENT → BENCHMARKING → PROFILING → FINE-TUNING\n    (1-2 wk)           (3 days)            (3 days)         (2-3 wk)"
    p.font.size = Pt(11)
    p.font.name = "Courier New"
    p.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    lifecycle.fill.solid()
    lifecycle.fill.fore_color.rgb = RGBColor(0xe8, 0xe8, 0xe8)

    # Portfolio targets
    targets = slide1.shapes.add_textbox(Inches(0.4), Inches(2.25), Inches(6), Inches(0.9))
    tf = targets.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2026 Portfolio Targets:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RED

    for bullet in ["20 production-ready models across 6 categories",
                   "3 market segments: Robotics, Healthcare, Industrial",
                   "Unified SDK installer with integrated tooling"]:
        p = tf.add_paragraph()
        p.text = "• " + bullet
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE

    # Model categories table
    table_data = [
        ["Category", "Models", "Status"],
        ["Vision/Detection", "YoloV12, MobileSAM, CrossFormer", "Active"],
        ["VLMs", "Qwen2.5-VL, Qwen3-VL, LLaMA3.2-Vision", "Active"],
        ["LLMs", "DeepSeek-R1", "In Progress"],
        ["Speech", "Whisper (ASR), XTTS (TTS)", "Active"],
        ["3D/Robotics", "CenterPoint, OpenVLA", "In Progress"],
        ["Medical", "MedSigLIP", "In Progress"],
    ]

    tbl = slide1.shapes.add_table(len(table_data), 3, Inches(0.4), Inches(3.55), Inches(6), Inches(2.1)).table
    tbl.columns[0].width = Inches(1.5)
    tbl.columns[1].width = Inches(3.3)
    tbl.columns[2].width = Inches(1.2)

    for row_idx, row in enumerate(table_data):
        for col_idx, cell_text in enumerate(row):
            cell = tbl.cell(row_idx, col_idx)
            cell.text = cell_text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            p.font.color.rgb = WHITE
            if row_idx == 0:
                p.font.bold = True
                cell.fill.solid()
                cell.fill.fore_color.rgb = RED
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(0x2a, 0x2a, 0x2a) if row_idx % 2 else BG_DARK

    # RIGHT COLUMN - Release Roadmap
    right_title = slide1.shapes.add_textbox(Inches(6.8), Inches(1.0), Inches(6), Inches(0.4))
    p = right_title.text_frame.paragraphs[0]
    p.text = "2026 Release Roadmap"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = WHITE

    roadmap_items = [
        ("R1: Foundation", ["Lifecycle framework operational", "CI/CD automation & GitHub Pages docs", "Release logistics streamlined"]),
        ("R2: Scale", ["8 production-ready models (P0/P1)", "Single SDK installer", "Quantization & Infra Beta (vLLM, ONNX-RT, Llama.cpp)", "Sample apps: ChatBot, Object Detection, GStreamer+ROCm"]),
        ("R3: Expand", ["8 additional models (16 total)", "Enhanced quantization & profiling tools", "Robotics simulator integration", "Model deployment infrastructure"]),
        ("R4: Production", ["20 total production models", "Multi-segment deployment ready", "Model training infrastructure (Drafter)", "2027 strategy planning"]),
    ]

    y = 1.45
    for phase, bullets in roadmap_items:
        phase_box = slide1.shapes.add_textbox(Inches(6.8), Inches(y), Inches(6), Inches(0.3))
        p = phase_box.text_frame.paragraphs[0]
        p.text = phase
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = RED
        y += 0.32

        for bullet in bullets:
            bullet_box = slide1.shapes.add_textbox(Inches(6.8), Inches(y), Inches(6), Inches(0.25))
            p = bullet_box.text_frame.paragraphs[0]
            p.text = "• " + bullet
            p.font.size = Pt(11)
            p.font.color.rgb = WHITE
            y += 0.24
        y += 0.1

    # ==================== SLIDE 2 ====================
    slide2 = prs.slides.add_slide(blank_layout)
    slide2.background.fill.solid()
    slide2.background.fill.fore_color.rgb = BG_DARK

    # Title
    title2 = slide2.shapes.add_textbox(Inches(0.4), Inches(0.25), Inches(12.5), Inches(0.5))
    p = title2.text_frame.paragraphs[0]
    p.text = "Open Source Distribution & Team Collaboration Model"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE

    line2 = slide2.shapes.add_shape(1, Inches(0.4), Inches(0.75), Inches(12.5), Pt(3))
    line2.fill.solid()
    line2.fill.fore_color.rgb = RED
    line2.line.fill.background()

    # LEFT COLUMN - Distribution Strategy
    left_title2 = slide2.shapes.add_textbox(Inches(0.4), Inches(1.0), Inches(6), Inches(0.4))
    p = left_title2.text_frame.paragraphs[0]
    p.text = "GitHub + HuggingFace Release Strategy"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = WHITE

    publish_label = slide2.shapes.add_textbox(Inches(0.4), Inches(1.45), Inches(6), Inches(0.3))
    p = publish_label.text_frame.paragraphs[0]
    p.text = "What We Publish:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    publish_items = [
        "Pre-optimized model weights (ONNX, TensorRT, ROCm)",
        "Quantized variants (INT8, FP16) for edge deployment",
        "Docker containers (GPU/NPU/Hybrid ready)",
        "Verified benchmark results & model cards"
    ]
    y = 1.75
    for item in publish_items:
        box = slide2.shapes.add_textbox(Inches(0.4), Inches(y), Inches(6), Inches(0.25))
        p = box.text_frame.paragraphs[0]
        p.text = "• " + item
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        y += 0.24

    # CI/CD Pipeline
    pipeline_label = slide2.shapes.add_textbox(Inches(0.4), Inches(y + 0.15), Inches(6), Inches(0.3))
    p = pipeline_label.text_frame.paragraphs[0]
    p.text = "CI/CD Pipeline:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    pipeline = slide2.shapes.add_textbox(Inches(0.4), Inches(y + 0.45), Inches(6), Inches(1.0))
    tf = pipeline.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Dev Branch → PR → Auto Tests → Release Branch\n              ↓\n      Benchmarking + Validation\n              ↓\nGitHub Release → HuggingFace Push → Docs Update"
    p.font.size = Pt(10)
    p.font.name = "Courier New"
    p.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    pipeline.fill.solid()
    pipeline.fill.fore_color.rgb = RGBColor(0xe8, 0xe8, 0xe8)

    # Infrastructure Tools
    infra_label = slide2.shapes.add_textbox(Inches(0.4), Inches(4.6), Inches(6), Inches(0.3))
    p = infra_label.text_frame.paragraphs[0]
    p.text = "Infrastructure Tools:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    tools = ["vLLM - LLM serving & inference", "Llama.cpp - Optimized CPU/GPU inference",
             "ONNX Runtime - Cross-platform deployment", "Lemonade - Performance profiling"]
    y = 4.9
    for tool in tools:
        box = slide2.shapes.add_textbox(Inches(0.4), Inches(y), Inches(6), Inches(0.25))
        p = box.text_frame.paragraphs[0]
        p.text = "• " + tool
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        y += 0.24

    # RIGHT COLUMN - Team Collaboration
    right_title2 = slide2.shapes.add_textbox(Inches(6.8), Inches(1.0), Inches(6), Inches(0.4))
    p = right_title2.text_frame.paragraphs[0]
    p.text = "Team Collaboration Model"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = WHITE

    collab_label = slide2.shapes.add_textbox(Inches(6.8), Inches(1.45), Inches(6), Inches(0.3))
    p = collab_label.text_frame.paragraphs[0]
    p.text = "PAVS (Internal) vs External Partners:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    # Collaboration table
    collab_data = [
        ["Stage", "PAVS Team", "External (MCW/AIG)"],
        ["Enablement", "Lead", "Support"],
        ["Profiling", "Initial", "Deep Analysis"],
        ["Benchmarking", "Setup", "Automation"],
        ["Fine-tuning", "Goals+Lead", "Execution"],
    ]

    tbl2 = slide2.shapes.add_table(len(collab_data), 3, Inches(6.8), Inches(1.8), Inches(5.8), Inches(1.5)).table
    tbl2.columns[0].width = Inches(1.5)
    tbl2.columns[1].width = Inches(2.0)
    tbl2.columns[2].width = Inches(2.3)

    for row_idx, row in enumerate(collab_data):
        for col_idx, cell_text in enumerate(row):
            cell = tbl2.cell(row_idx, col_idx)
            cell.text = cell_text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.font.color.rgb = WHITE
            if row_idx == 0:
                p.font.bold = True
                cell.fill.solid()
                cell.fill.fore_color.rgb = RED
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(0x2a, 0x2a, 0x2a) if row_idx % 2 else BG_DARK

    # Handoff Criteria
    handoff_label = slide2.shapes.add_textbox(Inches(6.8), Inches(3.45), Inches(6), Inches(0.3))
    p = handoff_label.text_frame.paragraphs[0]
    p.text = "Handoff Criteria:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    handoff_items = [
        "Model runs on target hardware",
        "Profiling report complete",
        "Baseline benchmarks established",
        "Optimization opportunities documented"
    ]
    y = 3.75
    for item in handoff_items:
        box = slide2.shapes.add_textbox(Inches(6.8), Inches(y), Inches(6), Inches(0.25))
        p = box.text_frame.paragraphs[0]
        p.text = "• " + item
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        y += 0.24

    # Key Benefits
    benefits_label = slide2.shapes.add_textbox(Inches(6.8), Inches(y + 0.15), Inches(6), Inches(0.3))
    p = benefits_label.text_frame.paragraphs[0]
    p.text = "Key Benefits:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED

    benefits = [
        "Better ROI on external resources",
        "Clear deliverables with measurable outcomes",
        "Faster time to production",
        "PAVS Lead on goal-setting, partners focus on execution"
    ]
    y += 0.45
    for item in benefits:
        box = slide2.shapes.add_textbox(Inches(6.8), Inches(y), Inches(6), Inches(0.25))
        p = box.text_frame.paragraphs[0]
        p.text = "• " + item
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        y += 0.24

    # Add footers to all slides
    total_pages = len(prs.slides)
    for idx, slide in enumerate(prs.slides, 1):
        add_footer(slide, idx, total_pages)

    prs.save(output_file)
    print(f"Created: {output_file}")

if __name__ == '__main__':
    create_pptx('PAVS_2_Slide_Executive_Summary_v3.pptx')
