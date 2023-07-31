import sqlite3

conn = sqlite3.connect('datafile.sqlite')
cursor = conn.cursor()

name = input("Please type the name you want to search: ")

# result = cursor.execute(
#     """SELECT * FROM people WHERE name=:username""", {'username': name})
result = cursor.execute(
    """SELECT * FROM people WHERE name=?""", (name,))
print(result.fetchall())

conn.commit()
conn.close()
