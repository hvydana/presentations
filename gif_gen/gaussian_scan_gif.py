#!/usr/bin/env python3
"""
Generate an animated GIF showing:
1. BEFORE: Sequential loop scanning through grid (slow)
2. AFTER: Vectorized parallel computation (fast)
"""

import os
import imageio
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, FancyBboxPatch

# Style constants
BG = '#1a1a1a'
FG = '#ffffff'
RED = '#ED1C24'
GREEN = '#4CAF50'
ORANGE = '#FF9800'
CYAN = '#00BCD4'
GRAY = '#888888'

WIDTH, HEIGHT = 1920, 1080
DPI = 100

# Grid configuration
GRID_ROWS = 8
GRID_COLS = 8
TOTAL_CELLS = GRID_ROWS * GRID_COLS

# Output directory
OUT_DIR = 'gaussian_frames'
os.makedirs(OUT_DIR, exist_ok=True)


def create_before_frame(current_row, current_col, frame_idx):
    """BEFORE: Loop-based sequential processing."""
    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    iteration = current_row * GRID_COLS + current_col + 1

    # ========== HEADER ==========
    ax.text(0.5, 0.95, 'BEFORE: Sequential Loop',
            ha='center', va='center', color=RED,
            fontsize=36, fontweight='bold')

    # ========== LEFT SIDE: Grid ==========
    grid_x = 0.06
    grid_y = 0.25
    cell_w = 0.048
    cell_h = 0.062
    grid_w = GRID_COLS * cell_w
    grid_h = GRID_ROWS * cell_h

    ax.text(grid_x + grid_w / 2, 0.87, f'Position  i = {iteration}  of  3,136',
            ha='center', va='center', color=FG, fontsize=20)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * cell_w
            y = grid_y + (GRID_ROWS - 1 - row) * cell_h
            idx = row * GRID_COLS + col
            cur = current_row * GRID_COLS + current_col

            if idx < cur:
                ax.add_patch(Rectangle((x, y), cell_w, cell_h,
                             edgecolor=GREEN, facecolor=GREEN, alpha=0.4))
            elif idx == cur:
                ax.add_patch(Rectangle((x, y), cell_w, cell_h,
                             edgecolor=RED, facecolor=RED, alpha=0.7, linewidth=3))
                ax.add_patch(Ellipse((x + cell_w/2, y + cell_h/2), 0.08, 0.10,
                             edgecolor=ORANGE, facecolor='none', linewidth=3, linestyle='--'))
            else:
                ax.add_patch(Rectangle((x, y), cell_w, cell_h,
                             edgecolor=GRAY, facecolor='none', linewidth=0.5))

    # Legend
    ly = 0.17
    ax.add_patch(Rectangle((grid_x, ly), 0.018, 0.018, facecolor=GREEN, alpha=0.4))
    ax.text(grid_x + 0.025, ly + 0.009, 'Done', color=GREEN, fontsize=11, va='center')
    ax.add_patch(Rectangle((grid_x + 0.09, ly), 0.018, 0.018, facecolor=RED, alpha=0.7))
    ax.text(grid_x + 0.115, ly + 0.009, 'Current', color=RED, fontsize=11, va='center')
    ax.add_patch(Ellipse((grid_x + 0.23, ly + 0.009), 0.025, 0.02, edgecolor=ORANGE, facecolor='none', linewidth=2, linestyle='--'))
    ax.text(grid_x + 0.25, ly + 0.009, 'N(μᵢ, Σᵢ)', color=ORANGE, fontsize=11, va='center')

    # ========== RIGHT SIDE: Pseudocode ==========
    rx = 0.48

    ax.add_patch(FancyBboxPatch((rx, 0.30), 0.50, 0.54,
                 boxstyle='round,pad=0.02', facecolor='#252525', edgecolor=RED, linewidth=2))

    ax.text(rx + 0.25, 0.80, 'LOOP ALGORITHM', ha='center', color=RED, fontsize=20, fontweight='bold')

    # Pseudocode - mathematical style
    y = 0.72
    gap = 0.065

    ax.text(rx + 0.03, y, 'For each position  i = 1, 2, ..., 3136 :', color=FG, fontsize=17)
    y -= gap

    ax.text(rx + 0.06, y, '1.  Extract feature vector  xᵢ', color=FG, fontsize=16)
    y -= gap

    ax.text(rx + 0.06, y, '2.  Get learned mean  μᵢ', color=FG, fontsize=16)
    y -= gap

    ax.text(rx + 0.06, y, '3.  Get covariance matrix  Σᵢ', color=FG, fontsize=16)
    y -= gap

    # Highlighted expensive step
    ax.add_patch(FancyBboxPatch((rx + 0.04, y - 0.025), 0.43, 0.055,
                 boxstyle='round,pad=0.01', facecolor=RED, alpha=0.25))
    ax.text(rx + 0.06, y, '4.  Compute inverse  Σᵢ⁻¹ = inv(Σᵢ)', color=ORANGE, fontsize=16, fontweight='bold')
    ax.text(rx + 0.38, y - 0.002, '← O(n³)', color=RED, fontsize=14, fontweight='bold')
    y -= gap

    ax.text(rx + 0.06, y, '5.  Distance  dᵢ = √[(xᵢ−μᵢ)ᵀ Σᵢ⁻¹ (xᵢ−μᵢ)]', color=FG, fontsize=16)
    y -= gap

    ax.text(rx + 0.03, y, 'End loop', color=FG, fontsize=17)

    # ========== COUNTER ==========
    cx = rx + 0.03
    cy = 0.22

    ax.text(cx, cy, 'Inversions computed:', color=FG, fontsize=16)
    ax.text(cx + 0.26, cy, f'{iteration}', color=ORANGE, fontsize=24, fontweight='bold')
    ax.text(cx + 0.32, cy, f'of {TOTAL_CELLS}', color=GRAY, fontsize=14)

    ops = iteration * 1_000_000
    ax.text(cx, cy - 0.05, 'Total operations:', color=FG, fontsize=16)
    ax.text(cx + 0.26, cy - 0.05, f'{ops:,}', color=RED, fontsize=20, fontweight='bold')

    # Progress bar
    bx, by, bw, bh = cx, cy - 0.09, 0.42, 0.018
    ax.add_patch(Rectangle((bx, by), bw, bh, facecolor='#333'))
    ax.add_patch(Rectangle((bx, by), bw * iteration / TOTAL_CELLS, bh, facecolor=RED))

    # ========== BOTTOM ==========
    ax.text(0.5, 0.05, '621 ms  per image   |   1.6 FPS   |   TOO SLOW FOR REAL-TIME',
            ha='center', color=RED, fontsize=22, fontweight='bold')

    fname = f'{OUT_DIR}/frame_{frame_idx:03d}.png'
    fig.savefig(fname, dpi=DPI, facecolor=BG)
    plt.close(fig)
    return fname


