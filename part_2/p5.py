import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nStatistical Information:")
print(df_csv.describe())