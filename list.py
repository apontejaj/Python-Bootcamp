my_list = ["string", 2, 3.131526]

print (len(my_list))
print (my_list[1])

my_list.pop(1)

print (len(my_list))
print (my_list[1])

my_new_list = []
print (len(my_new_list))

my_new_list.append("hELLO")

print (len(my_new_list))

my_new_list.append(2)

matrix = [my_list, my_new_list]

print (matrix[0])

print (row[0] for row in matrix)
