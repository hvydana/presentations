import os
import imageio
import matplotlib.pyplot as plt

# -----------------------------
# Global Style / Utilities
# -----------------------------

BG = '#1a1a1a'
FG = '#ffffff'
RED = '#ED1C24'
GREEN = '#4CAF50'
ORANGE = '#FF9800'
CYAN = '#00BCD4'
GRAY = '#888888'

WIDTH, HEIGHT = 1920, 1080
DPI = 100

os.makedirs('frames', exist_ok=True)

def new_fig():
    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    return fig, ax

def save_frame(idx, fig):
    fname = f'frames/frame_{idx:02d}.png'
    fig.savefig(fname, dpi=DPI, facecolor=BG)
    plt.close(fig)
    return fname


# -----------------------------
# Slide Implementations
# -----------------------------

def slide_01():
    """Title card"""
    fig, ax = new_fig()
    ax.text(0.5, 0.78, 'PaDiM INFERENCE OPTIMIZATION',
            ha='center', va='center', color=FG,
            fontsize=40, fontweight='bold')
    ax.text(0.5, 0.72, 'From Loop to Parallel',
            ha='center', va='center', color=CYAN,
            fontsize=28)

    # Baseline
    ax.add_patch(plt.Rectangle((0.18, 0.48), 0.24, 0.16,
                               edgecolor=RED, facecolor='none', linewidth=3))
    ax.text(0.3, 0.56, '621 ms\n1.6 FPS',
            ha='center', va='center', color=RED,
            fontsize=30, fontweight='bold')

    # Optimized
    ax.add_patch(plt.Rectangle((0.58, 0.48), 0.24, 0.16,
                               edgecolor=GREEN, facecolor='none', linewidth=3))
    ax.text(0.7, 0.56, '8 ms\n125 FPS',
            ha='center', va='center', color=GREEN,
            fontsize=30, fontweight='bold')

    # Arrow
    ax.annotate('', xy=(0.58, 0.56), xytext=(0.42, 0.56),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))
    ax.text(0.5, 0.6, '77× SPEEDUP',
            ha='center', va='center', color=ORANGE,
            fontsize=28, fontweight='bold')

    return save_frame(1, fig)


def slide_02():
    """The Problem: Baseline 621 ms"""
    fig, ax = new_fig()
    ax.text(0.5, 0.8, 'THE PROBLEM: TOO SLOW FOR REAL-TIME',
            ha='center', va='center', color=FG,
            fontsize=36, fontweight='bold')

    # Progress bar
    ax.add_patch(plt.Rectangle((0.15, 0.6), 0.7, 0.06,
                               edgecolor=RED, facecolor=RED, alpha=0.9))
    ax.text(0.5, 0.63, '621 ms per image',
            ha='center', va='center', color=FG, fontsize=26)

    # Warning & goal
    ax.text(0.5, 0.48, 'WARNING: TOO SLOW FOR PRODUCTION LINE',
            ha='center', va='center', color=RED,
            fontsize=26, fontweight='bold')
    ax.text(0.5, 0.38, 'Goal: Real-time anomaly detection for manufacturing QA',
            ha='center', va='center', color=FG, fontsize=22)

    return save_frame(2, fig)


def slide_03():
    """Time Breakdown (95% Mahalanobis)"""
    fig, ax = new_fig()
    ax.text(0.5, 0.85, 'WHERE IS TIME SPENT?',
            ha='center', va='center', color=FG,
            fontsize=34, fontweight='bold')

    total = 621
    segments = [
        ('Mahalanobis', 590, RED),
        ('ResNet', 15, ORANGE),
        ('Embedding', 12, ORANGE),
        ('Post', 4, ORANGE),
    ]
    x0, y0, h = 0.15, 0.6, 0.07
    current_x = x0
    for name, val, color in segments:
        w = 0.7 * (val / total)
        ax.add_patch(plt.Rectangle((current_x, y0), w, h,
                                   edgecolor=color, facecolor=color))
        if val / total > 0.08:
            ax.text(current_x + w/2, y0 + h/2, f'{name} ({val} ms)',
                    ha='center', va='center', color=FG, fontsize=16)
        current_x += w

    ax.text(0.5, 0.5,
            'Mahalanobis = ~590 ms (≈ 95% of total)',
            ha='center', va='center', color=RED, fontsize=26, fontweight='bold')

    ax.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.7),
                arrowprops=dict(arrowstyle='->', color=RED, linewidth=2))

    ax.text(0.5, 0.35, 'TARGET: Optimize the Mahalanobis step',
            ha='center', va='center', color=FG, fontsize=22)

    return save_frame(3, fig)


