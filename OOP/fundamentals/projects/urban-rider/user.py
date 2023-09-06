import hashlib
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        pwd_encript = hashlib.md5(password.encode()).hexdigest()

        with open('user.txt', 'w') as file:
            file.write(f'{email} {pwd_encript}')
            file.close()
    @staticmethod
    def log_in(self,email, password):
        store_pass = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                     _, store_pass = line.split(' ')
        file.close()

        pwd_encript = hashlib.md5(password.encode()).hexdigest()
        if pwd_encript == store_pass:
            print('valid user')
            return True
        else:
            print('non valid')
            return False
class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance

    def start_a_trip(self, location):
        self.location = location
    def request_trip(self, location):
        self.location

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.earnings = 0

diti = User('diti', 'diti@dey.com', 'diti12')
diti.log_in('diti@dey.com', 'diti12')