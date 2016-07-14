'''
Generator Functions:
- Allows us to write a function that can send back a value and then later resume to pick up where it left off.
- Syntax: yield statement
- When compiled, generators become objects that support an iteration protocol
- Automatically suspends and resumes their execution and state around the last point of value generation
- Instead of having to compute an entire series of values upfront and the generator functions can be suspended
- Known as state suspension
'''

# Generator function for the cube of numbers (power of 3)
def gencubes(num):
    for num in range(num):
        yield num**3

for x in gencubes(10):
    print x

# Generators are best for calculating large sets of results (particularly in calculations that involve loops
# themselves) in cases where we don't want to allocate the memory for all of the results at the same time.

print "\n"

# next() and iter() built-in functions:
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print next(g)
print next(g)
print next(g)
# print next(g)   #error: StopIteration

# Lets see how to use iter(). Remember that strings are iterables:
s = 'hello'

#Iterate over string
for let in s:
    print let

# That doesn't meen that the string itself is an iterator!!
# next(s)   #produces an error

# the string object supports iterator, but is not itself an iterator. this is were iter() comes into play
s_iter = iter(s)
print next(s_iter)

