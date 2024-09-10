import random, time
from tkinter import *

class GUI():
    def __init__(self):
        window2 = Tk()
        self.window2 = window2
        self.label = Label(self.window2, text = "For the graph use ** instead of ^ for powers")
        self.label.pack()
        self.window2.update()
        self.colours = ["black","red","yellow","green","orange","blue"]
        self.colour_choice = 0
        self.blankgraph()
    def blankgraph(self):
        window = Tk()
        self.window = window
        self.canvas = Canvas(self.window, width = 500, height=500)
        self.canvas.pack()
        self.canvas.create_line(250,0,250,500)
        self.canvas.create_line(0,250,500,250)
        self.input_entry = Entry(self.window)
        self.input_entry.pack()
        self.input_button = Button(self.window, text="Enter graph", command = self.input_graph)
        self.input_button.pack(side=TOP)

    def input_graph(self):
        self.graph = self.input_entry.get()
        if self.graph == "":
            self.window.destroy()
            self.blankgraph()
        else:
            print(self.graph)
            self.colour_choice = self.colour_choice + 1
            if self.colour_choice == len(self.colours):
                self.colour_choice = 0
            for x in range(-250,250):
                point1 = 0.01*eval(self.graph)
                x = x + 1
                point2 = 0.01*eval(self.graph)
                x = x - 1
                self.canvas.create_line(x+250,500-(point1+250),x+251,500-(point2+250), fill=self.colours[self.colour_choice])
                #self.canvas.create_oval((10*x)+250,500-(((eval(self.graph))+250)),(10*x)+251,500-((eval(self.graph)+251)), fill=self.colours[self.colour_choice])
GUI()
mainloop()
