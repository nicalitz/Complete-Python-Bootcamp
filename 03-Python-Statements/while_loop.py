'''
break = breaks out of the closest enclosing loop
continue = goes to the top of the closest enclosing loop
pass = does nothing at all
'''

test_val = 0

while test_val < 10:
    if test_val in (1,2,3):
        test_val += 1
        continue            # returns to the top of the while loop
    elif test_val == 7:
        break               # ends/breaks the while loop
    print test_val
    test_val += 1