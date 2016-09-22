# the following summation code will build a full list of squares in memory, iterate over those values, and, when
# the reference is no longer needed, delete the list

print sum([x*x for x in range(10)])

# Memory is conserved by using a generator expression instead:

print sum(x*x for x in range(10))