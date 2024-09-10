from tkinter import *
import random, time, math

window = Tk()
canvas = Canvas(window, width = 500, height=500)
canvas.pack()

global NPCs, IDinc
NPCs = []
IDinc = 1

class objects():
    def __init__(self, canvas, ID, mass, Xpos, Ypos, veloX, veloY, drag, bounce):
        self.drag = drag
        self.canvas = canvas
        self.ID = ID
        self.mass = mass
        self.veloX = veloX
        self.veloY = veloY
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.bounce = bounce
        self.NPCbody = self.canvas.create_oval(self.Xpos-5,self.Ypos-5,self.Xpos+5,self.Ypos+5, fill="green")
        self.movement_calc()
        self.movement()


    def movement_calc(self):
        global NPCs
        for a in NPCs:
            if a.ID != self.ID:
                dispX = a.canvas.coords(a.NPCbody)[0] - self.canvas.coords(self.NPCbody)[0] # changeinX
                dispY = a.canvas.coords(a.NPCbody)[1] - self.canvas.coords(self.NPCbody)[1]# changeinY
                dispvec = ((dispX**2)+(dispY**2))**0.5 # hypotinuse of above
                dispvecF = (self.mass*a.mass)/(dispvec**2) # force due to hypotinuse
                try:
                    angle = math.atan(abs(dispY)/abs(dispX))
                except: # to stop zero division if dispX = 0
                    pass
                self.FX = math.cos(angle) * dispvecF
                self.FY = math.sin(angle) * dispvecF

                if a.canvas.coords(a.NPCbody)[0] > self.canvas.coords(self.NPCbody)[0]:
                    self.veloX += self.FX/self.mass
                else:
                    self.veloX -= self.FX/self.mass
                if a.canvas.coords(a.NPCbody)[1] > self.canvas.coords(self.NPCbody)[1]:
                    self.veloY += self.FY/self.mass
                else:
                    self.veloY -= self.FY/self.mass


                self.disX = ((self.canvas.coords(self.NPCbody)[0]+self.canvas.coords(self.NPCbody)[2])/2) - ((a.canvas.coords(a.NPCbody)[0]+a.canvas.coords(a.NPCbody)[2])/2)
                self.disY = ((self.canvas.coords(self.NPCbody)[1]+self.canvas.coords(self.NPCbody)[3])/2) - ((a.canvas.coords(a.NPCbody)[1]+a.canvas.coords(a.NPCbody)[3])/2)
                if (self.disX**2 + self.disY**2) < 225: # if the two particles hit, (the distance is smaller than 15)
                    self.check_collision(a)


        self.veloX = self.veloX * self.drag
        self.veloY = self.veloY * self.drag # simulates drag so that there is not infinite motion
        
        if self.canvas.coords(self.NPCbody)[0] < 0: # if the ball hits the side of a wall
            while self.canvas.coords(self.NPCbody)[0] < 0:
                self.canvas.move(self.NPCbody,10,0)
            self.veloX = -1*self.veloX
        if self.canvas.coords(self.NPCbody)[2] > self.canvas.winfo_width()-4:
            while self.canvas.coords(self.NPCbody)[2] > self.canvas.winfo_width()-4:
                self.canvas.move(self.NPCbody,-10,0)
            self.veloX = -1*self.veloX
        if self.canvas.coords(self.NPCbody)[1] < 0:
            while self.canvas.coords(self.NPCbody)[1] < 0:
                self.canvas.move(self.NPCbody,0,10)
            self.veloY = -1*self.veloY
        if self.canvas.coords(self.NPCbody)[3] > self.canvas.winfo_height()-4:
            while self.canvas.coords(self.NPCbody)[3] > self.canvas.winfo_height()-4:
                self.canvas.move(self.NPCbody,0,-10)
            self.veloY = -1*self.veloY

        window.after(50, self.movement_calc)

    def movement(self):
        self.canvas.move(self.NPCbody, self.veloX, self.veloY)
        window.after(50, self.movement)

    def check_collision(self, a):
        self.angle = math.atan(abs(self.veloX)/abs(self.veloY))
        print(self.angle/math.pi*180)
        
        



def mouseclick(event):
    global IDinc
    NPCs.append(objects(canvas,IDinc,1000,event.x, event.y,0,0,0.9,random.randint(0,1)))
    IDinc += 1

window.bind("<Button-1>", mouseclick)
        
mainloop()
