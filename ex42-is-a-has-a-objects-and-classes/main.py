## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is-a subclass of animal class
## dog inherits the animal classes properties
class Dog(Animal):

    def __init__(self, name):
        ## the dogs name is assigned to the instance variable name
        self.name = name

## cat is-a subclass of animal class
# cat also inherits the animal classes properties
class Cat(Animal):

    def __init__(self, name):
        ## the cats name gets assigned to instance variable name
        self.name = name
## person is a class 
class Person(object):

    def __init__(self, name):
        ## assigns persons name to variable name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is a subclass of the class person
class Employee(Person):

    def __init__(self, name, salary):
        ## calling __init__ function of person
        # this is to make sure the employee class inherits
        # the persons name
        #  hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## assigns employees salary to instance variable salary
        self.salary = salary

## fish is an animal object
class Fish(object):
    pass

## salmon is an object that is also a fish object
class Salmon(Fish):
    pass

## halibut is an object that is also a fish object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## sparkle is-a cat
sparkle = Cat("Sparkle")

## mary is-a person
mary = Person("Mary")

## mary's pet is a cat object named sparkle
mary.pet = sparkle

## frank is an employee with a salary of 120000
frank = Employee("Frank", 120000)

## franks pet is-a dog object named rover
frank.pet = rover

## flipper is an instance of fish

flipper = Fish()

## crouse is an instance of the salmon subclass
crouse = Salmon()

## harry is an instance of te halibut subclass 
harry = Halibut()

