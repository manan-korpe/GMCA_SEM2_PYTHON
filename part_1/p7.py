# Write a Python program to check if the number provided by the user is an Armstrong number.
num = number = int(input("Enter Number :"))
number_size = len(str(number))

sum = 0

for n in range(0,number_size):
    current = number % 10 
    power = 1
    for x in range(0,number_size):
       power =  power * current
    sum = sum + power
    number = int(number / 10)

if num == sum:
    print(f"Number {num} is Armstrong number")
else:
    print(f"Number {num} is not Armstrong number")
