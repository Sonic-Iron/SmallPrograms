from tkinter import *
import random, os, time, sqlite3
inventory = []
roomnamesfloor1 = ["living room","dining room", "bathroom", "kitchen"]
roomnamesfloor2 = ["bedroom","bathroom","storageroom"]

if os.path.isfile('roomdatabase.db'):
    os.remove('roomdatabase.db')

conn = sqlite3.connect('roomdatabase.db')
db = conn.cursor()

db.execute("""CREATE TABLE rooms (roomID INTEGER PRIMARY KEY, roomName TEXT,floor INTEGER, traps INTEGER)""")


    

for a in range(10):
    traps = random.uniform(0,1)
    traps = round(traps,1)
    if traps >= 0.8:
        traps = 1
    else:
        traps = 0
    floorlevel = random.randint(1,2)
    if floorlevel == 1:
        roomname = random.choice(roomnamesfloor1)
    elif floorlevel == 2:
        roomname = random.choice(roomnamesfloor2)
    db.execute("INSERT INTO rooms (roomID,roomName,floor,traps) VALUES (NULL,?,?,?)",(roomname,floorlevel,traps));


def print_table(sql):
    db.execute(sql)
    all_rows = db.fetchall()
    for rows in all_rows:
        for i in rows:
            print(i, end=' | \t')
        print()
    print()
sql = "SELECT * FROM rooms"
print_table(sql)

db.execute(sql)
database = db.fetchall()
for rows in database:
    for i in rows:
        print(i, end=' | \t')
    print()
print()

print(database)

conn.commit()
conn.close()
