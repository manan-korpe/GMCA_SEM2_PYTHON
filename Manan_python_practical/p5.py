import re

pattern = r'^www\.[A-Za-z0-9-]+\.(com|edu|net|org|in)$'

domains = [
    "www.yahoo.com",
    "www.foothill.edu",
    "www.google.net",
    "www.wikipedia.org",
    "yahoo.com",
    "www..com"
]

for domain in domains:
    if re.match(pattern, domain):
        print(domain, "-> Matched")
    else:
        print(domain, "-> Not Matched")