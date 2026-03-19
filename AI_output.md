### Data Analysis with Pandas and Visualization with Matplotlib

#### 1. Pandas — Core Operations

**`loc` vs `iloc`**

`loc` selects data by **label** (row index name or column name).
`iloc` selects data by **integer position** (0-based index).

```python
import pandas as pd

df = pd.read_csv('titanic.csv')

# loc — label-based
df.loc[0:4, ['Name', 'Age', 'Fare']]           # rows 0–4, named columns
df.loc[df['Survived'] == 1, ['Name', 'Pclass']] # conditional row filter

# iloc — position-based
df.iloc[0:5, 0:3]   # first 5 rows, first 3 columns
df.iloc[-5:, -2:]   # last 5 rows, last 2 columns
```

**Filtering with multiple conditions:**
```python
# Female 1st-class survivors
filtered = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Survived'] == 1)]

# Above-average fare
avg = df['Fare'].mean()
high_fare = df[df['Fare'] > avg]
```

**Descriptive Statistics:**
```python
print(df.describe())
# Outputs: count, mean, std, min, 25%, 50%, 75%, max for all numeric columns
```

> *Source: Pandas documentation — pandas.pydata.org*

---

#### 2. Matplotlib — Visualization

**Histogram:**
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df['Age'].dropna(), bins=30, color='steelblue', edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
# Interpretation: reveals spread, skewness, and mode of the distribution.
```

**Bar Plot:**
```python
surv_rate = df.groupby('Pclass')['Survived'].mean() * 100
surv_rate.plot(kind='bar', color=['green', 'orange', 'red'], edgecolor='white')
plt.title('Survival Rate by Class')
plt.ylabel('Survival Rate (%)')
plt.show()
```

**Line Chart:**
```python
rolling = df['Fare'].rolling(window=20).mean()
plt.plot(rolling, color='teal', linewidth=2)
plt.title('Rolling Mean Fare')
plt.show()
```

**KDE Plot:**
```python
from scipy.stats import gaussian_kde
import numpy as np

data = df['Age'].dropna()
x = np.linspace(data.min(), data.max(), 300)
kde = gaussian_kde(data)
plt.plot(x, kde(x), color='crimson', linewidth=2)
plt.title('Age KDE')
plt.show()
# KDE is a smoothed histogram — not dependent on bin width.
```

### Key Differences

| Plot Type | Best Used For | Key Insight |
| :--- | :--- | :--- |
| **Histogram** | Distribution of numeric values | Skewness, spread, mode |
| **Bar Plot** | Category vs numeric comparison | Ranking, group comparison |
| **Line Chart** | Trends over index or time | Direction and continuity |
| **KDE Plot** | Smooth density distribution | Shape without bin-width bias |
