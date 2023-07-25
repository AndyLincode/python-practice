import datetime

x = datetime.datetime.now()

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
# 2023
# 7
# 25
# 9
# 28
# 36
# 847133

print(x.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-07-25 09:28:36
