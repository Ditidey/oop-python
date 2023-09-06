largest = max(45, 89, 54, 116)
print(largest)

numbers = [1, 2, 3, 4, 5, 6]
numbers_rev = reversed(numbers)
print(list(numbers_rev))

actors = [
    {'name': 'diti', 'age': 25}
    {'name': 'piti', 'age': 34}
    {'name': 'miti', 'age': 15}
    {'name': 'eiti', 'age': 5}
]

sorted_actors = sorted(actors, key = lambda actor: actor['age'])
print(sorted_actors)
