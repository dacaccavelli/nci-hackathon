class Car:
    def __init__(self, make=None, model=None, year=None, color=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
    
    def setMake(self, make):
        self.make = make
    def getMake(self):
        return self.make

    def setModel(self, model):
        self.model = model
    def getModel(self):
        return self.model

    def setYear(self, year):
        self.year = year
    def getYear(self):
        return self.year

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color

    def setPrice(self, price):
        self.price = price
    def getPrice(self):
        return self.price
    
    subtotal = 0
for car in list_of_cars:
    subtotal += car.price
    cars.getprice()
    
salesTax = subtotal * 0.06
print('Sales Tax = ${}'.format(salesTax))

total_car_amount = (subtotal + salesTax)
