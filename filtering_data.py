import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Filter 1: Multiple conditions — female passengers in 1st or 2nd class who survived
survivors = df[(df['Survived'] == 1) & (df['Sex'] == 'female') & (df['Pclass'] <= 2)]
print("Filter 1 — Female survivors in 1st/2nd class:")
print(survivors[['Name', 'Pclass', 'Age', 'Fare']].head())
print(f"  Count: {len(survivors)}")

# Filter 2: High fare passengers (top 10% — Fare above 90th percentile)
fare_90 = df['Fare'].quantile(0.90)
high_fare = df[df['Fare'] > fare_90]
print(f"\nFilter 2 — High-fare passengers (Fare > {fare_90:.2f}):")
print(high_fare[['Name', 'Fare', 'Pclass']].head())
print(f"  Count: {len(high_fare)}")

# Filter 3: Specific category — passengers who embarked from Cherbourg ('C'), age < 30
young_cherbourg = df[(df['Embarked'] == 'C') & (df['Age'] < 30)]
print("\nFilter 3 — Cherbourg embarkers under 30:")
print(young_cherbourg[['Name', 'Age', 'Embarked', 'Pclass']].head())
print(f"  Count: {len(young_cherbourg)}")
