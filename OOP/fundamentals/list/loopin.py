numbers = [12, 45, 65, 23, 89, 78, 11, 10]
total = sum(numbers)
print(total)

for i in numbers:
    total += i

print(total)

nums = {11, 12, 13, 14, 15}
mum =0
for num in nums:
    mum += num

print(mum)

marks = {'physics': 12, 'chemistry': 45, 'math': 56}
for mark in marks:
    val = marks[mark]
    print(mark, val)

for subject, mark in marks.items():
    print(subject, mark)

numbers = [12, 45, 65, 23, 89, 78, 11]
for i, num in enumerate(numbers):
    print(i, num)

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers) 

odd_numbers2 = [num for num in numbers if num % 2 == 1]
print(odd_numbers2)

names = ['diti', 'arghya', 'pratim', 'pratima']
ages = [25, 26, 35, 36]
pairs = [(name, age) for name in names for age in ages]
print(pairs)


