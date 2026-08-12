# Import Python Libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

## BASIC DATA ANALYSIS ##

# To check the shape of the dataset (count of rows and columns)
print("Shape of the dataset:", df.shape)

# To check the first 5 rows of the dataset (details of the dataset)
print("First 5 rows of the dataset:")
print(df.head())

# To check the information of the dataset (data types, null values, etc.)
print("Information of the dataset:")
print(df.info())

# Delete unwanted columns from the dataset
df = df.drop(['Status', 'unnamed1'], axis=1)
print(df.head())

# To check the duplicate values in the dataset
print("Duplicate values in the dataset:")
print(df.duplicated().sum())

# To show the duplicate values in the dataset
print("Duplicate values in the dataset:")
print(df[df.duplicated(keep=False )])

# To remove the duplicate values from the dataset
df = df.drop_duplicates()

# To check the duplicate values in the dataset after removing them
print("Duplicate values in the dataset:")
print(df.duplicated().sum())

# To check the null values in the dataset
print("Null values in the dataset:")
print(df.isnull().sum())

# To show the null values in the dataset
print("Null values in the dataset:")
print(df[df.isnull().any(axis=1)])

# To remove the null values from the dataset
df = df.dropna()

# To check the null values in the dataset after removing them
print("Null values in the dataset:")    
print(df.isnull().sum())

# To rename & convert the column names of the dataset
df = df.rename(columns={'User_ID': 'User_ID', 'Cust_name': 'Customer_Name', 'Age Group': 'Age_Group'})
print("Renamed column names of the dataset:")
print(df.head())  

# To check the data types of the dataset
print("Data types of the dataset:")
print(df.dtypes)

# To convert the data types of the dataset
df['Amount'] = df['Amount'].astype(int)
print("Data types of the dataset after conversion:")
print(df.dtypes)

# To check the unique values of the dataset
print("Unique values of the dataset:")
print(df.nunique())

# To check the statistical summary of the dataset
print("Statistical summary of the dataset:")
print(df[['Age', 'Orders', 'Amount']].describe())

## EXPLORATORY DATA ANALYSIS ##

