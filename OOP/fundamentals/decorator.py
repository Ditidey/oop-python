import math
import time 
def timer(func):
    def inner(*args):
        print('start')
        start = time.time()
        end = time.time()
        func(*args)
        print(f'time end. total time taken {end- start}')
    return inner 

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

#timer(get_factorial)()
get_factorial(5)