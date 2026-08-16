# ============================================================
# EXPERIMENT 4
# Consumer Price Trend Analytics
# Comparative Visualization
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
file_path = "All India Consumer Price Index.csv"
df = pd.read_csv(file_path)

df["General index"] = pd.to_numeric(
    df["General index"],
    errors="coerce"
)


sector_cpi = (
    df.groupby("Sector")["General index"]
    .mean()
)


print("Average General CPI by Sector:")
print(sector_cpi)


plt.figure(figsize=(8, 5))

plt.bar(
    sector_cpi.index,
    sector_cpi.values
)

plt.title(
    "Average Consumer Price Index by Sector"
)

plt.xlabel(
    "Sector"
)

plt.ylabel(
    "Average General CPI"
)

plt.show()


df["Date"] = pd.to_datetime(
    df["Month"] + " " + df["Year"].astype(str),
    format="%B %Y",
    errors="coerce"
)


sector_trend = (
    df.groupby(
        ["Date", "Sector"]
    )["General index"]
    .mean()
    .reset_index()
)


# Sort by date

sector_trend = sector_trend.sort_values(
    "Date"
)


# Plot each sector

plt.figure(figsize=(12, 6))


for sector in sector_trend["Sector"].unique():

    data = sector_trend[
        sector_trend["Sector"] == sector
    ]

    plt.plot(
        data["Date"],
        data["General index"],
        label=sector
    )


plt.title(
    "Consumer Price Index Trend by Sector"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "General CPI"
)

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
