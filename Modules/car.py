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