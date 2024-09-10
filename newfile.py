from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100,bd=0,highlightthickness=0)
w.configure(bg="black")
w.pack()

w.create_line(0, 0, 200, 100, fill="red")
w.create_line(0, 100, 200, 0, fill="red")
master.mainloop()
