import pandas as pd

df_csv = pd.read_csv("Book1.csv")

print("\nBOOK with Price greater than 85:")
print(df_csv[df_csv["Price"] > 500])
