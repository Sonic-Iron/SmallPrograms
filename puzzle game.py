import time, random

admin = True


print("\t \t \t Welcome to [puzzle game]")

player_name = input("What is your name?")
location = [["*","*","*","*","*"],
            ["1","*","*","*","*"],
            ["*","*","*","*","*"],
            ["*","*","*","*","*"],
            ["*","*","*","*","*"],]
#player stats
level = 1
xp = 0
#door variables
door_x = random.randint(0,4)
door_y = random.randint(0,4)
if admin == True: print("across:",door_x,"down:",door_y)

print(location[0],"\n",location[1],"\n",location[2],"\n",location[3],"\n",location[4],"\n")

player_location_x = 0
player_location_y = 1
while True:
    if level > 1:
        print("\n\n\t\t\tYou move down to the next level")
        print()
        print(location[0],"\n",location[1],"\n",location[2],"\n",location[3],"\n",location[4],"\n")
        door_x = random.randint(0,4)
        door_y = random.randint(0,4)
        if admin == True: print("across:",door_x,"down:",door_y)
    
    while True:
        move = input("In which direction would you like to move?, up [u], down [d], left [l], or right [r]")
        if move.upper() == "U":
            if (player_location_y - 1) < 0:
                print("You cannot move upwards")
            else:
                location[player_location_y][player_location_x] = "*"
                location[player_location_y-1][player_location_x] = "1"
                player_location_y -= 1
        if move.upper() == "D":
            if (player_location_y + 1) > 4:
                print("You cannot move downwards")
            else:
                location[player_location_y][player_location_x] = "*"
                location[player_location_y+1][player_location_x] = "1"
                player_location_y += 1
        if move.upper() == "L":
            if (player_location_x - 1) < 0:
                print("You cannot move left")
            else:
                location[player_location_y][player_location_x] = "*"
                location[player_location_y][player_location_x-1] = "1"
                player_location_x -= 1
        if move.upper() == "R":
            if (player_location_x + 1) > 4:
                print("You cannot move right")
            else:
                location[player_location_y][player_location_x] = "*"
                location[player_location_y][player_location_x+1] = "1"
                player_location_x += 1

        if (player_location_y == door_y) and (player_location_x == door_x):
            downwards = input("Would you like to enter the next level of the puzzle maze? , Yes /  No")
            if downwards == "Yes":
                level += 1
                location[player_location_y][player_location_x] = "*"
                location[0][0] = "1"
                player_location_x = 0
                player_location_y = 0
                break
            else:
                print("You move away from the door but stay in the room")
                
      #  if (player_location_y == magic_y) and (player_location_x == magic_x):
       #     power = random.choice(power_pool)
            

        print(location[0],"\n",location[1],"\n",location[2],"\n",location[3],"\n",location[4],"\n")
        print()


