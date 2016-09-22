'''
The collections module is a built-in module that implements specialized container datatypes providing alternatives to
Python's general purpose built-in containers
'''

# standard tuple uses numerical indices to access its members

t = (12,13,14)
print t[1]

'''
For simple use cases, this is usually enough. On the other hand, remembering which index should be used for each
value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used.
A namedtuple assigns names, as well as the numerical index, to each member.

Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function.
The arguments are the name of the new class and a string containing the names of the elements.

You can think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.
'''

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')
sam = Dog(age = 2, breed = 'Lab', name='Sammy')
frank = Dog(age = 2, breed = 'Shepard', name = 'Frankie')

print "sam: ",sam
print "sam.age: ",sam.age
print "frank.breed: ",frank.breed
print "sam[0]: ",sam[0]