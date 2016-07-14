'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

def prime_factor(num):
    for n in xrange(2,int(num**0.5)):
        if num % n == 0:
            return '{0} x {1}'.format(str(n),prime_factor(num/n))
    return str(num)


def is_prime(num):
    for n in range(2,int(num**0.5)):
        if num%n == 0:
            return False
    return True

print prime_factor(104534534572)
print is_prime(2011)