def slide_04():
    """Complete optimization story in ONE slide"""
    fig, ax = new_fig()
    ax.text(0.5, 0.96, 'PaDiM OPTIMIZATION: THE COMPLETE STORY',
            ha='center', va='center', color=FG,
            fontsize=28, fontweight='bold')

    # TOP ROW: Image → ResNet → Patch
    y_top = 0.82

    # Input Image
    ax.add_patch(plt.Rectangle((0.05, y_top-0.05), 0.08, 0.08,
                               edgecolor=CYAN, facecolor='none', linewidth=2))
    ax.text(0.09, y_top+0.05, 'Image',
            ha='center', va='center', color=FG, fontsize=14)

    ax.annotate('', xy=(0.15, y_top), xytext=(0.13, y_top),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))

    # ResNet
    ax.add_patch(plt.Rectangle((0.15, y_top-0.05), 0.1, 0.08,
                               edgecolor=ORANGE, facecolor='none', linewidth=2))
    ax.text(0.2, y_top, 'ResNet18',
            ha='center', va='center', color=ORANGE, fontsize=14, fontweight='bold')

    ax.annotate('', xy=(0.27, y_top), xytext=(0.25, y_top),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))

    # Patch
    ax.add_patch(plt.Rectangle((0.27, y_top-0.05), 0.1, 0.08,
                               edgecolor=GREEN, facecolor='none', linewidth=2))
    ax.text(0.32, y_top+0.02, 'Patch',
            ha='center', va='center', color=GREEN, fontsize=14, fontweight='bold')
    ax.text(0.32, y_top-0.02, '448×56×56',
            ha='center', va='center', color=FG, fontsize=11)

    # MIDDLE-TOP: Grid with Gaussian circling (SLOW)
    y_grid = 0.65
    ax.text(0.2, 0.73, 'BASELINE: Sequential Loop (SLOW ⚠️)',
            ha='center', va='center', color=RED, fontsize=16, fontweight='bold')

    # Draw 8x8 grid representing 56x56
    grid_size = 8
    cell_w, cell_h = 0.025, 0.025
    grid_x, grid_y = 0.08, y_grid - 0.15

    for i in range(grid_size):
        for j in range(grid_size):
            x = grid_x + i * cell_w
            y = grid_y + j * cell_h
            # Highlight current pixel being processed
            if i == 2 and j == 3:
                ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                                           edgecolor=RED, facecolor=RED, alpha=0.7, linewidth=2))
                # Gaussian circle around it
                circle = plt.Circle((x + cell_w/2, y + cell_h/2), 0.04,
                                   edgecolor=ORANGE, facecolor='none', linewidth=2, linestyle='--')
                ax.add_patch(circle)
            else:
                ax.add_patch(plt.Rectangle((x, y), cell_w, cell_h,
                                           edgecolor=GRAY, facecolor='none', linewidth=0.5))

    ax.text(0.2, y_grid - 0.18, '3,136 iterations',
            ha='center', va='center', color=RED, fontsize=12, fontweight='bold')

    # Code snippet showing the problem
    code_problem = '''for i in 3136:
  inv = np.linalg.inv(cov[i])  ❌
  dist[i] = mahal(x[i], μ[i], inv)'''
    ax.text(0.2, y_grid - 0.26, code_problem,
            ha='center', va='center', color=FG, fontsize=10,
            family='monospace', bbox=dict(boxstyle='round', facecolor=BG, edgecolor=RED))

    ax.text(0.2, y_grid - 0.33, '621 ms / 1.6 FPS',
            ha='center', va='center', color=RED, fontsize=14, fontweight='bold')

    # BIG ARROW showing optimization
    ax.annotate('', xy=(0.43, 0.65), xytext=(0.38, 0.65),
                arrowprops=dict(arrowstyle='->', color=GREEN, linewidth=6))
    ax.text(0.405, 0.71, 'OPTIMIZE',
            ha='center', va='center', color=GREEN, fontsize=16, fontweight='bold')

    # RIGHT SIDE: Optimizations
    opt_x = 0.7

    ax.text(0.7, 0.73, 'OPTIMIZED: Parallel (FAST ✓)',
            ha='center', va='center', color=GREEN, fontsize=16, fontweight='bold')

    # Step 1: Move inv outside
    ax.add_patch(plt.Rectangle((0.48, 0.58), 0.44, 0.11,
                               edgecolor=ORANGE, facecolor='none', linewidth=2))
    ax.text(0.5, 0.66, '1️⃣', ha='center', va='center', color=ORANGE, fontsize=16)
    ax.text(0.58, 0.66, 'Pre-compute inv outside loop',
            ha='left', va='center', color=ORANGE, fontsize=13, fontweight='bold')
    code_opt1 = "# Training: inv = np.linalg.inv(cov)  (once!)\n# Inference: dist = mahal(x, μ, inv)  ✓"
    ax.text(0.7, 0.61, code_opt1,
            ha='center', va='center', color=FG, fontsize=9, family='monospace')

    # Step 2: Vectorize
    ax.add_patch(plt.Rectangle((0.48, 0.44), 0.44, 0.11,
                               edgecolor=CYAN, facecolor='none', linewidth=2))
    ax.text(0.5, 0.52, '2️⃣', ha='center', va='center', color=CYAN, fontsize=16)
    ax.text(0.58, 0.52, 'Vectorize loop with einsum',
            ha='left', va='center', color=CYAN, fontsize=13, fontweight='bold')
    code_opt2 = "# All 3136 at once:\ntmp = einsum('cdi,bdi->bci', inv, diff)"
    ax.text(0.7, 0.47, code_opt2,
            ha='center', va='center', color=FG, fontsize=9, family='monospace')

    # Step 3: ONNX + GPU
    ax.add_patch(plt.Rectangle((0.48, 0.3), 0.44, 0.11,
                               edgecolor=GREEN, facecolor='none', linewidth=2))
    ax.text(0.5, 0.38, '3️⃣', ha='center', va='center', color=GREEN, fontsize=16)
    ax.text(0.58, 0.38, 'ONNX Runtime + GPU',
            ha='left', va='center', color=GREEN, fontsize=13, fontweight='bold')
    ax.text(0.7, 0.33, 'Fused ops + GPU parallel execution',
            ha='center', va='center', color=FG, fontsize=10)

    # BOTTOM: Results comparison
    ax.text(0.5, 0.2, 'RESULTS',
            ha='center', va='center', color=FG, fontsize=20, fontweight='bold')

    # Before bar
    ax.add_patch(plt.Rectangle((0.15, 0.12), 0.3, 0.05,
                               edgecolor=RED, facecolor=RED, alpha=0.8))
    ax.text(0.3, 0.145, '621 ms (1.6 FPS)',
            ha='center', va='center', color=FG, fontsize=14, fontweight='bold')

    # Arrow
    ax.annotate('', xy=(0.52, 0.145), xytext=(0.46, 0.145),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=3))
    ax.text(0.49, 0.165, '77×', ha='center', va='center',
            color=ORANGE, fontsize=16, fontweight='bold')

    # After bar
    ax.add_patch(plt.Rectangle((0.55, 0.12), 0.04, 0.05,
                               edgecolor=GREEN, facecolor=GREEN, alpha=0.8))
    ax.text(0.68, 0.145, '8 ms (125 FPS)',
            ha='center', va='center', color=GREEN, fontsize=14, fontweight='bold')

    ax.text(0.5, 0.04, 'Key: Move expensive ops outside loop → Vectorize → Hardware acceleration',
            ha='center', va='center', color=CYAN, fontsize=14)

    return save_frame(4, fig)


