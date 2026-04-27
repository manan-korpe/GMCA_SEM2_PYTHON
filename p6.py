# Write a program which will allow user to enter 10 numbers and display largest oddnumber from them. It will display 
# appropriate message in case if no odd number is found.

odd = 0

for i in range(1,11):
    number = int(input(f"Enter Number {i} : "))
    if number % 2 == 1 and number > odd:
        odd = number
    
if odd:
    print(number)
else:
    print("no odd number is found")
             