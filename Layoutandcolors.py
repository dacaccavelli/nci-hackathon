import os
from os import system
from objects import Car
from colorama import Style, Fore, Back
# Python program to print 
# colored text and background 
def prRed(skk): 
    print("\033[91m {}\033[00m".format(skk)) 
def prGreen(skk): 
    print("\033[92m {}\033[00m".format(skk)) 
def prYellow(skk): 
    print("\033[93m {}\033[00m".format(skk)) 
def prLightPurple(skk): 
    print("\033[94m {}\033[00m".format(skk)) 
def prPurple(skk): 
    print("\033[95m {}\033[00m".format(skk)) 
def prCyan(skk): 
    print("\033[96m {}\033[00m".format(skk)) 
def prLightGray(skk): 
    print("\033[97m {}\033[00m".format(skk)) 
def prBlack(skk): 
    print("\033[98m {}\033[00m".format(skk)) 
def prBlue(skk): 
    print("\033[34m {}\033[00m".format(skk)) 


system('cls')

Car1 = Car('Honda', 'Accord', 2020, 'Black', 25999)
Car2 = Car('Honda', 'Civic', 2021, 'Red', 21999)
Car3 = Car('Honda', 'NSX', 2021, 'White', 157000)
Car4 = Car('Honda', 'Ridgeline', 2021, 'Blue', 34999)
Car5 = Car('Honda', 'Accord', 2021, 'Silver', 27999)

carList = []
carList.append(Car1)
carList.append(Car2)
carList.append(Car3)
carList.append(Car4)
carList.append(Car5)

prRed("{: >4} {: >11} {: >5} {: >10} {: >10}".format('MAKE', 'MODEL', 'YEAR', 'COLOR', 'PRICE($)'))
for cars in carList:
    prCyan("{: >5} {: >10} {: >5} {: >10} {: >10}".format(cars.getMake(), cars.getModel(), cars.getYear(), cars.getColor(), cars.getPrice()))

print(' ')
print(' ')
prRed("{: >4} {: >11} {: >5} {: >10} {: >10}".format('MAKE', 'MODEL', 'YEAR', 'COLOR', 'PRICE($)'))
prPurple("{: >4} {: >10} {: >5} {: >10} {: >10}".format(Car1.getMake(), Car1.getModel(), Car1.getYear(), Car1.getColor(), Car1.getPrice()))
prCyan("{: >4} {: >10} {: >5} {: >10} {: >10}".format(Car2.getMake(), Car2.getModel(), Car2.getYear(), Car2.getColor(), Car2.getPrice()))
prGreen("{: >4} {: >10} {: >5} {: >10} {: >10}".format(Car3.getMake(), Car3.getModel(), Car3.getYear(), Car3.getColor(), Car3.getPrice()))
prYellow("{: >4} {: >10} {: >5} {: >10} {: >10}".format(Car4.getMake(), Car4.getModel(), Car4.getYear(), Car4.getColor(), Car4.getPrice()))
prBlue("{: >4} {: >10} {: >5} {: >10} {: >10}".format(Car5.getMake(), Car5.getModel(), Car5.getYear(), Car5.getColor(), Car5.getPrice()))

    
