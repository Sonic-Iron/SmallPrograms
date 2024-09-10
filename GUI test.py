################################GUI########################################
from tkinter import *
import random
import os, sys
import time

jump = 0
pause = True


###################################################################################menu##################################################
window = Tk()
canvas = Canvas(width = 500, height = 500)
start = Button(window,text="Start Game",command = lambda: start_game())
start.pack(expand=True)
end = Button(window,text="Quit Game",command= lambda: os._exit(0))
pause_button = Button(window, text = "Pause Game", command = lambda: Pause())
end.pack(expand=True)

def start_game():
    global pause
    print("starting game")
    start.pack_forget()
    end.pack_forget()
    window.after(10)
    canvas.pack()
    pause = False
    pause_button.pack()
    end.pack(side=TOP)




player = canvas.create_rectangle(10, 300, 30, 320, fill = "yellow", outline = "yellow")
health = canvas.create_rectangle(10,10,490,20, fill = "green", outline = "black")
enemy1 = canvas.create_oval(0,0,20,20, fill = "red", outline = "red")#  make these an object (class), this is so i can do different sizes



floor = canvas.create_rectangle(-20, 400, 500, 500, fill = "blue", outline = "blue")
floor2 = canvas.create_rectangle(600,400,1000,500, fill = "blue", outline = "blue")
floor1ledge = canvas.create_rectangle(300,300,400,400, fill = "blue", outline = "blue")
floordeadly = canvas.create_rectangle(1100,400,1200,500, fill = "red", outline = "red")
floor3midddle = canvas.create_rectangle(1125, 399, 1175, 500, fill="blue", outline="blue")
floor41 = canvas.create_rectangle(1300, 400, 1600, 500, fill="blue", outline = "blue")
floor42 = canvas.create_rectangle(1400, 300, 1600, 500, fill="blue", outline = "blue")
floor43 = canvas.create_rectangle(1500, 200, 1600, 500, fill="blue", outline = "blue")
floor5 = canvas.create_rectangle(1900, 400, 2050, 500, fill= "black", outline = "black")
floor5deadly1 = canvas.create_rectangle(2000, 400, 2010, 500, fill= "red", outline = "red")
floor5deadly2 = canvas.create_rectangle(2020, 400, 2030, 500, fill= "red", outline = "red")
floor6 = canvas.create_rectangle(2300, 400, 3200, 500, fill= "black", outline = "black") 

canvas.itemconfig(floor, tags=("floor"))
canvas.itemconfig(floor2, tags=("floor"))
canvas.itemconfig(floor1ledge, tags=("floor"))
canvas.itemconfig(floordeadly, tags=("floor","deadly"))
canvas.itemconfig(floor3midddle, tags =("floor"))
canvas.itemconfig(floor41, tags =("floor"))
canvas.itemconfig(floor42, tags =("floor"))
canvas.itemconfig(floor43, tags =("floor"))
canvas.itemconfig(floor5, tags =("floor"))
canvas.itemconfig(floor5deadly1, tags =("floor", "deadly"))
canvas.itemconfig(floor5deadly2, tags =("floor", "deadly"))
canvas.itemconfig(floor6, tags =("floor"))
canvas.itemconfig(enemy1, tags= ("floor","deadly", "enemy"))




##################################################player movement ######################################################
pressedStatus = {"Up": False, "Down": False, "Left": False, "Right": False, "space": False}

def pressed(event):
    pressedStatus[event.keysym] = True

def released(event):
    pressedStatus[event.keysym] = False

def set_bindings():
    for char in ["Up", "Down", "Left", "Right", "space"]:
        window.bind("<KeyPress-%s>" % char, pressed)
        window.bind("<KeyRelease-%s>" % char, released)

def animate():
    global jump
    if pause == False:
        if pressedStatus["Up"] == True:
                tagged_objects = canvas.find_withtag("floor")
                overlapping_objects = canvas.find_overlapping(*canvas.coords(player))

                for item in overlapping_objects:
                    if (item in tagged_objects):
                        canvas.move(player, 0 , -100)            
        if pressedStatus["Left"] == True:
            if (canvas.coords(player) < [40.0, 380.0, 60.0, 400.0]):
                for item in canvas.find_withtag("floor"):
                    canvas.move(item, 10, 0)
            else:
                canvas.move(player, -10, 0)
        if pressedStatus["Right"] == True:
            if (canvas.coords(player) > [300.0, 379.0, 480.0, 399.0]):
                for item in canvas.find_withtag("floor"):
                    canvas.move(item, -10, 0)
            else:
                canvas.move(player, 10, 0)
        if pressedStatus["space"] == True:
            print("Spacebar pressed")
        canvas.update()
    else:
        ""
    window.after(40, animate)

############################################################## obstacles##########################

def hurt():
    if pause == False:
        tagged_objects = canvas.find_withtag("deadly")
        overlapping_objects = canvas.find_overlapping(*canvas.coords(player))
        if canvas.coords(player)[1] > 500:
            x = canvas.coords(health)[2]
            x = x - 10
            canvas.coords(health, canvas.coords(health)[0],canvas.coords(health)[1],x,canvas.coords(health)[3])

        for item in overlapping_objects:
            if (item in tagged_objects):
                x = canvas.coords(health)[2]
                x = x - 10
                canvas.coords(health, canvas.coords(health)[0],canvas.coords(health)[1],x,canvas.coords(health)[3])
                if canvas.coords(health)[0] > canvas.coords(health)[2]:
                    while True:
                        time.sleep(1)
    else:
        ""
    window.after(100, hurt)            

def enemy_movement():
    if pause == False:
        for a in canvas.find_withtag("enemy"):
            canvas.move(a, 0.005*(canvas.coords(player)[0]-canvas.coords(a)[0]), 0.005*(canvas.coords(player)[1]-canvas.coords(a)[1]))
    else:
        ""
    window.after(5, enemy_movement)


###################################other
def gravity():
    global jump
    if pause == False:
        tagged_objects = canvas.find_withtag("floor")
        overlapping_objects = canvas.find_overlapping(*canvas.coords(player))

        for item in overlapping_objects:
            if (item in tagged_objects):
                canvas.move(player, 0, -1.5)
            else:
                canvas.move(player, 0 , 1)
                jump = 0
    else:
        ""
    window.after(3, gravity)

def Pause():
    global pause
    if pause == True:
        pause = False
    elif pause == False:
        pause = True
    else:
        print("Waaa")



####################################################################### function runnings 

# Bind the (← ↑ → ↓) keys's Press and Release events
set_bindings()

# Start the animation loop
animate()

# Launch the window
window.after(100, enemy_movement)   
window.after(100, hurt) 
window.after(100, gravity)
mainloop()
