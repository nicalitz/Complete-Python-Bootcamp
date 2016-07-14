s = 'hello world'

# CHANGE CASE
print s.capitalize()    # capitalize the word in string
print s.upper()
print s.lower()


# LOCATION AND COUNTING
print s.count('o')
print s.find('o')


# FORMATTING
print s.center(20,'-')
print 'hello\thi'.expandtabs()


t = 'hello'

# IS CHECK METHODS
print t.isalnum()       # return True if all characters are alphanumeric
print t.isalpha()       # return True if all characters are alphabetic
print t.islower()       # return True if all cased characters are lowercase and there is at least one cased character
print t.isupper()       # return True if all cased characters are uppercase and there is at least one cased character
print t.isspace()       # return True if all character are whitespace
print t.istitle()       # return True if t is a Titlecased string (uppercase character follow uncased characters, lowercase characters only cased ones)
print t.endswith('o')   # boolean check on t[-1]


# BUILT-IN REG EXPRESSIONS
print s.split('e')
print s.partition('e')  # return tuple that includes separator (first occurence)

