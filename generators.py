import random

def gencubes(n):            # The generator generates values and pauses until the outer function is ready to go on
    for num in range(n):
        yield num**3

for x in gencubes(10):  # It saves memory because we don't need to keep track of all the values
    print(x)

def genfibon(n): # Another generator
    a = 1
    b = 1

    for i in range(n):
        yield a
        t = a
        a = b
        b = t + b

for num in genfibon(10):
    print (num)

def simple_gen ():
    for x in range(3):
        yield x

g = simple_gen()

print (next(g))         # The next function allows you to iterate over generators
print (next(g))
print (next(g))

s = "hello"             # Strings are iterables, but they are not generators
s_iter = iter(s)        # With the iter function, we can convert any iterable structure in a generator

print (next(s_iter))    # And then use the next function
print (next(s_iter))
print (next(s_iter))

# HOMEWORK

def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(10):
    print (x)

def random_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in random_num(1,10,12):
    print (num)

print("gencomp")

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3) # Generator comprenhension!!!

print (next(gencomp))
