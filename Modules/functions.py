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

def displayCars(app, conn, where=None):
    
    query = "SELECT * FROM car_dealership"
    if where is not None:
        query += where

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        if query.find('car_id') == -1:
            for row in cursor:
               app.carListbox.insert(0,"{: >3} {: >6} {: >11} {: >5} {: >10} ${: >8}".format(row[0],row[1], row[2], row[3], row[4], row[5]))
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


def searchCar(app, make=None, model=None, year=None, color=None):
    # Function to break down the list of total cars for
    # viewing based on the passed params.

    if make == 'None':
        make = None
    if model == 'None':
        model = None
    if year == 'None':
        year = None
    if color == 'None':
        color = None
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
        displayCars(app, conn)
    else:
        displayCars(app, conn, where_string)
    conn.close()


def selectCar(car_id=None):
    # Function to break down the list of total cars for
    # viewing based on the passed params.

    if car_id is not None:
        where_string = " WHERE car_id = {}".format(car_id)
        conn = c.returnConnection()
        car_info = displayCars(None, conn, where_string)
        conn.close()
        return car_info


def totalPrice(carList):
        
        childString = ""
        subtotal = 0
        for car in carList:
            subtotal += car.getPrice()
        childString += 'Subtotal = ${}.\n'.format(subtotal)
        salesTax = round(subtotal * 0.06, 2)
        childString += 'Sales Tax = ${}.\n'.format(salesTax)
        total = round(subtotal + salesTax)
        childString += "Total = ${}.\n".format(total)
        return childString


def discountCalc(n1, n2):
    discount = round(n1 - n1 * n2, 2)
    return discount


def cashbonus(n1, n2):
    bonus = n1 - n2
    return bonus


def priceAdjust(price, color, vet):
    
    # if car is black
    color = color.lower()
    childString = ""
    if color == 'black': #black car discount
        childString += 'So that brings your total to ${}.\n'.format(discountCalc(price, .25))
        if vet == 1:
            bprice = discountCalc(price, .25)
            childString += """
Awesome! Thank you for your service.
You get a 25% discount.
So 25% off of that price is...${}'
And a $500 cash bonus!!!'
So now your price is ${}""".format(discountCalc(bprice, .25), cashbonus(discountCalc(bprice, .25), 500))
            baseprice = cashbonus(discountCalc(bprice, .25), 500)
        else: 
            childString += 'Alright so your total is still at ${}.'.format(discountCalc(price, .25))
            baseprice = discountCalc(price, .25)
    elif color == 'white': # if car is white cash bonus
        wprice= cashbonus(price, 400)
        if vet == 1:
            childString += """
Awesome! Thank you for your service.
You get a 25% discount.
So 25% off of that price is...${}.
And a $500 cash bonus!!!
So now your price is ${}.""".format(cashbonus(discountCalc(price, .25), 400), cashbonus(cashbonus(discountCalc(price, .25), 400), 500))
            baseprice = cashbonus(cashbonus(discountCalc(price, .25), 500), 400)
        else: 
            childString += 'No worries, with the cash bonus for\nwhite cars your price is ${}.'.format(cashbonus(price, 400))
            baseprice = cashbonus(price, 400)
    else:
        childString += 'Alright the color is not white or black\nso unfortunately, no cash bonus.\n'
        if vet == 1:
            childString += """
Awesome! Thank you for your service.
You get a 25% discount.
So 25% off of {} is...${}.
And a $500 cash bonus!!!
So now your price is ${}.""".format(price, discountCalc(price, .25), cashbonus(discountCalc(price, .25), 500))
            baseprice = cashbonus(discountCalc(price, .25), 500)
        else:
            childString += 'No worries, we still offer great prices!\nYour price is still at ${}.'.format(price)
            baseprice = price
    return baseprice, childString
