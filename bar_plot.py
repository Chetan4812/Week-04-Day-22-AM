import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar Plot 1 — Survival rate by Passenger Class
surv_by_class = df.groupby('Pclass')['Survived'].mean() * 100
colors = ['#2ecc71', '#e67e22', '#e74c3c']
bars = axes[0].bar(surv_by_class.index.astype(str), surv_by_class.values,
                   color=colors, edgecolor='white', width=0.5)
for bar, val in zip(bars, surv_by_class.values):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                 f'{val:.1f}%', ha='center', fontsize=10, fontweight='bold')
axes[0].set_title('Survival Rate by Passenger Class', fontweight='bold')
axes[0].set_xlabel('Passenger Class')
axes[0].set_ylabel('Survival Rate (%)')
axes[0].set_ylim(0, 85)

# Bar Plot 2 — Average Fare by Passenger Class
avg_fare = df.groupby('Pclass')['Fare'].mean()
bars2 = axes[1].bar(avg_fare.index.astype(str), avg_fare.values,
                    color=['#3498db', '#9b59b6', '#1abc9c'], edgecolor='white', width=0.5)
for bar, val in zip(bars2, avg_fare.values):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'£{val:.1f}', ha='center', fontsize=10, fontweight='bold')
axes[1].set_title('Average Fare by Passenger Class', fontweight='bold')
axes[1].set_xlabel('Passenger Class')
axes[1].set_ylabel('Average Fare (£)')

plt.suptitle('Bar Plots — Titanic Dataset', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('bar_plot.png', dpi=150)
plt.show()

# Interpretation:
# 1st class had the highest survival rate (~63%) and paid the most (avg ~£84).
# 3rd class had the lowest survival rate (~24%) and paid the least (avg ~£14).
# Clear positive correlation between class/wealth and survival probability.
