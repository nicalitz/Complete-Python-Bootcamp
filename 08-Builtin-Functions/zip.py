# coding=utf-8
'''
zip() makes an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument
sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single
iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

zip() is equivalent to:

def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values
from the longer iterables.
'''

x = [1,2,3]
y = [4,5,6]
print zip(x,y)

x = [1,2,3]
y = [4,5,6,7,8]
print zip(x,y)  #zip stops when the shortest iterable is exhausted

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
print zip(d1,d2)
print zip(d1,d2.itervalues())


# switch the keys and values of two dictionaries
def switch(d1,d2):
    dout = {}

    for d1key,d2value in zip(d1,d2.itervalues()):
        dout[d1key] = d2value

    return dout

print switch(d1,d2)