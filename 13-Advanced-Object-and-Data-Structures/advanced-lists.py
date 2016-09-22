ls = [1, 2, 3]

# COUNT
# count() takes an element and returns the number of times it occurs in the list
print ls.count(2)

# APPEND
# appends object to the end of list
ls.append([1, 2])
print ls
ls.pop()

# EXTEND
# extend list by appending elements from an iterable
ls.extend([1, 2])
print ls

# INDEX
# return the index of whatever element is placed as an argument
print ls.index(2)

# INSERT  -  insert(index, object)
# places object at the index supplied
ls.insert(2, 'bacon')
ls.insert(4, 'fish')
print ls

# POP
ls.pop()    # pops last value in list
ls.pop(2)   # pops value at index 2
print ls

# REMOVE
# removes the first occurance of value
ls.remove('fish')
print ls

# REVERSE
# reverse list
ls.reverse()
print ls

# SORT
# sort in place
ls.sort()
print ls
