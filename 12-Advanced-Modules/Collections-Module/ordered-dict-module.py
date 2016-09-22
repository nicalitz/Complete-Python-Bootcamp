'''
The collections module is a built-in module that implements specialized container datatypes providing alternatives to
Python's general purpose built-in containers
'''

# ORDEREDDICT:
# an OrderedDict is a dictionary subclass that remembers the order in which its contents were added

from collections import OrderedDict

print "Normal Dictionary:"

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for key,value in d.items():
    print key, value

print ""

print "Ordered Dictionary:"

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for key,value in d.items():
    print key, value

print ""

# Equality with an ordered dictionary
# a regular dict looks at its contents when testing for equality. an ordered dict also considers the order in which
# the items were added

print "Normal dictionaries are equal?"

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print ""

print "Orderd dictionaries are equal?"

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

