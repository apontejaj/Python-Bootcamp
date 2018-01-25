l = []
for num in range(0,10):
    l.append(num)


for num in l:
    print (num)

print ("-- We can also put a third parameter which is a step")

l = []
for num in range(0,10,2):
    l.append(num)


for num in l:
    print (num)

print ("how to iterate over dictionaries")

dict = {"k1":0, "k2":1, "k3":2}
print dict

for item in dict:  
    print item # Only gives you the keys
    print dict[item]

for k,v in dict.iteritems():
    print ("key: {} value: {}".format(k,v))
    print ("key: %s value: %s" %(k,v))

for k,v in dict.items():
    print ("key: {} value: {}".format(k,v))
    print ("key: %s value: %s" %(k,v))


