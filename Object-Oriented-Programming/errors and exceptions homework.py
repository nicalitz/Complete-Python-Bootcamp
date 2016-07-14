from __future__ import print_function

# PROBLEM 1:
# Handle the exception thrown by the code below by using try and except blocks

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Power of a string literal not supported")


# PROBLEM 2:
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Division by zero not allowed. ",end='')
finally:
    print("All done")


# PROBLEM 3:
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():
    while True:
        num = raw_input("Please enter an integer: ")
        try:
            num = int(num)
        except ValueError:
            print("You did not enter an integer!")
            continue
        else:
            print(num**2)
            break

ask()