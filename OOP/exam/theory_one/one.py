
def exp(a, n):
    print('Exponential result is: ', int(a) ** int(n))
    res = pow(int(a), int(n))
    print(res)

x, y = input('Enter numbers: ').split()
exp(x, y)
