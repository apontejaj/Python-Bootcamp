def square(num):
    return num**2

print (square(4))

# So, we can simplify this into a smaller type of function that is generally
# used to for small operations, leaving functions for more elaborated operations

lambda_square = lambda num: num**2

print (lambda_square(5))

comparing = lambda value: value == 3

print (comparing(4))
