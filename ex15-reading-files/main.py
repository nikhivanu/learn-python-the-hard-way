#using argv to get a filename 
from sys import argv

script, filename = argv

#command called open 
#it takes a parameter and returns a value you can set to
#your own variable 
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())