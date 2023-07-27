num = "1234-5"
forbidden = "-"

print([int(i) for i in str(num) if i not in forbidden])
