import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ── Task 1: Grouped Analysis ──────────────────────────────────────────────────

# Group by Pclass and compute mean values for key numerical columns
grouped = df.groupby('Pclass')[['Age', 'Fare', 'Survived']].mean().round(2)
grouped.columns = ['Mean Age', 'Mean Fare', 'Survival Rate']
grouped['Survival Rate'] = (grouped['Survival Rate'] * 100).round(1)
print("Grouped by Passenger Class — Mean Values:")
print(grouped)

# Group by Sex
grouped_sex = df.groupby('Sex')[['Age', 'Fare', 'Survived']].mean().round(2)
print("\nGrouped by Sex — Mean Values:")
print(grouped_sex)

# ── Task 2: Visualise Grouped Results ─────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

# Mean Age by class
axes[0].bar(grouped.index.astype(str), grouped['Mean Age'],
            color=['#3498db', '#e67e22', '#e74c3c'], edgecolor='white', width=0.5)
axes[0].set_title('Mean Age by Class', fontweight='bold')
axes[0].set_xlabel('Passenger Class')
axes[0].set_ylabel('Mean Age')

# Mean Fare by class
axes[1].bar(grouped.index.astype(str), grouped['Mean Fare'],
            color=['#2ecc71', '#9b59b6', '#1abc9c'], edgecolor='white', width=0.5)
axes[1].set_title('Mean Fare by Class', fontweight='bold')
axes[1].set_xlabel('Passenger Class')
axes[1].set_ylabel('Mean Fare (£)')

# Survival rate by class
bars = axes[2].bar(grouped.index.astype(str), grouped['Survival Rate'],
                   color=['gold', 'silver', '#cd7f32'], edgecolor='white', width=0.5)
for bar, val in zip(bars, grouped['Survival Rate']):
    axes[2].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'{val:.1f}%', ha='center', fontsize=10, fontweight='bold')
axes[2].set_title('Survival Rate by Class', fontweight='bold')
axes[2].set_xlabel('Passenger Class')
axes[2].set_ylabel('Survival Rate (%)')
axes[2].set_ylim(0, 80)

plt.suptitle('Grouped Analysis — Titanic by Passenger Class', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('grouped_bar_plots.png', dpi=150)
plt.show()

# ── Task 3: Compare Two Numerical Features — Age vs Fare (KDE) ───────────────

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# KDE comparison: Age and Fare per class
class_colors = {1: '#3498db', 2: '#e67e22', 3: '#e74c3c'}

for pclass, color in class_colors.items():
    subset = df[df['Pclass'] == pclass]['Age'].dropna()
    x = np.linspace(0, 80, 300)
    kde = gaussian_kde(subset)
    axes[0].plot(x, kde(x), color=color, linewidth=2, label=f'Class {pclass}')
    axes[0].fill_between(x, kde(x), alpha=0.1, color=color)

axes[0].set_title('Age Distribution by Class (KDE)', fontweight='bold')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Density')
axes[0].legend()

# Line chart: cumulative mean Fare vs Age (binned)
df_clean = df[['Age', 'Fare']].dropna()
df_clean['AgeBin'] = pd.cut(df_clean['Age'], bins=range(0, 85, 5))
age_fare = df_clean.groupby('AgeBin', observed=False)['Fare'].mean()

axes[1].plot(range(len(age_fare)), age_fare.values, 'o-', color='teal',
             linewidth=2, markersize=5)
axes[1].set_xticks(range(len(age_fare)))
axes[1].set_xticklabels([str(b) for b in age_fare.index], rotation=45, fontsize=7)
axes[1].set_title('Mean Fare by Age Group (Line Chart)', fontweight='bold')
axes[1].set_xlabel('Age Bin')
axes[1].set_ylabel('Mean Fare (£)')

plt.suptitle('Comparing Age and Fare — Titanic', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('age_fare_comparison.png', dpi=150)
plt.show()

# ── Task 4: Insights ──────────────────────────────────────────────────────────
print("\n── Insights ────────────────────────────────────────────────────────────")
print("1. 1st class passengers were older on average (~38) vs 3rd class (~25).")
print("2. Fare gap is dramatic: 1st class avg £84 vs 3rd class avg £14.")
print("3. Survival strongly correlated with class: 63% (1st) → 24% (3rd).")
print("4. Age KDE shows 3rd class had more young adults; 1st class more middle-aged.")
print("5. Mean fare spikes for passengers aged 40–60, likely wealthy older travellers.")
