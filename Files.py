my_file = open ("Text File.txt", "w+") # w+ allows you to read and write. But it'll wipe it up

my_file.write("adding a new line\n")
my_file.writelines("is this in the middle\n")
my_file.write("and another one\n")

my_file.close()

my_file = open("Text File.txt")

print (my_file.read())
print (my_file.read())
my_file.seek(3)
print (my_file.read())
my_file.seek(3)
print (my_file.readline())

my_file.seek(0)
print (my_file.readline())
print (my_file.readline())
my_file.close()

my_file = open("Text File.txt")
i = 0
for line in my_file:
    print ("line number {} is {}".format(i, line))
    print ("line number %s is %s" %(i, line))
    i += 1

my_file.close()

