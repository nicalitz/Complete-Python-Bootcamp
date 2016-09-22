'''
PYTHON 3: reduce returns an iterable (use list() if required). import from functools

Syntax:   reduce(function,sequence)

reduce the elements in the sequence to a single value by iteratively applying the specified function
'''

list = [4,56,23,453,666,23,6789,34]

print reduce(lambda a,b: a if (a>b) else b,list)    # find the maximum value of a list