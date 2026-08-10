# 🏠 Gurgaon Real Estate Market Analysis

A Python-based data analysis project focused on exploring and understanding the **Gurgaon real estate market** using property-level data.

The project uses **Pandas** for data cleaning and analysis and **Seaborn & Matplotlib** for data visualization. It answers important business questions related to property prices, localities, BHK configurations, property types, builders, RERA approval, and price per square foot.

## 📌 Project Objective

The main objective of this project is to analyze Gurgaon real estate data and identify useful insights such as:

* Which is the costliest flat?
* Which locality has the highest average property price?
* Which locality has the highest rate per square foot?
* How do ready-to-move and under-construction properties differ in pricing?
* Does RERA approval affect property prices?
* How does property area impact price?
* Which BHK configuration is the most expensive?
* Which property type has the highest average price?
* Which builders have higher average property prices?
* Does property size affect the price per square foot?

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 📊 Seaborn
* 📈 Matplotlib

## 🔄 Data Analysis Process

```text
Raw Dataset
     ↓
Load Dataset
     ↓
Standardize Column Names
     ↓
Convert Numeric Columns
     ↓
Clean Categorical Data
     ↓
Handle RERA Approval
     ↓
Remove Duplicate Records
     ↓
Exploratory Data Analysis
     ↓
Business Questions
     ↓
Data Visualization
     ↓
Key Insights
```

## 🧹 Data Cleaning

The following data-cleaning operations were performed:

* Standardized column names
* Removed leading/trailing spaces
* Converted column names to lowercase
* Replaced spaces with underscores
* Converted price values into numeric format
* Converted rate per square foot into numeric format
* Cleaned categorical columns
* Standardized property status
* Standardized flat type
* Converted RERA approval into Boolean values
* Removed duplicate records

Example:

```python
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.drop_duplicates(inplace=True)
```

## 📊 Analysis Performed

### 1. Costliest Property

Identifies the most expensive property in the dataset and displays:

* Flat type
* Locality
* Price
* Area
* Rate per square foot
* Builder
* RERA approval status

### 2. Highest Average Price by Locality

Calculates the average property price for each locality and identifies the locality with the highest average price.

### 3. Highest Rate per Square Foot

Compares the average rate per square foot across different localities.

### 4. Ready-to-Move vs Under-Construction

Compares the median property price between:

* Ready to Move
* Under Construction

### 5. RERA Approval & Pricing

Compares the median price of RERA-approved properties to understand whether approval may be associated with higher pricing.

### 6. Area vs Price

A scatter plot is used to visualize the relationship between property area and price.

### 7. BHK Configuration Analysis

Identifies which BHK configuration has the highest average property price.

### 8. Property Type Analysis

Compares average prices across different property types.

### 9. Builder Price Analysis

Identifies builders with the highest average property prices.

### 10. Area vs Rate per Square Foot

A scatter plot is used to analyze whether larger homes have higher or lower prices per square foot.

## 📈 Visualizations

The project currently includes visual analysis such as:

### Area vs Price

```python
sns.scatterplot(x="area", y="price", data=df)
plt.show()
```

### Area vs Rate per Square Foot

```python
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()
```

These visualizations help identify relationships and trends within the real estate market.

## 📂 Project Structure

```text
Gurgaon-Real-Estate-Market-Analysis/
│
├── Gurgaon_Real_Estate_Data.csv
├── analysis_main.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Gurgaon-Real-Estate-Market-Analysis
```

### 3. Install required libraries

```bash
pip install pandas seaborn matplotlib
```

### 4. Run the project

```bash
python main.py
```

---

## 🎯 Key Skills Demonstrated

This project helped me practice:

* Python programming
* Pandas
* Data Cleaning
* Data Transformation
* GroupBy & Aggregation
* Sorting and Filtering
* Statistical Analysis
* Exploratory Data Analysis
* Data Visualization
* Business Question Analysis
* Working with Real-World Datasets
* 
## 🚀 Future Improvements

Planned improvements for this project include:

* Adding more visualizations
* Creating a complete EDA notebook
* Adding correlation analysis
* Creating an interactive dashboard
* Adding SQL-based analysis
* Building a property price prediction model
* Adding more advanced statistical analysis


## 👨‍💻 Author

**Mohd Sahil**

This project is part of my learning journey in **Python and Data Analytics**.

> **Learn → Practice → Analyze → Build → Improve** 🚀

