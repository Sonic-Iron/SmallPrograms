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
    print('Chat server started on port ' + str(PORT))
    accept_client(s)

def accept_client(s):
    while True:  
        conn, addr = s.accept()
        print("Connected to " + addr[0] + ":" + str(addr[1]))
        clients.append(conn)
        Thread(target = message, args=[conn]).start()

def message(conn):
    while True:
        try:
            data = conn.recv(1024)
            if data:
                broadcast(conn, data)
        except error as e:
            print(str(e))
            clients.remove(conn)
            break

def broadcast(conn, msg):
    for client in clients:
        if client != conn:
            client.send(msg)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5023
    listener(HOST,PORT)
