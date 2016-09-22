# grab every letter in a string
lst1 = [x for x in 'word']
print lst1

# square numbers in range and turn into list
lst2 = [x**2 for x in range(1, 6)]
print lst2

# add if statements
lst3 = [x for x in range(11) if x % 2 == 0]
print lst3

# nested list comprehension
lst4 = [x**2 for x in [x**2 for x in range(1, 6)]]
print lst4

# perform complicated arithmetic
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [(32 + temp * (float(9) / 5)) for temp in celsius]
print fahrenheit