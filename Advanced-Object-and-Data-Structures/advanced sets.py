s = set()

# ADD
s.add(1)
s.add(2)
print s

# CLEAR
s.clear()
print s

# COPY
s = {1, 2, 3}
sc = s.copy()
print sc
s.add(4)
print sc    # note changes to the original do not affect the copy
print s

# DIFFERENCE
# syntax: set1.difference(set2)
print s.difference(sc)

# DIFFERENCE UPDATE
# syntax: set1.difference_update(set2)
# returns set1 after removing elements found in set2
s1 = {1, 2, 3}
s2 = {6, 2, 4}
s1.difference_update(s2)
print s1

# DISCARD
s.discard(2)
print s

# INTERSECTION and INTERSECTION_UPDATE
# returns intersection of two or more sets as a new set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print s1.intersection(s2)
s1.intersection_update(s2)
print s1

# ISDISJOINT
# returns True if two sets have a null intersection
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print s1.isdisjoint(s2)
print s1.isdisjoint(s3)

# ISSUBSET and ISSUPERSET
print s1.issubset(s2)
print s2.issubset(s1)
print s1.issuperset(s2)
print s2.issuperset(s1)

# SYMMETRIC_DIFFERENCE and SYMMETRIC_UPDATE
# return the symmetric difference of two sets as a new set (i.e. all elements that are in exactly one of the sets)
print s1.symmetric_difference(s2)
s2.symmetric_difference_update(s1)
print s2

# UNION
print s1.union(s2)

# UPDATE
# update set with the union of itself and others
s1.update(s2)
print s1

