import re

with open("researchpaper.txt", encoding="utf8") as f:
    text = f.read()
    x = re.findall(r"\([A-Za-z0-9\s]+, \d{4,}\)", text)
    print(x)
