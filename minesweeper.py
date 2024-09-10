from tkinter import *
import random
size = 16
grid = []
for a in range(size):
    grid.append([])
    for b in range(size):
        grid[a].append("")



for a in range(round(len(grid)*0.35*size)):
    x = random.randint(0,size-1)
    y = random.randint(0,size-1)
    if grid[y][x] == "*":
        while grid[y][x] == "*":
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)
    else:
        grid[y][x] = "*"
print(grid)
    
for a in range(len(grid)):
    for b in range(len(grid[a])):
        bombs_surrounding = 0
        if grid[a][b] == "*":
            pass
        else:
            try:
                if grid[a][b-1] == "*":
                    if b <= 0:
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a][b+1] == "*":
                    if b>=(size-1):
                        pass
                    else:
                        bombs_surrounding += 1

            except:
                pass
            try:
                if grid[a-1][b-1] == "*":
                    if (a<=0) or (b<=0):
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a-1][b] == "*":
                    if a<=0:
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a-1][b+1] == "*":
                    if (a<=0) or (b >= size-1):
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a+1][b-1] == "*":
                    if (a>=(size-1)) or (b <= 0):
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a+1][b] == "*":
                    if a>=(size-1):
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            try:
                if grid[a+1][b+1] == "*":
                    if (a>=(size-1)) or (b>=(size-1)):
                        pass
                    else:
                        bombs_surrounding += 1
            except:
                pass
            grid[a][b] = str(bombs_surrounding)


class GUI():
    def __init__(self,grid):
        self.window = Tk()
        self.grid = grid
        self.button_grid = []
        self.button_text_grid = []
        for a in range(len(self.grid)):
            self.button_grid.append([])
        for a in range(len(self.grid)):    
            for b in range(len(self.grid[a])):
                self.button_grid[a].append("")
                
        for a in range(len(self.grid)):
            self.button_text_grid.append([])
        for a in range(len(self.grid)):    
            for b in range(len(self.grid[a])):
                self.button_text_grid[a].append("")# creates a text_grid from the grid

        for a in range(len(self.button_text_grid)):
            for b in range(len(self.button_text_grid[a])):
                self.button_text_grid[a][b] = StringVar()
                self.button_text_grid[a][b].set("")
                
        for a in range(len(self.button_grid)):
            for b in range(len(self.button_grid[a])):
                self.button_grid[a][b] = Button(self.window, textvariable=self.button_text_grid[a][b], height = 2, width = 4, command = lambda row = a, column = b : self.show_button(row,column))
                self.button_grid[a][b].bind("<Button-3>",lambda event, a = a, b=b : self.plant_flag(a,b))
                self.button_grid[a][b].grid(row=a, column=b)


    def show_button(self,row,column):
        self.button_text_grid[row][column].set(self.grid[row][column])
        if self.grid[row][column] == "*":
            for row in range(len(self.grid)):
                for column in range(len(self.grid)):
                    self.button_text_grid[row][column].set(self.grid[row][column])
            self.window.update()
            self.window.after(5000)
            stop_window = Tk()
            stop_label = Label(stop_window, text="Whoops! You hit a mine!")
            stop_window.update()
            stop_label.pack()
            self.window.destroy()
        elif self.grid[row][column] != "0":
            pass
        else:
            pass


    def plant_flag(self,row,column):
        if self.button_text_grid[row][column].get() == "!":
            self.button_text_grid[row][column].set("?")
        elif self.button_text_grid[row][column].get() == "?":
            self.button_text_grid[row][column].set("")
        elif self.button_text_grid[row][column].get() == "":
            self.button_text_grid[row][column].set("!")
        else:
            pass
            
            
                            
            
            





GUI(grid)
                    
