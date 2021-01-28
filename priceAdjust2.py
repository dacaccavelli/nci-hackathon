#import Price
#... Price ('20000', 'MSRP')
#MSRP 20000

#Price('15000', 'Black')
#Black 15000

#Price('19600', 'White')
#White 19600

#Price('14500', 'Veteran')
#Veteran 14500
import os
from os import system
system('cls')

def discountCalc(n1, n2):
    discount = n1 - n1 * n2
    return discount

def cashbonus(n1, n2):
    bonus = n1 - n2
    return bonus

car = input('Please enter the color of the car >> ')
# if car is black
if car == 'black': #black car discount
    print('So that brings your total to $', discountCalc(20000, .25))
    vet = input('Are you a veteran? Please type Y/N >> ')
    if vet == 'y':
        bprice = discountCalc(20000, .25)
        print('Awesome! Thank you for your service. You get a 25% discount.')
        print('So 25% off of that price is...')
        print('And a $500 cash bonus!!!')
        print('So now your price is $', cashbonus(discountCalc(bprice, .25), 500))
    else: 
        print('Alright so your total is still at $', discountCalc(20000, .25))
elif car == 'white': # if car is white cash bonus
    wprice= cashbonus(20000, 400)
    vet = input('Are you a veteran? Please type Y/N >> ')
    if vet == 'y':
        print('Awesome! Thank you for your service. You get a 25% discount.')
        print('So 25% off of that price is...')
        print('And a $500 cash bonus!!!')
        print('So now your price is $', cashbonus(cashbonus(discountCalc(20000, .25), 500), 400))
    else: print('No worries, with the cash bonus for white cars your price is $', cashbonus(20000, 400))
else:
    print('Alright the color is not white or black so unfortunately, no cash bonus')
    vet = input('Are you a veteran? Please type Y/N >> ')
    if vet == 'y':
        print('Awesome! Thank you for your service. You get a 25% discount.')
        print('So 25% off of 20000 is...')
        print('$', discountCalc(20000, .25)) # discount if veteran
        print('And a $500 cash bonus!!!')
        print('So now your price is $', cashbonus(discountCalc(20000, .25), 500))
    else:
        print('No worries, we still offer great prices! Your price is still at $20000.')
