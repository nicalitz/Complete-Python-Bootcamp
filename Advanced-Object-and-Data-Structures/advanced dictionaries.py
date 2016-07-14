d = {'k1': 1, 'k2': 2}

# DICTIONARY COMPREHENSION
print {x:x**2 for x in range(1,5)}


# ITERATION OVER KEYS, VALUES AND ITEMS
for key in d.iterkeys():
    print key

for value in d.itervalues():
    print value

for item in d.iteritems():
    print item


# VIEW KEYS, VALUES AND ITEMS
print d.viewkeys()
print d.viewvalues()
print d.viewitems()