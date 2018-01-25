x = 25 # this variable is visible for any function, it is global

def printer():
    return "from printer one {}".format(x)

print (x)
print (printer())

# But we can redifine this variable in a function

def printer_two():
    x = 50
    return "from printer two {}".format(x)

print (printer_two())
print (x) # and the internal doesnt have anything to do with the external

# Now that is a problem when you want a function to use a variable from outside
# But we can sort it using global

def printer_three():
    global x
    print ("from printer three {}".format(x))
    x = x + 2
    print ("from printer three {}".format(x))

printer_three()
print x

print (printer_two())

