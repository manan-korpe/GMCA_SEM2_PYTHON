# Write a program in python to find out maximum and minimum number out of three user entered number
list1 = []

for i in range(0,3):
    list1.append(int(input(f"Enter value {i}: ")))

min = max = list1[0]

for i in range(0,len(list1)):
    if list1[i] > max:
        max = list1[i]
    
    if list1[i] < min:
        min = list1[i]

print("Max: ",max," Min: ",min)