import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Serif'

# ── helpers ───────────────────────────────────────────────────────────────────

def shade(color, factor):
    r, g, b = mcolors.to_rgb(color)
    return (min(1, r * factor), min(1, g * factor), min(1, b * factor))

def draw_box(ax, cx, cy, fw, fh, fd,
             color, alpha=0.90, skew=0.32, zbase=1):
    """
    cx, cy  : centre of front face
    fw      : front-face width  (represents channels, log-scaled)
    fh      : front-face height (represents feature map H, log-scaled)
    fd      : 3-D depth         (represents feature map W, log-scaled)
    """
    ox = fd * skew
    oy = fd * skew * 0.5

    x0, x1 = cx - fw / 2, cx + fw / 2
    y0, y1 = cy - fh / 2, cy + fh / 2

    kw = dict(linewidth=0.7, alpha=alpha)

    # dashed back edges
    for xs, ys, xe, ye in [
        (x0+ox, y0+oy, x1+ox, y0+oy),
        (x0+ox, y0+oy, x0+ox, y1+oy),
        (x0+ox, y0+oy, x0,    y0),
    ]:
        ax.plot([xs, xe], [ys, ye], '--', color='#999',
                lw=0.5, alpha=0.45, zorder=zbase)

    # right face
    ax.add_patch(plt.Polygon(
        [[x1, y0], [x1+ox, y0+oy], [x1+ox, y1+oy], [x1, y1]],
        fc=shade(color, 0.58), ec='#444', zorder=zbase+1, **kw))

    # top face
    ax.add_patch(plt.Polygon(
        [[x0, y1], [x1, y1], [x1+ox, y1+oy], [x0+ox, y1+oy]],
        fc=shade(color, 0.75), ec='#444', zorder=zbase+2, **kw))

    # front face
    ax.add_patch(plt.Polygon(
        [[x0, y0], [x1, y0], [x1, y1], [x0, y1]],
        fc=color, ec='#333', linewidth=1.0,
        alpha=alpha, zorder=zbase+3))

    return x1, x1 + ox   # front-right x, back-right x

# ── visual scaling (log) ──────────────────────────────────────────────────────

def vis_w(C): return np.log2(C + 1) * 0.22   # channels  → box width
def vis_h(H): return np.log2(H + 1) * 0.70   # H         → box height
def vis_d(W): return np.log2(W + 1) * 0.30   # W         → 3-D depth

# ── architecture definition ───────────────────────────────────────────────────
# (name, dim_label, C, H, W, color)
LAYERS = [
    ('Input',   '1×32×64',   1,   32, 64, '#CCCCCC'),
    ('Conv1',   '32×32×64',  32,  32, 64, '#AFC8D8'),
    ('DSC+CA',  '64×16×32',  64,  16, 32, '#89C4E1'),
    ('DSC+CA',  '128×8×16',  128,  8, 16, '#89C4E1'),
    ('DSC+CA',  '256×4×8',   256,  4,  8, '#89C4E1'),
    ('GAP',     '256×1×1',   256,  1,  1, '#AFC8D8'),
    ('FC',      '→ 2',         2,  6,  1, '#F4A87C'),
]

SKEW = 0.32
CY   = 2.5

fig, ax = plt.subplots(figsize=(17, 5.5))
ax.set_aspect('equal')
ax.axis('off')

x      = 0.5
prev_rx = None

for i, (name, dim, C, H, W, color) in enumerate(LAYERS):
    fw = vis_w(C)
    fh = vis_h(H)
    fd = vis_d(W)
    ox = fd * SKEW
    oy = fd * SKEW * 0.5

    cx = x + ox + fw / 2

    rx_front, rx_back = draw_box(ax, cx, CY, fw, fh, fd,
                                  color, skew=SKEW)

    # dim label above box
    ax.text(cx + ox / 2, CY + fh / 2 + oy + 0.09, dim,
            ha='center', va='bottom', fontsize=6.8,
            color='#222', zorder=20)

    # layer name below box
    ax.text(cx, CY - fh / 2 - 0.13, name,
            ha='center', va='top', fontsize=7.8,
            fontweight='bold', color='#333', zorder=20)

    # arrow from previous layer
    if prev_rx is not None:
        x_start = prev_rx + 0.04
        x_end   = cx - fw / 2 - 0.04
        if x_end > x_start + 0.05:
            ax.annotate('', xy=(x_end, CY), xytext=(x_start, CY),
                        arrowprops=dict(arrowstyle='->', color='#555',
                                        lw=1.2, mutation_scale=10),
                        zorder=20)

    prev_rx = rx_front
    x = rx_back + 0.32

# ── legend ────────────────────────────────────────────────────────────────────
from matplotlib.patches import Patch
ax.legend(handles=[
    Patch(fc='#CCCCCC', ec='#333', label='Input'),
    Patch(fc='#AFC8D8', ec='#333', label='Conv / GlobalAvgPool'),
    Patch(fc='#89C4E1', ec='#333', label='DSC Block + CoordAtt  ×3'),
    Patch(fc='#F4A87C', ec='#333', label='Fully Connected'),
], loc='upper right', fontsize=8.5, framealpha=0.85)

ax.set_title('LightweightCNN Architecture', fontsize=13,
             pad=14, fontweight='bold')

ax.autoscale_view()
xl = ax.get_xlim()
yl = ax.get_ylim()
ax.set_xlim(xl[0] - 0.2, xl[1] + 0.2)
ax.set_ylim(yl[0] - 0.4, yl[1] + 0.6)

plt.tight_layout()
plt.savefig('fig4_1_architecture.png', dpi=300,
            bbox_inches='tight', facecolor='white')
print("Saved: fig4_1_architecture.png")
plt.show()
