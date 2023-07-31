import sqlite3

conn = sqlite3.connect('datafile.sqlite')
cursor = conn.cursor()

cursor.execute("""UPDATE people SET count=:usercount WHERE name=:username""", {
               'username': 'John', 'usercount': 29})

result = cursor.execute("""SELECT * FROM people""")
print(result.fetchall())  # [(1, 'Andy', 15), (2, 'John', 29), (3, 'Mary', 19)]

conn.commit()
conn.close()
