'''
PYTHON 3: filter returns an iterable, not a list as in python 2. Use list() if required

Syntax:   filter(function,sequence)

filter returns all elements in the sequence iterable for which the function returns True
'''

lst = range(10)

print filter(lambda x: x%2==0, lst)     # return all even numbers
print filter(lambda x: x>3, lst)        # return all numbers greater than 3