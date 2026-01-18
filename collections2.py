my_collection = [23, 34, 65, 67, 34, 23]

my_collection[0] = 999

print(my_collection)
print(my_collection[1])

my_collection[2] = my_collection[0] * my_collection[1]

print(my_collection)

my_collection.pop(0)
print(my_collection)
