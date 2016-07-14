# CLASS:
# User defined objects are created using the class keyword
# The class is a blueprint that defines the nature of a future object
# From classes we can construct instances

class Sample(object):   #create a new object type called Sample
    pass

x = Sample()            #create an instance of Sample

print type(x)           #<class '__main__.Sample'>



# ATTRIBUTES:
# An attribute is a characteristic of an object
# The syntax for creating an attribute is:  [self.attribute = something]
# Special method __init__() is called when a class is instantiated - Used to initialize the attributes of an object

class Dog(object):                  #create a new object type called Dog
    species = 'mammal'              #class object attribute: same for any instance of the class

    def __init__(self,breed,name):  #each method in a class definition begins with a reference to the instance object (by convention named self)
        self.breed = breed
        self.name = name

sam = Dog(breed='Lab',name='Sam')
frank = Dog('Huskie','Frank')

print sam.breed     #note no parenthesis, since attributes don't take arguments
print frank.name
print frank.species