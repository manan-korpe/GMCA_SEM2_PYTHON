import csv

# Open CSV file
f = open("student.csv", "r")

# Create CSV reader object
r = csv.reader(f)

# Read and display data
for row in r:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Marks:", row[2])
    print()

# Close file
f.close()