import random, time
from tkinter import *


window = Tk()
window.title("AdventureGameGUI")

class locations():
    def __init__(self, name, description, objects_in_building, directions):
        self.name = name
        self.desciption = description
        self.objects_in_building = objects_in_building
        self.directions = directions


Portal = locations("Portal","A large area of nothing, a door hovers in the air", " ",["House","House2","House3"])
   

inventory = ("Brick")
drop_buttons = Frame(window)
pickup_buttons = Frame(window)

################################# tkinter variables ###############
canvas = Canvas(window, height = 500, width = 500).pack(side = LEFT)
input_entry = Entry(window)

inventory_button = Button(window, text="Inventory", command = lambda: check_inventory())

move_button = Button(window, text="move", command = lambda: move_part1())

drop_button = Button(window, text = "drop", command = lambda: drop_item())

pick_up_button = Button(window, text = "pick up item", command = lambda: pick_up_item())

output_text = StringVar()
look_button = Button(window, text="look", command = lambda: look())

output_text_label = Label(window, textvariable=output_text)

gointeger = IntVar()
input_button = Button(window, text="ENTER", command = lambda: gointeger.set(1))

################################ other varibles ################################

current_location = Portal
move_function_running = False
################################### main #####################

input_entry.pack()
inventory_button.pack(side=RIGHT)
move_button.pack(side = RIGHT)
drop_button.pack(side=RIGHT)
pick_up_button.pack(side=RIGHT)
look_button.pack(side=RIGHT)
output_text_label.pack(side = BOTTOM)
input_button.pack(side=TOP)


    

def check_inventory():
    ""

def move_part1():
    global database, current_location
    input_entry.pack()
    inventory_button.pack_forget()
    move_button.pack_forget()
    drop_button.pack_forget()
    pick_up_button.pack_forget()
    look_button.pack_forget()
    output_text_label.pack_forget()
    input_button.pack_forget()

    directiontogo = StringVar()
    for a in current_location.directions:
        buttonname = a
        newbuttonname = buttonname
        newbuttonname = Button(window, text=a, command= move_part2(buttonname))
        newbuttonname.pack()


def move_part2(buttonname):
    print(buttonname)
    
        



        
    

mainloop()
