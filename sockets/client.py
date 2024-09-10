from socket import *
from threading import Thread
import sys

def client(host,port):

    s = socket(AF_INET, SOCK_STREAM)

    try:
        s.connect((HOST, PORT))
    except error as e:
        print(str(e))
        sys.exit()
        
    print('Connected to remote host...')
    uname = input('Enter your name to enter the chat > ')

    Thread(target = send_data,args=(s,uname)).start()
    Thread(target = receive_data,args=(s,)).start()

#    s.close()

def send_data(s,uname):
    while True:
        msg = input('Me> ')
        data = '\n' + uname + '> ' + msg + '\nMe> '
        s.send(data.encode())
    s.close()

def receive_data(s):
    while True:
        try:
            data = s.recv(1024)
            print(str(data.decode()), end="")
        except error as e:
            print(str(e))
            sys.exit()        

if __name__ == "__main__":   
    HOST = 'localhost'
    PORT = 5023
    client(HOST,PORT)
