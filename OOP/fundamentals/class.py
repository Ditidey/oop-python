class Phone:
    name = 'Sumsumng 15 pro'
    brand = 'Sum Sung'
    price = 15000

# print(Phone.name)

class Calculator:
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
    def multification(self, mul1, mul2):
        mul = mul1 * mul2
        return mul
    
cal = Calculator()
sum = cal.add(4, 5)
mul = cal.multification(3, 4)
print(sum, mul)