import pandas as pd

# Load dataset (using seaborn's built-in titanic as a 500+ row CSV alternative)
# To use your own CSV: df = pd.read_csv('your_file.csv')
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(f"Dataset shape: {df.shape}")
print(df.head(3))
print()

# ── loc: label-based selection ───────────────────────────────────────────────

# Example 1: Select rows 0–4, specific columns by name
ex1 = df.loc[0:4, ['Name', 'Age', 'Fare', 'Survived']]
print("loc Example 1 — rows 0–4, selected columns:")
print(ex1)

# Example 2: Filter survived passengers, show Name + Pclass + Age
ex2 = df.loc[df['Survived'] == 1, ['Name', 'Pclass', 'Age']]
print("\nloc Example 2 — survived passengers (first 5):")
print(ex2.head())

# Example 3: Passengers in 1st class with Fare > 100
ex3 = df.loc[(df['Pclass'] == 1) & (df['Fare'] > 100), ['Name', 'Fare', 'Embarked']]
print("\nloc Example 3 — 1st class, Fare > 100 (first 5):")
print(ex3.head())

print("\n" + "─" * 50)

# ── iloc: integer position-based selection ───────────────────────────────────

# Example 1: First 5 rows, first 4 columns
ex4 = df.iloc[0:5, 0:4]
print("\niloc Example 1 — rows 0–4, columns 0–3:")
print(ex4)

# Example 2: Every 50th row, columns at positions 1, 2, 4 (Name, Sex, Age)
ex5 = df.iloc[::50, [1, 2, 4]]
print("\niloc Example 2 — every 50th row, cols 1/2/4:")
print(ex5)

# Example 3: Last 5 rows, last 3 columns
ex6 = df.iloc[-5:, -3:]
print("\niloc Example 3 — last 5 rows, last 3 columns:")
print(ex6)
