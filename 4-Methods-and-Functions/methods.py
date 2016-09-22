'''
Methods are essentially functions build into objects

Methods are in the form:
    object.method(arg1,arg2,etc...)

You'll later see that we can think of methods as having an argument 'self' referring to the object itself.
You can't see this argument but we will be using it later on in the course during the OOP lectures.
'''

l = [1, 2, 3, 4, 5]

# append() allows us to add elements to the list
l.append(6)
print l

# count() will count the number of occurrences of an element in the list
print l.count(2)

# extend list by appending items from an iterable
l.extend(x for x in range(7, 11))
print l

# insert object before index
l.insert(2, 'insert')
print l

# remove and return item at index (default last item)
print l.pop()
print l.pop(2)
print l

# remove first occurance of a value (returns ValueError if value not present)
l.remove(5)
print l

try:
    l.remove(5)
except ValueError:
    print 'Value not present'

# reverse in place
l.reverse()
print l

# l.sort(cmp=None, key=None, reverse=False)
l.sort()
print l
l.sort(reverse=True)
print l
