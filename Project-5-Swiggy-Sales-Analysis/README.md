# Swiggy Sales Analysis

## 📊 Project Overview

This project performs an end-to-end **Swiggy Sales Analysis** using Python, Pandas, NumPy, Matplotlib, Seaborn, and Plotly.

The objective is to analyze sales performance, customer ratings, food categories, geographical performance, and time-based sales trends to generate meaningful business insights.

---

## 🎯 Objectives

* Analyze overall Swiggy sales performance
* Calculate important business KPIs
* Identify monthly and weekly sales trends
* Compare Veg vs Non-Veg sales contribution
* Analyze state-wise sales performance
* Evaluate quarterly business performance
* Identify the Top 5 cities by sales
* Understand customer rating patterns
* Perform basic data cleaning and preprocessing

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations and categorization
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical and trend visualization
* **Plotly** – Interactive visualization
* **Excel** – Source dataset

---

## 📂 Project Structure

```text
Project-12-Swiggy-Sales-Analysis/
│
├── analysis_main.py
├── swiggy_data.xlsx
└── README.md
```

---

## 🔍 Data Preparation & Cleaning

The following data-quality checks and preprocessing steps were performed:

* Checked sample records using `head()` and `tail()`
* Checked dataset dimensions using `shape`
* Reviewed column names using `columns`
* Checked data types using `dtypes`
* Identified missing values
* Identified duplicate records
* Removed duplicate rows using `drop_duplicates()`
* Converted `Order Date` into datetime format
* Created additional time-based features such as:

  * Month
  * Day Name
  * Quarter
* Created a **Food Category** classification using dish names

---

## 📌 Key Performance Indicators (KPIs)

The analysis calculates the following KPIs:

| KPI                     | Description                             |
| ----------------------- | --------------------------------------- |
| **Total Sales**         | Total revenue generated from all orders |
| **Average Rating**      | Average customer rating                 |
| **Average Order Value** | Average revenue generated per order     |
| **Rating Count**        | Total number of ratings                 |
| **Total Orders**        | Total number of orders in the dataset   |

---

## 📈 Data Visualizations

### 1. Monthly Sales Trend

A line chart is used to analyze how sales change across different months.

**Purpose:**

* Identify sales growth or decline
* Detect seasonal patterns
* Understand monthly performance

---

### 2. Sales by Day of Week

A bar chart analyzes total sales across:

* Monday
* Tuesday
* Wednesday
* Thursday
* Friday
* Saturday
* Sunday

**Purpose:**

* Identify high-performing days
* Understand weekly ordering patterns
* Support operational and marketing decisions

---

### 3. Veg vs Non-Veg Revenue Contribution

A donut chart compares revenue contribution from:

* **Veg**
* **Non-Veg**

Food categories are identified using dish-name keywords such as chicken, egg, fish, mutton, prawn, biryani, kebab, etc.

**Purpose:**

* Understand customer food preferences
* Compare revenue contribution by food category

> **Note:** Keyword-based classification may classify some dishes imperfectly, such as vegetarian biryani. For production-level analysis, a dedicated food-category field would provide more accurate classification.

---

### 4. Total Sales by State

A horizontal bar chart compares total sales across different states.

**Purpose:**

* Identify high-performing states
* Compare geographical sales performance
* Identify potential expansion opportunities

---

### 5. Quarterly Performance Summary

Quarter-wise performance is calculated using:

* Total Sales
* Total Orders
* Average Order Value
* Average Rating
* Rating Count

This provides a consolidated view of business performance across quarters.

---

### 6. Top 5 Cities by Sales

The analysis identifies the **Top 5 cities based on total sales**.

**Purpose:**

* Identify major revenue-generating cities
* Understand high-value markets
* Support location-specific business strategies

---

## 💡 Business Insights

This analysis can help answer important business questions such as:

* Which months generate the highest sales?
* Which days of the week perform best?
* Which states contribute the most revenue?
* Which cities are the strongest markets?
* What is the revenue contribution of Veg vs Non-Veg food?
* Which quarter performs best?
* What is the average value of each order?
* How strong is customer engagement through ratings?

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Project-12-Swiggy-Sales-Analysis
```

### 3. Install required libraries

```bash
python -m pip install pandas numpy matplotlib seaborn plotly openpyxl
```

### 4. Run the analysis

```bash
python analysis_main.py
```

---

## 📊 Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Aggregation
* KPI Development
* Time-Series Analysis
* Feature Engineering
* GroupBy Analysis
* Duplicate Handling
* Missing Value Analysis
* Business Data Analysis
* Data Visualization
* Python Programming
* Business Insight Generation

---

## 👨‍💻 Author

**Mohd Sahil**

Aspiring **Data Analyst** | Python | Pandas | SQL | Data Visualization | Business Analytics

---

## ⭐ Project Highlights

> **From raw Swiggy order data to actionable business insights using Python-based data analytics.**

If you find this project useful, feel free to ⭐ the repository.
