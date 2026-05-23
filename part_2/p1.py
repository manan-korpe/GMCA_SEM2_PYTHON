import pandas as pd

df_csv = pd.read_csv("Book1.csv")
print("DataFrame from CSV File:")
print(df_csv)

dict_data = {
    "Name": ["Ram", "Shyam", "Mohan"],
    "Age": [20, 21, 22]
}
df_dict = pd.DataFrame(dict_data)

print("\nDataFrame from Dictionary:")
print(df_dict)

tuple_data = [
    (1, "Laptop", 50000),
    (2, "Mobile", 20000),
    (3, "Tablet", 15000)
]

df_tuple = pd.DataFrame(
    tuple_data,
    columns=["Product_ID", "Product_Name", "Price"]
)

print("\nDataFrame from List of Tuples:")
print(df_tuple)