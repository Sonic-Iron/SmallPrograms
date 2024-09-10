from socket import *
from threading import Thread
import sys

clients = []

def listener(host,port):
    
    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.bind((host,port))
    except error as e:
        print(str(e))
        sys.exit()

    s.listen(1)
    print('Server started on port ' + str(PORT))
    accept_client(s)

def accept_client(s):
    while True:  
        conn, addr = s.accept()
        print("Connected to " + addr[0] + ":" + str(addr[1]))
        clients.append(conn)
        if len(clients) >= 3:
            conn.send("PlayerKick".encode())
            clients.remove(conn)
            conn.close()
        else:
            print("There are online: ",len(clients))
            Thread(target = message, args=[conn]).start()

def message(conn):
    while True:
        print("There are online:",len(clients))
        try:
            data = conn.recv(1024)
            print("Decoded Data: ",data.decode())
            if data.decode() == "player1":
                recieving_players(conn, "player1")
                print("Player 1 sent")
            elif data.decode() == "player2":
                recieving_players(conn, "player2")
                print("Player 2 sent")
            else: # not the player start code
                print("sending : ",data.decode())
                data = data.decode()
                data = data.split(":")
                if data[0] == "P1":
                    if data[1] == "move":
                        conn1.send(("P1:move:"+data[2]+":"+data[3]).encode())
                if data[0] == "P2":
                    if data[1] == "move":
                        conn2.send(("P2:move:"+data[2]+":"+data[3]).encode())
        except error as e:
            print(str(e))
            clients.remove(conn)
            conn.close()
            break
        
def recieving_players(conn, pp): # making sure that both the players see their game screens at the same time
    global conn1, conn2, conn1found, conn2found
    try:
        conn1found
    except:
        conn1found = False
        print("conn1found set to false")
    try:
        conn2found
    except:
        conn2found = False
        print("conn2found set to false")
    if (pp == "player1") and (conn1found==False):
        conn1 = conn
        conn1found = True
        print("P1found set to true")
    if (pp == "player2") and (conn2found==False):
        conn2 = conn
        conn2found = True
        print("P2found set to true")
    print(conn1found, conn2found)
    try:
        if (conn1found and conn2found) == True:
            conn1.send("player1".encode())   
            conn2.send("player2".encode())
            print("Sending start game now")
        else:
            pass
    except:
            print("ERROR - some of the players disconneded")
            conn1found = False
            conn2found = False
        

def broadcast(conn, msg):
    for client in clients:
        client.send(msg.encode())

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5023
    listener(HOST,PORT)
