# Consumer Price Trend Analytics

## Data Visualization Techniques Lab

This project analyzes the **All India Consumer Price Index (CPI)** dataset using Python-based data processing, data mining methodologies, preprocessing techniques, and exploratory data visualization.

### Dataset

**Dataset:** All India Consumer Price Index (2013–2023)

The dataset contains CPI information across different sectors and consumer categories, including food and beverages, clothing, housing, fuel and light, health, transport and communication, education, and the overall General Index.

---

## Project Objective

The objective of this project is to analyze Consumer Price Index data, identify meaningful patterns and trends, preprocess the dataset, apply data mining methodologies, and represent the results through suitable visualizations.

The project demonstrates how data visualization can transform CPI data into understandable insights about:

- Consumer price trends over time
- Sector-wise CPI differences
- Category-wise price variations
- Relationships between CPI categories
- Distribution of CPI values
- Correlations among consumer price categories
- Outliers and unusual CPI observations

---

# Experiments

## Experiment 1 — CRISP-DM, SEMMA, and KDD Methodologies

### Aim

To compare the CRISP-DM, SEMMA, and KDD methodologies for Consumer Price Index analysis and identify a suitable approach for building a machine learning model for CPI prediction.

### Work Performed

The three data mining methodologies were applied to the CPI dataset.

**CRISP-DM**
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

**SEMMA**
1. Sample
2. Explore
3. Modify
4. Model
5. Assess

**KDD**
1. Selection
2. Preprocessing
3. Transformation
4. Data Mining
5. Interpretation/Evaluation

A Random Forest Regressor was trained and evaluated using MAE, RMSE, and R² Score.

### Outcome

The experiment demonstrates how different data mining methodologies can be applied to the same CPI analysis workflow. CRISP-DM provides the most complete end-to-end project lifecycle, while SEMMA and KDD provide structured approaches for analytics, preprocessing, modeling, and evaluation.

---

## Experiment 2 — Data Conversion and Database Integration

### Aim

To perform data conversion and database integration operations on the Consumer Price Index dataset.

### Work Performed

The CPI dataset was processed through multiple data formats and storage methods:

- CSV
- Excel
- JSON
- SQLite

The dataset was converted between formats, stored in an SQLite database, retrieved using SQL, and analyzed using Python.

A sector-wise visualization was also created to understand the distribution of CPI records.

### Visualization

**Sector-wise Consumer Price Index Record Count**

This visualization shows the number of CPI records available for different sectors such as Rural, Urban, and Rural+Urban.

---

## Experiment 3 — Data Preprocessing

### Aim

To preprocess the Consumer Price Index dataset by handling missing values, duplicate records, outliers, data types, and feature scaling.

### Work Performed

The following preprocessing operations were performed:

- Identification of missing values
- Missing-value replacement
- Conversion of CPI attributes to numerical format
- Duplicate-record detection and removal
- Outlier detection using the Interquartile Range (IQR) method
- Box-plot based outlier visualization
- Column-name cleaning
- Min-Max normalization
- Saving the cleaned dataset

### Outcome

The preprocessing step prepares the CPI dataset for reliable analysis and modeling by improving data consistency and handling common data-quality issues.

---

## Experiment 4 — CPI Trend and Sector Analysis

### Aim

To analyze and visualize Consumer Price Index differences and trends across sectors.

### Work Performed

The experiment calculates average General CPI values for different sectors and visualizes them using bar charts.

A time-based analysis is also performed by creating a date attribute from the year and month fields and plotting the General CPI trend.

### Visualizations

- Average CPI by sector
- General CPI trend over time

### Outcome

The visualizations provide an intuitive understanding of sector-wise CPI differences and changes in consumer prices over time.

---

## Experiment 5 — Exploratory Data Visualization

### Aim

To explore the Consumer Price Index dataset using different graphical visualization techniques.

### Visualizations Performed

1. **Scatter Plot**  
   Food and Beverages CPI vs General CPI

2. **Box Plot**  
   General CPI outlier detection

3. **Correlation Heatmap**  
   Correlation between major CPI categories

4. **Count Plot**  
   Number of CPI records by sector

5. **Line Plot**  
   General CPI trend over time

6. **Pie Chart**  
   Sector-wise distribution of CPI records

7. **Bar Chart**  
   Top 10 consumer categories based on average CPI

8. **Histogram**  
   Distribution of General CPI values

9. **Pair Plot**  
   Relationships among Food and Beverages, Fuel and Light, Health, and General CPI

### Outcome

The exploratory visualizations reveal trends, relationships, distributions, sector differences, category variations, and correlations within the CPI dataset.

---

# How This Project Aligns with Data Visualization

The project directly applies the principles of **Data Visualization Techniques** by converting raw CPI data into graphical representations that make patterns and relationships easier to understand.

### 1. Comparison

Bar charts are used to compare:

- Average CPI across sectors
- Average CPI across consumer categories
- Number of records across sectors

### 2. Trends

Line charts are used to visualize how the General CPI changes over time.

### 3. Distribution

Histograms and box plots are used to understand the distribution and spread of CPI values and identify potential outliers.

### 4. Relationships

Scatter plots are used to study relationships such as Food and Beverages CPI versus General CPI.

### 5. Correlation

Correlation heatmaps show how different consumer-price categories are related to each other.

### 6. Composition

Pie charts represent the proportion of CPI records across different sectors.

### 7. Multivariate Analysis

Pair plots allow multiple CPI variables to be compared simultaneously and help identify relationships between different consumer categories.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQLite
- Jupyter Notebook
- GitHub

---

# Project Structure

```text
Consumer-Price-Trend-Analytics/
│
├── All India Consumer Price Index.csv
│
├── DVT_Experiment1.ipynb
├── DVT_Experiment2.ipynb
├── DVT_Experiment3.ipynb
├── DVT_Experiment4.ipynb
├── DVT_Experiment5.ipynb

```

---

# Conclusion

The **Consumer Price Trend Analytics** project demonstrates the complete data-analysis workflow from data understanding and preprocessing to data mining and visualization.

The project uses the Consumer Price Index dataset to demonstrate how different visualization techniques can communicate complex information effectively. Through bar charts, line charts, scatter plots, heatmaps, histograms, box plots, pie charts, and pairwise visualizations, the project provides meaningful insights into consumer price patterns, sector-wise differences, category relationships, and temporal trends.

The combination of data preprocessing, data mining methodologies, and visualization makes the project suitable for demonstrating the practical application of **Data Visualization Techniques** to a real-world economic dataset.

---

## Dataset Source

Kaggle — All India Consumer Price Index (2013–2023)

https://www.kaggle.com/datasets/vaibhavkh/consumer-price-index-cpi-2013-2023

## Repository

https://github.com/code2de/Data-Visualization-Techniques-Project
