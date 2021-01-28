# import mysql.connector
# from mysql.connector import connect
import connection as c


def readCars(conn, where):
    try:
        cursor = conn.cursor()
        query = "SELECT 8 FROM"
        cursor.execute('SELECT * FROM car_dealership')
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
        displayCars(conn)
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)


def searchCar(make=None, model=None, year=None, color=None):
    # Function to break down the list of total cars for
    # viewing based on the passed params.

    
    details = {"car_make": make, "car_model": model, "car_year": year, "car_color": color]
    where_string = "WHERE "
    for key, value in details.items():
        if value is not None:
            where_string += "{} LIKE '{}'".format(key, value) 
    conn = c.returnConnection()
    displayCars(conn)