test_val = 0

# Loops support using else statements

while test_val < 3:  # the else statement is executed when the while condition becomes false
    print test_val
    test_val += 1
else:
    print 'Finished'

for k in range(1, 5):
    for i in (1, 2, 3):  # the else statement is executed when the for loop has exhausted iterating the list
        if i == k:
            print '%d - True' % (k)
            break
    else:
        print '%d - False' % (k)