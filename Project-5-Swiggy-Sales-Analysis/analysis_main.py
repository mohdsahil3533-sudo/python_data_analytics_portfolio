### IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

### IMPORTING RAW DATA
df = pd.read_excel("swiggy_data.xlsx")

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
print("Missing values:")
print(df.isnull().sum())


## DUPLICATE VALUES ##
print("Duplicate values:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()
print("Duplicate values after removing:", df.duplicated().sum())

## DATA INFO ##
print("Information of data:",df.info())

## DATA SUMMERY ##
print("Summery of data:",df.describe())

### KPI's
# Total Sales
total_sales = df["Price (INR)"].sum()
print("Total Sales in INR:", round(total_sales, 2))

# Average Rating
avg_rating = df["Rating"].mean()
print("Average Rating:", round(avg_rating, 1))

# Average Order Value
avg_order_value = df["Price (INR)"].mean()
print("Average Order Valuein INR:", round(avg_order_value, 2))

# Rating Count
rating_count = df["Rating Count"].sum()
print("Rating Count:", rating_count)

# Total Orders
total_orders = len(df)
print("Total Orders:", total_orders)

### CHART DESIGN
## MONTHLY SALES TREND ##
# Convert Order Date into datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month column
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Price (INR)"].sum().reset_index()

# Line Chart
plt.figure(figsize=(6, 5))

sns.lineplot(
    data=monthly_sales,
    x="Month",
    y="Price (INR)",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


## DAILY SALES TREND ##
# Convert Order Date to datetime
df["DayName"] = pd.to_datetime(df["Order Date"]).dt.day_name()

# Calculate daily sales by day name
daily_sales = df.groupby("DayName")["Price (INR)"].sum().reset_index()

# Arrange days in correct order
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily_sales["DayName"] = pd.Categorical(
    daily_sales["DayName"],
    categories=day_order,
    ordered=True
)

daily_sales = daily_sales.sort_values("DayName")

# Bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(
    daily_sales["DayName"],
    daily_sales["Price (INR)"]
)

# Add labels
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():,.0f}',
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.title("Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

## Total Sales by Food Type (Veg vs Non Veg)
non_veg_keywords = [
    "chicken",
    "egg",
    "fish",
    "mutton",
    "prawn",
    "biryani",
    "kabab",
    "kebab",
    "non-veg",
    "non veg"
]

# Create Food Category
df["Food Category"] = np.where(
    df["Dish Name"].str.lower().str.contains(
        "|".join(non_veg_keywords),
        na=False
    ),
    "Non-Veg",
    "Veg"
)

# Calculate revenue by food category
food_revenue = (
    df.groupby("Food Category")["Price (INR)"]
    .sum()
    .reset_index()
)

# Donut chart
fig = px.pie(
    food_revenue,
    values="Price (INR)",
    names="Food Category",
    hole=0.5,
    title="Revenue Contribution: Veg vs Non-Veg"
)

# Add percentage and labels
fig.update_traces(
    textinfo="percent+label",
    pull=[0.05, 0]
)

fig.update_layout(
    height=500,
    margin=dict(t=60, b=40, l=40, r=40)
)

fig.show()


## TOTAL SALES BY STATE ##
state_sales = (
    df.groupby("State")["Price (INR)"]
    .sum()
    .reset_index()
    .sort_values("Price (INR)", ascending=True)
)

plt.figure(figsize=(10, 8))

bars = plt.barh(
    state_sales["State"],
    state_sales["Price (INR)"]
)

# Add labels
for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f'₹{bar.get_width():,.0f}',
        va="center",
        fontsize=8
    )

plt.title("Total Sales by State")
plt.xlabel("Total Sales (INR)")
plt.ylabel("State")

plt.tight_layout()
plt.show()


## QUARTERLY PERFORMANCE SUMMARY ##
# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Quarter column
df["Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)

# Quarterly performance
quarterly_summary = (
    df.groupby("Quarter")
    .agg(
        Total_Sales=("Price (INR)", "sum"),
        Total_Orders=("Price (INR)", "count"),
        Average_Order_Value=("Price (INR)", "mean"),
        Average_Rating=("Rating", "mean"),
        Rating_Count=("Rating Count", "sum")
    )
    .reset_index()
)

# Round values
quarterly_summary["Total_Sales"] = quarterly_summary["Total_Sales"].round(2)
quarterly_summary["Average_Order_Value"] = quarterly_summary["Average_Order_Value"].round(2)
quarterly_summary["Average_Rating"] = quarterly_summary["Average_Rating"].round(2)

print("\nQuarterly Performance Summary:")
print(quarterly_summary)


## TOP 5 CITIES BY SALES ##
top_5_cities = (
    df.groupby("City")["Price (INR)"]
    .sum()
    .reset_index()
    .sort_values("Price (INR)", ascending=False)
    .head(5)
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    top_5_cities["City"],
    top_5_cities["Price (INR)"]
)

# Add sales labels
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'₹{bar.get_height():,.0f}',
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Top 5 Cities by Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales (INR)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()