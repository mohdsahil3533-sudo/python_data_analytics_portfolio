import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import Data
df = pd.read_csv('Customer Churn Data.csv')
print(df.head())
df.info()

# Data Cleaning and Preprocessing

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print(df.duplicated().sum())

# Check for data types
print(df.dtypes)

# Replacing blanks with 0 as tenure is 0 and no total charges are recorded 
df['TotalCharges'] = df['TotalCharges'].replace(' ', 0)

# Convert data types as total charges is now numeric
df['TotalCharges'] = df['TotalCharges'].astype(float)
df.info()

# Convert 0 and 1 values of senior citizen to yes/no to make it easier to understand
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
print(df.head(30))
print(df.describe()) 

# Data Visualization

# Check the distribution of churned customers with labels of churned customers
ax = sns.countplot(x='Churn', data=df)
ax.bar_label(ax.containers[0])
plt.xlabel('Churn')
plt.ylabel('Count')
plt.title('Distribution of Churned Customers')
plt.show()

# Check the Percentage of churned customers
plt.figure(figsize = (4,4))
gb = df.groupby("Churn").agg({'Churn':"count"})
plt.pie(gb['Churn'], labels = gb.index, autopct = "%1.2f%%")
plt.title("Percentage of Churned Customeres", fontsize = 10)
plt.show()

# Check the distribution of churned customers based on gender 
plt.figure(figsize = (5,5))
sns.countplot(x = "gender", data = df, hue = "Churn")
plt.title("Churn by Gender")
plt.show()

# Check the distribution of churned customers based with labels based seniority 
plt.figure(figsize = (6,6))
ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()

# Visualize the data of Senior Citizen and Churn relationship in the percentage. 
total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# Plot
fig, ax = plt.subplots(figsize=(6, 6))  # Adjust figsize for better visualization

# Plot the bars
total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])  # Customize colors if desired

# Add percentage labels on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor = (0.9,0.9))  # Customize legend location
plt.show()

# Check how many people who have used our services for a long time have stayed and people who have used our sevices 1 or 2 months have churned
plt.figure(figsize = (9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()

# Check how many people who have month to month contract and they are likely to churn then from those who have 1 or 2 years or contract
plt.figure(figsize = (6,6))
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()

# Columns for subplot
columns = [
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StreamingMovies'
]

# Number of columns in subplot grid
n_cols = 3

# Calculate required number of rows
n_rows = (len(columns) + n_cols - 1) // n_cols

# Create subplots
fig, axes = plt.subplots(
    n_rows,
    n_cols,
    figsize=(18, n_rows * 5)
)

# Flatten axes array
axes = axes.flatten()

# Create count plots
for i, col in enumerate(columns):

    sns.countplot(
        data=df,
        x=col,
        hue='Churn',
        ax=axes[i]
    )

    axes[i].set_title(f'Count Plot of {col}', fontsize=12)
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

    # Rotate x-axis labels if required
    axes[i].tick_params(axis='x', rotation=30)

# Remove unused subplots
for j in range(len(columns), len(axes)):
    fig.delaxes(axes[j])

# Automatically adjust spacing
plt.tight_layout(pad=2)

plt.show()

# Check the customer have churned by payment method
plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()