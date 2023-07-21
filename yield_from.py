def sub_generator(x):
    for i in range(x):
        yield i ** 2


def gen(y):
    yield from sub_generator(y)


for num in gen(15):
    print(num)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
