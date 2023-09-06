class Person:
    def __init__(self, name, age, phone) -> None:
        assert age > 18, f'age greater than 13 is accepted'
        assert len(phone) > 11, f'invalid phone number'
        self.name = name
        self.age = age
        self.phone = phone

    def __repr__(self) -> str:
         return f'{self.name} {self.age} {self.phone}'
    
user = Person('diti', '13123234343', 11)
