import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# ── KDE vs Histogram: Age ─────────────────────────────────────────────────────
age_data = df['Age'].dropna()
x_age = np.linspace(age_data.min(), age_data.max(), 300)
kde_age = gaussian_kde(age_data)

axes[0].hist(age_data, bins=30, density=True, color='steelblue',
             alpha=0.4, edgecolor='white', label='Histogram (density)')
axes[0].plot(x_age, kde_age(x_age), color='crimson', linewidth=2.5, label='KDE')
axes[0].set_title('Age — Histogram vs KDE', fontweight='bold')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Density')
axes[0].legend()

# ── KDE: Age by Survival status ───────────────────────────────────────────────
survived     = df[df['Survived'] == 1]['Age'].dropna()
not_survived = df[df['Survived'] == 0]['Age'].dropna()

x_range = np.linspace(0, 80, 300)
kde_surv  = gaussian_kde(survived)
kde_nsurv = gaussian_kde(not_survived)

axes[1].plot(x_range, kde_surv(x_range),  color='green', linewidth=2.5, label='Survived')
axes[1].plot(x_range, kde_nsurv(x_range), color='crimson', linewidth=2.5, label='Did Not Survive')
axes[1].fill_between(x_range, kde_surv(x_range),  alpha=0.15, color='green')
axes[1].fill_between(x_range, kde_nsurv(x_range), alpha=0.15, color='crimson')
axes[1].set_title('Age KDE — Survived vs Not Survived', fontweight='bold')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Density')
axes[1].legend()

plt.suptitle('KDE Plots — Titanic Dataset', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('kde_plot.png', dpi=150)
plt.show()

# Interpretation:
# KDE is a smoothed version of the histogram — it shows the underlying probability
# density without being affected by bin width choices.
# The survival KDE shows children (age 0–10) had higher survival density,
# while non-survivors peak around age 20–30 (many young men in 3rd class).
