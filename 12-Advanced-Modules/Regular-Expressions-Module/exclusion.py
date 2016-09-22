'''
EXCLUSION
- use ^ to exclude terms by incorporating it into the brackets syntax notation
- eg: [^...] will match any single character not in the bracket notation
'''

import re

test_phrase = 'This is a string! But it has punctutation. How can we remove it?'

print ' '.join(re.findall('[^!.? ]+',test_phrase))
print re.findall('[^!.? ]+',test_phrase)

