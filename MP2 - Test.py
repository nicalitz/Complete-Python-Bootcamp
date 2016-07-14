import itertools

suits = ['Diamonds','Clubs','Hearts','Spades']
deck = list(itertools.product(range(1,11),suits)) + list(itertools.product(['Jack','Queen','King'],suits))
