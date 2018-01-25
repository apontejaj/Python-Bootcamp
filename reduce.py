# Reduce reduces the list that it is being applied to

find_min = lambda x, y: x if (x < y) else y
list = [23, 53, 68, 0]

number = reduce (find_min, list)
print (number)

# We can't use reduce with lambdas or function that don't take 2 arguments.
