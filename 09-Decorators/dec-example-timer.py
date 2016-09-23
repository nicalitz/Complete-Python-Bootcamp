# usefull example of how to use decorator
# decorator prints the execution time of the wrapped function

import time


def timerWrapper(func):
    def executionTime(str):
        t0 = time.time()
        func(str)
        t1 = time.time()
        print "Execution time: ", t0-t1
    return executionTime

@timerWrapper
def printText(str):
    print str

printText('This is some random text to print')