# ite a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (do not use Len ())
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

def countVowel(value):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    
    for i in value:
        if i in vowel:
            count = count + 1
    
    return count

def strLength(value):
    count = 0
    for i in value:
        count = count + 1
    
    return count

def strReverse(value):
    return value[-1::-1]

def find(value):
    f = str(input("Enter value you want to find :"))
    return value.find(f)

def replace(value):
    old = str(input("Enter old string: "))
    new = str(input("Enter new string: "))
    return value.replace(old, new)

def isPalindrome(value):
    return value == value[-1::-1]

strinput = str(input("Enter input: "))
print("vowel count: ",countVowel(strinput))
print("length: ",strLength(strinput))
print("reverse:",strReverse(strinput))
print("find at",find(strinput))
print("replaced",replace(strinput))
print(f"{strinput} is palindrome" if isPalindrome(strinput) else f"{strinput} is not palindrome")