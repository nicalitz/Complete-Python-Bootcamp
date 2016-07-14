"""
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document string (docstring) goes
    '''
    # Do stuff here
    # Return desired result


def function_name(parameters):
   '''docstring'''
   statement(s)
"""

import math

def is_prime(num):
    '''
    Naive method of checking for primes
    :param num: number to check for prime status
    :return: NONE
    '''
    for n in xrange(2,num):
        if num % n == 0:
            print 'not prime'
            break
    else:   # if never mod zero, then prime
        print 'prime'

is_prime(16)

def is_prime2(num):
    '''
    Better method of checking for primes
    :param num: number to check for prime
    :return: prime status
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print is_prime2(16)
