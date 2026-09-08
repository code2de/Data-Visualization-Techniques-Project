# ============================================================
# EXPERIMENT 5
# Consumer Price Trend Analytics
# Exploratory Data Visualization
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "All India Consumer Price Index.csv"
)

print("First 5 Records:")
print(df.head())

numeric_columns = [
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


for col in numeric_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


plt.figure(figsize=(8, 5))


sns.scatterplot(
    data=df,
    x="Food and beverages",
    y="General index",
    hue="Sector"
)


plt.title(
    "Food and Beverages CPI vs General CPI"
)

plt.xlabel(
    "Food and Beverages CPI"
)

plt.ylabel(
    "General CPI"
)

plt.show()


plt.figure(figsize=(8, 5))


sns.boxplot(
    x=df["General index"]
)


plt.title(
    "General Consumer Price Index Outlier Detection"
)

plt.xlabel(
    "General CPI"
)

plt.show()

correlation_columns = [
    "Cereals and products",
    "Meat and fish",
    "Milk and products",
    "Fruits",
    "Vegetables",
    "Food and beverages",
    "Clothing",
    "Fuel and light",
    "Health",
    "Transport and communication",
    "Education",
    "General index"
]


plt.figure(figsize=(12, 8))


corr = df[
    correlation_columns
].corr()


sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)


plt.title(
    "Consumer Price Index Correlation Heatmap"
)

plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 5))


sns.countplot(
    data=df,
    x="Sector"
)


plt.title(
    "Consumer Price Index Records by Sector"
)

plt.xlabel(
    "Sector"
)

plt.ylabel(
    "Number of Records"
)

plt.tight_layout()

plt.show()

df["Date"] = pd.to_datetime(
    df["Month"] + " " + df["Year"].astype(str),
    format="%B %Y",
    errors="coerce"
)

overall = df[
    df["Sector"] == "Rural+Urban"
].copy()


overall = overall.sort_values(
    "Date"
)


plt.figure(figsize=(12, 5))


plt.plot(
    overall["Date"],
    overall["General index"],
    marker="o"
)


plt.title(
    "General Consumer Price Index Trend Over Time"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "General CPI"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()

sector = df[
    "Sector"
].value_counts()


plt.figure(figsize=(8, 8))


plt.pie(
    sector,
    labels=sector.index,
    autopct="%1.1f%%",
    startangle=90
)


plt.title(
    "Consumer Price Index Sector Distribution"
)

plt.show()

category_columns = [
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
    "Miscellaneous"
]


category_average = (
    df[category_columns]
    .mean()
)


category_average = (
    category_average
    .sort_values(
        ascending=False
    )
    .head(10)
)


plt.figure(figsize=(10, 5))


category_average.plot(
    kind="bar"
)


plt.title(
    "Top 10 Categories by Average Consumer Price Index"
)

plt.xlabel(
    "Consumer Category"
)

plt.ylabel(
    "Average CPI"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 5))


sns.histplot(
    df["General index"].dropna(),
    bins=30,
    kde=True
)


plt.title(
    "Consumer Price Index Distribution"
)

plt.xlabel(
    "General CPI"
)

plt.ylabel(
    "Number of Records"
)

plt.show()


pair_columns = [
    "Food and beverages",
    "Fuel and light",
    "Health",
    "General index"
]


pair_df = df[
    pair_columns
].dropna()


sns.pairplot(
    pair_df
)


plt.show()
