# ============================================================
# EXPERIMENT 3
# Consumer Price Trend Analytics
# Data Preprocessing
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler

file_path = "All India Consumer Price Index.csv"

df = pd.read_csv(file_path)

print("Original Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values in Dataset:")
print(df.isnull())

print("\nTotal Missing Values in Each Column:")
print(df.isnull().sum())

# All CPI columns except Sector and Month
numeric_columns = df.select_dtypes(
    include=np.number
).columns.tolist()

# Housing is stored as object because it contains "NA"
# Convert it into numeric format
cpi_columns = [
    "Cereals and products",
    "Meat and fish",
    "Egg",
    "Milk and products",
    "Oils and fats",
    "Fruits",
    "Vegetables",
    "Pulses and products",
    "Sugar and Confectionery",
    "Spices",
    "Non-alcoholic beverages",
    "Prepared meals, snacks, sweets etc.",
    "Food and beverages",
    "Pan, tobacco and intoxicants",
    "Clothing",
    "Footwear",
    "Clothing and footwear",
    "Housing",
    "Fuel and light",
    "Household goods and services",
    "Health",
    "Transport and communication",
    "Recreation and amusement",
    "Education",
    "Personal care and effects",
    "Miscellaneous",
    "General index"
]

for col in cpi_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


# Update numeric columns
numeric_columns = df.select_dtypes(
    include=np.number
).columns.tolist()


print("\nNumeric Columns:")
print(numeric_columns)


# Numerical columns:
# Replace missing values with column mean

for col in numeric_columns:

    df[col] = df[col].fillna(
        df[col].mean()
    )


# Categorical columns:
# Replace missing values with mode

categorical_columns = df.select_dtypes(
    include="object"
).columns.tolist()

for col in categorical_columns:

    if df[col].isnull().sum() > 0:

        df[col] = df[col].fillna(
            df[col].mode()[0]
        )


print("\nMissing Values After Replacement:")
print(df.isnull().sum())


print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# Remove duplicate records

df = df.drop_duplicates()


print("\nDuplicate Rows After Removing:")
print(df.duplicated().sum())


print("\nOutlier Detection:")

outlier_result = {}


for col in numeric_columns:

    Q1 = df[col].quantile(0.25)

    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)

    upper_bound = Q3 + (1.5 * IQR)

    outliers = df[
        (df[col] < lower_bound) |
        (df[col] > upper_bound)
    ]

    outlier_result[col] = len(outliers)
print(outlier_result)
# Display box plots for major CPI indicators
visualization_columns = [
    "Food and beverages",
    "Fuel and light",
    "Health",
    "Transport and communication",
    "Education",
    "General index"
]


for col in visualization_columns:

    plt.figure(figsize=(6, 4))

    sns.boxplot(
        x=df[col]
    )

    plt.title(
        "Outlier Detection : " + col
    )

    plt.xlabel(
        col
    )

    plt.show()
# Remove spaces from column names

df.columns = df.columns.str.strip()


# Convert column names into lowercase

df.columns = df.columns.str.lower()


# Replace spaces with underscores

df.columns = (
    df.columns
    .str.replace(" ", "_")
    .str.replace(",", "")
)


print("\nCleaned Column Names:")
print(df.columns)


scaler = MinMaxScaler()

df[numeric_columns] = scaler.fit_transform(
    df[numeric_columns]
)


print("\nTransformed Dataset:")
print(df.head())


output_file = "cleaned_consumer_price_index.xlsx"

df.to_excel(
    output_file,
    index=False
)


print("\nCleaned Dataset Saved Successfully!")

print(
    "File Name:",
    output_file
)
