# empty list
numbers = []

def fill_list(numbers, count):
    i = 0
    while i < count:
        print(f"At the top i is {i}")
        # adds i to end of list
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

count = int(input("Please enter a number of elements: "))
fill_list(numbers, count)