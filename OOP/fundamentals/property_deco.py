
class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name 
        self.email = f'{self.first}.{self.last}@user.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self, value):
        self.first = value.split(' ')[0]
        self.last = value.split(' ')[1]

mark = User('mark', 'zuku')
print(mark.first)
print(mark.last)
print(mark.email)
print(mark.full_name)
mark.full_name = 'Tom hanks'
print(mark.full_name)