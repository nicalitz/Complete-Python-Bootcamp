'''
all() and any() are built-in functions in Python that allow us to convienently check for boolean matching in an
iterable. all() will return True if all elements in an iterable are True. It is the same as this function code:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

any() will return True if any of the elements in the iterable are True. It is equivalent to the following funciton code:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''


lst = [True,True,False,True]
print all(lst)
print any(lst)