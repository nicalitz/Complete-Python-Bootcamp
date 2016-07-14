'''
the lambda expression allows us to create "anonymous" functions

lambda's body is a single expression, not a block of statements

For a great breakdown of the lambda expression:
https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
'''

def square1(num):
    result = num**2
    return result

def square2(num):
    return num**2

def square3(num): return num**2     # this is the form that the lambda expression intends to replicate

print square1(2),square2(2),square3(2)

# Determine the square using a lambda function
square = lambda num: num**2
print type(square)  # note that the variable square is assigned a function
print square(2)

# Determine if a number is even
even = lambda x: x%2==0
print even(2), even(3)

# Return the first letter of a string
first = lambda s: s[0]
print first("Hello")

# Reverse a string
rev = lambda s: s[::-1]
print rev("Hello")

# We can accept more than one function in the lambda expression
adder = lambda x,y: x+y
print adder(2,4)
