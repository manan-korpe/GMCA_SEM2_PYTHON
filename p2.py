# Write a program in python to swap two variables without using temporary variable
num1 = 10
num2 = 20

print("before num1:",num1," num2:",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("before num1:",num1," num2:",num2)