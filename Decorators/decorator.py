'''
Decorators can be thought of as functions which modify the functionality of another function.
They help to make your code shorter and mote "Pythonic".
'''

def decorate_function(func):
    def wrap_func():
        print "This goes before the function"
        func()
        print "This goes after the function"
    return wrap_func        #NB: not returned with parentheses. function is not called, rather returned and assigned

def basic_function():
    print "BASIC FUNCTION EXECUTED"

basic_function()

basic_function = decorate_function(basic_function)
#basic_function()
