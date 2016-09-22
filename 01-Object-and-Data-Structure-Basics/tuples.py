# Tuples are similar to list, but immutable

t = (1, 2, 3, 4, 5, 1, 2, 3)   # t[0] = 5 would produce an error

print len(t)
print t
print t[0]
print t[-1]
print t[::-1]

# Tuples methods
print t.index(2)    # Return the index of a value
print t.count(2)    # Counts the number of times a value appears
