str = 'this is a string'

for letter in str:
    print letter

# notice the special property of using tuples in a for loop
t = ((1,2),(3,4),(5,6))

for tup in t:
    print tup

for (t1,t2) in t:   # here we can access individual elements of a tuple
    print t1

d = {'key1': 1, 'key2': 2,'key3': 3}

for item in d:
    print item  # notice: only the keys are printed

# PYTHON 2: iteritems()

for j,k in d.iteritems():   # d.iteritems() creates a generator
    print '{a} , {b}'.format(a=j,b=k)
    print '{0} , {1}'.format(j,k)
    print '%s , %d' %(j,k)

"""
# PYTHON 3: items()

for j,k in d.items():
    print ('{0} , {1}'.format(j,k))
"""

test_val = 0

# Loops support using else statements

while test_val < 3: # the else statement is executed when the while condition becomes false
    print test_val
    test_val += 1
else:
    print 'Finished'

for k in range(1,5):
    for i in (1,2,3):  # the else statement is executed when the for loop has exhausted iterating the list
        if i == k:
            print '%d - True' %(k)
            break
    else:
        print '%d - False' %(k)

