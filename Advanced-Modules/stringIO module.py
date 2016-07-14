'''
STRINGIO:
- implements an in-memory file like object
- this object can be used in input or output to most functions that would expect a standard file object
- especially useful in web scraping cases where you want to read some string you scraped as a file
'''

import StringIO

message = 'This is just a normal string'
f = StringIO.StringIO(message)  # Use StringIO method to set as file object

print f.read()

f.write(' Second line written to file like object')
f.seek(0)
print f.read()