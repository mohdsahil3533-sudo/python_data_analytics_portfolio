## IMPORT LIBRARIES ##

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## IMPORT RAW DATA ##
df = pd.read_csv(r"C:\Users\mohds\OneDrive\Documents\Data Analytics\Python for Data Analytics\Projects\Project-11-Blinkit-Sales-Analysis\blinkit_data.csv")

## SAMPLE DATA ##
print(df.head(10))
print(df.tail(10))

## SIZE OF DATA ##
print("Size of data:",df.shape)

## FIELD INFO ##
print(df.columns)

## DATA TYPES ##
print(df.dtypes)

## NULL VALUES ##

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing Item Weight values with median
df['Item Weight'] = df['Item Weight'].fillna(df['Item Weight'].median())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

## DUPLICATE VALUES ##
print("Duplicate values:")
print(df.duplicated().sum())

## REPLACE VALUES ##

# Check values before replace
print(df["Item Fat Content"].unique())

df["Item Fat Content"] = df["Item Fat Content"].replace({"low fat" : "Low Fat", "LF" : "Low Fat", "reg" : "Regular"})

# Check values after replace
print(df["Item Fat Content"].unique())

## DATA INFO ##
print("Information of data:",df.info())

## DATA SUMMERY ##
print("Summery of data:",df.describe())

## BUSINESS REQUIREMENTS ##
## KPI's Requirement ##

# Total Sales
total_sales = df["Sales"].sum()

# Average Sales
average_sales = df["Sales"].mean()

# Num of Items Sold
num_of_items_sold = df["Sales"].count()

# Average rating
ave_rating = df["Rating"].mean()

# Display
print(f"Total Sales: ${total_sales:,.1f}")
print(f"Average Sales: ${average_sales:,.1f}")
print(f"Num of Items Sold: ${num_of_items_sold:,.1f}")
print(f"Average rating: ${ave_rating:,.1f}")

## CHARTS REQUIREMENTS ##
# Total Sales by Fat Content
sales_by_fat = (df.groupby("Item Fat Content")["Sales"].sum().sort_values(ascending=False))
plt.figure(figsize=(8, 5))
bars = plt.bar(sales_by_fat.index, sales_by_fat.values)
plt.title("Total Sales by Item Fat Content", fontsize=14, fontweight="bold")
plt.xlabel("Item Fat Content")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

# Add sales values on bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()

# Total Sales by Item Type
sales_by_item_type = (
    df.groupby("Item Type")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    sales_by_item_type.index,
    sales_by_item_type.values
)

plt.title("Total Sales by Item Type", fontsize=14, fontweight="bold")
plt.xlabel("Item Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")

# Add sales values on bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.show()

# Total Sales by Item Type
grouped = df.groupby(['Outlet Location Type', 'Item Fat Content']) ['Sales'].sum().unstack()
grouped = grouped [['Regular', 'Low Fat']]
ax = grouped.plot(kind='bar', figsize=(8, 5), title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()

# Total Sales by Outlet Establishment Year
sales_by_year = (
    df.groupby("Outlet Establishment Year")["Sales"]
      .sum()
      .sort_index()
)

plt.figure(figsize=(10, 6))

plt.plot(
    sales_by_year.index,
    sales_by_year.values,
    marker="o",
    linewidth=2
)

plt.title(
    "Total Sales by Outlet Establishment Year",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Outlet Establishment Year")
plt.ylabel("Total Sales")

plt.xticks(sales_by_year.index, rotation=45)

# Add sales values
for year, sales in sales_by_year.items():
    plt.text(
        year,
        sales,
        f"{sales:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# Total Sales by Outlet Size
sales_by_outlet_size = (
    df.groupby("Outlet Size")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

plt.pie(
    sales_by_outlet_size,
    labels=sales_by_outlet_size.index,
    autopct="%.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1},
    textprops={"fontsize": 10}
)

plt.title(
    "Total Sales Distribution by Outlet Size",
    fontsize=14,
    fontweight="bold"
)

plt.axis("equal")
plt.tight_layout()
plt.show()

# Total Sales by Outlet Location
sales_by_location = (
    df.groupby("Outlet Location Type")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

bars = plt.bar(
    sales_by_location.index,
    sales_by_location.values
)

plt.title(
    "Total Sales by Outlet Location Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Outlet Location Type")
plt.ylabel("Total Sales")

# Add sales values on bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()


