def create_after_frame(frame_idx):
    """AFTER: Vectorized parallel processing."""
    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # ========== HEADER ==========
    ax.text(0.5, 0.95, 'AFTER: Vectorized Parallel',
            ha='center', va='center', color=GREEN,
            fontsize=36, fontweight='bold')

    # ========== LEFT SIDE: All Green Grid ==========
    grid_x = 0.06
    grid_y = 0.25
    cell_w = 0.048
    cell_h = 0.062
    grid_w = GRID_COLS * cell_w
    grid_h = GRID_ROWS * cell_h

    ax.text(grid_x + grid_w / 2, 0.87, 'ALL 3,136 positions at once',
            ha='center', va='center', color=GREEN, fontsize=20)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * cell_w
            y = grid_y + (GRID_ROWS - 1 - row) * cell_h
            ax.add_patch(Rectangle((x, y), cell_w, cell_h,
                         edgecolor=GREEN, facecolor=GREEN, alpha=0.5))

    ax.text(grid_x + grid_w / 2, 0.17, 'Parallel  →  Single operation',
            ha='center', color=GREEN, fontsize=14)

    # ========== RIGHT SIDE: Vectorized Pseudocode ==========
    rx = 0.48

    ax.add_patch(FancyBboxPatch((rx, 0.30), 0.50, 0.54,
                 boxstyle='round,pad=0.02', facecolor='#1a2e1a', edgecolor=GREEN, linewidth=2))

    ax.text(rx + 0.25, 0.80, 'VECTORIZED ALGORITHM', ha='center', color=GREEN, fontsize=20, fontweight='bold')

    y = 0.72
    gap = 0.07

    ax.text(rx + 0.03, y, 'Pre-compute  Σ⁻¹  during training (once)', color=GRAY, fontsize=15, style='italic')
    y -= gap

    ax.text(rx + 0.03, y, '1.  Compute all differences:', color=FG, fontsize=16)
    ax.text(rx + 0.35, y, 'D = X − μ', color=CYAN, fontsize=16, fontweight='bold')
    y -= gap

    # Highlighted parallel steps
    ax.add_patch(FancyBboxPatch((rx + 0.02, y - 0.025), 0.45, 0.055,
                 boxstyle='round,pad=0.01', facecolor=GREEN, alpha=0.2))
    ax.text(rx + 0.03, y, '2.  Multiply all at once:', color=FG, fontsize=16)
    ax.text(rx + 0.35, y, 'T = Σ⁻¹ · D', color=CYAN, fontsize=16, fontweight='bold')
    y -= gap

    ax.add_patch(FancyBboxPatch((rx + 0.02, y - 0.025), 0.45, 0.055,
                 boxstyle='round,pad=0.01', facecolor=GREEN, alpha=0.2))
    ax.text(rx + 0.03, y, '3.  Dot product all at once:', color=FG, fontsize=16)
    ax.text(rx + 0.35, y, 'd² = D · T', color=CYAN, fontsize=16, fontweight='bold')
    y -= gap

    ax.text(rx + 0.03, y, '4.  Square root:', color=FG, fontsize=16)
    ax.text(rx + 0.35, y, 'd = √(d²)', color=CYAN, fontsize=16, fontweight='bold')
    y -= gap

    ax.text(rx + 0.03, y, 'No loop  •  No runtime inverse', color=GREEN, fontsize=16, fontweight='bold')

    # ========== COUNTER ==========
    cx = rx + 0.03
    cy = 0.22

    ax.text(cx, cy, 'Inversions at runtime:', color=FG, fontsize=16)
    ax.text(cx + 0.28, cy, '0', color=GREEN, fontsize=24, fontweight='bold')
    ax.text(cx + 0.32, cy, '(pre-computed)', color=GRAY, fontsize=13)

    ax.text(cx, cy - 0.05, 'Tensor operations:', color=FG, fontsize=16)
    ax.text(cx + 0.28, cy - 0.05, '2', color=GREEN, fontsize=24, fontweight='bold')
    ax.text(cx + 0.32, cy - 0.05, 'parallel ops', color=GRAY, fontsize=13)

    # Full progress bar
    bx, by, bw, bh = cx, cy - 0.09, 0.42, 0.018
    ax.add_patch(Rectangle((bx, by), bw, bh, facecolor=GREEN))

    # ========== BOTTOM: Comparison ==========
    ax.add_patch(FancyBboxPatch((0.12, 0.025), 0.76, 0.065,
                 boxstyle='round,pad=0.01', facecolor='#1a2e1a', edgecolor=GREEN, linewidth=2))

    ax.text(0.22, 0.058, 'BEFORE:', color=GRAY, fontsize=16)
    ax.text(0.32, 0.058, '621 ms', color=RED, fontsize=20, fontweight='bold')

    ax.text(0.46, 0.058, '→', color=FG, fontsize=28, fontweight='bold')

    ax.text(0.54, 0.058, 'AFTER:', color=GRAY, fontsize=16)
    ax.text(0.64, 0.058, '8 ms', color=GREEN, fontsize=20, fontweight='bold')

    ax.text(0.78, 0.058, '77× FASTER', color=GREEN, fontsize=20, fontweight='bold')

    fname = f'{OUT_DIR}/frame_{frame_idx:03d}.png'
    fig.savefig(fname, dpi=DPI, facecolor=BG)
    plt.close(fig)
    return fname


