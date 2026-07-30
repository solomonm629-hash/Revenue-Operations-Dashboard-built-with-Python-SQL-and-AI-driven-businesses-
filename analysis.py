# Revenue Operations Dashboard Analysis

import pandas as pd

# Load the revenue data
df = pd.read_csv("revenue_data.csv")

print("Revenue Operations Dashboard")
print("============================")
print(df)

print("\nTotal Revenue:", df["Revenue"].sum())
print("Average Revenue:", df["Revenue"].mean())
print("Highest Revenue:", df["Revenue"].max())
print("Average Churn Rate:", df["Churn"].mean())
print("Total Customers:", df["Customers"].max())
