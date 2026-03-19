import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# describe() gives count, mean, std, min, 25%, 50%, 75%, max for numerical columns
stats = df.describe()
print("Descriptive Statistics:")
print(stats)

print("\n── Manual Interpretation ──────────────────────────────────")

# Age
age_mean = df['Age'].mean()
age_std  = df['Age'].std()
age_min  = df['Age'].min()
age_max  = df['Age'].max()
print(f"\nAge:")
print(f"  Mean : {age_mean:.2f}  → average passenger was ~{age_mean:.0f} years old")
print(f"  Std  : {age_std:.2f}  → ages spread ~{age_std:.0f} years around the mean")
print(f"  Min  : {age_min:.1f}   → youngest passenger")
print(f"  Max  : {age_max:.1f}  → oldest passenger")

# Fare
fare_mean = df['Fare'].mean()
fare_std  = df['Fare'].std()
fare_min  = df['Fare'].min()
fare_max  = df['Fare'].max()
print(f"\nFare:")
print(f"  Mean : {fare_mean:.2f}  → average ticket price")
print(f"  Std  : {fare_std:.2f}  → high spread suggests very wide price range")
print(f"  Min  : {fare_min:.2f}   → some passengers paid nothing (crew / free passage)")
print(f"  Max  : {fare_max:.2f} → most expensive ticket was ~£{fare_max:.0f}")

# Survived
surv_mean = df['Survived'].mean()
print(f"\nSurvived:")
print(f"  Mean : {surv_mean:.4f} → ~{surv_mean*100:.1f}% of passengers survived")
