import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram — Age distribution
axes[0].hist(df['Age'].dropna(), bins=30, color='steelblue', edgecolor='white', alpha=0.85)
axes[0].set_title('Age Distribution', fontweight='bold')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')
axes[0].axvline(df['Age'].mean(), color='crimson', linestyle='--', linewidth=1.5,
                label=f"Mean = {df['Age'].mean():.1f}")
axes[0].axvline(df['Age'].median(), color='orange', linestyle='--', linewidth=1.5,
                label=f"Median = {df['Age'].median():.1f}")
axes[0].legend()

# Histogram — Fare distribution (right-skewed)
axes[1].hist(df['Fare'], bins=40, color='teal', edgecolor='white', alpha=0.85)
axes[1].set_title('Fare Distribution', fontweight='bold')
axes[1].set_xlabel('Fare (£)')
axes[1].set_ylabel('Frequency')
axes[1].axvline(df['Fare'].mean(), color='crimson', linestyle='--', linewidth=1.5,
                label=f"Mean = {df['Fare'].mean():.1f}")
axes[1].legend()

plt.suptitle('Histograms — Titanic Dataset', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('histogram.png', dpi=150)
plt.show()

# Interpretation:
# Age  → roughly bell-shaped (normal), slight right skew; most passengers were 20–40 years old.
# Fare → strongly right-skewed; majority paid low fares, a few outliers paid very high prices.
#        Mean > Median confirms positive (right) skew.
