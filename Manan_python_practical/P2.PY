import re

pattern = r'^[bh][iau]t$'

words = ["bit", "but", "bat", "hit", "hat", "hut", "mot"]

for word in words:
    if re.match(pattern, word):
        print(word, "-> Matched")
    else:
        print(word, "-> Not Matched")