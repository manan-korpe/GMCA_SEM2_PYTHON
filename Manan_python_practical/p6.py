
import re

pattern = r'^[0-9]+ [A-Za-z]+( [A-Za-z]+)* (Street|St|Road|Rd|Avenue|Ave|Drive|Dr|Boulevard|Blvd|Lane|Ln)$'

addresses = [
    "1180 Bordeaux Drive",
    "3120 De la Cruz Boulevard",
    "45 MG Road",
    "221 Baker Street",
    "12 Park Avenue",
    "Bordeaux Drive",
    "123",
    "12 @Road Street"
]

for address in addresses:
    if re.match(pattern, address):
        print(address, "-> Matched")
    else:
        print(address, "-> Not Matched")