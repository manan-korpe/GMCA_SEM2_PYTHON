import pandas as pd
import numpy as np

data = {
    "Name": ["Aaryan", "Yash", "Priya", "Amit", np.nan],
    "Marks": [90, np.nan, 85, 78, 95],
    "City": ["Rajkot", "Surat", np.nan, "Ahmedabad", "Vadodara"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values:")
print(df.isnull().sum())

df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("Not Available")

print("\nDataFrame after Filling Missing Values:")
print(df)

df_clean = df.dropna()

print("\nDataFrame after Dropping Missing Values:")
print(df_clean)