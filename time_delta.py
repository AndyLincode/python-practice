import datetime

now = datetime.datetime.now()
oneday = datetime.datetime(2023, 3, 12)

diff = now - oneday

print(diff)  # 135 days, 10:10:12.600356
print(diff.days)  # 135
print(diff.total_seconds())  # 11700612.600356
print(type(diff))  # <class 'datetime.timedelta'>

gap = datetime.timedelta(1)

tomorrow = now + gap
print(tomorrow)  # 2023-07-26 10:10:12.600356

print(now == oneday)
print(now > oneday)
print(now < oneday)
# False
# True
# False
