# create a mapping of state to abbreviation

states = {
    'Oregon' : 'OR',
    'Florida': "FL",
    'California': 'CA',
    'New York': 'NY', 
    'Michigan': 'MI', 
    # practicing
    'North Carolina' : 'NC',
    'Georgia': 'GA'
}

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    # practicing
    'NC': 'Charlotte',
    'GA': 'Atlanta'
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# trying it out
cities['NC'] = 'Charlotte'

# print out some cities
print('-' * 10)
# prints out NY State has: and pulls the cities from NY
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
# trying it out
print("North Carolina's abbreviation is: ", states['North Carolina'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
# trying it out
print("North Carolina has: ", cities[states['North Carolina']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the same city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

# if that state does not exist in the dictionary then it will 
# print "Sorry, no Texas" 
if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")