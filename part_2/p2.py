import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nShape of DataFrame:")
print(df_csv.shape)

print("\nHead of DataFrame:")
print(df_csv.head())

print("\nTail of DataFrame:")
print(df_csv.tail())