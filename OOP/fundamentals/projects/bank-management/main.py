"""Bank Account Management"""

class Account:
    act_id = 1
    def __init__(self, name, age, phone, balance) -> None:
        self.name = name
        self.age = age
        self.phone = phone
        self.balance = balance
        
        self.act_id =  Account.act_id
        Account.act_id += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

act1 = Account('diti', 25, 8899, 2000)

act1.deposit(500)
act1.withdraw(1000)
print(act1.balance)