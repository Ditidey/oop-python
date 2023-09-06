class car:
    def __init__(self, license, model, color):
        self.license = license
        self.model = model
        self.color = color 

    def __repr__(self):
        return f'{self.license}, {self.model}, {self.color}'

class Garage:
    def __init__(self):
        self.car_added = []
        self.spot = 10 
        self.car_infos = {}
        self.bill = 0
        self.ticket = []
    def Spots_available(self):
        return self.spot 

    def add_car_to_garage(self, car):
        user_date = str(car).split(',')
        self.spot_name = ['A1', 'B2', 'C3', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.Spots_available() > 0:
            print(user_date)

my_garage = Garage()
user_car = car('123MN', 'Herrari', 'Red')
my_garage.add_car_to_garage(user_car)



        



