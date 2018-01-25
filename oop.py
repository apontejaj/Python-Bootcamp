l = [1,2,3]
a = l.count(2)


print (type(l), type(a)) # the function type returns the type of the object

# First empty class
class Sample(object):
    pass

x = Sample()

print (type(x))

# let's put some attribute in the class

class Bus(object):
    def __init__(self, color, make):
        self.color = color
        self.make = make

dublin_bus = Bus(color = "Yellow", make= "nissan")
bus_eiran = Bus("blue", "toyota") # we can pass on the values for the attributes

print (dublin_bus.color)
print (bus_eiran.make)

# There is something called CLASS OBJECT ATTRIBUTE

class bike(object):
    #class object atribute
    number_of_wheels = 2

    def __init__(self, type):
        self.type = type

my = bike("hybrid")
print (my.type)
print (bike.number_of_wheels)
print (my.number_of_wheels)

# methods for a class

class car(object):
    wheels = 4

    def __init__(self, colour):
        self.colour = colour
        self.x = 0

    def move_forward(self, speed):
        self.x += speed

    def move_backwards(self, speed):
        self.x -= speed

golf = car("Red")
print(golf.colour)
print(golf.x)
golf.move_forward(3)
print(golf.x)
golf.move_backwards(4)
print(golf.x)

# We can have subclasses and inheritance

class taxi(car):
    def __init__(self):
        car.__init__(self, "Yellow")
        print ("taxi created")

my_taxy = taxi()
print (my_taxy.colour)
print (my_taxy.wheels)
print (my_taxy.x)
my_taxy.move_forward(3)
print(my_taxy.x)

# Special methods. They are used by python itself

class computer(object):
    def __init__(self, model, memory, hard_drive):
        self.model = model
        self.memory = memory
        self.hard_drive = hard_drive

    def __str__(self):
        return "This computer is a {}, with {} of memory and {} of hd".format(self.model, self.memory, self.hard_drive)

    def __len__(self):
        return self.memory

    def __del__(self):
        print ("destroyed")

    
pc = computer("laptop", 12, 512)
print (pc) # this line uses the method __str__
print (len(pc))
del (pc)

print (pc)
