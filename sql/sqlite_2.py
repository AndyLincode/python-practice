import sqlite3

conn = sqlite3.connect('datafile.sqlite')
cursor = conn.cursor()

result = cursor.execute("SELECT * FROM people")
# print(result.fetchall()) # [(1, 'Andy', 15), (2, 'John', 13), (3, 'Mary', 19)]
print(result.fetchmany(2))  # [(1, 'Andy', 15), (2, 'John', 13)]
result2 = cursor.execute(
    "SELECT * FROM people WHERE name=:username", {'username': 'John'})
print(result2.fetchall())  # [(2, 'John', 13)]
conn.commit()
conn.close()