def slide_05_bottleneck_code():
    """Show the bottleneck implementation code"""
    fig, ax = new_fig()
    ax.text(0.5, 0.92, 'THE BOTTLENECK: LOOP-BASED IMPLEMENTATION',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Code block
    code = '''def compute_mahalanobis_scipy(self, embedding):
    """
    The BOTTLENECK: Loop-based Mahalanobis computation.

    For each of 3,136 spatial positions:
    1. Extract the feature vector (100 dimensions)
    2. Compute matrix inverse of 100x100 covariance matrix
    3. Compute Mahalanobis distance using scipy
    """
    B, C, H, W = embedding.shape  # [1, 100, 56, 56]
    N = H * W  # 3,136 positions

    distances = []
    for i in range(N):  # 3,136 iterations!
        mean = self.mean[:, i]           # [100]
        cov = self.cov[:, :, i]          # [100, 100]

        # EXPENSIVE: Matrix inversion at runtime!
        cov_inv = np.linalg.inv(cov)     # O(n³) = O(100³) per position

        # scipy.spatial.distance.mahalanobis
        dist = mahalanobis(emb[:, i], mean, cov_inv)
        distances.append(dist)

    return np.array(distances).reshape(H, W)'''

    ax.text(0.5, 0.48, code,
            ha='center', va='center', color=FG, fontsize=14,
            family='monospace', linespacing=1.5)

    # Highlight the expensive operation
    ax.add_patch(plt.Rectangle((0.15, 0.36), 0.7, 0.04,
                               edgecolor=RED, facecolor='none', linewidth=3))

    ax.text(0.5, 0.08,
            '⚠️  cov_inv = np.linalg.inv(cov) called 3,136 times! ⚠️',
            ha='center', va='center', color=RED, fontsize=22, fontweight='bold')

    return save_frame(5, fig)


def slide_06_optimization_move_inverse():
    """Show moving inverse computation outside the loop"""
    fig, ax = new_fig()
    ax.text(0.5, 0.92, 'OPTIMIZATION INSIGHT: MOVE INVARIANT OUTSIDE LOOP',
            ha='center', va='center', color=FG,
            fontsize=28, fontweight='bold')

    # Before code (left side)
    code_before = '''for i in range(N):  # 3,136 iterations
    mean = self.mean[:, i]
    cov = self.cov[:, :, i]

    cov_inv = np.linalg.inv(cov)  ❌

    dist = mahalanobis(emb[:, i],
                       mean, cov_inv)
    distances.append(dist)'''

    ax.text(0.28, 0.55, code_before,
            ha='center', va='center', color=FG, fontsize=15,
            family='monospace', linespacing=1.6)

    ax.text(0.28, 0.86, 'BEFORE',
            ha='center', va='center', color=RED, fontsize=20, fontweight='bold')

    # Highlight the problematic line
    ax.add_patch(plt.Rectangle((0.08, 0.52), 0.4, 0.04,
                               edgecolor=RED, facecolor='none', linewidth=3))

    # Big arrow
    ax.annotate('', xy=(0.52, 0.6), xytext=(0.48, 0.6),
                arrowprops=dict(arrowstyle='->', color=GREEN, linewidth=4))
    ax.text(0.5, 0.65, 'Move\noutside!',
            ha='center', va='center', color=GREEN, fontsize=18, fontweight='bold')

    # After code (right side)
    code_after = '''# Pre-compute ONCE (training time)
for i in range(N):
    self.cov_inv[:,:,i] =
        np.linalg.inv(self.cov[:,:,i])

# Inference (fast!)
for i in range(N):  # 3,136 iterations
    mean = self.mean[:, i]
    cov_inv = self.cov_inv[:, :, i]  ✓

    dist = mahalanobis(emb[:, i],
                       mean, cov_inv)
    distances.append(dist)'''

    ax.text(0.73, 0.48, code_after,
            ha='center', va='center', color=FG, fontsize=13,
            family='monospace', linespacing=1.5)

    ax.text(0.73, 0.86, 'AFTER',
            ha='center', va='center', color=GREEN, fontsize=20, fontweight='bold')

    # Highlight the fast lookup
    ax.add_patch(plt.Rectangle((0.56, 0.445), 0.34, 0.025,
                               edgecolor=GREEN, facecolor='none', linewidth=3))

    ax.text(0.5, 0.12,
            'Inverse computation moved from inference → training (one-time cost)',
            ha='center', va='center', color=GREEN, fontsize=20, fontweight='bold')

    ax.text(0.5, 0.05,
            'Result: 621 ms → ~80 ms (≈8× speedup)',
            ha='center', va='center', color=CYAN, fontsize=18)

    return save_frame(6, fig)


def slide_07_vectorize_merge():
    """Merge for loop and Mahalanobis with vectorized computation"""
    fig, ax = new_fig()
    ax.text(0.5, 0.92, 'OPTIMIZATION 2: VECTORIZE THE LOOP',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Before: Loop-based
    ax.text(0.28, 0.82, 'LOOP-BASED (SLOW)',
            ha='center', va='center', color=RED, fontsize=18, fontweight='bold')

    code_loop = '''for i in range(N):  # 3,136 iterations
    mean = self.mean[:, i]
    cov_inv = self.cov_inv[:, :, i]

    diff = emb[:, i] - mean

    dist = mahalanobis(diff,
                       mean,
                       cov_inv)

    distances.append(dist)

return np.array(distances).reshape(H, W)'''

    ax.text(0.28, 0.5, code_loop,
            ha='center', va='center', color=FG, fontsize=14,
            family='monospace', linespacing=1.5)

    # Big arrow
    ax.annotate('', xy=(0.52, 0.55), xytext=(0.48, 0.55),
                arrowprops=dict(arrowstyle='->', color=GREEN, linewidth=4))
    ax.text(0.5, 0.62, 'Vectorize',
            ha='center', va='center', color=GREEN, fontsize=18, fontweight='bold')

    # After: Vectorized
    ax.text(0.73, 0.82, 'VECTORIZED (FAST)',
            ha='center', va='center', color=GREEN, fontsize=18, fontweight='bold')

    code_vectorized = '''# All positions at once!
B, C, H, W = embedding.shape
N = H * W

# Reshape for batch computation
emb = embedding.view(B, C, N)

# Vectorized difference
diff = emb - self.mean  # [B, C, N]

# Batched matrix multiplication
# tmp[b,c,i] = sum_d( cov_inv[c,d,i] * diff[b,d,i] )
tmp = torch.einsum('cdi,bdi->bci',
                   self.cov_inv, diff)

# Element-wise multiply and sum
dist_sq = (diff * tmp).sum(dim=1)  # [B, N]
dist = torch.sqrt(dist_sq)

return dist.reshape(B, H, W)'''

    ax.text(0.73, 0.45, code_vectorized,
            ha='center', va='center', color=FG, fontsize=12,
            family='monospace', linespacing=1.4)

    ax.text(0.5, 0.08,
            'All 3,136 positions computed in parallel! 80 ms → 36 ms (≈2× additional)',
            ha='center', va='center', color=GREEN, fontsize=18, fontweight='bold')

    return save_frame(7, fig)


def slide_08_three_moving_images():
    """Show three key concepts moving together as images"""
    fig, ax = new_fig()
    ax.text(0.5, 0.92, 'THREE KEY OPTIMIZATIONS',
            ha='center', va='center', color=FG,
            fontsize=32, fontweight='bold')

    # Box 1: Pre-compute inverse
    ax.add_patch(plt.Rectangle((0.05, 0.52), 0.25, 0.32,
                               edgecolor=ORANGE, facecolor='none', linewidth=3))
    ax.text(0.175, 0.8, '1. Pre-compute',
            ha='center', va='center', color=ORANGE, fontsize=20, fontweight='bold')
    ax.text(0.175, 0.74, 'Σ⁻¹ inverse',
            ha='center', va='center', color=FG, fontsize=18)
    ax.text(0.175, 0.67, 'Move to',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.175, 0.62, 'training time',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.175, 0.56, '621→80 ms',
            ha='center', va='center', color=ORANGE, fontsize=18, fontweight='bold')

    # Box 2: Vectorize loop
    ax.add_patch(plt.Rectangle((0.375, 0.52), 0.25, 0.32,
                               edgecolor=GREEN, facecolor='none', linewidth=3))
    ax.text(0.5, 0.8, '2. Vectorize',
            ha='center', va='center', color=GREEN, fontsize=20, fontweight='bold')
    ax.text(0.5, 0.74, 'Replace loop',
            ha='center', va='center', color=FG, fontsize=18)
    ax.text(0.5, 0.67, 'with einsum',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.5, 0.62, 'batch ops',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.5, 0.56, '80→36 ms',
            ha='center', va='center', color=GREEN, fontsize=18, fontweight='bold')

    # Box 3: ONNX + GPU
    ax.add_patch(plt.Rectangle((0.7, 0.52), 0.25, 0.32,
                               edgecolor=CYAN, facecolor='none', linewidth=3))
    ax.text(0.825, 0.8, '3. ONNX+GPU',
            ha='center', va='center', color=CYAN, fontsize=20, fontweight='bold')
    ax.text(0.825, 0.74, 'Runtime',
            ha='center', va='center', color=FG, fontsize=18)
    ax.text(0.825, 0.67, 'optimization',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.825, 0.62, '+ GPU accel',
            ha='center', va='center', color=FG, fontsize=16)
    ax.text(0.825, 0.56, '36→8 ms',
            ha='center', va='center', color=CYAN, fontsize=18, fontweight='bold')

    # Flow arrows
    ax.annotate('', xy=(0.375, 0.68), xytext=(0.3, 0.68),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=3))
    ax.annotate('', xy=(0.7, 0.68), xytext=(0.625, 0.68),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=3))

    # Timeline
    y_timeline = 0.35
    ax.plot([0.1, 0.9], [y_timeline, y_timeline], color=FG, linewidth=2)

    # Timeline markers
    positions = [0.1, 0.3, 0.5, 0.7, 0.9]
    labels = ['621 ms\n(baseline)', '80 ms\n(8×)', '36 ms\n(17×)', '16 ms\n(39×)', '8 ms\n(77×)']
    colors = [RED, ORANGE, GREEN, CYAN, CYAN]

    for pos, label, color in zip(positions, labels, colors):
        ax.plot(pos, y_timeline, 'o', color=color, markersize=12)
        ax.text(pos, 0.26, label, ha='center', va='top', color=color, fontsize=14)

    ax.text(0.5, 0.10,
            'Sequential optimizations compound to 77× total speedup',
            ha='center', va='center', color=GREEN, fontsize=22, fontweight='bold')

    return save_frame(8, fig)


