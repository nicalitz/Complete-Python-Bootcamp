# sets are an unordered collection of unique elements
x = set()
x.add(1)
print x

x.add(2)
x.add(1)    #note that, since the value 1 is already in the set, the contents of x will remain unchanged
print x

l = [1,2,2,3,3,4,4,4,5,6]
print set(l)    #notice that the duplicated are removed

# Boolean: We can use the placeholder NONE for a variable we don't want to asign yet
test = None

