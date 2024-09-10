from tkinter import *
import random

window = Tk()

canvas = Canvas(window, height = 500, width = 500)
canvas.pack()

velocity_x = 0
velocity_y = 0
acceleration_x = 0
acceleration_y = 0
aim_scoped = True

body_x = random.randint(100,400)
body_y = random.randint(100,400)
enemy_body = canvas.create_rectangle(body_x, body_y, body_x+10, body_y+20, fill = "black", tag="enemy")
enemy_head = canvas.create_oval(body_x, body_y-10,body_x+10,body_y, fill="black", tag="enemy")
enemy_leg1 = canvas.create_rectangle(body_x,body_y+10,body_x+3,body_y+35, fill="black",tag="enemy")
enemy_leg2 = canvas.create_rectangle(body_x+10, body_y+10, body_x+7, body_y+35, fill="black",tag="enemy")
enemy_arm1 = canvas.create_rectangle(body_x-3,body_y+1, body_x, body_y+15, fill = "black", tag="enemy")
enemy_arm2 = canvas.create_rectangle(body_x+10, body_y+1, body_x+13, body_y+15, fill="black", tag="enemy")
aim_pointer = canvas.create_oval(245,245,250,250, fill="red")

#movement
pressedStatus = {"Up": False, "Down": False, "Left": False, "Right": False, "space": False, "a":False, "s":False, "w":False, "d":False,"q":False}

def pressed(event):
    pressedStatus[event.keysym] = True

def released(event):
    pressedStatus[event.keysym] = False

def set_bindings():
    for char in ["Up", "Down", "Left", "Right", "space","a","s","w","d","q"]:
        window.bind("<KeyPress-%s>" % char, pressed)
        window.bind("<KeyRelease-%s>" % char, released)
def animate():
    global velocity_x, velocity_y, acceleration_x, acceleration_y, scoped
    if pressedStatus["Up"] == True:
        acceleration_y -= 0.2
    if pressedStatus["Down"] == True:
        acceleration_y += 0.2
    if pressedStatus["Left"] == True:
        acceleration_x -= 0.2
    if pressedStatus["Right"] == True:
        acceleration_x += 0.2
    window.after(4, animate)

# scripts
def moveaim_pointer():
    global velocity_x, velocity_y, acceleration_x, acceleration_y
    canvas.move(aim_pointer, velocity_x, velocity_y)
    window.after(100, moveaim_pointer)

def move_enemy():
    random_x = random.randint(-5,5)
    random_y = random.randint(-5,5)
    random_y_aim = random.randint(-15,15)
    random_x_aim = random.randint(-15,15)
    for a in canvas.find_withtag("enemy"):
        if a in canvas.find_overlapping(*canvas.bbox(aim_pointer)):
            for a in canvas.find_withtag("enemy"):
                canvas.move(a, random_x_aim, random_y_aim)
        else:
            for a in canvas.find_withtag("enemy"):
                canvas.move(a, random_x, random_y)
    window.after(2000, move_enemy)
    
def acceleration():
    global velocity_x, velocity_y, acceleration_x, acceleration_y
    velocity_x = round(velocity_x,1) + acceleration_x
    velocity_y = velocity_y + acceleration_y
    acceleration_x = 0
    acceleration_y = 0
    if acceleration_x == 0 and velocity_x > 0:
        velocity_x = velocity_x - 0.2
        velocity_x = round(velocity_x, 1)
    if acceleration_x == 0 and velocity_x < 0:
        velocity_x = velocity_x + 0.2
        velocity_x = round(velocity_x, 1)
    if acceleration_y == 0 and velocity_y > 0:
        velocity_y = velocity_y - 0.2
        velocity_y = round(velocity_y, 1)
    if acceleration_y == 0 and velocity_y < 0:
        velocity_y = velocity_y + 0.2
        velocity_y = round(velocity_y, 1)
    window.after(24, acceleration)


def playermovement():
    if pressedStatus["a"] == True:
        for a in canvas.find_withtag("enemy"):
            canvas.move(a, 10, 0)
    if pressedStatus["d"] == True:
        for a in canvas.find_withtag("enemy"):
            canvas.move(a,-10,0 )
    window.after(100, playermovement)

def shoot():
    if pressedStatus["space"] == True:
        for a in canvas.find_withtag("enemy"):
            if a in canvas.find_overlapping(*canvas.bbox(aim_pointer)):
                if a == enemy_head:
                    for a in canvas.find_withtag("enemy"):
                        canvas.move(a, random.randint(-10,10), random.randint(-10,10))
                        canvas.itemconfig(a, tags=(), fill="red")
                else:
                    canvas.move(a, random.randint(-10,10), random.randint(-10,10))
                    canvas.itemconfig(a, tags=(), fill="red")
    window.after(10, shoot)


    
set_bindings()
animate()
window.after(100, acceleration)
window.after(100, moveaim_pointer)
window.after(100, move_enemy)
window.after(100, shoot)
mainloop()
