# Floating point numbers
print "Num: %1.2f" %(13.114)
print "Num: %1.0f" %(13.114)
print "Num: %1.5f" %(13.114)
print "Num: %10.2f" %(13.114)
print "Num: %25.2f" %(13.114)

# Conversion format methods:
# %s and %r actually convert any python object to a string using two seperate methods: str() and repr()
print 'Here is a number: %s. Here is a string: %s' %(123.1,'hi')
print 'Here is a number: %r. Here is a string: %r' %(123.1,'hi')

# .format() method
print "This is a %s or a %s" %("bacon", "cat")
print "This is a {a} or a {b}".format(a="bacon", b="cat")

