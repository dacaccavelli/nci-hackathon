import Modules.functions as functions
import Modules.connection
import Modules.car as carObj
import Modules.colors as clr

functions.clear()
# Taking customers' main information
print ("Welcome To XX Dealership! To better assist you, please help answer the below questions")
first_name=input("Enter First Name: ")
last_name =input("Enter Last Name: " )
zip_code = input ("Enter your Zip Code: ")

veteran = False 
# ask veteran/disabled

carList = []
while True: 

    functions.clear()

    # Collecting customer car preferences
    car_make = input("Enter Car Make: ")
    car_model = input("Enter Car Model: ")
    car_year = input("Enter Car Year: ")
    car_color = input("Enter Car Color: ")

    functions.clear()

    #Testing ==============
    car_make = 'Honda'
    car_model = None
    car_year = None
    #color = 'Blue'
    #=====================

    print("These are the cars we found:")
    functions.searchCar(car_make, car_model, car_year, car_color)

    print('''   Select the ID corresponding to the car
            you would like to select.''')
    selection = input("Enter 0 if you would like to search again: ")

    if selection != '0':
        car_info = functions.selectCar(selection)
        print(car_info)
        #functions.priceAdjust(car_info[5], veteran)
        newcar = carObj.Car(car_info[1], car_info[2], car_info[3], car_info[4], float(car_info[5]))
        carList.append(newcar)

        clr.prRed("{: >4} {: >11} {: >5} {: >10} {: >10}".format('MAKE', 'MODEL', 'YEAR', 'COLOR', 'PRICE($)'))
        for car in carList:
            clr.prCyan("{: >5} {: >10} {: >5} {: >10} {: >10}".format(car.getMake(), car.getModel(), car.getYear(), car.getColor(), car.getPrice()))
        selection = input("Would you like to choose another car (y/n)?: ")
        selection = selection.lower()

        if selection == 'n':
            functions.totalPrice(carList)
            break