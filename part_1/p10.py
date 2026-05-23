# Define a procedure histogram () that takes a
# list of integers and prints a histogram to
# thescreen. For example, histogram ([4, 9, 7])
# should print the following:
# ****
# *********
# *******
def histogram(data):
    for n in data:
        print("*" * n)

histogram([4, 9, 7])