from pylab import *
import csv

subjects = []
marks = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        subjects.append(row[0])
        marks.append(int(row[1]))

figure(figsize=(6, 4))
bar(subjects, marks)
title("Bar Graph")
xlabel("Subjects")
ylabel("Marks")
show()

figure(figsize=(6, 4))
hist(marks, bins=5)
title("Histogram")
xlabel("Marks Range")
ylabel("Frequency")
show()

figure(figsize=(6, 4))
pie(marks, labels=subjects, autopct='%1.1f%%')
title("Pie Chart")
show()

figure(figsize=(6, 4))
plot(subjects, marks, marker='o')
title("Line Chart")
xlabel("Subjects")
ylabel("Marks")
grid(True)
show()