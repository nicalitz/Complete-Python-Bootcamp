'''
The collections module is a built-in module that implements specialized container datatypes providing alternatives to
Python's general purpose built-in containers
'''

# COUNTER
# dict subclass which helps count hashable objects
# elements are stored as dictionary keys and counts of the object are stored as the value

from collections import Counter

l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print Counter(l)

s = 'aaaabffkdlssjdoedfssd'
print Counter(s)

words = 'How many times does each word show up in this sentence word times each each word'
print Counter(words.split())

print ""

# Methods with counter:
c = Counter(words.split())
print "Two most common words: ",c.most_common(2)
print "Sum of all counts: ",sum(c.values())
print "List unique elements: ",list(c)
print "Converts to a set: ",set(c)
print "Converts to a regular dictionary: ",dict(c)
print "Convert to a list of (elem,cnt) pairs: ",c.items()
print "Convert from a list of (elem,cnt) pairs: Counter(dict(list_of_pairs)))"
print "3 least common elements: ",c.most_common()[:-4:-1]
print "Remove zero and negative counts: c+= Counter()"