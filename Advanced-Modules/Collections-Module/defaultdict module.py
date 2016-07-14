'''
The collections module is a built-in module that implements specialized container datatypes providing alternatives to
Python's general purpose built-in containers
'''

# DEFAULTDICT:
# dictionary like object which provides all methods provided by dictionary but takes first argument (default_factory)
# as default datatype for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method

from collections import defaultdict

d = {}
#print d['one']    #KeyError

# a defaultdict will never raise a KeyError
# any key that does not exist gets the value returned by the default factory

d = defaultdict(object)
print d['one']

for item in d:
    print item

# defaultdict can also initialize with default values
d = defaultdict(lambda: 0)
print d['one']