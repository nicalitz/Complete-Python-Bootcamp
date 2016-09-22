'''
The idea of scope can be described by 3 general rules:
1. Name assignments will create or change local names by default
2. Name references search (at most) four scopes, these are:
    - local
    - enclosing functions
    - global
    - built-in
3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes
'''


# Local - Names assigned in any way within a function (def or lambda), and not declared global in that function
f = lambda x: x**2


# Enclosing function locals - Name in scope of any and all enclosing functions (def and lambda), from inner to outer
name = "this is a global name"

def greet():
    # enclosing function
    name = "sammy"

    def hello():
        print 'Hello '+name
    hello()
greet()


# Global (module) - Name assigned at the top level of a module file, or declared global in a def within the file
print name


# Built-in (python) - Names preassigned in the built-in names module: open,range,SyntaxError,...
print type(len)


# Local variables
x = 20
def changeX(x):
    print "x is ",x
    x = 50
    print "changed x to ",x
changeX(x)
print "x is still ",x


# Global statement
x = 50
def func():
    global x
    print 'This function is now using the global x!'
    print 'Because of global x is: ', x
    x = 2
    print 'Ran func(), changed global x to', x

print 'Before calling func(), x is: ', x
func()
print 'Value of x (outside of func()) is: ', x