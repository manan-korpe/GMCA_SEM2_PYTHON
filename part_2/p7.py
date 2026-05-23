import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nAverage Marks City-wise:")
group_data = df_csv.groupby("City")["Marks"].mean()
print(group_data)