numbers = [12, 45, 65, 23, 89, 78, 11]
print(numbers)

numbers_tuple = 12, 45, 65, 23, 89, 78, 11
print(numbers_tuple)
print(numbers_tuple[5])

tuple2D = ([12, 13, 11], [34, 33, 32])
tuple2D[0][1] = 99
tuple2D[1][1] = 90
print(tuple2D)

short_tuple = 2,
print(short_tuple)

tuple_from_list = tuple(numbers)
print(tuple_from_list)