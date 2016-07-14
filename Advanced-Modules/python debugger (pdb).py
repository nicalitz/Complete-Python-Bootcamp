'''
Pyhon Debugger (pdb)

- interactive debugging environment
- pause you program, look at values, execute step-by-step

'''
import pdb

x = [1,3,4]
y = 2
z = 3

result = x + z
print result

# set a trace using python debugger
pdb.set_trace()

result2 = y + x
print result2