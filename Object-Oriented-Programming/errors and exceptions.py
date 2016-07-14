'''
try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block.
'''

try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then excute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written succesfully"
   f.close()


try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then excute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written succesfully"
   f.close()


'''
FINALLY: block of code that with always be run regardless if there was an exception in the try block code

try:
   Code block here
   ...
   Due to any exception, this code may be skipped!
finally:
   This code block would always be executed.
'''

def askint():
    while True:
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you did not enter an integer!"
            continue
        else:
            print 'Yep thats an integer!'
            break
        finally:
            print "Finally, I executed!"
        print val

askint()