# To plot the bar graph of the dataset (Gender vs Count)
sns.set(rc={'figure.figsize':(10,5)})
ax = sns.countplot(x = 'Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)

plt.show()

# To plot the bar graph of the dataset (Gender vs Total Amount)
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

plt.show()

# To plot the count graph of the dataset (Age Group vs Gender)
sns.set(rc={'figure.figsize':(10,5)})
ax = sns.countplot(x = 'Age_Group', hue = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)

plt.show()  

# Total Amount vs Age Group
sales_age = df.groupby(['Age_Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(10,5)})

sns.barplot(x = 'Age_Group',y= 'Amount' ,data = sales_age)
plt.show()  

# Total number of orders in top 5 states
top_states = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x = 'State',y= 'Orders' ,data = top_states)
plt.show()

# Marital Status vs Count
sns.set(rc={'figure.figsize':(10,5)})
ax = sns.countplot(x = 'Marital_Status', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Marital Status vs Total Amount
sales_marital = df.groupby(['Marital_Status'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x = 'Marital_Status',y= 'Amount' ,data = sales_marital)
plt.show()

# Occupation vs Count
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x = 'Occupation', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show() 

# Occupation vs Total Amount
sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Occupation',y= 'Amount' ,data = sales_occupation)
plt.show()

# Product Category vs Count
sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(x = 'Product_Category', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Product Category vs Total Amount
sales_product = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(x = 'Product_Category',y= 'Amount' ,data = sales_product)
plt.show()

# Top 10 most sold products
top_products = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_ID',y= 'Orders' ,data = top_products)
plt.show()

# ============================================================
# CONCLUSION AND INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("              CONCLUSION AND INSIGHTS")
print("=" * 60)

# 1. Total Sales
total_sales = df['Amount'].sum()
total_orders = df['Orders'].sum()
total_customers = df['User_ID'].nunique()

print("\n1. Overall Sales Performance")
print(f"Total Sales Amount: ₹{total_sales:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Unique Customers: {total_customers:,}")


# 2. Gender Analysis
gender_sales = df.groupby('Gender')['Amount'].sum().sort_values(ascending=False)
gender_orders = df.groupby('Gender')['User_ID'].count().sort_values(ascending=False)

top_gender_sales = gender_sales.index[0]
top_gender_sales_amount = gender_sales.iloc[0]

top_gender_orders = gender_orders.index[0]
top_gender_order_count = gender_orders.iloc[0]

print("\n2. Gender Insights")
print(
    f"- {top_gender_sales} gender generated the highest total sales "
    f"of ₹{top_gender_sales_amount:,}."
)
print(
    f"- {top_gender_orders} gender had the highest number of transactions "
    f"with {top_gender_order_count:,} records."
)


# 3. Age Group Analysis
age_sales = df.groupby('Age_Group')['Amount'].sum().sort_values(ascending=False)
age_orders = df.groupby('Age_Group')['User_ID'].count().sort_values(ascending=False)

top_age_sales = age_sales.index[0]
top_age_sales_amount = age_sales.iloc[0]

top_age_orders = age_orders.index[0]
top_age_order_count = age_orders.iloc[0]

print("\n3. Age Group Insights")
print(
    f"- The {top_age_sales} age group generated the highest sales "
    f"of ₹{top_age_sales_amount:,}."
)
print(
    f"- The {top_age_orders} age group had the highest number of transactions "
    f"with {top_age_order_count:,} records."
)


# 4. State Analysis
state_sales = df.groupby('State')['Amount'].sum().sort_values(ascending=False)
state_orders = df.groupby('State')['Orders'].sum().sort_values(ascending=False)

top_state_sales = state_sales.index[0]
top_state_sales_amount = state_sales.iloc[0]

top_state_orders = state_orders.index[0]
top_state_order_count = state_orders.iloc[0]

print("\n4. State Insights")
print(
    f"- {top_state_sales} generated the highest sales "
    f"of ₹{top_state_sales_amount:,}."
)
print(
    f"- {top_state_orders} recorded the highest number of orders "
    f"with {top_state_order_count:,} orders."
)


# 5. Marital Status Analysis
marital_sales = (
    df.groupby('Marital_Status')['Amount']
    .sum()
    .sort_values(ascending=False)
)

top_marital = marital_sales.index[0]
top_marital_amount = marital_sales.iloc[0]

print("\n5. Marital Status Insights")
print(
    f"- Marital Status {top_marital} customers generated the highest sales "
    f"of ₹{top_marital_amount:,}."
)


# 6. Occupation Analysis
occupation_sales = (
    df.groupby('Occupation')['Amount']
    .sum()
    .sort_values(ascending=False)
)

top_occupation = occupation_sales.index[0]
top_occupation_amount = occupation_sales.iloc[0]

print("\n6. Occupation Insights")
print(
    f"- Customers working in the {top_occupation} occupation generated "
    f"the highest sales of ₹{top_occupation_amount:,}."
)


# 7. Product Category Analysis
category_sales = (
    df.groupby('Product_Category')['Amount']
    .sum()
    .sort_values(ascending=False)
)

category_orders = (
    df.groupby('Product_Category')['Orders']
    .sum()
    .sort_values(ascending=False)
)

top_category_sales = category_sales.index[0]
top_category_sales_amount = category_sales.iloc[0]

top_category_orders = category_orders.index[0]
top_category_order_count = category_orders.iloc[0]

print("\n7. Product Category Insights")
print(
    f"- {top_category_sales} generated the highest sales "
    f"of ₹{top_category_sales_amount:,}."
)
print(
    f"- {top_category_orders} had the highest number of orders "
    f"with {top_category_order_count:,} orders."
)


# 8. Top Product Analysis
product_orders = (
    df.groupby('Product_ID')['Orders']
    .sum()
    .sort_values(ascending=False)
)

top_product = product_orders.index[0]
top_product_orders = product_orders.iloc[0]

print("\n8. Product Insights")
print(
    f"- Product ID {top_product} was the most ordered product "
    f"with {top_product_orders:,} orders."
)


# ============================================================
# FINAL BUSINESS CONCLUSION
# ============================================================

print("\n" + "=" * 60)
print("                 FINAL CONCLUSION")
print("=" * 60)

print(
    f"""
The Diwali Sales Analysis shows that the highest sales were generated
by {top_gender_sales} customers, with the {top_age_sales} age group
being the strongest customer segment.

Among the states, {top_state_sales} generated the highest total sales.
Customers working in the {top_occupation} occupation contributed the
highest sales among the occupation groups.

In terms of product categories, {top_category_sales} generated the
highest revenue, while {top_category_orders} recorded the highest
number of orders.

Overall, the analysis can help the business focus its marketing
campaigns, offers and product promotions on the highest-performing
customer segments, states, occupations and product categories.
"""
)