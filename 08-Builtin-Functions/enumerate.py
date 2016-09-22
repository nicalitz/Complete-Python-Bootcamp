'''
Enumerate allows you to keep a count as you iterate through an object.
It does this by returning a tuple in the form (count,element).

The function self is equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
'''

lst = ['a','b','c']

for number,item in enumerate(lst):
    print number,item

for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print item