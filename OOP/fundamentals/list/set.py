numbers = [12, 45, 56, 45, 12]
print(numbers)
nums = {12, 45, 56, 45, 12}
print(nums)

numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(77)
numbers_set.add(44)
numbers_set.remove(12)
print(numbers_set)
print(len(numbers_set))
