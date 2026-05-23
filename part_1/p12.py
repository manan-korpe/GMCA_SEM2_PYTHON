# Write a program in python to implement factorial series up to user entered number.
# (Use recursive Function)

def factorial(n):
    if(n <= 1):
        return 1

    val = factorial(n-1)
    print(val)
    return n

factorial(3)
