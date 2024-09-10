from tkinter import *
import random

class chess():
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, height=810,width=810)
        self.canvas.pack()
        for x in range(8):
            for y in range(8):
                self.canvas.create_rectangle(100+(50*x),100+(50*y),100+(50*(x+1)),150+(50*y), activefill="yellow")
        
        self.picturebpwn = PhotoImage(file='black_pwn.gif')
        self.b_pwn1 = self.canvas.create_image(125,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        picvar1 = self.picturebpwn
        self.b_pwn2 = self.canvas.create_image(175,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn3 = self.canvas.create_image(225,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn4 = self.canvas.create_image(275,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn5 = self.canvas.create_image(325,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn6 = self.canvas.create_image(375,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn7 = self.canvas.create_image(425,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn8 = self.canvas.create_image(475,175, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.picturebking = PhotoImage(file='black_king.gif')
        self.b_king = self.canvas.create_image(325,125, image=self.picturebking,tag=("piece","black","black_king"))
        picvar2 = self.picturebking


        label = Label()
        label2 = Label()
        label.image = self.picturebpwn
        label2.image = self.picturebking  # these are used to store the images of the pieces

        self.turn = "black"

        self.window.bind("<Button-1>",self.getorigin)
        self.window.bind("<Button-3>",self.getorigin2)

    def main(self):
        pass
        try:
            int(self.mouse_first_x)
        except:
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn
            return
        
        if 100 < self.mouse_first_x < 150:
            self.x1 = 1
        elif 150 < self.mouse_first_x < 200:
            self.x1 = 2
        elif 200 < self.mouse_first_x < 250:
            self.x1 = 3
        elif 250 < self.mouse_first_x < 300:
            self.x1 = 4
        elif 300 < self.mouse_first_x < 350:
            self.x1 = 5
        elif 350 < self.mouse_first_x < 400:
            self.x1 = 6
        elif 400 < self.mouse_first_x < 450:
            self.x1 = 7
        elif 450 < self.mouse_first_x < 500:
            self.x1 = 8
            
        if 100 < self.mouse_first_y < 150:
            self.y1 = 1
        elif 150 < self.mouse_first_y < 200:
            self.y1 = 2
        elif 200 < self.mouse_first_y < 250:
            self.y1 = 3
        elif 250 < self.mouse_first_y < 300:
            self.y1 = 4
        elif 300 < self.mouse_first_y < 350:
            self.y1 = 5
        elif 350 < self.mouse_first_y < 400:
            self.y1 = 6
        elif 400 < self.mouse_first_y < 450:
            self.y1 = 7
        elif 450 < self.mouse_first_y < 500:
            self.y1 = 8

        if 100 < self.mouse_second_x < 150:
            self.x2 = 1
        elif 150 < self.mouse_second_x < 200:
            self.x2 = 2
        elif 200 < self.mouse_second_x < 250:
            self.x2 = 3
        elif 250 < self.mouse_second_x < 300:
            self.x2 = 4
        elif 300 < self.mouse_second_x < 350:
            self.x2 = 5
        elif 350 < self.mouse_second_x < 400:
            self.x2 = 6
        elif 400 < self.mouse_second_x < 450:
            self.x2 = 7
        elif 450 < self.mouse_second_x < 500:
            self.x2 = 8

        if 100 < self.mouse_second_y < 150:
            self.y2 = 1
        elif 150 < self.mouse_second_y < 200:
            self.y2 = 2
        elif 200 < self.mouse_second_y < 250:
            self.y2 = 3
        elif 250 < self.mouse_second_y < 300:
            self.y2 = 4
        elif 300 < self.mouse_second_y < 350:
            self.y2 = 5
        elif 350 < self.mouse_second_y < 400:
            self.y2 = 6
        elif 400 < self.mouse_second_y < 450:
            self.y2 = 7
        elif 450 < self.mouse_second_y < 500:
            self.y2 = 8

            

        
        if self.turn == "black":
            for a in self.canvas.find_withtag("black"):
                if 100+((self.x1-1)*50) < self.canvas.coords(a)[0] < 150+((self.x1-1)*50):
                    if 100+((self.y1-1)*50) < self.canvas.coords(a)[1] < 150+((self.y1-1)*50):
                        self.real_piece = a
            print(self.canvas.coords(self.real_piece))
            if self.real_piece in self.canvas.find_withtag("black_pwn"):
                self.Black_Pwns()
                

    def Black_Pwns(self):
        if 150 < self.canvas.coords(self.real_piece)[1] < 200:
            if self.y2 - self.y2 == 50:
                if self.x2 - self.x1 == 0:
                    self.canvas.move(self.real_piece,0,50)
            elif self.y2 - self.y1 == 100:
                if self.x2 - self.x1 == 0:
                    self.canvas.move(self.real_piece,0,100)


    def getorigin(self, eventorigin):
        self.mouse_first_x = eventorigin.x
        self.mouse_first_y = eventorigin.y
        return
    
    def getorigin2(self, eventorigin):
        self.mouse_second_x = eventorigin.x
        self.mouse_second_y = eventorigin.y
        self.main()
        return
    
    
        


        
chess()
mainloop()
