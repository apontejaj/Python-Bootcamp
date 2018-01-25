x = range(1,11) # Good to know: Range returns a list

print (x[2])

x = range(11) # also, start is zero by defaoult

print (x[2])

x = range(10,0, -1) # Good to know: Range returns a list

print (x)

for x in xrange(9,-1,-1): # This doesn't store the list in memory
    print (x)

list = [x for x in "word"]
print (list)
