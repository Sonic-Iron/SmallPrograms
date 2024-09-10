from tkinter import *
import math
import random

window = Tk()
canvas = Canvas(width=500, height=500,bg="black")
canvas.pack()
window.update()
left_paddle = canvas.create_rectangle(0.01*(canvas.winfo_width()-4),0.4*(canvas.winfo_height()-4),(0.031*(canvas.winfo_width()-4)),0.6*(canvas.winfo_height()-4),fill="white",outline="white")
right_paddle = canvas.create_rectangle(0.969*(canvas.winfo_width()-4),0.4*(canvas.winfo_height()-4),0.99*(canvas.winfo_width()-4),0.6*(canvas.winfo_height()-4),fill="white",outline="white")
ball = canvas.create_oval((canvas.winfo_width()-4)/2,(canvas.winfo_height()-4)/2,((canvas.winfo_width()-4)/2)+(0.02*(canvas.winfo_width()-4)),((canvas.winfo_height()-4)/2)+(0.02*(canvas.winfo_width()-4)),fill="white",outline="white")


score_left,score_right = 0,0
global angle
angle = 0



pressedStatus = {"q":False,"a":False,"o":False,"l":False}
def pressed(event):
    pressedStatus[event.keysym] = True
def released(event):
    pressedStatus[event.keysym] = False
def set_bindings():
    for char in ["q","a","o","l"]:
        window.bind("<KeyPress-%s>" % char, pressed)
        window.bind("<KeyRelease-%s>" % char, released)
def movement(pressedStatus):
    if pressedStatus["q"] == True:
        if canvas.coords(left_paddle)[1] > 0:
            canvas.move(left_paddle,0,-5)
    if pressedStatus["a"] == True:
        if canvas.coords(left_paddle)[3] < canvas.winfo_height()-4:
            canvas.move(left_paddle,0,5)
    if pressedStatus["o"] == True:
        if canvas.coords(right_paddle)[1] > 0:
            canvas.move(right_paddle,0,-5)
    if pressedStatus["l"] == True:
        if canvas.coords(right_paddle)[3] < canvas.winfo_height()-4:
            canvas.move(right_paddle,0,5)
    window.update()
    window.after(10,movement,pressedStatus)
def ballmovement():
    global angle
    if 0 <= angle < 90:
        anglemovement = math.radians(90-angle)
        canvas.move(ball, 4*math.cos(anglemovement),-4*math.sin(anglemovement))#WORKS DO NOT CHANGE --- MOVEMENT
    if 90 <= angle < 180:
        anglemovement = angle-90
        anglemovement = math.radians(anglemovement)
        canvas.move(ball, 4*math.cos(anglemovement), 4*math.sin(anglemovement))
    if 180 <= angle < 270:
        anglemovement = 90-(angle-180)
        anglemovement = math.radians(anglemovement)
        canvas.move(ball,-4*math.cos(anglemovement), 4*math.sin(anglemovement))
    if 270 <= angle < 360:
        anglemovement = (angle-270)
        anglemovement = math.radians(anglemovement)
        canvas.move(ball,-4*math.cos(anglemovement),-4*math.sin(anglemovement))#WORKS DO NOT CHANGE --- MOVEMENT
    if canvas.coords(ball)[1] < 5:#WORKS DO NOT CHANGE -- WALL COLLISIONS
        if 0 < angle < 90:
            angle = 90 + (90-angle)
            canvas.move(ball,0,5)
        if 270 < angle < 360:
            angle = 270 - (angle-270)
            canvas.move(ball,0,5)
    if canvas.coords(ball)[3] > canvas.winfo_height()-9:
        if 90 < angle < 180:
            angle = 90 - (angle-90)
            canvas.move(ball, 0, -5)
        if 180 < angle < 270:
            angle = 270 + (270-angle)
            canvas.move(ball,0,-5)#WORKS DO NOT CHANGE -- WALL COLLISIONS
    if 1 in canvas.find_overlapping(*canvas.coords(ball)):#WORKS DO NOT CHANGE -- paddle collisions
        if canvas.coords(left_paddle)[1] < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(left_paddle)[1] + ((1/3)*(canvas.coords(left_paddle)[3]-canvas.coords(left_paddle)[2])):
            angle = 90 + random.randint(-45,45)
            canvas.move(ball,2,0)
        if canvas.coords(left_paddle)[1] + ((1/3)*(canvas.coords(left_paddle)[3]-canvas.coords(left_paddle)[2])) < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(left_paddle)[1] + ((2/3)*(canvas.coords(left_paddle)[3]-canvas.coords(left_paddle)[2])):
            angle = 90 + random.randint(-10,10)
            canvas.move(ball,2,0)
        if canvas.coords(left_paddle)[1] + ((2/3)*(canvas.coords(left_paddle)[3]-canvas.coords(left_paddle)[2])) < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(left_paddle)[3]:
            angle = 90 + random.randint(-45,45)
            canvas.move(ball,2,0)
    if 2 in canvas.find_overlapping(*canvas.coords(ball)):
        if canvas.coords(right_paddle)[1] < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(right_paddle)[1] + ((1/3)*(canvas.coords(right_paddle)[3]-canvas.coords(right_paddle)[2])):
            angle = 270 + random.randint(-45,45)
            canvas.move(ball,-2,0)
        if canvas.coords(right_paddle)[1] + ((1/3)*(canvas.coords(right_paddle)[3]-canvas.coords(right_paddle)[2])) < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(right_paddle)[1] + ((2/3)*(canvas.coords(right_paddle)[3]-canvas.coords(right_paddle)[2])):
            angle = 270 + random.randint(-10,10)
            canvas.move(ball,-2,0)
        if canvas.coords(right_paddle)[1] + ((2/3)*(canvas.coords(right_paddle)[3]-canvas.coords(right_paddle)[2])) < ((canvas.coords(ball)[1]+canvas.coords(ball)[3])/2) < canvas.coords(right_paddle)[3]:
            angle = 270 + random.randint(-45,45)
            canvas.move(ball,-2,0)#WORKS DO NOT CHANGE -- PADDLE COLLISIONS
    window.after(20,ballmovement)

##def score_count(score_left, score_right, direction):
##    global angle
    
##    window.after(100, score_count,score_left,score_right,direction)

set_bindings()
window.after(100,movement,pressedStatus)
direction = random.randint(1,2)
if direction == 1:
    angle = random.randint(260,280)
elif direction == 2:
    angle = random.randint(80,100)
ballmovement()
##score_count(score_left,score_right, direction)
mainloop()
