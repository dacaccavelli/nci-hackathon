import mysql.connector
from mysql.connector import connect
import Modules.connection as c
import platform
# # NEEDED FOR TESTING ============================
import os 
from os import system 
#import functions as func 
from colorama import Fore, Back, Style
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file under root folder and add the environment variables
# Saving the path to .env
dotenv_path = join(dirname(__file__), '../.env')
# Loading the env variables from the path.
load_dotenv(dotenv_path)
# # ================================================

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def displayCars(conn, where=None):
    
    query = "SELECT * FROM car_dealership"
    if where is not None:
        query += where

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        if query.find('car_id') == -1:
            for row in cursor:
                print(f'''
        ID              {row[0]}
        Make            {row[1]}
        Model           {row[2]}
        Year            {row[3]}
        Color           {row[4]}
        Price           {row[5]}
                ''')
            cursor.close()
        else:
            for row in cursor:
                return row
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)


def removeCar(index):
    # MySQL Syntax: DELETE FROM table_name WHERE id = number
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM car_dealership WHERE car_id = {}".format(index))
        cursor.close() 
        conn.commit()
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)


def searchCar(make=None, model=None, year=None, color=None):
    # Function to break down the list of total cars for
    # viewing based on the passed params.

    details = {"car_make": make,
               "car_model": model,
               "car_year": year,
               "car_color": color}
    where_string = " WHERE "
    for key, value in details.items():
        if value is not None:
            where_string += "{} LIKE '{}' AND ".format(key, value) 
    
    if where_string.endswith(' AND '):
        where_string = where_string[:-5]

    conn = c.returnConnection()

    if len(where_string) == 7:
        displayCars(conn)
    else:
        displayCars(conn, where_string)
    conn.close()


def selectCar(car_id=None):
    # Function to break down the list of total cars for
    # viewing based on the passed params.

    if car_id is not None:
        where_string = " WHERE car_id = {}".format(car_id)
        conn = c.returnConnection()
        car_info = displayCars(conn, where_string)
        conn.close()
        return car_info


def totalPrice(carList):
        
        subtotal = 0
        for car in carList:
            subtotal += car.getPrice()
    
        print('Subtotal = ${}'.format(subtotal))
        salesTax = subtotal * 0.06
        print('Sales Tax = ${}'.format(salesTax))
        total = subtotal + salesTax
        print ("Total = ${}".format(total))


def discountCalc(n1, n2):
    discount = round(n1 - n1 * n2, 2)
    return discount


def cashbonus(n1, n2):
    bonus = n1 - n2
    return bonus


def priceAdjust(price, color, vet):
    
    # if car is black
    color = color.lower()
    if color == 'black': #black car discount
        print('So that brings your total to $', discountCalc(price, .25))
        if vet == True:
            bprice = discountCalc(price, .25)
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of that price is...')
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(discountCalc(bprice, .25), 500))
            baseprice = cashbonus(discountCalc(bprice, .25), 500)
        else: 
            print('Alright so your total is still at $', discountCalc(price, .25))
            baseprice = discountCalc(price, .25)
    elif color == 'white': # if car is white cash bonus
        wprice= cashbonus(price, 400)
        if vet == True:
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of that price is...')
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(cashbonus(discountCalc(price, .25), 500), 400))
            baseprice = cashbonus(cashbonus(discountCalc(price, .25), 500), 400)
        else: 
            print('No worries, with the cash bonus for white cars your price is $', cashbonus(price, 400))
            baseprice = cashbonus(price, 400)
    else:
        print('Alright the color is not white or black so unfortunately, no cash bonus')
        if vet == True:
            print('Awesome! Thank you for your service. You get a 25% discount.')
            print('So 25% off of {} is...'.format(price))
            print('$', discountCalc(price, .25)) # discount if veteran
            print('And a $500 cash bonus!!!')
            print('So now your price is $', cashbonus(discountCalc(price, .25), 500))
            baseprice = cashbonus(discountCalc(price, .25), 500)
        else:
            print('No worries, we still offer great prices! Your price is still at ${}.'.format(price))
            baseprice = price
    return baseprice
