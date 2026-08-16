# ============================================================
# EXPERIMENT 2
# Consumer Price Trend Analytics
# Data Conversion, JSON, SQLite and Visualization
# ============================================================

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

file_path = "All India Consumer Price Index.csv"
df = pd.read_csv(file_path)
print("First 5 Records")
print(df.head())
print("\nDataset Information")
df.info()
print("\nStatistical Summary")
print(df.describe(include="all"))
excel_file = "consumer_price_index.xlsx"
df.to_excel(
    excel_file,
    index=False
)
print("\nCSV converted to Excel successfully!")
df_excel = pd.read_excel(excel_file)

print("\nFirst 5 Records from Excel")
print(df_excel.head())

csv_file = "consumer_price_index_converted.csv"

df_excel.to_csv(
    csv_file,
    index=False
)

print("\nExcel converted to CSV successfully!")

df_csv = pd.read_csv(csv_file)

print("\nFirst 5 Records from Converted CSV")
print(df_csv.head())

json_file = "consumer_price_index.json"

df_csv.to_json(
    json_file,
    orient="records",
    indent=4
)

print("\nJSON file created successfully!")


df_json = pd.read_json(json_file)

print("\nFirst 5 Records from JSON")
print(df_json.head())

print("\nJSON Dataset Information")
df_json.info()

print("\nJSON Statistical Summary")
print(df_json.describe(include="all"))

conn = sqlite3.connect(
    "consumer_price_index.db"
)

df.to_sql(
    "consumer_price_index",
    conn,
    if_exists="replace",
    index=False
)

print("\nData exported to SQLite successfully!")

conn.close()

conn = sqlite3.connect(
    "consumer_price_index.db"
)

df_sql = pd.read_sql(
    "SELECT * FROM consumer_price_index",
    conn
)

print("\nFirst 5 Records from SQLite")
print(df_sql.head())
print("\nSQLite Dataset Information")
df_sql.info()
print("\nSQLite Statistical Summary")
print(df_sql.describe(include="all"))
conn.close()
sector = df["Sector"].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(
    sector.index,
    sector.values
)
plt.title(
    "Sector-wise Consumer Price Index Records"
)
plt.xlabel(
    "Sector"
)
plt.ylabel(
    "Number of Records"
)
plt.show()
