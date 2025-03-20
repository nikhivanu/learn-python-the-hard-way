ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# this splits ten_things into elements for a list named stuff
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while length of stuff is under 10
while len(stuff) != 10:
    # variable named next_one takes element from more_stuff
    # then it pops that element from more_stuff
    # more_stuff.pop() call pop on more stuff
    # pop(more_stuff) call pop with argument more_stuff
    # the above two are the same thing
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # adds next_one to end of list stuff
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

# prints changed list- stuff
print("There we go", stuff)

print("Let's do some things with stuff.")

# prints element 2 in stuff
print(stuff[1])
# prints the last element of stuff
print(stuff[-1]) 
# prints last element of stuff and removes it
# pop(stuff) call pop with argument stuff
# stuff.pop call pop on stuff
print(stuff.pop())
# prints elements of list stuff with only spaces between them
# join(stuff) call join on stuff
print(' '.join(stuff))
# prints the 4th element (index 0) joined with:
# the 6th element (index 5) with a hash between them
print('#'.join(stuff[3:5]))