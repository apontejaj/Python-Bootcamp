# enumerate returs a tuple (number, item)

my_list = [10, 20, 30, 40, 50]

numbers = enumerate(my_list)

print (type (numbers))

for number, item in numbers:
    print ("the index is {} and the item is {}".format(number, item))
