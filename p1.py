# Write a Python Program to Convert Celsius to Fahrenheit and vice –a-versa.
def  Celsius_To_Fahrenheit(celsius):
    return (celsius * (9/5)) + 32

def Fahrenheit_To_Celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


print(Celsius_To_Fahrenheit(2))
print(Fahrenheit_To_Celsius(2))