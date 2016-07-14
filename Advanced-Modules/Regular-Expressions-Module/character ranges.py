'''
CHARACTER RANGES
- define a character set to include all of the contiguous characters between a start and stop point
- format:  [start-end]
- eg: [a-f] would return matches with any instance of letters between a and f
'''

import re

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = ['[a-z]+',          # sequences of lower case letters
                 '[A-Z]+',          # sequences of upper case letters
                 '[a-zA-Z]+',       # sequences of lower or upper case letters
                 '[A-Z][a-z]+']     # one upper case letter followed by lower case letters

for pattern in test_patterns:
    print re.findall(pattern,test_phrase)