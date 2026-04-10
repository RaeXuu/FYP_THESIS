"""
Conceptual confusion matrix figure for heart sound classification.
Adapted for Normal/Abnormal binary classification (Abnormal = positive class).
Shows TP/FP/TN/FN definitions + Se, Sp, M-Score formulas.

Output: photo-from-PC/fig_confusion_concept.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# ── colour palette ──────────────────────────────────────────────
GREEN = '#2e7d32'
RED   = '#c62828'
WHITE = 'white'

CELL_ALPHA = 0.88

# ── cell positions (left, bottom, width, height) ────────────────
cells = {
    'TP': (0.6, 2.6, 2.8, 2.8),   # top-left
    'FN': (3.5, 2.6, 2.8, 2.8),   # top-right
    'FP': (0.6, 0.2, 2.8, 2.4),   # bottom-left  (slightly shorter)
    'TN': (3.5, 0.2, 2.8, 2.4),   # bottom-right
}

colors = {'TP': GREEN, 'FN': RED, 'FP': RED, 'TN': GREEN}

for key, (x, y, w, h) in cells.items():
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="square,pad=0.0",
        facecolor=colors[key], edgecolor='black', linewidth=2,
        alpha=CELL_ALPHA, zorder=2
    )
    ax.add_patch(rect)

# ── cell text ───────────────────────────────────────────────────
cell_texts = {
    'TP': ("True Positive (TP)",
           "Abnormal correctly\nidentified as Abnormal"),
    'FN': ("False Negative (FN)",
           "Abnormal missed,\npredicted as Normal"),
    'FP': ("False Positive (FP)",
           "Normal misclassified\nas Abnormal"),
    'TN': ("True Negative (TN)",
           "Normal correctly\nidentified as Normal"),
}

offsets = {          # (cx, cy)
    'TP': (2.00, 4.00),
    'FN': (4.90, 4.00),
    'FP': (2.00, 1.40),
    'TN': (4.90, 1.40),
}

for key, (title, desc) in cell_texts.items():
    cx, cy = offsets[key]
    ax.text(cx, cy + 0.45, title,
            ha='center', va='center', fontsize=9.5, fontweight='bold',
            color=WHITE, zorder=3)
    ax.text(cx, cy - 0.15, desc,
            ha='center', va='center', fontsize=8.5,
            color=WHITE, style='italic', zorder=3, linespacing=1.5)

# ── axis labels ─────────────────────────────────────────────────
# "Predicted" arrow on top
ax.annotate('', xy=(6.45, 5.7), xytext=(0.55, 5.7),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(3.5, 5.85, 'Predicted', ha='center', va='center',
        fontsize=11, fontweight='bold')

ax.text(2.00, 5.55, 'Abnormal', ha='center', va='center', fontsize=9.5)
ax.text(4.90, 5.55, 'Normal',   ha='center', va='center', fontsize=9.5)

# "Actual" arrow on left
ax.annotate('', xy=(0.45, 0.1), xytext=(0.45, 5.5),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(0.18, 2.85, 'Actual', ha='center', va='center',
        fontsize=11, fontweight='bold', rotation=90)

ax.text(0.52, 4.00, 'Abnormal', ha='center', va='center',
        fontsize=9.5, rotation=90)
ax.text(0.52, 1.40, 'Normal',   ha='center', va='center',
        fontsize=9.5, rotation=90)

# ── formula annotations beside matrix ───────────────────────────
# Sensitivity (Se) — right of top row
ax.text(6.6, 4.00,
        r'$Se = \frac{TP}{TP + FN}$',
        ha='left', va='center', fontsize=11)

# Specificity (Sp) — right of bottom row
ax.text(6.6, 1.40,
        r'$Sp = \frac{TN}{TN + FP}$',
        ha='left', va='center', fontsize=11)

# ── vertical divider ────────────────────────────────────────────
ax.plot([8.55, 8.55], [0.0, 5.95], color='#bbbbbb', lw=1.2, ls='--', zorder=1)

# ── M-Score box on far right ────────────────────────────────────
ax.text(8.75, 4.80,
        r'$M\text{-}Score = \frac{Se + Sp}{2}$',
        ha='left', va='center', fontsize=11)

ax.text(8.75, 3.40,
        r'$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$',
        ha='left', va='center', fontsize=10)

ax.text(8.75, 2.15,
        r'$Precision = \frac{TP}{TP + FP}$',
        ha='left', va='center', fontsize=10)

ax.text(8.75, 1.05,
        r'$F1 = \frac{2 \cdot Se \cdot Precision}{Se + Precision}$',
        ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('photo-from-PC/fig_confusion_concept.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Saved: photo-from-PC/fig_confusion_concept.png")
