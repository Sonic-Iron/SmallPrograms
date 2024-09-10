from socket import *
from threading import Thread
import sys
from tkinter import *
import math
global s
s = socket(AF_INET, SOCK_STREAM)

host, port = 'localhost', 5023

window = Tk()

canvas = Canvas(window, height=500, width = 500, bg = "white")
player1_head = canvas.create_oval(125,250,135,260, fill = "black", tags="player1")
player1_body = canvas.create_line(130,260,130,271, fill = "black", tags="player1")
player1_leg_left = canvas.create_line(125,280,130,270, fill = "black", tags="player1")
player1_leg_right = canvas.create_line(135,280,130,270, fill = "black", tags="player1")
player1_arm_left = canvas.create_line(127,268,130,262, fill = "black", tags="player1")
player1_arm_right = canvas.create_line(133,268,130,262, fill = "black", tags="player1")
player1_sword = canvas.create_line(133,268,148,253, fill = "red", tags="player1")


player2_head = canvas.create_oval(375,250,385,260,fill ="black", tags="player2")
player2_body = canvas.create_line(380,260,380,270, fill = "black", tags="player2")
player2_leg_left = canvas.create_line(380,270,375,280, fill = "black", tags="player2")
player2_leg_right = canvas.create_line(380,270,385,280, fill = "black", tags="player2")
player2_arm_left = canvas.create_line(380,262,377,268, fill = "black", tags="player2")
player2_arm_right = canvas.create_line(380,262,383,268, fill = "black", tags="player2")
player2_sword = canvas.create_line(377,268,362,253, fill = "red", tags="player2")

player1_b = Button(window, text="Player 1", command = lambda: send_pp(s,"player1",player1_b,player2_b))
player2_b = Button(window, text="Player 2", command = lambda: send_pp(s,"player2",player1_b,player2_b))


def client(host,port):
    try:
        s.connect((host, port))
    except error as e:
        print(str(e))
        sys.exit()    
    Thread(target = receive_data, args = (s,canvas)).start()
    player1_b.pack(side=LEFT)
    player2_b.pack(side=RIGHT)

def main(s,canvas,pp): # will be used to animate the user player
    print("STARTING MAIN")
    canvas.pack()
    def animate_arms(canvas): # animate attacks
        def attack_light():
            print("Working light attack")

        def attack_heavy():
            print("Working heavy attack")
        #window.bind("<KeyPress-E>", attack_light)
        #window.bind("<KeyPress-R>", attack_heavy)

    def animate_movement(canvas,pp): # movement
        print("Started movement")
        
        pressedStatus = {"w":False,"a":False,"s":False,"d":False}

        def pressed(event):
            pressedStatus[event.keysym] = True

        def released(event):
            pressedStatus[event.keysym] = False

        def animate_legs(canvas,pp):
            print("Starting animations")
            if pp == "player1":
                while True:
                    if pressedStatus["w"] == True:
                        canvas.move("player1",0,-0.05)
                        s.send("P1:move:0:-0.05".encode())
                    if pressedStatus["a"] == True:
                        canvas.move("player1",-0.05,0)
                        s.send("P1:move:-0.05:0".encode())
                    if pressedStatus["s"] == True:
                        canvas.move("player1",0,0.05)
                        s.send("P1:move:0:0.05".encode())
                    if pressedStatus["d"] == True:
                        canvas.move("player1",0.05,0)
                        s.send("P1:move:0.05:0".encode())
            elif pp == "player2":
                while True:
                    if pressedStatus["w"] == True:
                        canvas.move("player2",0,-0.05)
                        s.send("P2:move:0:-0.05".encode())
                    if pressedStatus["a"] == True:
                        canvas.move("player2",-0.05,0)
                        s.send("P2:move:-0.05:0".encode())
                    if pressedStatus["s"] == True:
                        canvas.move("player2",0,0.05)
                        s.send("P2:move:0:0.05".encode())
                    if pressedStatus["d"] == True:
                        canvas.move("player2",0.05,0)
                        s.send("P2:move:0.05:0".encode())



                    
            


        def set_bindings():
            for char in ["w", "a", "s", "d"]:
                print(char, "binding")
                window.bind("<KeyPress-%s>" % char, pressed)
                window.bind("<KeyRelease-%s>" % char, released)
            

        set_bindings()
        animate_legs(canvas,pp)
        
        
    #Thread(target=animate_arms, args=(canvas)).start()
    Thread(target=animate_movement, args=(canvas,pp)).start()

def send_pp(s,player_position,player1_b,player2_b):
    player1_b.destroy()
    player2_b.destroy()
    s.send(player_position.encode())
    

    
def receive_data(s,canvas): # will be used to animate the other player
    print("RUNNING")
    while True:
        try:
            data = s.recv(1024)
            if data.decode() == "PlayerKick":
                window.destroy()
                sys.exit()
            if (data.decode() == "player1"):
                Thread(target=main, args=(s,canvas,"player1")).start()
                print(data.decode())
            elif data.decode() == "player2":
                Thread(target=main, args=(s,canvas,"player2")).start()
                print(data.decode())
            else:
                data = data.decode()
                data = data.split(":")# where the code to animate the other player goes
                data = data[0:4]
                try:
                    if "P1" in data[3]:
                        data[3].remove("P1")
                        print("Removed")
                except:
                    pass
                try:
                    if "P2" in data[3]:
                        data[3].remove("P2")
                        print("Removed")
                except:
                    pass
                print(data)
                try:
                    if data[0] == "P1": ######################  need to remove the P1/P2 in data[3]
                        if data[1] == "move":
                            canvas.move("player1",float(data[2]),float(data[3]))
                    elif data[0] == "P2":
                        if data[1] == "move":
                            canvas.move("player2",float(data[2]),float(data[3]))
                    else:
                        pass
                except:
                    pass
        except error as e:
            print(str(e))
            sys.exit()

client(host,port)

mainloop()

# some code from:
#http://effbot.org/zone/tkinter-complex-canvas.htm
