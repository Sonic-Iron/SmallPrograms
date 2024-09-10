import random
from tkinter import *

class chess():
    def __init__(self):
        window = Tk()
        self.window = window
        self.canvas = Canvas(window, height=920, width=1000)
        self.responcetexttext = StringVar()
        self.responcetexttext.set("Whites Turn")
        self.responcetext = Label(self.window, textvariable=self.responcetexttext)
        self.whiteEntry = Entry(self.window)
        self.blackEntry = Entry(self.window)
        self.blackEntryButton = Button(self.window, text="Enter for black", command= lambda: self.main_black())
        self.whiteEntryButton = Button(self.window, text="Enter for white", command= lambda: self.main_white())
        self.responcetext.pack(side=TOP)
        self.blackEntry.pack(side=RIGHT)
        self.blackEntryButton.pack(side=RIGHT)
        self.whiteEntry.pack(side=RIGHT)
        self.whiteEntryButton.pack(side=RIGHT)
        self.turn = "white"
        self.canvas.pack()


        for a in range(9):
            self.canvas.create_line(75,(75*(a+1)),675,(75*(a+1)))   #horizontal lines
        for a in range(9):
            self.canvas.create_line((75*(a+1)),75,(75*(a+1)),675)
        self.canvas.create_text(370,65,text="A                    B                          C                        D                          E                        F                    G                   H")
        self.canvas.create_text(65,112,text="1")
        self.canvas.create_text(65,197,text="2")
        self.canvas.create_text(65,272,text="3")
        self.canvas.create_text(65,347,text="4")
        self.canvas.create_text(65,422,text="5")
        self.canvas.create_text(65,497,text="6")
        self.canvas.create_text(65,572,text="7")
        self.canvas.create_text(65,647,text="8")
        


        
        #black pieces
        self.picturebpwn = PhotoImage(file='black_pwn.gif')
        self.b_pwn1 = self.canvas.create_image(112,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        picvar1 = self.picturebpwn
        self.b_pwn2 = self.canvas.create_image(187,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn3 = self.canvas.create_image(262,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn4 = self.canvas.create_image(337,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn5 = self.canvas.create_image(412,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn6 = self.canvas.create_image(487,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn7 = self.canvas.create_image(562,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.b_pwn8 = self.canvas.create_image(637,187, image=self.picturebpwn,tag=("piece","black","black_pwn"))
        self.picturebking = PhotoImage(file='black_king.gif')
        self.b_king = self.canvas.create_image(340,115, image=self.picturebking,tag=("piece","black","black_king"))
        picvar2 = self.picturebking
        self.picturebroot= PhotoImage(file='')
        self.piece_pos_x = {"A":75,"B":150,"C":225,"D":300,"E":375,"F":450,"G":525,"H":600}
        self.piece_pos_y = {"1":75,"2":150,"3":225,"4":300,"5":375,"6":450,"7":525,"8":600}
               
    def main_white(self):
        if self.turn == "white":
            self.turn = "black"
            self.whitego = self.whiteEntry.get()
            try:
                self.tomove,self.moveto = self.whitego.split("-")
            except:
                self.responcetexttext.set("Thats not a valid move, blacks' go")
                return
            poss_pieces = []
            for a in self.canvas.find_withtag("piece"):
                if self.piece_pos_x[self.tomove[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.tomove[0]]+75:
                    if self.piece_pos_y[self.tomove[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.tomove[1]]+75:
                        if a in self.canvas.find_withtag("white"):
                            poss_pieces.append(a)
            if len(poss_pieces) == 0:
                self.responcetexttext.set("Thats not a valid move, blacks go")
            else:
                self.poss_piece = poss_pieces[0]
                if self.poss_piece in self.canvas.find_withtag("white_pwn"):
                    self.white_pwn()
                elif self.poss_piece in self.canvas.find_withtag("white_rook"):
                    #self.white_rook()
                    pass
        else:
            pass
        
    def white_pwn(self):
        print("This works")


    def main_black(self):
        if self.turn == "black":
            self.turn = "white"
            self.blackgo = self.blackEntry.get()
            try:
                self.tomove,self.moveto = self.blackgo.split("-")
            except:
                self.responcetexttext.set("That's not a valid move, whites' go")
            poss_pieces = []
            for a in self.canvas.find_withtag("piece"):
                if self.piece_pos_x[self.tomove[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.tomove[0]]+75:
                    if self.piece_pos_y[self.tomove[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.tomove[1]]+75:
                        if a in self.canvas.find_withtag("black"):
                            poss_pieces.append(a)
            if len(poss_pieces) == 0:
                self.responcetexttext.set("That's not a valid move, whites' go")
            else:
                self.real_piece = poss_pieces[0]
                if self.real_piece in self.canvas.find_withtag("black_pwn"):
                    self.black_pwn()
                elif self.real_piece in self.canvas.find_withtag("black_king"):
                    self.black_king()

    

    def black_pwn(self):
        for a in self.canvas.find_withtag("black"):
            if self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75:
                if self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75:
                    self.responcetexttext.set("That's not a valid move, whites' turn")
                    return
        if self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 0:
            if 150 < self.canvas.coords(self.real_piece)[1] < 225:
                if self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 150:
                    self.canvas.move(self.real_piece, 0, 150)
                elif self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 75:
                    self.canvas.move(self.real_piece, 0, 75)
            else:
                if self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 75:
                    self.canvas.move(self.real_piece, 0, 75)
                else:
                    self.responcetexttext.set("That's not a valid move, whites' go")
        elif self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == (-75 or 75):
            if self.piece_pos_y[self.moveto[1]] - self.piece_pos_x[self.tomove[0]] == 75:
                for a in self.canvas.find_withtag("white"):
                    if self.piece_pos_x[self.moveto[0]]< self.canvas.coords(a) < self.piece_pos_x[self.moveto[0]] + 75:
                        self.canvas.move(self.real_piece, 75,75)
                        self.a.destroy()
                    elif self.piece_pos_x[self.moveto[0]] < self.canvas.coords < self.piece_pos_x[self.moveto[0]] + 75:
                        self.canvas.move(self.real_piece, -75, 75)
                        self.a.destroy()
            else:
                self.responcetexttext.set("That's not a valid move, whites' go")
        if self.piece_pos_y[self.moveto[1]] < self.canvas.coords(self.real_piece)[1] < self.piece_pos_y[self.moveto[1]] + 75:
            pass ### add the pawn --> queen thing here

    def black_king(self):
        moved = False
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 0):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, 75, 0)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 0) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, 0, 75)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == -75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 0):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, -75, 0)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 0) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == -75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, 0, -75)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, 75, 75)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == 75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == -75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, 75, -75)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == -75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == -75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, -75, -75)
            moved = True
        if (self.piece_pos_x[self.moveto[0]] - self.piece_pos_x[self.tomove[0]] == -75) and (self.piece_pos_y[self.moveto[1]] - self.piece_pos_y[self.tomove[1]] == 75):
            for a in self.canvas.find_withtag("black"):
                if (self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]] + 75) and (self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]] + 75):
                    self.responcetexttext.set("That's not a valid move, whites' go")
                    return()
            self.canvas.move(self.real_piece, -75, 75)
            moved = True
        if moved == True:
            for a in self.canvas.find_withtag("white"):
                print(a)
                if self.piece_pos_x[self.moveto[0]] < self.canvas.coords(a)[0] < self.piece_pos_x[self.moveto[0]]+75:
                    if self.piece_pos_y[self.moveto[1]] < self.canvas.coords(a)[1] < self.piece_pos_y[self.moveto[1]]+75:
                        self.canvas.delete(a)

    def black_rook(self):
        pass
        
        








chess()
mainloop()

