# creates a variable called car and assigns the value 100
cars = 100
# creates a variable called space_in_a_car and assigns it 4.0
# float is better since integers round down
space_in_a_car = 4.0
# creates a variable called drivers = 30
drivers = 30
# creates a variable called passengers and assigns it 90
passengers = 90
# creates a variable called cars_not_driven and assigns it the difference between car and drivers
cars_not_driven = cars - drivers
# creates a variable called cars_driven and assigns it drivers
cars_driven = drivers
# creates a variable called carpool_capacity and assigns it the result of cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# creates a variable called average_passengers_per_car which equals passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

# prints number of cars available
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# user didn't define the variable before calling it
# 