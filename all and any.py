# all() returns true if all the elements of a sequence are true
# any() returns true if any of the elements of a sequence is true

# Remember the map

equals_two = lambda x: x == 2
my_list= [0, 1, 2, 3, 4, 5]

result = map(equals_two, my_list)
print(result)
print(all(result))
print(any(result))
