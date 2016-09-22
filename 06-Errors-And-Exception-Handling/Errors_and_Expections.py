
''' SYNTAX:

try:
   You do your operations here...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
else:
   If there is no exception then execute this block.
finally:
    This code block would always be executed.
'''


def askint():
    while True:   # notice the use of a while loop to keep prompting
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