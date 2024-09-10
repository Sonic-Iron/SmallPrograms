import random
from tkinter import *
window = Tk()



rock_button = Button(window, text="rock", justify = LEFT,command = lambda: play("rock")).pack()
paper_button = Button(window, text="paper", justify = LEFT, command = lambda: play("paper")).pack()
scissors_button = Button(window, text = "scissors", justify = LEFT, command = lambda: play("scissors")).pack()
file = open("./playermoves.txt","w")
file.close()


def play(player_hand):
    if player_hand == "rock":
        print("rock")
        file = open("./playermoves.txt","a")
        file.write("rock:")
        file.close()
    if player_hand == "paper":
        print("paper")
        file = open("./playermoves.txt","a")
        file.write("paper:")
        file.close()
    if player_hand == "scissors":
        print("scissors")
        file = open("./playermoves.txt","a")
        file.write("scissors:")
        file.close()
    file = open("./playermoves.txt","r")
    player_moves = []
    for a in file.readlines():
        player_moves.append(a)
        a.split(":")

    #CPU_move = max(rock_moves,paper_moves,scissors_moves)
    #print(CPU_move)
        


 

window.mainloop()
