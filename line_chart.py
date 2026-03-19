import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Index-based trend: rolling average of Fare across passenger index
# (Titanic has no datetime column; we use PassengerId as the x-axis)
df_sorted = df.sort_values('PassengerId').reset_index(drop=True)
rolling_fare = df_sorted['Fare'].rolling(window=20, min_periods=1).mean()
rolling_age  = df_sorted['Age'].rolling(window=20, min_periods=1).mean()

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Line Chart 1 — Rolling average fare
axes[0].plot(df_sorted.index, df_sorted['Fare'], color='lightsteelblue',
             alpha=0.4, linewidth=0.8, label='Fare')
axes[0].plot(df_sorted.index, rolling_fare, color='steelblue',
             linewidth=2, label='Rolling Mean (window=20)')
axes[0].set_title('Fare Trend across Passenger Index (Rolling Mean)', fontweight='bold')
axes[0].set_xlabel('Passenger Index')
axes[0].set_ylabel('Fare (£)')
axes[0].legend()

# Line Chart 2 — Rolling average age
axes[1].plot(df_sorted.index, df_sorted['Age'], color='#f0a500',
             alpha=0.3, linewidth=0.8, label='Age')
axes[1].plot(df_sorted.index, rolling_age, color='darkorange',
             linewidth=2, label='Rolling Mean (window=20)')
axes[1].set_title('Age Trend across Passenger Index (Rolling Mean)', fontweight='bold')
axes[1].set_xlabel('Passenger Index')
axes[1].set_ylabel('Age')
axes[1].legend()

plt.suptitle('Line Charts — Titanic Dataset', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('line_chart.png', dpi=150)
plt.show()

# Interpretation:
# Fare shows high volatility with a few large spikes (luxury tickets); rolling mean
# stays mostly flat with occasional peaks, suggesting most passengers paid similar fares.
# Age rolling mean stays around 28–32 throughout, indicating consistent age distribution.
