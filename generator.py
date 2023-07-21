def cube(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


for i in cube(10):
    print(i)
# 0
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
