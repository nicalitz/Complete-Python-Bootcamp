# CLASS
# user defined object are created using the class keyword
# from classes we create instances (specific object created from a particular class)

class Sample(object):   # by convention class names start with a capital letter
    pass

# instance of sample
x = Sample()

print type(x)




# ATTRIBUTES
# attributes are charateristics of an object
# syntax:    self.attribute = something
# special method used to initialize attributes:    __init__()

class Dog(object):
    species = 'mammal'   # class object attribute (same for any instance of class)
    def __init__(self, breed, name):   # called automatically after object has been created
        self.breed = breed   # each attribute in a class defenition begins with a reference to the instance object (by convention named self)
        self.name = name

sam = Dog(breed='Lab', name='Sam')
print sam.breed   # note no parentheses (attributes dont take arguments)
print sam.name




# METHODS
# functions defined inside the body of a class
# perform operations with the attributes of an object

class Circle(object):
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius * Circle.pi)

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

c = Circle()
c.setRadius(2)
print 'Radius is: ', c.getRadius()
print 'Area is: ', c.area()




# INHERITANCE
# way to form new classes using classes that have already been defined
# newly formed classes are called derived classes
# derived classes (descendants) override or extend the functionality of base classes (ancestors)

class Animal(object):
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "Woof!"

dog = Dog()   # note that the print statements of both the Animal and Dog classes are executed (functionality extended)
dog.whoAmI()    # overwrites functionality
dog.bark()   # extends functionality
dog.eat()   # inherits functionality




# SPECIAL METHODS
# these methods are not called directly but by Python specific language syntax

class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):   # called when print Book_instance is executed
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):   # called when len(Book_instance) is executed
        return self.pages

    def __del__(self):  # called when an instance of the Book class is destroyed
        print "A book is destroyed"

book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print book
print len(book)
del book
