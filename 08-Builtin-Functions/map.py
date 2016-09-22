'''
PYTHON 3: map returns an iterable, not a list as in python 2. Use list() if required

Syntax:   map(function,sequence)

map subjects each element in the sequence to the specified function, and returns the results in the form of a list
'''

# NOTE:  map(F, S) can almost always be written as [F(x) for x in S] -> lambda is slower than list comprehension

def farenheit(T):
    return (9.0/5)*T + 32

temps = [0, 22.5, 40, 100]

print map(farenheit, temps)      # notice that the function is not passed with parentheses

print map(lambda T: (9.0/5)*T + 32, temps)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print map(lambda x, y, z: x+y+z, a, b, c)     # lambda function can use muliple arguments