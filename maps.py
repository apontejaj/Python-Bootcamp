# A map is a funtion. It takes another function and a sequence (for example,
# a list) and resturns another list with the result of all the elements in the
# sequence after overgoing through the function

def rect(x):                # This is a function
    return ((3 * x) + 2)

xs = [0, 1, 2, 3, 4]        # This is a sequence

ys = map (rect, xs)

print (ys)

# we can do this with a lambda expresions

comparing = map(lambda value: value == 3, xs)
print (comparing)

# We can use maps with more than one sequence

comparing2 = map(lambda value1, value2: (value1 == 3) or (value2 == 2), xs, ys)
print (comparing2)
