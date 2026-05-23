import re

pattern = r'^[A-Za-z]+ [A-Za-z]+$'

names = [
    "John Smith",
    "Alice Brown",
    "Rahul Patel",
    "John",
    "John  Smith",
    "John123 Smith"
]

for name in names:
    if re.match(pattern, name):
        print(name, "-> Matched")
    else:
        print(name, "-> Not Matched")