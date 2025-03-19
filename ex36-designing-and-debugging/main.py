from sys import exit

def puppy_room():
    print("You walk into a room filled with puppies.")
    print("While you're distracted playing with the dogs.")
    print("The killer slips in the room.")
    print("Fight him or no? y or n")
    choice = input(">")
    if choice == "y":
        dead("KO")
    elif choice == "n":
        balcony()
    else:
        dead("Too slow")


def plant_room():
    print("A sunroom room full of plants. ")
    print("You find a door to the backyard")
    backyard()
    

def kitty_room():
    print("Nice! you walked into a room with a lion in it")
    dead("The lion ate you.")

# user input taken as a choice
def balcony():
    print("Nice, you've made it to the balcony.")
    print("Jump or climb the roof?")
    choice = input("> ")

    if choice == "jump":
        dead("You broke your leg and the killer got you.")
    elif choice == "climb the roof":
        print("Nice. You climb a tree.")
        backyard()
    else:
        dead("Too slow. The killer got you")

def backyard():
    print("Looks like you've found the backyard garden.")
    print("You hop the fence and escape.")
    exit()


def dead(reason):
    print(reason, "rip")
    exit(0)

# start of game function definition
def escape_the_slasher():
    print("You've been planted inside an old mansion.")
    print("Good luck getting out.")
    print("You see 3 doors, which one do you take?")
    print("There are doors with pictures of a plant, dog, and cat")

    choice = input("> ")

    # checking users input
    # if they choose wrong they get a second chance
    if choice == "plant":
        plant_room()

    elif choice == "dog":
        puppy_room()
    elif choice == "cat":
        kitty_room()
    else:
        print("You hear footsteps")
        print("The killers getting closer. Quick! choose a room")
        input("> ")
        if choice == "plant":
            plant_room()
        elif choice == "dog":
            puppy_room()
        elif choice == "cat":
            kitty_room()
        else:
            dead("You were too slow.")

# starts game
escape_the_slasher()