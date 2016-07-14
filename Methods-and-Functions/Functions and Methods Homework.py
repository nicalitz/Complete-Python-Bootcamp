# Write a function that computes the volume of a sphere given its radius
import math
def vol(rad):
    return (4/3) * math.pi * (rad**3)
print vol(5)


# write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        return True
    return False
print ran_check(5,6,10)
print ran_check(10,6,10)


# write a python module that accepts a string and returns the number of upper case and lower case letters
def up_low(s):
    count = {'upper':0, 'lower':0}
    for letter in s:
        if letter.islower():
            count['lower'] += 1
        elif letter.isupper():
            count['upper'] += 1
    print "Upper: ",count['upper']
    print "Lower: ",count['lower']
up_low("This is B")


# write a Python function that accepts a list and returns a new list with all the unique values
l = [1,1,1,1,2,3,3,4,4,4,5]
def unique_list(lst):
    temp = []
    for num in set(lst):
        temp += [num]
    return temp
print unique_list(l)

def unique_list2(lst):
    return list(set(lst))
print unique_list2(l)


# write a python function that multiplies all the numbers in a list
def multiply(numbers):
    mult = numbers[0]
    for num in range(1,len(numbers)):
        mult *= numbers[num]
    return mult
print multiply([1,2,3,4])


# write a Python function that checks whether a passed string is a pallendrome or not
def palindrome(s):
    test = ""
    for word in s.split():
        test += word
    if test == test[::-1]:
        return True
    else:
        return False
print palindrome("Test Files case")
print palindrome("nurses run")

# suggested solution
def palindrome_sug(s):
    s = s.replace(' ','')   #replace all spaces with no space
    return s == s[::-1]     #check through slicing
print palindrome_sug('nurses run')

# write a python function to check whether a passed string is a pangram or not (contains all letters of the alphabet)
import string

def is_pangram(s, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    alphaset.add(" ")
    return alphaset <= set(s.lower())   # determine if the string set contains each entry in the alphaset set
print is_pangram('the quick brown fox jumps over the lazy 123456789')
print is_pangram('the quick brown fox jumps over the lazy dog')
print is_pangram('thequickbrownfoxjumpsoverthelazydog!')
