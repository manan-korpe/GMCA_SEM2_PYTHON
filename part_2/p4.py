import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nMaximum Price:")
print(df_csv["Price"].max())

print("\nMinimum Price:")
print(df_csv["Price"].min())