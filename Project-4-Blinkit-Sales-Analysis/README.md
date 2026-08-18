# 🛒 Blinkit Sales Analysis

## 📌 Project Overview

This project performs an exploratory **Blinkit Sales Analysis** using Python, Pandas, NumPy, Seaborn, and Matplotlib.

The objective is to analyze sales performance across different **item categories, fat content, outlet characteristics, outlet locations, and establishment years** and present the findings through clear and business-oriented visualizations.

The project also includes basic data cleaning and preprocessing, including handling missing values and standardizing inconsistent categorical values.

## 🎯 Business Objectives

The analysis focuses on the following business requirements:

* Analyze overall sales performance.
* Calculate key sales KPIs.
* Compare sales by item fat content.
* Identify sales contribution by item type.
* Analyze sales across different outlet tiers.
* Compare sales trends by outlet establishment year.
* Analyze sales contribution by outlet size.
* Compare sales across outlet location types.
* Identify patterns that can support inventory, outlet, and product-level decisions.

## 🛠️ Technologies Used

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Data analysis and visualization |
| Pandas     | Data manipulation and analysis  |
| NumPy      | Numerical operations            |
| Matplotlib | Data visualization              |
| Seaborn    | Statistical visualization       |
| CSV        | Raw dataset format              |

## 📂 Project Structure

```text
Project-11-Blinkit-Sales-Analysis/
│
├── blinkit_data.csv
├── analysis_main.py
└── README.md
```

## 📊 Dataset

The analysis uses a Blinkit sales dataset containing information related to:

* Item Identifier
* Item Fat Content
* Item Type
* Item Weight
* Outlet Identifier
* Outlet Establishment Year
* Outlet Size
* Outlet Location Type
* Outlet Type
* Item Visibility
* Sales
* Rating

## 🔍 Data Cleaning & Preprocessing

### 1. Missing Value Analysis

Missing values were checked using:

```python
df.isnull().sum()
```

The `Item Weight` column contained missing values.

Instead of removing the affected records, missing values were handled using the **median**:

```python
df['Item Weight'] = df['Item Weight'].fillna(
    df['Item Weight'].median()
)
```

This preserves the available records while providing a robust estimate for the missing numerical values.

### 2. Duplicate Value Check

Duplicate records were checked using:

```python
df.duplicated().sum()
```

### 3. Standardizing Categorical Values

The `Item Fat Content` column contained inconsistent labels such as:

* `low fat`
* `LF`
* `reg`

These were standardized as:

* `Low Fat`
* `Regular`

using:

```python
df["Item Fat Content"] = df["Item Fat Content"].replace({
    "low fat": "Low Fat",
    "LF": "Low Fat",
    "reg": "Regular"
})
```

This ensures consistent grouping and more accurate analysis.

# 📈 Key Performance Indicators (KPIs)

The project calculates the following KPIs:

### 💰 Total Sales

Total revenue generated across all records.

```python
total_sales = df["Sales"].sum()
```

### 📊 Average Sales

Average sales value per record.

```python
average_sales = df["Sales"].mean()
```

### 📦 Number of Items Sold

Number of sales records/items represented in the dataset.

```python
num_of_items_sold = df["Sales"].count()
```

### ⭐ Average Rating

Average customer/product rating.

```python
ave_rating = df["Rating"].mean()
```

---

# 📊 Data Visualizations

The project includes multiple business-focused visualizations.

## 1. Total Sales by Item Fat Content

A bar chart compares total sales between different fat-content categories.

**Purpose:**
To understand how different item fat-content categories contribute to overall sales.

---

## 2. Total Sales by Item Type

A bar chart compares sales across different product categories.

**Purpose:**
To identify item types with relatively higher and lower sales contributions.

---

## 3. Outlet Tier by Item Fat Content

A grouped bar chart compares sales by:

* Outlet Location Type
* Item Fat Content

**Purpose:**
To understand how product fat-content categories perform across different outlet tiers.

---

## 4. Total Sales by Outlet Establishment Year

A line chart shows total sales across outlet establishment years.

**Purpose:**
To examine sales patterns and changes associated with outlet establishment periods.

---

## 5. Total Sales Distribution by Outlet Size

A pie chart displays the percentage contribution of different outlet sizes to total sales.

**Purpose:**
To understand the sales contribution of different outlet-size categories.

---

## 6. Total Sales by Outlet Location Type

A bar chart compares total sales across different outlet location tiers.

**Purpose:**
To evaluate sales performance across different geographical outlet categories.

---

# 💡 Business Value

This analysis can help businesses understand:

* Which product categories generate higher sales.
* How item fat content contributes to sales.
* How outlet tiers perform against each other.
* How outlet size contributes to overall revenue.
* Sales patterns across outlet establishment years.
* Which outlet locations generate stronger sales.
* Product and outlet-level patterns that can support business planning.

---

# 🧹 Data Quality Considerations

The project demonstrates several important data-analysis practices:

* Dataset structure inspection
* Data type validation
* Missing value identification
* Missing value treatment
* Duplicate record detection
* Categorical value standardization
* Descriptive statistical analysis
* KPI calculation
* Business-oriented visualization

---

# 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Project-11-Blinkit-Sales-Analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the analysis

```bash
python analysis_main.py
```

---

# 📌 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python for Data Analytics
* Pandas
* NumPy
* Data Cleaning
* Missing Value Handling
* Duplicate Detection
* Data Transformation
* GroupBy Operations
* KPI Development
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Analysis
* GitHub Project Documentation
  
## 👨‍💻 Author

**Mohd Sahil**

Data Analytics | Python | Pandas | Data Visualization | Exploratory Data Analysis

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

