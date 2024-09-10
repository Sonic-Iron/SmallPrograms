from tkinter import *
from tkinter import Image, ImageTk
import random




windom= Tk()
canvas = Canvas(width = 1000, height = 500)
#sidebar_left =
#sidebar_right =
mS = Image.open('./englandnorthseaimage.svg')
mSI = ImageTk.PhotoImage(mS)
mapimage = Label(image=mSI)
mapimage.image = mSI
mapimage.pack()

canvas.pack()
