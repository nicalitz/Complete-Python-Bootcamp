from __future__ import print_function,division

# PROBLEM 1:
# Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line
class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())



# From answers
class Line2(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1))/(x2-x1)



# Test
class Line3(object):

    def __init__(self,coor1,coor2):
        self.x1,self.y1 = coor1
        self.x2,self.y2 = coor2

    def distance(self):
        return ( (self.x2-self.x1)**2 + (self.y2-self.y1)**2 )**0.5

    def slope(self):
        return float((self.y2-self.y1))/(self.x2-self.x1)

li = Line3(coordinate1,coordinate2)

print(li.distance())
print(li.slope())