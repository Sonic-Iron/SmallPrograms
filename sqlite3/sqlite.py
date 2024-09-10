import sqlite3, os
if os.path.isfile('database.db'):
    print("removed")
    os.remove('database.db')

conn = sqlite3.connect('database.db')
db = conn.cursor()

db.execute(""" CREATE TABLE people (name STRING PRIMARY KEY, age INTEGER)""")

db.execute("INSERT INTO people (name,age) VALUES ('Sam',16)");
db.execute("INSERT INTO people (name,age) VALUES ('Elvan',17)");
sql = ("SELECT * FROM people")

db.execute(sql)
print(db.fetchall()[0][1])
