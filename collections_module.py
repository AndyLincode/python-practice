from collections import Counter

my_list = [1, 2, 2, 3, 3, 1, 3, 1, 2, 3]

result = Counter(my_list)
print(result)  # Counter({3: 4, 1: 3, 2: 3})

letters = "aaccbcaabbdddaaaaacbbddbbcabaabbc"

c = Counter(letters)
print(c.most_common())  # [('a', 12), ('b', 10), ('c', 6), ('d', 5)]
print(c.most_common(1))  # [('a', 12)]
print(c.most_common(2))  # [('a', 12), ('b', 10)]
