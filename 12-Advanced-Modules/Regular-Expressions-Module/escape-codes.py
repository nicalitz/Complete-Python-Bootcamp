'''
ESCAPE CODES
- special escape codes to find specific types of patterns in your data
- escapes are indicated by prefixing the characters with a backslash
- backslash itself must be escaped in normal Python strings
- using raw strings, created by prefixing the literal value with r, for creating regular expressions takes care of this problem

\d  -   digit
\D  -   non-digit
\s  -   whitespace (tab, space, newline, ect)
\S  -   non-whitespace
\w  -   alphanumeric
\W  -   non-alphanumeric

'''

import re

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns = [r'\d+',  # sequence of digits
                 r'\D+',  # sequence of non-digits
                 r'\s+',  # sequence of whitespace
                 r'\S+',  # sequence of non-whitespace
                 r'\w+',  # alphanumeric characters
                 r'\W+',  # non-alphanumeric
                 ]

for pattern in test_patterns:
    print re.findall(pattern,test_phrase)