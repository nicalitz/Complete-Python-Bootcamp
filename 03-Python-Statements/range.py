x = range(0, 10)
print type(x), x

'''
notice that the range function stores the values in memory as a list

when using for loops in python 2, the function xrange() should rather be used. xrange() creates a generator, only providing
each value in the for loop as it is needed

in python 3, the range() function serves as generator in a for loop
'''

for i in xrange(0, 5):
    print i
