
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Retail_Sales_Data_Unlox (1).csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create a folder for charts
import os
os.makedirs("charts", exist_ok=True)

# 1. Monthly revenue trend
monthly_revenue = (
    df.set_index("Date")["Revenue"]
    .resample("MS")
    .sum()
)

plt.figure(figsize=(12, 5))
monthly_revenue.plot(marker="o")
plt.title("Monthly Revenue Trend (2023-2024)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png", dpi=150)
plt.close()

# 2. Revenue by region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values()

plt.figure(figsize=(9, 5))
region_revenue.plot(kind="barh")
plt.title("Revenue by Region")
plt.xlabel("Revenue")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png", dpi=150)
plt.close()

# 3. Revenue by product category
category_revenue = (
    df.groupby("Product_Category")["Revenue"].sum().sort_values()
)

plt.figure(figsize=(10, 6))
category_revenue.plot(kind="barh")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig("charts/revenue_by_category.png", dpi=150)
plt.close()

print("Sales charts created successfully!")
print("Check the charts folder for:")
print("1. monthly_revenue.png")
print("2. revenue_by_region.png")
print("3. revenue_by_category.png")
