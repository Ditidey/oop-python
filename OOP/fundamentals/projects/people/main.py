"""Human data"""

class Human:
    def __init__(self, gender, profession, age):
        self.gender = gender
        self.age = age
        self.profession = profession

class Teacher(Human):
    def __init__(self, gender, profession, age, experience, location):
        super().__init__(gender, profession, age)
        self.experience = experience
        self.location = location

class Researcher(Human):
    def __init__(self, gender, profession, age, field, members):
        super().__init__(gender, profession, age)
        self.field = field
        self.members = members

tech = Teacher('male', 'teacher', 32, 2, 'dublin')
print(tech.location)