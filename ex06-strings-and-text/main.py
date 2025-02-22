# creates an int variable called types_of_people
types_of_people = 10

#creates a string variable called x
x = f"There are {types_of_people} types of people"

#creates a string variable called binary
binary = "binary"
#creates a string variable called do_not
do_not = "don't"
#creates a variable y and assigning it a format string
y = f"Those who know {binary} and those who {do_not}."

#prints variable x
print(x)
#prints variable y
print(y)

#prints a format string that takes the variable x
print(f"I said: {x}")   
# I said: There are 10 types of people

#prints a format string that takes the value of y
print(f"I also said: '{y}'") 
# I also said: 'Those who know binary and those who don't.'

#creates the boolean variable hilarious
hilarious = False
#using .format to finish a string then assign to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}" 

#prints joke_evaluation.format and takes hilarious 
print(joke_evaluation.format(hilarious))
# Isn't that joke so funny?! False

#creates a variable w
w = "This is the left side of..."
#creates a variable e
e = "a string with a right side."

#concatenates and prints the strings 
print(w+e)
# This is the left side of...a string with a right side.