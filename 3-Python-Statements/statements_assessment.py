st = 'Print only the words that start with s in this sentence'

# Use for, split(), and if to create a Statement that will print out words that start with 's':
st = st.split()
for item in st:
    if item[0] == 's':
        print item

# Use range() to print all the even numbers from 0 to 10.
print [x for x in xrange(11) if x%2 == 0]
print range(0,11,2)

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisble by 3.
div3 = [x for x in xrange(1,51) if x%3==0]
print div3

# Go through the string below and if the length of a word is even print "even!"
lst = []
st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
for word in st:
    if len(word)%2==0:
        lst.append(word)
print lst


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
lst2 = []
for num in xrange(1,101):
    if num%3 == 0 and num%5 == 0:
        lst2.append("FizzBuzz")
    elif num%3 == 0:
        lst2.append("Fizz")
    elif num%5 == 0:
        lst2.append("Buzz")
    else:
        lst2.append(num)
print lst2

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
lst3 = [x[0] for x in st.split()]
print lst3

