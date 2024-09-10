from tkinter import *

window = Tk()
canvas = Canvas(window, width = 500, height=500)
canvas.pack()
global densities
densities = {"air":1}

class object_create():
    def __init__(self, canvas, size, mass):
        self.canvas = canvas
        self.size = size
        self.mass = mass
        self.object_name = self.canvas.create_rectangle(0,0,self.size,self.size)
        self.acc_y = 0
        self.acc_x = 0
        self.velo_x = 0
        self.velo_y = 0
        self.velocity_calculate()

    def accelerate(self, force_x, force_y):
        global densities
        self.acc_x = self.acc_x + (force_x/self.mass)
        self.acc_y =  self.acc_y + (force_y/self.mass)
        

    def velocity_calculate(self):
        drag_x = 0.5 * densities["air"] * ((self.velo_x)**2) * (self.size**2)
        drag_y = 0.5 * densities["air"] * ((self.velo_y)**2) * (self.size**2)
        self.velo_x = self.velo_x + (self.acc_x) - (drag_x/self.mass)
        self.velo_y = self.velo_y + (self.acc_y) + 0.1 - (drag_y/self.mass)
        self.canvas.move(self.object_name,self.velo_x,-1*self.velo_y)
        print(self.velo_x,self.velo_y)
        window.after(1, self.velocity_calculate)

guy = object_create(canvas, 10, 1)
sam = object_create(canvas, 20, 5)

while True:
    guy.accelerate(0,0)
    sam.accelerate(0,0)
    window.update()
mainloop()
