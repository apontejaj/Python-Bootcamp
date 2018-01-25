# Zip functions return tuples of elements from the sequences given

a = [0, 1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10, 11]
c = [12, 13, 14]

one_argument = zip(a)
print ("Returns tuples of only one value")
print (one_argument)

two_arguments = zip (a,c)
print ("Returns tuples of two values, and as many as the smaller")
print (two_arguments)

three_arguments = zip (a, b, c)
print ("Retunrs tuples of three values, and as many as the smaller")
print (three_arguments)

# zip can be used with dictionaries, but retunrs tuples with the keys
