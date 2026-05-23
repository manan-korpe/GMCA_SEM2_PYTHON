# Write a program in python to implement fibonacci series up to user entered number.
# (Use recursive Function). 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(20):
    print(fibonacci(i), end=" ")