import json

data = '{"name":"Aaryaan","city":"Ahmedabad","age":20}'

x = json.loads(data)

print("Name:", x["name"])
print("City:", x["city"])
print("Age:", x["age"])

import xml.etree.ElementTree as ET

data = """
<student>
    <name>Aaryaan</name>
    <city>Ahmedabad</city>
    <age>20</age>
</student>
"""

root = ET.fromstring(data)

print("Name:", root.find("name").text)
print("City:", root.find("city").text)
print("Age:", root.find("age").text)