import mysql.connector
from mysql.connector import connect
import connection as c

# NEEDED FOR TESTING ============================
import os 
from os import system 
import functions as func 
from colorama import Fore, Back, Style
from os.path import join, dirname
from dotenv import load_dotenv

system('cls')

# Create .env file under root folder and add the environment variables
# Saving the path to .env
dotenv_path = join(dirname(__file__), '../.env')
# Loading the env variables from the path.
load_dotenv(dotenv_path)
# ================================================

def displayCars(conn, where=None):
    
    query = "SELECT * FROM car_dealership"
    if where is not None:
        query += where
    #print(query)

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        for row in cursor:
            print(f'''
            Make            {row[1]}
            Model           {row[2]}
            Year            {row[3]}
            Color           {row[4]}
            Price           {row[5]}
            ''')
        cursor.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)


def removeCar(index):
    # MySQL Syntax: DELETE FROM table_name WHERE id = number
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM car_dealership WHERE id = {}".format(index))
        cursor.close() 
        conn.commit()
        #displayCars(conn)
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

    displayCars(conn, where_string)

    conn.close()

make = 'Honda'
model = None
year = None
color = 'Blue'

searchCar(make, model, year, color)
