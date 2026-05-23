# Write a program in Python to implement readline, readlines, write line and writelines
# file handling mechanisms

with open("p13.txt","r") as f:
    print(f.readline())
    print(f.readlines())

with open("p13.txt","w") as f:
    f.write("this is new line added \n")
    f.writelines(["this is first line \n", "this is second lline"])
