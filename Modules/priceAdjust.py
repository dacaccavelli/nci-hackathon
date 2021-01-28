import os
from os import system

def discountCalc(n1, n2):
    discount = n1 - n1 * n2
    return discount

def cashbonus(n1, n2):
    bonus = n1 - n2
    return bonus

def priceAdjust(price, color, vet):
    
    # if car is black
    if color == 'black': #black car discount
        print('So that brings your total to $', discountCalc(price, .25))
        vet = input('Are you a veteran? Please type Y/N >> ')
        if vet == 'y':
            bprice = discountCalc(price, .25)
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of that price is...')
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(discountCalc(bprice, .25), 500))
        else: 
            print('Alright so your total is still at $', discountCalc(price, .25))
    elif color == 'white': # if car is white cash bonus
        wprice= cashbonus(price, 400)
        if vet == True:
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of that price is...')
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(cashbonus(discountCalc(price, .25), 500), 400))
        else: print('No worries, with the cash bonus for white cars your price is $', cashbonus(price, 400))
    else:
        print('Alright the color is not white or black so unfortunately, no cash bonus')
        vet = input('Are you a veteran? Please type Y/N >> ')
        if vet == True:
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of 20000 is...')
            print('$', discountCalc(price, .25)) # discount if veteran
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(discountCalc(price, .25), 500))
        else:
            print('No worries, we still offer great prices! Your price is still at ${}'.format(price))
