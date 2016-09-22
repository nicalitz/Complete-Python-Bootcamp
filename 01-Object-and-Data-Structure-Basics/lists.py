my_list = [1, 4, "b", "c", 5.3]
print my_list[:2]
print my_list[2:]

my_list += ["e"]

print my_list
print my_list[5] + " " + my_list[2] + " " + my_list[3]

print my_list * 2

# Append method
my_list.append("added")
print my_list

# Pop method - Pop off an item from the list
my_list.pop(0)  # pop off item at index zero
my_list.pop()
print my_list

# Reverse method
my_list.reverse()
print my_list

# Sort method - Alphabetical for charaters, ascending for numbers
my_list.sort()
print my_list
