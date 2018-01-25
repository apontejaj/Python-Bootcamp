def say_hello():
    '''
    This function says hello
    '''
    print ("hello world")

def greeting(name):
    '''
    This function says a personalise hello
    '''
    print ("hello {} How are you".format(name))
    print ("hello %s How are you" %(name))

def building_greeting(name):
    '''
    This function only builds the greeting and returns it as a string
    '''
    return "hello {}".format(name)

say_hello()
greeting("Amilcar")
print (building_greeting("Amilcar"))
a = "or we can put it in a local variable %r and then print it" %(building_greeting("Mike"))
b = "or we can put it in a local variable {} and then print it".format(building_greeting("Mike"))

print (a)
print (b)

def is_prime(num):
    '''
    method to verify if a given number is prime
    '''
    for n in range(2,num):
        if num%n == 0:
            print ("not prime")
            break
        if n == num-1:
            print ("is prime")
        
is_prime(33)