def slide_05():
    """ResNet Feature Extraction"""
    fig, ax = new_fig()
    ax.text(0.5, 0.9, 'STEP 1: FEATURE EXTRACTION (ResNet18)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Input image
    ax.add_patch(plt.Rectangle((0.05, 0.6), 0.18, 0.18,
                               edgecolor=FG, facecolor='none', linewidth=2))
    ax.text(0.14, 0.7, 'Input\n[3, 224, 224]',
            ha='center', va='center', color=FG, fontsize=20)

    # ResNet block
    ax.add_patch(plt.Rectangle((0.3, 0.5), 0.25, 0.35,
                               edgecolor=FG, facecolor='none', linewidth=2))
    ax.text(0.425, 0.82, 'ResNet18', ha='center', va='center',
            color=FG, fontsize=24, fontweight='bold')
    ax.text(0.425, 0.76, 'Conv1 → BN', ha='center', va='center',
            color=FG, fontsize=18)
    ax.text(0.425, 0.7, 'Layer1 → f₁ [64, 56, 56]', ha='center', va='center',
            color=CYAN, fontsize=18)
    ax.text(0.425, 0.64, 'Layer2 → f₂ [128, 28, 28]', ha='center', va='center',
            color=CYAN, fontsize=18)
    ax.text(0.425, 0.58, 'Layer3 → f₃ [256, 14, 14]', ha='center', va='center',
            color=CYAN, fontsize=18)

    # Arrows
    ax.annotate('', xy=(0.3, 0.69), xytext=(0.23, 0.69),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))

    return save_frame(9, fig)


