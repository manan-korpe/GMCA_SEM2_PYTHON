# Write a Python program to check if the number provided by the user is a palindrome or not.
def isPalindrome(number):
    size = len(str(number))
    temp = number
    reverser = 0 
    for i in range(0,size):
        reverser = reverser*10
        reminder = temp % 10
        reverser = reverser + reminder
        temp = int(temp / 10)
        
    return  number == reverser

number = int(input("Enter Number : "))
if isPalindrome(number):
    print(f"number {number} is palindrome")
else:
    print(f"number {number} is not palindrome")