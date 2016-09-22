'''
REGULAR EXPRESSIONS:
- text matching patterns described with a formal syntax
- 'regex' or 'regexp'
- can include a variety of rules for finding repetition, text-matching, ect.
- a lot of parsing problems can be solved with regular expressions
'''

# SEARCHING FOR PATTERNS IN TEXT
import re

# List of patterns to search for
patterns = [ 'term1', 'term2' ]

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print 'Searching for "%s" in: \n"%s"' % (pattern, text),

    #Check for match
    if re.search(pattern, text):
        print '\n'
        print 'Match was found. \n'
    else:
        print '\n'
        print 'No Match was found.\n'

# RETURN TYPE: Match object (None if no match was found)
pattern = 'term1'
text = 'This is a string with term1, but it does not have the other term.'
match = re.search(pattern, text)
print type(match)   #returns a Match object

# Match object returned by search() is more than just a Boolean or None
print match.start()
print match.end()



# SPLIT WITH REGULAR EXPRESSIONS
split_term = '@'
phrase = 'What is the domain name of someone with the email: hello@gmail.com'
print re.split(split_term, phrase)



# FIND ALL INSTANCES OF A PATTERN
print re.findall('match','test phrase match is in middle')