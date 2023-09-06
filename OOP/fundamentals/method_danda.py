class Person:
    def __init__(self, name, age, money, height):
        self.name = name
        self.age = age 
        self.money = money
        self.height = height

    def __call__(self):
        print(f'This is {self.name} with age {self.age} and have {self.money}')
    
    def __add__(self, other):
        return self.age + other.age 
    def __eq__(self, other):
        return self.age == other.age
    def __len__(self):
        return self.height 

alim = Person('Alim', 15, 400, 68)
delim = Person('Delim', 16, 500, 65)

print(alim + delim)
print(alim.age)
alim()
print(alim == delim)
print(len(alim))



