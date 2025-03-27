# inheritance indicates that one class gets most of its features
# from a parent class

# actions on a child class override the parent
# actions on the child alter the action on the parent
# actions on the child imply an action on the parent

# implicit inheritance

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")

# tells python that you want an empty block
# creates a class named child while saying theres nothing
# new to add to it
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# override explicitly

# has function named override in both classes
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

# runs parent.override function 
dad.override()
# runs child.override function bc son is an instance of child
# child overrides that function by defining its own version
son.override()

# Alter before or after

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")

        # aware of inheritance and gets parent class for you
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# all three combined 

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        
        # aware of inheritance and gets parent class for you
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.altered()
son.altered()

# multiple inheritance is when you define a class that inherits
# from one or more classes 

# composition
# just using other classes and modiles
# rather than relying on implicit inhereitance 
# calling functions in a module to replicate 
# exploiting inheritance
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

# not using name parent since there is no parent-child
# relationship instead theres a has-a relationship
son = Child()
son.implicit()
son.override()
son.altered()