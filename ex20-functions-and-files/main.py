from sys import argv

script, input_file = argv

#prints all lines in input file
def print_all(f):
    print(f.read())

#changes position of file handle to 0
def rewind(f):
    f.seek(0)

#prints each line with the line number in front
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

#calling print all function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#calling rewind function
rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)