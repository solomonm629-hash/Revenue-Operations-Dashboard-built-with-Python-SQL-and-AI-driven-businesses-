
import pandas as pd

# Load data
df = pd.read_csv("revenue_data.csv")

# Calculate profit
df["Profit"] = df["Revenue"] - df["Expenses"]

print("===== Revenue Operations Dashboard =====")
print(df)

print("\nBusiness Summary")
print("----------------")
print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
print(f"Total Expenses: ${df['Expenses'].sum():,.0f}")
print(f"Total Profit: ${df['Profit'].sum():,.0f}")
print(f"Average Monthly Revenue: ${df['Revenue'].mean():,.0f}")
print(f"Highest Monthly Revenue: ${df['Revenue'].max():,.0f}")
print(f"Average Churn: {df['Churn'].mean():.2f}%")
print(f"Latest Customer Count: {df['Customers'].iloc[-1]:,}")