import random

print(random.randrange(10, 20))  # 10 - 20 含10不含20
print(random.randint(10, 20))  # 10 - 20 含10含20

for n in range(10):
    print(random.randrange(10, 20, 3))  # 10-20中 10 + 3n 的數字
