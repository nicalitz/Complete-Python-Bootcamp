'''
module: timeit
'''
import timeit

# for loop
print 'For Loop: ',timeit.timeit('".".join(str(n) for n in range(100))',number=10000)

# list comprehension
print 'List Comprehension: ',timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)

# map()
print 'Map(): ',timeit.timeit('"-".join(map(str,range(100)))',number=10000)

# NB: see iPython implementation of %timeit funtion