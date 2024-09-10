import sqlite3
conn = sqlite3.connect('logindatabase.db')
db = conn.cursor()
db.execute("""CREATE TABLE Users (name STRING PRIMARY KEY, email STRING, password STRING)""")
conn.commit()
conn.close()


