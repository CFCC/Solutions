done = False
# Generating the rooms using description, then rooms in NESW order
room_list = []
room = ["A small bedroom, there is a door to the east.", None, 1, None, None]
room_list.append(room)
room = ["A hallway, there is are doors to the east and west.  The hallway continues to the north", 4, 2, None, 0]
room_list.append(room)
room = ["A dining room that seats 6, there is an exit to the west.", None, None, None, 1]
room_list.append(room)
room = ["A Master Bedroom, there is a door to the east", None, 4, None, None]
room_list.append(room)
room = ["A hallway, there are doors to the north, east, and west.  The hallway continues south.", 6, 5, 1, 3]
room_list.append(room)
room = ["A fancy kitchen, there is a door to the west.", None, None, None, 4]
room_list.append(room)
room = ["You are on a balcony. A magnificent view of the gardens below dances in the morning light.", None, None, 4,
        None]
room_list.append(room)

current_room = 0
print()
print("Welcome to Test Adventure Game.  You may move (N)orth (E)ast (S)outh and (W)est.  Type (Q)uit to quit")
print()

while not done:
    print(room_list[current_room][0])
    user_input = input("Which way do you go?  Options: N/E/S/W ")
    '''
    Evaluates User Input to determine which way to move the player.
    Uses the array portions from setting up rooms.
    '''
    if user_input.upper() == "N" or user_input.upper() == "NORTH":
        if room_list[current_room][1] is None:
            print("You can't go that way.")
        else:
            current_room = room_list[current_room][1]
    elif user_input.upper() == "E" or user_input.upper() == "EAST":
        if room_list[current_room][2] is None:
            print("You can't go that way.")
        else:
            current_room = room_list[current_room][2]
    elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
        if room_list[current_room][3] is None:
            print("You can't go that way.")
        else:
            current_room = room_list[current_room][3]
    elif user_input.upper() == "W" or user_input.upper() == "WEST":
        if room_list[current_room][4] is None:
            print("You can't go that way.")
        else:
            current_room = room_list[current_room][4]
    elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
        print("Thank you for playing, please play again.")
        done = True
    else:
        print("I'm sorry, I didn't quite get that, please try again.")
