import sqlite3

conn = sqlite3.connect('datafile.sqlite')
cursor = conn.cursor()

cursor.execute("""DELETE FROM people WHERE name='Andy'""")

result = cursor.execute("""SELECT * FROM people""")
print(result.fetchall())  # [(2, 'John', 29), (3, 'Mary', 19)]

conn.commit()
conn.close()
