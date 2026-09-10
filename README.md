# Used Cars — Exploratory Data Analysis & Interactive Dashboard

## Project Overview

This project performs a complete Exploratory Data Analysis (EDA) on a used cars dataset.

The project focuses on understanding the dataset, identifying and fixing data quality issues, creating useful features, exploring patterns and relationships, and presenting the results through an interactive Streamlit dashboard.

The project workflow is:

**Data Inspection → Data Cleaning → Feature Engineering → Univariate Analysis → Bivariate Analysis → Multivariate Analysis → Interactive Dashboard**

---

## Dataset

The dataset contains used car listings with information about:

* Car name
* Manufacturing year
* Selling price
* Kilometers driven
* Fuel type
* Seller type
* Transmission
* Owner type

### Original Dataset

The original dataset contains:

* **4,345 rows**
* **8 columns**

[View Original Dataset](./car_data.csv)

---

# 1. Data Inspection

The first step was to inspect the structure and quality of the dataset before making any changes.

The inspection included:

* Dataset shape
* Column names and data types
* Statistical summaries
* Missing values
* Duplicate records
* Unique categorical values

The initial inspection revealed several data quality issues that needed to be handled before analysis.

---

# 2. Data Cleaning

The dataset contained intentionally introduced data quality issues, so the cleaning process was an important part of the project.

## 2.1 Duplicate Records

The original dataset contained **112 exact duplicate rows**.

These duplicates were removed because repeated identical records can affect statistical analysis and cause some observations to be counted more than once.

```python
df_clean = df.drop_duplicates().copy()
```

After standardizing categorical values, some additional rows became identical because different misspellings were converted into the same correct value.

Therefore, duplicates were checked again and removed.

---

## 2.2 Inconsistent Fuel Types

The `fuel` column contained several misspelled versions of the same categories.

Examples included:

* `Petrrol`
* `Petorl`
* `Petrl`
* `Deisel`
* `Diesl`

These values were standardized to:

* `Petrol`
* `Diesel`
* `CNG`
* `LPG`
* `Electric`

This was necessary because treating different spellings as separate categories would produce incorrect frequency counts and misleading visualizations.

---

## 2.3 Inconsistent Seller Types

The `seller_type` column also contained spelling inconsistencies.

Examples included:

* `Indvidual`
* `Indivudal`
* `Deelar`
* `Dealerr`

These were standardized to:

* `Individual`
* `Dealer`
* `Trustmark Dealer`

This ensures that the same seller category is represented consistently throughout the analysis.

---

## 2.4 Incorrect Data Type in `km_driven`

The `km_driven` column was initially stored as an `object` instead of a numerical column.

It also contained values such as:

* `50000km`
* `10k`
* `abc`
* `unknown`

The values were cleaned by:

1. Removing the `km` suffix.
2. Converting values ending in `k` to thousands.
3. Converting invalid values to missing values.
4. Converting the final column to a numerical data type.

This was necessary because mileage is a numerical variable and must be numeric for statistical analysis and visualization.

---

## 2.5 Invalid Manufacturing Years

The `year` column contained unrealistic manufacturing years.

Examples included:

* `1800`
* `1890`
* `2050`
* `3000`

These values do not represent realistic manufacturing years for the dataset.

Instead of deleting the complete rows, the invalid year values were replaced with missing values.

This preserves the remaining information in those records while preventing unrealistic values from affecting the analysis.

---

## 2.6 Invalid Selling Prices

The `selling_price` column contained a negative value.

A negative selling price is not meaningful for a car listing, so the invalid value was replaced with a missing value instead of removing the entire row.

This approach preserves the other useful information contained in the record.

---

## 2.7 Missing Values

Missing values were found in both numerical and categorical columns.

For categorical variables, missing values were replaced with:

`Unknown`

This was used instead of removing the rows because missing categorical information does not necessarily make the entire record unusable.

For numerical variables such as `year`, `selling_price`, and `km_driven`, missing values were kept as `NaN` during the EDA process.

---

## 2.8 Final Cleaning Result

After duplicate removal and data cleaning, the dataset contained:

* **4,032 rows**
* **8 original columns**

The final dataset was then used for Feature Engineering and EDA.

[View Cleaned Dataset](./cleaned_car_data.csv)

---

# 3. Feature Engineering

After cleaning the data, two new features were created to make the analysis more meaningful.

## 3.1 Car Age

A new feature called `car_age` was created using the latest manufacturing year available in the dataset:

```python
df_clean['car_age'] = 2020 - df_clean['year']
```

This converts the manufacturing year into an easier-to-interpret measure of vehicle age.

For example:

