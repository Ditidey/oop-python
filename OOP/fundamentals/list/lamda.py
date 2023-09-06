def square(x):
    return x * x

result = square(6)
print(result)

square_two = lambda x: x*x

res = square_two(3)
print(res)

add = lambda x, y: x + y

sum = add(45, 56)
print(sum)


numbers = [12, 45, 65, 23, 89, 78, 11]

def double_it(x):
    return x * 2
# doubled_number = map(lambda x: x*2, numbers)
doubled_number = map(double_it, numbers)
print(list(doubled_number))

bigger_numbers = filter(lambda num: num > 50, numbers)
print(list(bigger_numbers))

actors = [{'name': 'sakib', 'age': 34}
    {'name': 'akib', 'age': 24}
    {'name': 'rakib', 'age': 44}
    {'name': 'makib', 'age': 64}
    ]

senior_artists = filter(lambda actors: actors['age'] > 35, actors)
print(list(senior_artists))