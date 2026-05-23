import re

pattern = r'^(\(\d{3}\)\s|\d{3}-)?\d{3}-\d{4}$'

numbers = [
    "800-555-1212",
    "555-1212",
    "(800) 555-1212",
    "8005551212",
    "(800)-555-1212",
    "55-1212"
]

for number in numbers:
    if re.match(pattern, number):
        print(number, "-> Valid")
    else:
        print(number, "-> Invalid")