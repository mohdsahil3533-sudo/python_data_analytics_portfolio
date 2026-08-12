# 🪔 Diwali Sales Data Analysis Using Python

This project focuses on analyzing **Diwali sales data** using Python to understand customer behavior, sales performance, product categories, and purchasing trends.

The analysis uses **Pandas, NumPy, Seaborn, and Matplotlib** to clean the dataset, perform exploratory data analysis (EDA), create visualizations, and generate meaningful business insights.

## 🎯 Project Objective

The main objective of this project is to analyze Diwali sales data and identify:

* Customer purchasing patterns
* Highest-performing customer segments
* Sales performance across states
* Gender-wise sales performance
* Age-group-wise sales
* Marital-status-wise sales
* Occupation-wise sales
* Product-category performance
* Top-selling products
* Overall sales and order performance

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📊 Seaborn
* 📈 Matplotlib
* 📓 Jupyter Notebook / Python

## 📂 Dataset

The project uses a **Diwali Sales Dataset** containing customer, order, demographic, geographical, and product-related information.

Important columns include:

```text
User_ID
Customer_Name
Gender
Age
Age_Group
State
Marital_Status
Occupation
Product_Category
Product_ID
Orders
Amount
```

## 🧹 Data Cleaning

The following data-cleaning steps were performed:

* Checked dataset shape
* Inspected the first few records
* Checked data types and dataset information
* Removed unnecessary columns
* Checked duplicate records
* Removed duplicate records
* Checked missing values
* Removed rows containing missing values
* Renamed selected columns
* Converted `Amount` into integer format
* Checked unique values
* Generated statistical summaries

Example:

```python
df = df.drop(['Status', 'unnamed1'], axis=1)

df = df.drop_duplicates()

df = df.dropna()

df['Amount'] = df['Amount'].astype(int)
```

## 📊 Exploratory Data Analysis

### Gender Analysis

Analyzed:

* Number of transactions by gender
* Total sales amount by gender

### Age Group Analysis

Analyzed:

* Number of transactions by age group and gender
* Total sales by age group

### State Analysis

Identified the **top 5 states based on total orders**.

### Marital Status Analysis

Compared:

* Number of transactions
* Total sales amount

between different marital-status groups.

### Occupation Analysis

Analyzed:

* Customer count by occupation
* Total sales by occupation

### Product Category Analysis

Analyzed:

* Number of transactions by product category
* Total sales by product category

### Top Products

Identified the **top 10 products based on total orders**.

## 📈 Visualizations

The project includes visualizations such as:

* Gender-wise customer count
* Gender-wise sales
* Age group vs gender
* Age group vs sales
* Top 5 states by orders
* Marital status vs customer count
* Marital status vs sales
* Occupation vs customer count
* Occupation vs sales
* Product category vs customer count
* Product category vs sales
* Top 10 products by orders

## 💡 Key Business Insights

The project automatically identifies the highest-performing:

* Gender
* Age group
* State
* Marital status
* Occupation
* Product category
* Product

It also calculates:

```text
Total Sales Amount
Total Orders
Total Unique Customers
```

These insights can help businesses understand their customers and make better decisions regarding **marketing campaigns, customer targeting, product promotions, and sales strategies**.

## 🔄 Analysis Workflow

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Duplicate & Null Handling
     ↓
Data Type Conversion
     ↓
Exploratory Data Analysis
     ↓
Data Visualization
     ↓
Business Insights
     ↓
Final Conclusion
```

## 📁 Project Structure

```text
Diwali-Sales-Analysis/
│
├── Diwali Sales Data.csv
├── main.py
└── README.md
```

## ▶️ How to Run

### Install required libraries

```bash
pip install numpy pandas seaborn matplotlib
```

### Run the Python file

```bash
python main.py
```

Make sure `Diwali Sales Data.csv` is present in the project directory.

## 🎓 Skills Practiced

Through this project, I practiced:

* Python
* NumPy
* Pandas
* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* GroupBy and Aggregation
* Sorting and Filtering
* Statistical Analysis
* Data Visualization
* Business Insight Generation

## 🚀 Future Improvements

* Add more advanced visualizations
* Create an interactive dashboard
* Perform deeper customer segmentation
* Add SQL-based analysis
* Add more statistical analysis
* Build predictive models for sales/customer behavior

## 👨‍💻 Author

**Mohd Sahil**

This project is part of my learning journey in **Python and Data Analytics**.

> **Learn → Practice → Analyze → Build → Improve** 🐍📊

