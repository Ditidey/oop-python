class add_power:
    def add(self, x, n):
        print('Sum is: ', sum(int(x), int(n)))
        print('power: ', pow(int(x), int(n)))

x, n = input('Enter two numers: ').split()
add_power().add(x, n)
