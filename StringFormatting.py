# Strings
word = "hello".upper()


print ("trying to do new things %s" %(word))

print("this is another way {}".format("to do it"))

# Floating Point Numbers

my_float = 3.141526

print ("%1.2f" %(my_float))
print ("%1.3f" %(my_float)) #This method rounds up depending on the next decimal

# putting things together

print ("%s is a word and %1.2f is a float" %(word, my_float))
print ("%s is a word and %1.3f is a float" %(word, my_float))
print ("{} is a word and {} is a float".format(word, my_float))
print ("%s is a word, %s is another word and %1.2f is a float" %(word, word, my_float))

print (word[0].isupper())
