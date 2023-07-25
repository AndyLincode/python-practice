import re


text = "My number is 0911222333.Numbers are 10 numbers"

patt = "number"

match = re.search(patt, text)
print(match.group())  # number
print(match.span())  # (3, 9)
print(match.start())  # 3
print(match.end())  # 9

find = re.findall(patt, text)
print(find)  # ['number', 'number'] 回傳符合的字串list
