# METHODS:
# Functions defined inside the body of a class
# Used to perform operations with the attributes of our objects
# Think of methods as functions acting on an Object that take the Object itself into account through its self argument

class Circle(object):
    pi = 3.14

    # Circle get instantiaed with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius

c = Circle()

c.setRadius(2)
print 'Radius is: ',c.getRadius()
print 'Area is: ',c.area()
