my_file = open('test_file.txt','w+')    # open (create) file for writing
my_file.write('This is new data\n')     # write data to file
my_file.write('Some more data')

my_file.seek(0)     #reset cursor to start
print my_file.readlines()   #read data and store in memory

my_file.seek(0)
print my_file.read()    #print data sequentially

my_file.seek(0)
for line in open('test_file.txt'):
    print line