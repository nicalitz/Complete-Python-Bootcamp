'''
CHARACTER SETS
- used to match any one of a group of characters at a point in the input
- brackets are used to construct character set inputs
- eg: the input [ab] searches for occurances of either a or b
'''

import re

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

patterns = ['[sd]',     # either s or d
            's[sd]+']   # s followed by one or more s or d

for pattern in patterns:
    print 'Searching phrase with re statement: '+pattern
    print re.findall(pattern,test_phrase)
    print '\n'