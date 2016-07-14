'''
module: datetime

- helps you deal with timestamps in your code
- time values are represented with the time class
- times have attributes for hours, minutes, seconds and microseconds
- can also include timezone information
- the arguments to initialize a time instance is optional (defaults to zero)

'''

# TIME
import datetime

t = datetime.time(4, 20, 1)

print t
print 'hour: ',t.hour
print 'minute: ',t.minute
print 'second: ',t.second
print 'microsecond: ',t.microsecond
print 'time zone info: ',t.tzinfo

# note: a time instance holds only the values of time, and not the date associated with that time

# check the min and max values a time of day can have in the module
print 'earliest: ',datetime.time.min
print 'latest: ',datetime.time.max
print 'resolution: ',datetime.time.resolution



# DATES
# - calendar date values are represented with the date class
# - instances have attributes for year, month and day

today = datetime.date.today()
print today
print 'ctime: ',today.ctime()
print 'tuple: ',today.timetuple()
print 'ordinal:', today.toordinal()
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day

# check the min and max values a date can have in the module
print 'earliest: ',datetime.date.min
print 'latest: ',datetime.date.max
print 'resolution: ',datetime.date.resolution

# another way to create new date instances is to use the replace() method of an existing date
d1 = datetime.date(2015,3,11)
print 'd1: ',d1
d2 = d1.replace(year=1990)
print 'd2: ',d2



# ARITHMETIC

print 'd1-d2: ',d1-d2