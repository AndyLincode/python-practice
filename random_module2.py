import random

# random.seed(10)

# for i in range(5):
#     print(random.randint(1, 1000))
# 586
# 34
# 440
# 495
# 592

sentence = "Hi , this is a python project !"
print(random.choice(sentence))

fruits = ['apple', 'banana', 'cherry']
result = random.choices(fruits, weights=[2, 1, 1], k=10)  # 意思是 1/2 1/4 1/4
result2 = random.choices(fruits, weights=[0.2, 0.1, 0.3], k=10)  # 意思是
print(result)
print(result2)
# ['apple', 'apple', 'apple', 'apple', 'banana', 'apple', 'cherry', 'apple', 'apple', 'apple']
# ['apple', 'cherry', 'apple', 'apple', 'apple', 'cherry', 'apple', 'banana', 'apple', 'cherry']


result3 = random.sample(fruits, k=2)
print(result3)  # ['cherry', 'banana']

random.shuffle(fruits)
print(fruits)  # ['cherry', 'apple', 'banana'] 會影響原資料

my_tuple = (3, 4, 1, 5, 8, 9, 6)
my_list = random.sample(my_tuple, k=len(my_tuple))
print(my_list)  # [5, 6, 8, 4, 1, 9, 3]
