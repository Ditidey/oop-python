
# 1. finding float and ceil of a number
import math
num = float(input("give a number: "))
floorNum = math.floor(num)
print(math.floor(num))
print(math.ceil(num))

# 2. taking multple input from user and showing its absolate value
x, y, z = float(input("give three numbers").split())
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if(num1 >= 0):
    print(num1)
else: print(-num1)
if(num2 >= 0):
    print(num2)
else: print(-num2)
if(num3 >= 0):
    print(num1)
else: print(-num3)

# 3. rock, paper, scissor game
a = input("give a word rock/paper/scissor ")
b = input("give another word rock/paper/scissor ")

if(a == 'rock' and b == 'paper' or a== 'paper' and b == 'rock'):
    print('Paper')
elif(a == 'scissor' and b == 'rock' or a == 'rock' and b == 'scissor'):
    print('Rock')
elif(a == 'paper' and b == 'scissor' or a == 'scissor' and b == 'paper'):
    print('Scissor')

# 4. quit program
while True:
    user_input = input("Enter quit to stop: ")

    if(user_input == 'quit'):
        break
    else:
        num = int(input("Enter a number "))
        if(num == 0):
           print( num, "is Zero")
        elif(num < 0):
           print(num, "is Negative")
        else: print(num, "is Positive")

# 5. fizzbuzz game
 
for num in range(1, 50):
    if(num % 3 == 0 and num % 5 == 0):
        print("FuzzBuzz")
    elif(num % 5 == 0):
        print("Buzz")
    elif(num % 3 == 0):
        print("Fizz")
    else: print(num)

# print first letter of you name using pattern
