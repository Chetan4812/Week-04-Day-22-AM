import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Filter rows where a column value is greater than the column's average

# Example 1: Passengers whose Fare is above average
avg_fare = df['Fare'].mean()
above_avg_fare = df[df['Fare'] > avg_fare]

print(f"Average Fare : £{avg_fare:.2f}")
print(f"Rows above average fare: {len(above_avg_fare)} / {len(df)}")
print(above_avg_fare[['Name', 'Fare', 'Pclass']].head())

# Example 2: Passengers whose Age is above average
avg_age = df['Age'].mean()
above_avg_age = df[df['Age'] > avg_age]

print(f"\nAverage Age : {avg_age:.2f}")
print(f"Rows above average age: {len(above_avg_age)} / {len(df)}")
print(above_avg_age[['Name', 'Age', 'Pclass']].head())
