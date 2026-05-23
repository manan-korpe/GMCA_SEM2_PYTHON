import pandas as pd
import numpy as np
from pylab import *

df = pd.read_csv("dta.csv")

print("Data Frame from CSV File:")
print(df)

data = {
    'Name': ['Amit', 'Neha', 'Raj'],
    'Marks': [85, 90, 78]
}
df_dict = pd.DataFrame(data)

print("\nData Frame from Dictionary:")
print(df_dict)

data2 = [
    ('Aman', 21),
    ('Riya', 20),
    ('Kunal', 22)
]
df_tuple = pd.DataFrame(data2, columns=['Name', 'Age'])

print("\nData Frame from List of Tuples:")
print(df_tuple)

print("\nShape:")
print(df.shape)

print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nMarks Column:")
print(df['Marks'])

print("\nName and Marks Columns:")
print(df[['Name', 'Marks']])

print("\nFirst 2 Rows:")
print(df.iloc[0:2])

print("\nMaximum Marks:")
print(df['Marks'].max())

print("\nMinimum Marks:")
print(df['Marks'].min())

print("\nStatistical Information:")
print(df.describe())

print("\nStudents with Marks > 80:")
print(df[df['Marks'] > 80])


ENROLLMENT NO: 255690694020		NAME: KORPE MANAN K. 