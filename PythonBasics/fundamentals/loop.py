# while loop
num = 1
while num < 10: 
    num = num + 1
    print(num)

# using break
while num < 10:
    if num == 7:
       break
    num = num + 1
    # print(num)
# using continue

while num < 20:
    if num % 2 == 1:
        continue
    num = num + 1
    print(num)

# for for loop
country = 'Ireland'
for char in country:
    print(char)

for num in range(10):
    print(num)

for n in range(1, 10, 2):
    print(n)
