📊 Customer Churn Analysis

📌 Project Overview

This project focuses on Customer Churn Analysis using Python. The objective is to explore customer behavior and identify patterns associated with customer churn across demographics, tenure, contracts, subscribed services, and payment methods.

The project follows an Exploratory Data Analysis (EDA) approach, starting from data inspection and cleaning and progressing to visualization and business-oriented insights.

🎯 Objectives

Understand the overall distribution of customer churn.
Analyze churn across different customer demographics.
Compare churn behavior between senior and non-senior customers.
Investigate the relationship between customer tenure and churn.
Analyze churn across different contract types.
Examine how subscribed services relate to churn.
Analyze churn patterns across different payment methods.
Identify potential areas for customer retention strategies.

🛠️ Technologies & Libraries

Python
Pandas – Data manipulation and analysis
NumPy – Numerical operations
Seaborn – Statistical data visualization
Matplotlib – Data visualization

📂 Project Structure

Customer-Churn-Analysis/
│
├── Customer Churn Data.csv
├── analysis_main.py
└── README.md

🔄 Data Analysis Workflow

Raw Customer Data
        ↓
Data Inspection
        ↓
Data Quality Checks
        ↓
Data Cleaning
        ↓
Data Type Conversion
        ↓
Feature Transformation
        ↓
Exploratory Data Analysis
        ↓
Visualization
        ↓
Churn Pattern Analysis
        ↓
Business Insights

🧹 Data Cleaning & Preprocessing

The project performs the following preprocessing steps:

Inspects the dataset using head() and info().
Checks for missing values.
Checks for duplicate records.
Reviews column data types.
Replaces blank values in TotalCharges with 0.
Converts TotalCharges into a numeric data type.
Converts SeniorCitizen values from 0/1 into No/Yes for better readability.

These steps prepare the dataset for further exploratory analysis.

📊 Exploratory Data Analysis

The project analyzes customer churn through the following dimensions:

1. Overall Churn Distribution

The project uses a count plot and pie chart to understand the distribution of customers who churned versus remained.

2. Churn by Gender

Customer churn is compared across gender categories to identify differences in churn behavior.

3. Senior Citizen Analysis

The analysis compares senior and non-senior customers and calculates the percentage distribution of churn within each group.

4. Tenure Analysis

Customer tenure is analyzed using a histogram to investigate how churn varies according to the length of the customer relationship.

5. Contract Analysis

Different contract types are compared against churn to identify potential differences in customer retention.

6. Service Analysis

The following services are analyzed:

PhoneService
MultipleLines
InternetService
OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies

A subplot grid is used to compare churn across these services.

7. Payment Method Analysis

Customer churn is analyzed across different payment methods to identify potential differences between payment-method segments.

The above analyses are implemented in the supplied Python script.

💡 Key Business Questions

This project attempts to answer questions such as:

What proportion of customers are churning?
Does churn differ between genders?
Do senior citizens show different churn patterns?
Does customer tenure influence churn?
Which contract types show different churn behavior?
Are particular services associated with different churn patterns?
Does payment method appear to be related to churn?
📈 Business Value

Customer churn directly affects customer retention and business revenue. This analysis can help businesses:

Identify customer segments requiring additional attention.
Understand potential churn-related patterns.
Improve customer retention strategies.
Develop targeted customer engagement programs.
Identify areas requiring deeper analysis.
🚀 Future Improvements

The current project is primarily an Exploratory Data Analysis project. Future improvements could include:

Calculate detailed churn rates for each customer segment.
Analyze MonthlyCharges and TotalCharges.
Perform deeper statistical analysis.
Create customer churn-risk segments.
Build an interactive dashboard using Power BI or Tableau.
Develop a machine-learning model to predict customer churn.
Evaluate model performance using appropriate classification metrics.
🏁 Conclusion

This project demonstrates a practical Python-based Customer Churn EDA workflow, covering data cleaning, preprocessing, exploratory analysis, and visualization.

It provides a foundation for understanding customer churn and identifying potential retention opportunities. The project can be further enhanced by adding quantitative churn-rate analysis, dashboards, and predictive modeling.

👨‍💻 Skills Demonstrated

Python | Pandas | NumPy | Seaborn | Matplotlib | Data Cleaning | EDA | Data Visualization | Business Analysis | Customer Churn Analysis
