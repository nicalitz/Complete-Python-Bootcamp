def func():
    return 1
print func()

s = 'Global Variable'

def func_locals():
    print locals()

# Local and global variables can be determined using the locals() and globals() functions

print 'Global variable keys:  ',globals().keys()
print 'Value of global variable at key "s":  ',globals()['s']

print func_locals()


# Remember: EVERYTHING in Python is an object

def hello(name='Nico'):
    print 'Hello '+name
hello()
greet = hello       #notice no parentheses. the function hello is not called, rather just assigned to the greet variable
print type(greet)   #greet is now a function

del hello
greet()             #the existance of the greet() function is not dependant on that of the hello() function

# FUNCTIONS INSIDE FUNCTIONS:
def new_hello(name='Nico'):
    print 'The hello() function has been executed'

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print greet()
    print welcome()
    print "Now we are back inside the hello() function"

new_hello()

# RETURNING FUNCTIONS
def final_hello(name='Nico'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Nico':
        return greet
    else:
        return welcome
x = final_hello()
y = final_hello('Bacon')

print x()       #assigned the greet() function
print y()       #assigned the welcome() function

# FUNCTIONS AS ARGUMENTS
def this_hello():
    return 'Hi Nico!'

def other(func):
    print 'Other code would go here'
    print func()

print this_hello()
print other(this_hello)