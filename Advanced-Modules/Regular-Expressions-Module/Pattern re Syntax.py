'''
Use metacharacters along with re to find specific types of patterns

Repetition Syntax:
1. A pattern followed by the metacharacter * is repeated zero or more times.
2. Replace the * with + and the pattern must appear at least once.
3. Using ? means the pattern appears zero or one time.
4. For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times the pattern should repeat.
5. Use {m,n} where m is the minimum number of repetitions and n is the maximum. Leaving out n ({m,}) means the value appears at least m times, with no maximum.
'''

import re

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' %pattern
        print re.findall(pattern,phrase)
        print '\n'

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',         # s followed by zero or more d's
                 'sd+',          # s followed by one or more d's
                 'sd?',          # s followed by zero or one d's
                 'sd{3}',        # s followed by three d's
                 'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)