def main():
    print("Generating frames...")

    frames = []
    idx = 0

    # BEFORE: Loop animation - VERY SLOW
    print("Creating BEFORE frames (loop)...")
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            fname = create_before_frame(row, col, idx)
            frames.append(fname)
            idx += 1
            print(f"  Frame {idx}/{TOTAL_CELLS}")

    # AFTER: Single frame repeated many times
    print("Creating AFTER frame...")
    after_frame = create_after_frame(idx)
    idx += 1

    print(f"\nTotal unique frames: {idx}")

    # Create GIF
    print("Creating GIF...")
    images = [imageio.imread(f) for f in frames]

    # Add the AFTER frame image
    after_image = imageio.imread(after_frame)

    # Build durations for BEFORE frames - VERY SLOW
    durations = []

    # First BEFORE frame - long pause
    durations.append(3.0)

    # Middle BEFORE frames - slow
    for i in range(1, TOTAL_CELLS - 1):
        durations.append(0.8)  # 800ms per frame = very slow

    # Last BEFORE frame - pause before transition
    durations.append(2.0)

    # Add AFTER frame multiple times with long duration
    # To make GIF stop, we add one final frame with very long duration
    # The last frame will effectively "stop" the GIF

    # Add AFTER image to the list
    images.append(after_image)
    durations.append(10.0)  # 10 seconds on final AFTER frame

    # Save GIF with loop=1 (play once and stop)
    # Note: loop=0 means infinite, loop=1 means play once
    imageio.mimsave('gaussian_scan.gif', images, duration=durations, loop=1)
    print("Done! Created gaussian_scan.gif")

    # Print total duration
    total_time = sum(durations)
    print(f"Total GIF duration: {total_time:.1f} seconds")
    print("GIF will play ONCE and stop (no repeat)")


if __name__ == '__main__':
    main()