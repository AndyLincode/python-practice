import sqlite3

conn = sqlite3.connect("datafile.sqlite")  # 存在disk
cursor = conn.cursor()
cursor.execute(
    """create table people ( id integer primary key, name text, count integer)""")
cursor.execute("""insert into people (name, count) values ('Andy', 15)""")
cursor.execute(
    """insert into people (name, count) values (?, ?)""", ('John', 13))
cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {
               'username': 'Mary', 'usercount': 19})


conn.commit()
conn.close()
