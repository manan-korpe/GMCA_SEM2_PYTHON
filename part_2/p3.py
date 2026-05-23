import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nRetrieve Single Column:")
print(df_csv["Book_Name"])

print("\nRetrieve Multiple Columns:")
print(df_csv[["Book_Name", "Author"]])

print("\nRetrieve First Two Rows:")
print(df_csv.iloc[0:2])