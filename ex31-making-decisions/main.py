print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
        print("""You're now roaming the building as a spirit. You find paths 1 and 2. 
        Which one do you want to follow?""")
        ghost = input(">")

        if ghost == "1":
            print("You found another player in the maze to mess with.")

        elif ghost == "2":
            print("You found a ghost puppy.")    

        else:
            print("You posess someone.")
        
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")


elif door == "2":
    print("You stare into the endless abyss at Cthulhus retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")