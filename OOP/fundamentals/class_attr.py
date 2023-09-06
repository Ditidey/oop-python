from tkinter import PhotoImage


class Phone:
    brand = 'Sumsung'
    color = 'Black'
    price = 25000
    features = ['camera', 'water proof', 'can be used as calculator']
    
    def __init__(self, brand, price, color):
        self.brand = brand
        self.brand = price
        self.color = color

    def call(self):
        print('ring ring ring')

    def send(self, num, text):
        sms = f'sending {text} to {num}'
        return sms 
my_phone = Phone('opp', 12000, 'white')
print(my_phone.brand)
print(my_phone.price)
print(my_phone.color)
my_phone.call()
sms = my_phone.send('01641199064', 'I love myself')
print(sms)

her_phone = Phone('Iphone', 90, 'white')
print(her_phone.features)


