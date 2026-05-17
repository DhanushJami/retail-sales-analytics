import pandas as pd
import numpy as np

df = pd.read_csv("data/SampleSuperstore.csv", encoding="latin1")
print("Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True,
    errors="coerce"
)

df.dropna(subset=["Order Date", "Ship Date"], inplace=True)

df["Profit Margin %"] = np.where(
    df["Sales"] != 0,
    (df["Profit"] / df["Sales"]) * 100,
    0
)

df["Order Year"] = df["Order Date"].dt.year

df.to_csv("data/cleaned_superstore.csv", index=False)
print("\nCleaned dataset saved successfully!")
print(df.head())