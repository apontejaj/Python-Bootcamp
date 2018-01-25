# Filters returns only the elements of the sequence to which the function
# returns TRUE

my_list = [0, 1, 2, 3, 4]
result = filter (lambda x: x == 2, my_list)

print (result)

# The function must return a boolean
