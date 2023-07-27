import csv

with open('new.csv', mode="w", newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerow(['a', 'b', 'c'])

# new.csv => a,b,c


with open('new.csv', mode="a", newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerows([['e', 'f', 'g'], ['h', 'i', 'j']])

# new.csv =>
# a,b,c
# e,f,g
# h,i,j
