import csv

with open("data.csv", "r") as f:

    r = csv.reader(f)

    html = "<table border='1'>"

    for row in r:

        html += "<tr> \n"

        for col in row:
            html += "<td>" + col + "</td>"

        html += "</tr> \n"

    html += "</table> \n"

with open("table.html", "w") as file:
    file.write(html)

print("HTML Table Created")