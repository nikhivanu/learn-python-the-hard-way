#prints Mary had a little lamb.
print("Mary had a little lamb.")
#prints Its fleece was white as snow.
#use format method to insert snow in the string
print("Its fleece was white as {}.".format('snow'))
print("." * 10) #prints . 10 times

#creating variables end1 to end12
end1 = "C"
end2 = "h"
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#watch end = ' ' at the end. try removing it to see what happens
#prints cheese burger (first print statement "cheese "- space at end instead of new line)
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)