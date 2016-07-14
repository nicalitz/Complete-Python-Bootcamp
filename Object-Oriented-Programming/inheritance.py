# INHERITANCE:
# Form new classes using classes that have already been defined
# The newly formed classes are called derived classes
# The classes we derive from are called base classes
# Benefits of inheritance: code reuse and reduction of complexity
# The derived classes (descendants) override or extend the functionality of base classes (ancestors)


class Animal(object):           #Animal is the base class
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):              #Dog is the derived class - derives the functionality of the case class
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):           #Derived class modifies the existing behaviour of the base class
        print "Dog"

    def bark(self):             #Derived class extends the functionality of the base class
        print "Woof!"

d = Dog()
d.whoAmI()
d.eat()
d.bark()