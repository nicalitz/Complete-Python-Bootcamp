from __future__ import print_function

# PROBLEM 1:
# Create a generator that generates the squares of numbers up to some number N
def gen_square(num):
    for n in range(num):
        yield n**2

new = gen_square(5)
for _ in range(5):
    print(next(new),end=' ')
print('\n')



# PROBLEM 2:
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
from random import randint

def rand_nums(n,low,high):
    for num in range(n):
        yield randint(low,high)

rand = rand_nums(5,2,9)
for _ in range(5):
    print(next(rand),end=' ')
print('\n')



# PROBLEM 3:
# Use the iter() function to convert the string below
s = 'hello'
s_gen = iter(s)
for letter in s_gen:
    print(letter,end='')
print('\n')



# PROBLEM 4:
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

# When iterating over a large range of numbers. Would require much less memory



# PROBLEM 5 (Extra):
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture!)
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# Generator expressions are high performance, memory efficient generalization fo list comprehensions and generators
# see 'generator expressions.py'