def slide_09a():
    """Multi-Scale Concatenation"""
    fig, ax = new_fig()
    ax.text(0.5, 0.9, 'STEP 2: MULTI-SCALE EMBEDDING',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Feature maps
    ax.text(0.2, 0.75, 'f₁ [64, 56, 56]', color=FG, ha='center', fontsize=20)
    ax.add_patch(plt.Rectangle((0.15, 0.62), 0.1, 0.1,
                               edgecolor=CYAN, facecolor='none'))

    ax.text(0.5, 0.75, 'f₂ [128, 28, 28]', color=FG, ha='center', fontsize=20)
    ax.add_patch(plt.Rectangle((0.45, 0.62), 0.1, 0.1,
                               edgecolor=CYAN, facecolor='none'))

    ax.text(0.8, 0.75, 'f₃ [256, 14, 14]', color=FG, ha='center', fontsize=20)
    ax.add_patch(plt.Rectangle((0.75, 0.62), 0.1, 0.1,
                               edgecolor=CYAN, facecolor='none'))

    # Upsampling arrows
    ax.annotate('Upsample 2×', xy=(0.5, 0.62), xytext=(0.5, 0.47),
                ha='center', color=FG,
                arrowprops=dict(arrowstyle='->', color=FG))
    ax.annotate('Upsample 4×', xy=(0.8, 0.62), xytext=(0.8, 0.47),
                ha='center', color=FG,
                arrowprops=dict(arrowstyle='->', color=FG))

    # Concatenate
    ax.add_patch(plt.Rectangle((0.35, 0.35), 0.3, 0.1,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.5, 0.4, 'Concatenate\n64 + 128 + 256 = 448 channels',
            ha='center', va='center', color=FG, fontsize=20)

    ax.add_patch(plt.Rectangle((0.4, 0.2), 0.2, 0.1,
                               edgecolor=GREEN, facecolor='none'))
    ax.text(0.5, 0.25, 'E = [448, 56, 56]\n3,136 spatial positions',
            ha='center', va='center', color=GREEN, fontsize=20)

    return save_frame(10, fig)


def slide_09b():
    """Patch positions grid"""
    fig, ax = new_fig()
    ax.text(0.5, 0.9, 'STEP 3: PATCH POSITIONS (56 × 56 = 3,136)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Grid representation
    ax.add_patch(plt.Rectangle((0.2, 0.3), 0.6, 0.4,
                               edgecolor=FG, facecolor='none', linewidth=2))
    ax.text(0.5, 0.56, 'E reshaped: [448, 56, 56] → [448, 3,136]',
            ha='center', va='center', color=FG, fontsize=22)

    # Few highlighted positions
    ax.add_patch(plt.Rectangle((0.25, 0.45), 0.04, 0.04,
                               edgecolor=CYAN, facecolor='none'))
    ax.text(0.27, 0.52, 'Position 1\nx₁ ∈ ℝ¹⁰⁰', color=FG,
            ha='center', va='center', fontsize=16)

    ax.add_patch(plt.Rectangle((0.45, 0.35), 0.04, 0.04,
                               edgecolor=CYAN, facecolor='none'))
    ax.text(0.47, 0.28, 'Position 2\nx₂ ∈ ℝ¹⁰⁰', color=FG,
            ha='center', va='center', fontsize=16)

    ax.add_patch(plt.Rectangle((0.7, 0.55), 0.04, 0.04,
                               edgecolor=CYAN, facecolor='none'))
    ax.text(0.73, 0.62, 'Position 3136\nx₃₁₃₆ ∈ ℝ¹⁰⁰', color=FG,
            ha='center', va='center', fontsize=16)

    ax.text(0.5, 0.18,
            'Dimension selection: 448 → 100 per position',
            ha='center', va='center', color=FG, fontsize=20)

    return save_frame(11, fig)


def slide_09c():
    """Gaussian per Position (Training)"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'TRAINING: Learn Gaussian at Each Position',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    ax.text(0.5, 0.75,
            'For N training images, at position i:',
            ha='center', va='center', color=FG, fontsize=24)

    ax.text(0.5, 0.62,
            'x₁ᵢ, x₂ᵢ, …, x_Nᵢ  →  fit Gaussian  N(μᵢ, Σᵢ)',
            ha='center', va='center', color=FG, fontsize=22)

    eq = (
        r'$\mu_i = \frac{1}{N}\sum_{k=1}^N x_{k i}$' '\n\n' +
        r'$\Sigma_i = \frac{1}{N-1}\sum_{k=1}^N (x_{k i} - \mu_i)(x_{k i} - \mu_i)^T + \varepsilon I$'
    )
    ax.text(0.5, 0.4, eq,
            ha='center', va='center', color=CYAN, fontsize=26)

    ax.text(0.5, 0.18,
            'Each spatial position learns its own Gaussian of normal features',
            ha='center', va='center', color=FG, fontsize=20)

    return save_frame(20, fig)


def slide_09d():
    """Gaussian Visualization: normal vs anomaly"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'GAUSSIAN DISTRIBUTION AT A PATCH POSITION',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Left: normal
    ax.text(0.25, 0.8, 'Normal sample', ha='center', va='center',
            color=FG, fontsize=22)

    # Ellipse-like patch
    ellipse_left = plt.Circle((0.25, 0.55), 0.1, edgecolor=FG,
                              facecolor='none', linestyle='dashed')
    ax.add_patch(ellipse_left)
    ax.text(0.25, 0.55, 'μᵢ', ha='center', va='center', color=CYAN, fontsize=18)

    # normal point inside
    ax.plot(0.28, 0.58, 'o', color=GREEN)
    ax.text(0.25, 0.35,
            'Inside ellipse → low distance\nNormal patch',
            ha='center', va='center', color=GREEN, fontsize=18)

    # Right: anomaly
    ax.text(0.75, 0.8, 'Anomalous sample', ha='center', va='center',
            color=FG, fontsize=22)
    ellipse_right = plt.Circle((0.75, 0.55), 0.1, edgecolor=FG,
                               facecolor='none', linestyle='dashed')
    ax.add_patch(ellipse_right)
    ax.text(0.75, 0.55, 'μᵢ', ha='center', va='center', color=CYAN, fontsize=18)

    # anomaly star outside
    ax.plot(0.9, 0.65, marker='*', color=RED, markersize=14)
    ax.text(0.75, 0.35,
            'Outside ellipse → high distance\nAnomalous patch',
            ha='center', va='center', color=RED, fontsize=18)

    return save_frame(21, fig)


def slide_09e():
    """Mahalanobis Distance Equation"""
    fig, ax = new_fig()
    ax.text(0.5, 0.82, 'MAHALANOBIS DISTANCE',
            ha='center', va='center', color=FG,
            fontsize=34, fontweight='bold')

    eq = r'$d(x) = \sqrt{(x - \mu_i)^T \Sigma_i^{-1} (x - \mu_i)}$'
    ax.text(0.5, 0.6, eq,
            ha='center', va='center', color=CYAN, fontsize=40)

    ax.text(0.5, 0.45,
            'x: test feature [100]\n'
            'μᵢ: mean from training [100]\n'
            'Σᵢ⁻¹: inverse covariance [100×100]',
            ha='center', va='center', color=FG, fontsize=22)

    ax.text(0.5, 0.25,
            'Interpretation:\n'
            '• d small → x is NORMAL (close to training data)\n'
            '• d large → x is ANOMALY (far from training data)',
            ha='center', va='center', color=FG, fontsize=22)

    return save_frame(22, fig)


def slide_11():
    """Baseline - The Slow Loop (detailed)"""
    fig, ax = new_fig()
    ax.text(0.5, 0.86, 'BASELINE: SEQUENTIAL LOOP (621 ms)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    code = (
        'FOR i = 1 TO 3136:\n'
        '  1. Extract xᵢ from embedding\n'
        '  2. Σᵢ⁻¹ = inverse(Σᵢ)    ← O(100³) per position (SLOW)\n'
        '  3. dᵢ = √[(xᵢ - μᵢ)ᵀ Σᵢ⁻¹ (xᵢ - μᵢ)]\n'
        'END FOR'
    )
    ax.text(0.5, 0.6, code,
            ha='center', va='center', color=FG, fontsize=22,
            family='monospace')

    ax.text(0.5, 0.32,
            '3,136 sequential iterations, each doing a 100×100 matrix inverse',
            ha='center', va='center', color=RED, fontsize=22)

    ax.text(0.5, 0.22,
            'Time: 621 ms (≈590 ms in Mahalanobis loop)',
            ha='center', va='center', color=ORANGE, fontsize=22)

    return save_frame(23, fig)


def slide_12():
    """Opt 1 - Pre-compute inverses"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'OPTIMIZATION 1: PRE-COMPUTE Σ⁻¹ (TRAINING)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Before block
    ax.add_patch(plt.Rectangle((0.08, 0.6), 0.36, 0.23,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.26, 0.76, 'BEFORE (Inference):', ha='center',
            va='center', color=FG, fontsize=20, fontweight='bold')
    ax.text(0.26, 0.64,
            'FOR i = 1..3136:\n'
            '  Σᵢ⁻¹ = inverse(Σᵢ)\n'
            '  dᵢ = mahal(xᵢ, μᵢ, Σᵢ⁻¹)\n'
            'END FOR',
            ha='center', va='center', color=FG, fontsize=18,
            family='monospace')

    # After block
    ax.add_patch(plt.Rectangle((0.56, 0.6), 0.36, 0.23,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.74, 0.76, 'AFTER (Training + Inference):',
            ha='center', va='center', color=FG, fontsize=20, fontweight='bold')
    ax.text(0.74, 0.66,
            'Training (once):\n'
            '  FOR i = 1..3136:\n'
            '    Σᵢ⁻¹ = inverse(Σᵢ)\n'
            '  SAVE Σᵢ⁻¹\n\n'
            'Inference:\n'
            '  LOAD Σᵢ⁻¹\n'
            '  FOR i: dᵢ = mahal(xᵢ, μᵢ, Σᵢ⁻¹)',
            ha='center', va='center', color=FG, fontsize=16,
            family='monospace')

    ax.text(0.5, 0.3,
            'Result: 3,136 matrix inversions removed from inference time',
            ha='center', va='center', color=GREEN, fontsize=22)
    ax.text(0.5, 0.2,
            'Time: 621 ms → ~80 ms (≈8× speedup)',
            ha='center', va='center', color=GREEN, fontsize=24, fontweight='bold')

    return save_frame(20, fig)


def slide_13():
    """Sequential problem visualization"""
    fig, ax = new_fig()
    ax.text(0.5, 0.86, 'WHY SEQUENTIAL LOOPS ARE SLOW',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Many small boxes in a row, only one highlighted
    n_boxes = 12
    x_start, y, w, h = 0.05, 0.5, 0.07, 0.08
    for i in range(n_boxes):
        color = RED if i == 2 else FG
        ax.add_patch(plt.Rectangle((x_start + i * (w + 0.01), y),
                                   w, h, edgecolor=color, facecolor='none'))
    ax.text(0.5, 0.42,
            'Each box = 1 patch position\nOnly one processed at a time',
            ha='center', va='center', color=FG, fontsize=20)

    ax.text(0.5, 0.3,
            '3,136 independent positions, but executed sequentially in Python',
            ha='center', va='center', color=ORANGE, fontsize=20)

    ax.text(0.5, 0.2,
            'Observation: positions are INDEPENDENT → perfect for vectorization',
            ha='center', va='center', color=GREEN, fontsize=22)

    return save_frame(21, fig)


def slide_14():
    """Opt 2 - Vectorize with einsum"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'OPTIMIZATION 2: VECTORIZATION WITH EINSUM',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Before: loop
    ax.text(0.25, 0.7, 'Before (loop):', color=FG,
            ha='center', va='center', fontsize=20, fontweight='bold')
    code_before = (
        'FOR i = 1..3136:\n'
        '  diff = x[:, i] - μ[:, i]\n'
        '  tmp  = Σ⁻¹[:, :, i] @ diff\n'
        '  d[i] = √(diff · tmp)\n'
        'END FOR'
    )
    ax.text(0.25, 0.55, code_before,
            ha='center', va='center', color=FG, fontsize=16,
            family='monospace')

    # After: einsum
    ax.text(0.75, 0.7, 'After (vectorized):', color=FG,
            ha='center', va='center', fontsize=20, fontweight='bold')
    code_after = (
        "diff = X - μ                # [B, 100, 3136]\n"
        "tmp  = einsum('cdi,bdi->bci', Σ⁻¹, diff)\n"
        "d²   = einsum('bci,bci->bi', diff, tmp)\n"
        "d    = √(d²)"
    )
    ax.text(0.75, 0.55, code_after,
            ha='center', va='center', color=FG, fontsize=16,
            family='monospace')

    ax.text(0.5, 0.34,
            'All 3,136 positions computed in a few batched tensor ops',
            ha='center', va='center', color=GREEN, fontsize=20)
    ax.text(0.5, 0.24,
            'Time: 80 ms → 36 ms (≈2× additional, ≈17× total speedup)',
            ha='center', va='center', color=GREEN, fontsize=22, fontweight='bold')

    return save_frame(22, fig)


def slide_15():
    """Einsum visualization"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'EINSUM: PARALLEL MATRIX OPERATIONS',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    ax.text(0.5, 0.75,
            "einsum('cdi,bdi->bci', Σ⁻¹, diff)",
            ha='center', va='center', color=CYAN, fontsize=26)

    ax.text(0.5, 0.64,
            'For ALL 3,136 positions simultaneously:',
            ha='center', va='center', color=FG, fontsize=22)

    ax.text(0.5, 0.48,
            'Σ₁⁻¹ [100×100] × diff₁ [100]\n'
            'Σ₂⁻¹ [100×100] × diff₂ [100]\n'
            '...\n'
            'Σ₃₁₃₆⁻¹ [100×100] × diff₃₁₃₆ [100]\n'
            '→ all computed in parallel (SIMD / BLAS)',
            ha='center', va='center', color=FG, fontsize=20)

    ax.text(0.5, 0.2,
            'No Python loop, all heavy math pushed into optimized kernels',
            ha='center', va='center', color=GREEN, fontsize=22)

    return save_frame(23, fig)


def slide_16():
    """Opt 3 - ONNX Runtime"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'OPTIMIZATION 3: ONNX RUNTIME',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # PyTorch vs ONNX
    ax.add_patch(plt.Rectangle((0.1, 0.6), 0.32, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.26, 0.7, 'PyTorch (eager)\nops executed one-by-one',
            ha='center', va='center', color=FG, fontsize=20)

    ax.add_patch(plt.Rectangle((0.58, 0.6), 0.32, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.74, 0.72, 'ONNX Runtime\n(graph execution)',
            ha='center', va='center', color=FG, fontsize=20)
    ax.text(0.74, 0.62,
            '• Operator fusion\n• Redundant op elimination\n• Memory planning',
            ha='center', va='center', color=FG, fontsize=16)

    ax.annotate('', xy=(0.58, 0.7), xytext=(0.42, 0.7),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))

    ax.text(0.5, 0.4,
            'Model: Input → ResNet18 → Embedding → Output[100, 56, 56]',
            ha='center', va='center', color=FG, fontsize=20)

    ax.text(0.5, 0.25,
            'Time: 36 ms → 16 ms (≈2×, ≈39× total speedup)',
            ha='center', va='center', color=GREEN, fontsize=22, fontweight='bold')

    return save_frame(20, fig)


def slide_17():
    """Opt 4 - GPU acceleration"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'OPTIMIZATION 4: GPU ACCELERATION',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # CPU block
    ax.add_patch(plt.Rectangle((0.12, 0.55), 0.3, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.27, 0.65, 'CPU (sequential cores)',
            ha='center', va='center', color=FG, fontsize=20)
    ax.text(0.27, 0.57, '16 ms', ha='center', va='center',
            color=FG, fontsize=18)

    # GPU block
    ax.add_patch(plt.Rectangle((0.58, 0.55), 0.3, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.73, 0.65, 'GPU (massively parallel)',
            ha='center', va='center', color=FG, fontsize=20)
    ax.text(0.73, 0.57, '8 ms', ha='center', va='center',
            color=FG, fontsize=18)

    ax.annotate('', xy=(0.58, 0.65), xytext=(0.42, 0.65),
                arrowprops=dict(arrowstyle='->', color=FG, linewidth=2))

    ax.text(0.5, 0.38,
            'Pipeline: Image → [GPU: ResNet + Embedding] → [CPU: Mahalanobis] → Score',
            ha='center', va='center', color=FG, fontsize=20)

    ax.text(0.5, 0.24,
            'Time: 16 ms → 8 ms (≈2×, ≈77× total speedup)',
            ha='center', va='center', color=GREEN, fontsize=22, fontweight='bold')

    return save_frame(21, fig)


def slide_18():
    """Complete pipeline before vs after"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'COMPLETE PIPELINE: BEFORE VS AFTER',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    # Before
    ax.text(0.5, 0.74, 'BEFORE (621 ms):',
            ha='center', va='center', color=FG, fontsize=22, fontweight='bold')
    ax.add_patch(plt.Rectangle((0.08, 0.64), 0.84, 0.08,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.5, 0.68,
            'Image → ResNet (15 ms, CPU) → Embed (12 ms, CPU) → FOR loop [inv+mahal] (590 ms) → Score',
            ha='center', va='center', color=RED, fontsize=18)

    # After
    ax.text(0.5, 0.52, 'AFTER (8 ms):',
            ha='center', va='center', color=FG, fontsize=22, fontweight='bold')
    ax.add_patch(plt.Rectangle((0.08, 0.42), 0.84, 0.08,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.5, 0.46,
            'Image → [ONNX on GPU: ResNet + Embedding] (6 ms) → Mahal(einsum, CPU) (2 ms) → Score',
            ha='center', va='center', color=GREEN, fontsize=18)

    ax.text(0.5, 0.28,
            'Key changes:\n'
            '• Σ⁻¹ pre-computed at training time\n'
            '• Loop → einsum (3136 ops → 1 batched op)\n'
            '• PyTorch → ONNX Runtime\n'
            '• CPU → GPU for convolutional backbone',
            ha='center', va='center', color=FG, fontsize=20)

    return save_frame(22, fig)


def slide_19():
    """Benchmark Results Bar Chart"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'BENCHMARK RESULTS (Inference Time)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    labels = [
        'Baseline PyTorch (CPU)',
        'Hybrid - CPU',
        'Mahal ONNX - CPU',
        'Full ONNX - CPU',
        'Hybrid - GPU',
        'Mahal ONNX - GPU',
        'Full ONNX - GPU'
    ]
    times = [621, 36, 32, 16, 12, 11, 8]
    colors = [RED, ORANGE, ORANGE, GREEN, GREEN, GREEN, GREEN]

    y_pos = list(range(len(labels)))
    ax_bar = fig.add_axes([0.12, 0.15, 0.75, 0.6])
    ax_bar.set_facecolor(BG)
    ax_bar.barh(y_pos, times, color=colors)
    ax_bar.set_yticks(y_pos)
    ax_bar.set_yticklabels(labels, color=FG, fontsize=14)
    ax_bar.invert_yaxis()
    ax_bar.set_xlabel('Time (ms)', color=FG, fontsize=16)
    ax_bar.tick_params(colors=FG)

    for i, t in enumerate(times):
        ax_bar.text(t + 5, i, f'{t} ms',
                    va='center', color=FG, fontsize=12)

    return save_frame(23, fig)


def slide_20():
    """Speedup Progression"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'OPTIMIZATION PROGRESSION (SPEEDUP)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    stages = ['Base', 'Pre-comp Σ⁻¹', 'Vectorize', 'ONNX', 'GPU']
    speedups = [1, 8, 17, 39, 77]

    ax_plot = fig.add_axes([0.12, 0.2, 0.75, 0.6])
    ax_plot.set_facecolor(BG)
    ax_plot.plot(stages, speedups, marker='o', color=GREEN, linewidth=3)
    ax_plot.set_ylabel('Speedup (×)', color=FG, fontsize=16)
    ax_plot.set_ylim(0, 80)
    ax_plot.tick_params(colors=FG)
    for x, y in zip(stages, speedups):
        ax_plot.text(x, y + 2, f'{y}×', ha='center', color=FG, fontsize=12)

    return save_frame(20, fig)


def slide_21():
    """FPS Comparison"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'FRAMES PER SECOND (FPS)',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    labels = ['Base CPU', 'ONNX CPU', 'Hybrid GPU', 'Mahal GPU', 'Full ONNX GPU']
    fps = [1.6, 63.1, 83.0, 92.3, 124.8]
    colors = [RED, ORANGE, GREEN, GREEN, GREEN]

    ax_bar = fig.add_axes([0.12, 0.2, 0.75, 0.6])
    ax_bar.set_facecolor(BG)
    ax_bar.bar(labels, fps, color=colors)
    ax_bar.set_ylabel('FPS', color=FG, fontsize=16)
    ax_bar.tick_params(axis='x', rotation=20, colors=FG)
    ax_bar.tick_params(axis='y', colors=FG)

    for i, v in enumerate(fps):
        ax_bar.text(i, v + 3, f'{v:.1f}', ha='center', color=FG, fontsize=12)

    return save_frame(21, fig)


def slide_22():
    """CPU vs GPU Comparison"""
    fig, ax = new_fig()
    ax.text(0.5, 0.88, 'CPU vs GPU COMPARISON',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    headers = ['Model', 'CPU (ms)', 'GPU (ms)', 'Speedup']
    rows = [
        ('Hybrid', 36.2, 12.0, 3.01),
        ('Full ONNX', 15.9, 8.0, 1.98),
        ('Mahal ONNX', 31.8, 10.8, 2.94),
    ]
    table_text = [headers] + [[
        r[0], f'{r[1]:.1f}', f'{r[2]:.1f}', f'{r[3]:.2f}×'
    ] for r in rows]

    ax_table = fig.add_axes([0.12, 0.3, 0.76, 0.4])
    ax_table.axis('off')
    table = ax_table.table(cellText=table_text,
                           loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(16)
    table.scale(1, 2)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(FG)
        cell.set_facecolor(BG)
        cell._text.set_color(FG)
        if row == 0:
            cell._text.set_weight('bold')

    ax.text(0.5, 0.18,
            'Key insight: Algorithmic optimizations ≈40×, GPU ≈2× on top.\n'
            'GPU alone without algorithm fix → only modest speedup.',
            ha='center', va='center', color=FG, fontsize=20)

    return save_frame(22, fig)


def slide_23():
    """Accuracy Preserved"""
    fig, ax = new_fig()
    ax.text(0.5, 0.86, 'ACCURACY VERIFICATION',
            ha='center', va='center', color=FG,
            fontsize=30, fontweight='bold')

    ax.add_patch(plt.Rectangle((0.12, 0.55), 0.32, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.28, 0.65, 'BEFORE (Baseline)',
            ha='center', va='center', color=FG, fontsize=20)
    ax.text(0.28, 0.58,
            'Image AUROC: 90.54%\nPixel AUROC: 96.52%',
            ha='center', va='center', color=FG, fontsize=18)

    ax.add_patch(plt.Rectangle((0.56, 0.55), 0.32, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.72, 0.65, 'AFTER (Optimized)',
            ha='center', va='center', color=FG, fontsize=20)
    ax.text(0.72, 0.58,
            'Image AUROC: 90.54%\nPixel AUROC: 96.52%',
            ha='center', va='center', color=FG, fontsize=18)

    ax.text(0.5, 0.42, '=',
            ha='center', va='center', color=GREEN, fontsize=40, fontweight='bold')

    ax.text(0.5, 0.3,
            'Floating-point difference < 1e-5, AUROC unchanged\n'
            '77× faster with ZERO accuracy loss',
            ha='center', va='center', color=GREEN, fontsize=22)

    return save_frame(23, fig)


def slide_24():
    """Key Equations Summary + Final Summary merged"""
    fig, ax = new_fig()
    ax.text(0.5, 0.9, 'FINAL SUMMARY',
            ha='center', va='center', color=FG,
            fontsize=32, fontweight='bold')

    # Equations block
    eq_text = (
        '1. Gaussian parameters (training):\n'
        r'   $\mu_i = \frac{1}{N}\sum_{k=1}^N x_{k i}$' '\n'
        r'   $\Sigma_i = \frac{1}{N-1}\sum_{k=1}^N (x_{k i}-\mu_i)(x_{k i}-\mu_i)^T + \varepsilon I$'
        '\n\n'
        '2. Mahalanobis distance (inference):\n'
        r'   $d_i = \sqrt{(x_i - \mu_i)^T \Sigma_i^{-1} (x_i - \mu_i)}$'
        '\n\n'
        "3. Vectorized (all positions):\n"
        r"   $D = \mathrm{einsum}('cdi,bdi\to bci', \Sigma^{-1}, X-\mu)$"
    )
    ax.text(0.5, 0.6, eq_text,
            ha='center', va='center', color=CYAN, fontsize=18)

    # Metrics table
    ax.add_patch(plt.Rectangle((0.27, 0.18), 0.46, 0.2,
                               edgecolor=FG, facecolor='none'))
    ax.text(0.5, 0.31,
            'Metric      BEFORE       AFTER\n'
            'Time        621 ms  →   8 ms\n'
            'FPS         1.6     →   125\n'
            'Speedup     1×      →   77×\n'
            'Accuracy    90.5%   →   90.5%',
            ha='center', va='center', color=FG, fontsize=20,
            family='monospace')

    ax.text(0.5, 0.12,
            '77× FASTER  •  REAL-TIME READY  •  ZERO ACCURACY LOSS',
            ha='center', va='center', color=GREEN, fontsize=22, fontweight='bold')

    return save_frame(24, fig)


# -----------------------------
# Main: render slides & build GIF
# -----------------------------

def main():
    slide_funcs = [
        slide_01,           # Title
        slide_02,           # The Problem
        slide_03,           # Time breakdown
        slide_04,           # PaDiM Model Architecture
        slide_05_bottleneck_code,  # Bottleneck code
        slide_06_optimization_move_inverse,  # Move inverse outside loop
        slide_07_vectorize_merge,  # Vectorize the loop
        slide_08_three_moving_images,  # Three key optimizations
        slide_05,           # ResNet Feature Extraction
        slide_09a,          # Multi-scale
        slide_09b,          # Patch positions
        slide_09c,          # Gaussian per position
        slide_09d,          # Normal vs anomaly
        slide_09e,          # Mahalanobis equation
        slide_11,           # Baseline slow loop
        slide_12,           # Opt1 pre-compute
        slide_13,           # Sequential problem
        slide_14,           # Opt2 vectorize
        slide_15,           # Einsum visualization
        slide_16,           # Opt3 ONNX
        slide_17,           # Opt4 GPU
        slide_18,           # Pipeline compare
        slide_19,           # Benchmarks
        slide_20,           # Speedup progression
        slide_21,           # FPS
        slide_22,           # CPU vs GPU
        slide_23,           # Accuracy
        slide_24,           # Final summary
    ]

    # Durations (seconds) - SLOWER GIF (+2 seconds per slide)
    durations = [
        8,   # 1 Title
        8,   # 2 Problem
        10,  # 3 Time breakdown
        10,  # 4 PaDiM Model Architecture
        12,  # 5 Bottleneck code (long code, needs time to read)
        12,  # 6 Move inverse outside loop (important optimization)
        12,  # 7 Vectorize merge (important optimization)
        10,  # 8 Three moving images
        8,   # 9 ResNet
        8,   # 10 Multi-scale
        8,   # 11 Patch positions
        10,  # 12 Gaussian per position
        10,  # 13 Normal vs anomaly
        10,  # 14 Mahalanobis equation
        10,  # 15 Baseline slow loop
        10,  # 16 Opt1 pre-compute
        8,   # 17 Sequential problem
        10,  # 18 Opt2 vectorize
        8,   # 19 Einsum visualization
        8,   # 20 Opt3 ONNX
        10,  # 21 Opt4 GPU
        10,  # 22 Pipeline compare
        10,  # 23 Benchmarks
        10,  # 24 Speedup progression
        8,   # 25 FPS
        8,   # 26 CPU vs GPU
        8,   # 27 Accuracy
        12,  # 28 Final summary
    ]

    frame_files = []
    for i, func in enumerate(slide_funcs, start=1):
        print(f'Rendering slide {i:02d}')
        frame_files.append(func())

    images = [imageio.v2.imread(f) for f in frame_files]
    imageio.mimsave('padim_optimization.gif', images, duration=durations)
    print('GIF saved to padim_optimization.gif')


if __name__ == '__main__':
    main()
