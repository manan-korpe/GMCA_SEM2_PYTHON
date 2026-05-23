import re

pattern = r'^[A-Za-z]+, [A-Za-z]$'

texts = [
    "Smith, J",
    "Patel, R",
    "Brown, A",
    "Smith,J",
    "Smith, John",
    "123, A"
]

for text in texts:
    if re.match(pattern, text):
        print(text, "-> Matched")
    else:
        print(text, "-> Not Matched")