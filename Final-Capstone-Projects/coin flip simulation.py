from random import randint

num_flips = 100
result = [randint(0,1) for _ in range(num_flips)]
print 'Heads: {0} ; Tails: {1}'.format(result.count(1),result.count(0))