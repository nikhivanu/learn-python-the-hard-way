from sys import exit

#user enters the gold room
def gold_room():
    print("This room is full of gold. How much do you take?")

    # taking user input as a string
    choice = input("> ")
    # if the user input has a 1 or a 0 in it then convert to int
    # and set to variable how_much
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        # if number does not contain either of those
        # kills user
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        just_kidding()
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear? (you can steal the honey or taunt the bear)")
    # by default bear is in users way
    bear_moved = False

    #while loop will keep running until user is either dead
    # or if they exit the room
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")   

def cthulhu_room():
    print("Here you see the great evil Cthulhu.") 
    print("He, it, whatever stares at you and you insane.") 
    print("Do you flee for your life or eat your head?") 

    # takes user input
    choice = input("> ") 

    # if else statements based off of users input
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!") 
    else:
        cthulhu_room()

def just_kidding():
    print("Haha, you thought it was over?")
    print("You have one more game to complete.")
    print("Select one of the doors: triangle, circle, or square?")

    choice = input("> ")
    if "triangle" in choice:
        print("You've escaped the building congrats!")
        exit()
    elif "square" in choice:
        dead("You're back in the room with the bear.")
    elif "circle" in choice:
        print("You're stuck in the building congrats!")
    else:
        dead("You can't follow instructions?")
        
# dead function exits the game
def dead(why):
    print(why, "Good job!") 
    exit(0)

# starts game
def start(): 
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.") 
# calls start game function
start()    
        
    
