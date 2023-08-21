#simple function declaration
# taking one argument
def double_it(num):
    result = num * 2
    # print(result)

double_it(5)

#taking multiple argument
def sum(num1, num2):
    result = num1 + num2
    # print(result)

sum(5, 9)

# taking multiple argument and return result
def multiply(one, two, three):
    result = one * two * three
    return result
output = multiply(12, 11, 10)
# print(output)

#passing args with name
def add(num1, num2):
    result = num1 + num2
    # print(f'num1: {num1} num2: {num2}')
    return result
output = add(num2=22, num1=32) # it sit according to naming position

#setting default value in parameter if do not pass argument all
def divide(num1, num2=2):
    result = num1 / num2
    # print(result)

divide(12)

#Tuples
#args: taking multiple arguments within one parameter
def showEach(*numbers):
    for num in numbers:
        print(num)
showEach(2, 4, 5, 2, 4, 9)