* A car manufactured in 2017 → age = 3
* A car manufactured in 2012 → age = 8

Missing manufacturing years naturally result in missing `car_age` values.

---

## 3.2 Car Brand

The `brand` feature was extracted from the first word of the car name.

For example:

* `Maruti 800 AC` → `Maruti`
* `Hyundai Verna 1.6 SX` → `Hyundai`
* `Honda Amaze VX i-DTEC` → `Honda`

This makes brand-level analysis easier without having to work with the complete car model name.

---

# 4. Univariate Analysis

Each variable was analyzed individually to understand its distribution and identify unusual values.

The analysis included:

* Selling price distribution
* Kilometers driven
* Manufacturing year
* Car age
* Fuel type
* Seller type
* Transmission
* Owner type
* Top car brands

### Main Findings

* Selling price is highly right-skewed.
* The median mileage is **60,000 km**.
* The dataset contains extremely high mileage values, including a maximum of **50,000,000 km**.
* Most cars were manufactured between 2011 and 2016.
* The median car age is **6 years**.
* Diesel and Petrol are the dominant fuel types.
* Individual sellers represent the majority of listings.
* Manual transmission cars are much more common than automatic cars.
* First Owner cars are the most common owner category.
* Maruti is the most represented brand.

---

# 5. Bivariate Analysis

The relationship between pairs of variables was explored using different visualizations.

The analysis included:

* Selling Price vs. Car Age
* Selling Price vs. Kilometers Driven
* Selling Price by Fuel Type
* Selling Price by Transmission

These visualizations help identify how vehicle characteristics are associated with selling price.

---

# 6. Multivariate Analysis

Multiple numerical variables were analyzed together using a correlation matrix.

The numerical variables included:

* `year`
* `selling_price`
* `km_driven`
* `car_age`

A second visualization examined the relationship between selling price and car age while distinguishing transmission types.

This helps provide a broader view of the interactions between vehicle characteristics.

---

# 7. Important Data Quality Observation

One of the most important findings was the presence of extreme values in `km_driven`.

The statistics were:

* **Median:** 60,000 km
* **75th percentile:** 90,000 km
* **Maximum:** 50,000,000 km

The maximum value is extremely large compared with the rest of the dataset and was therefore identified as a potential outlier.

The value was not automatically removed because an outlier should not be deleted without understanding whether it represents a genuine observation or an error.

This keeps the analysis transparent and documents the issue rather than silently modifying the data.

---

# 8. Final Insights

After completing the EDA, several important patterns were identified:

* The dataset is dominated by Petrol and Diesel vehicles.
* Individual sellers account for most listings.
* Manual transmission vehicles are much more common than automatic vehicles.
* First Owner vehicles are the most common owner category.
* Maruti is the most represented brand.
* Most vehicles are relatively recent, with a median age of 6 years.
* Selling prices are strongly right-skewed.
* The dataset contains extreme mileage values that require attention in any future modeling task.

---

# 9. Interactive Dashboard

An interactive dashboard was developed using **Streamlit**.

The dashboard allows users to explore the cleaned dataset interactively.

### Dashboard Features

* Total number of cars
* Average selling price
* Average kilometers driven
* Top car brand
* Selling price distribution
* Top 10 car brands
* Fuel type distribution
* Transmission distribution
* Owner distribution
* Selling price vs. car age
* Interactive filters
* Filtered data table

### Live Dashboard

🚗 **[Open the Live Dashboard](https://used-cars-eda-ormwx5of7umx8k49yjgdfs.streamlit.app/)**

---

# 10. Project Files

| File                   | Description                              |
| ---------------------- | ---------------------------------------- |
| `Used_Cars_EDA.ipynb`  | Complete EDA notebook                    |
| `car_data.csv`         | Original dataset before cleaning         |
| `cleaned_car_data.csv` | Cleaned dataset with engineered features |
| `app.py`               | Streamlit dashboard                      |
| `requirements.txt`     | Required Python libraries                |
| `README.md`            | Project documentation                    |

---

# 11. Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

---

# 12. Project Links

### GitHub Repository

🔗 **[View the Full Project on GitHub](https://github.com/hager-arafat-el-dabaa/Used-Cars-EDA)**

### Original Dataset

📄 **[View Original Dataset](./car_data.csv)**

### Cleaned Dataset

📄 **[View Cleaned Dataset](./cleaned_car_data.csv)**

### Live Streamlit Dashboard

🚗 **[Open Live Dashboard](https://used-cars-eda-ormwx5of7umx8k49yjgdfs.streamlit.app/)**

---

# Author

**Hager Arafat El Dabaa**

AI & Data Science Student
