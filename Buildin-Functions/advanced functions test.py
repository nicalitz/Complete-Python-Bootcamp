'''
For this test, you should use the built-in functions to be able to write the requested functions in one line.
'''

# PROBLEM 1:
# Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return
# the values in a list.The function will have an input of a string, and output a list of integers.

str = "This is bacon"
len_words = map(lambda x: len(x),str.split())
print len_words
len_words_solution = map(len,str.split())
print len_words_solution

# PROBLEM 2:
# Use reduce to take a list of digits and return the number that they correspond to.
# Do not convert the integers to strings!

num_list = [1,2,3,4,5]
num = reduce(lambda x,y: x*10+y,num_list)
print num

# PROBLEM 3:
# Use filter to return the words from a list of words which start with a target letter.

words = ['this','cow','fat','chicken','seen','cat']
c_words = filter(lambda x: x[0] == 'c', words)
print c_words

# PROBLEM 4:
# Use zip and list comprehension to return a list of the same length where each value is the two strings
# from L1 and L2 concatenated together with connector between them. Look at the example output below:

def concatenate(l1,l2,connector):
    return [x+connector+y for x,y in zip(l1,l2)]
print concatenate(['get','you'],['mad','skank'],'-')

# PROBLEM 5:
# Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index
# as the value. You may assume that a value will only appear once in the given list.

def swop_list(l):
    dout = {}
    for key,value in enumerate(l):
        dout[value] = key
    return dout
print swop_list(['a','b','c'])

lst = ['a','b','c']
dict_list = {key:value for value,key in enumerate(lst)}
print dict_list

# PROBLEM 6:
# Use enumerate and other skills from above to return the count of the number of items in the list
# whose value equals its index.

lst = [0,1,3,4,5,5]
eq_index = len(filter(lambda x: x[0]==x[1],enumerate(lst)))
print eq_index
eq_index_solution = len([num for count,num in enumerate(lst) if num == count])
print eq_index_solution

