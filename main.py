import Modules.functions as functions
import Modules.connection
import Modules.car as carObj
import Modules.colors as clr

functions.clear()
# Taking customers' main information
veteranBool=False
print ("Welcome To Continental Auto Dealers! To better assist you, please help answer the below questions")
first_name=input("Enter First Name: ")
last_name =input("Enter Last Name: " )
zip_code = input ("Enter your Zip Code: ")
veteran = input ("Are you a war veteran or disabled? (y/n): ")

# Checking veteran input
veteran = veteran.lower()
if veteran == 'y':
    print("Congratulations you are entitled to a discount")
    veteranBool = True 

# Making list to hold the cars
carList = []

# Main loop
while True: 

    # Lists with types of cars
    makes= [None, 'Honda', 'Toyota']
    hondaModels = [None, 'Pilot', 'Accord', 'Civic', 'Ridgeline']
    toyotaModels = [None, 'Highlander', 'Camry', 'Corolla', 'Tacoma']
    years = [None, '2020', '2019', '2018', '2017']
    colors = [None, 'Black', 'Red', 'Grey', 'Blue', 'White']

    # Collecting customer car preferences.
    # Loops through each list to display the options.
    for make in makes:
        print('{}:   {}'.format(makes.index(make),make))
    car_make = makes[int(input("Enter Car Make #(0 to skip): "))]

    if car_make == 'Honda':
        for model in hondaModels:
            print('{}:   {}'.format(hondaModels.index(model),model))
        car_model = hondaModels[int(input("Enter Car Model #(0 to skip): "))]
    elif car_make == 'Toyota':
        for model in toyotaModels:
            print('{}:   {}'.format(toyotaModels.index(model),model))
        car_model = toyotaModels[int(input("Enter Car Model #(0 to skip): "))]
    else:
        car_model = None

    for year in years:
        print('{}:   {}'.format(years.index(year),year))
    car_year = years[int(input("Enter Car Year #(0 to skip): "))]

    for color in colors:
        print('{}:   {}'.format(colors.index(color),color))
    car_color = colors[int(input("Enter Car Color #(0 to skip): "))]

    functions.clear()

    # Calls the function which selects all cars which meet the user's choices.
    print("These are the cars we found:")
    functions.searchCar(car_make, car_model, car_year, car_color)

    # Prompts the user for car ID selection
    print('''     Select the ID corresponding to the car
     you would like to select.''')
    selection = input("     Enter 0 if you would like to search again: ")

    # Finds the specific car if one was selected
    if selection != '0':
        car_info = functions.selectCar(selection)
        
        # Catches weird entries (out of range of table)
        if car_info == None:
            print("Sorry, we ran into an issue.")
            input("Press any key to search again.")
        else:
            # Function
            adjustedPrice = functions.priceAdjust(float(car_info[5]), car_info[4], veteranBool)
            newcar = carObj.Car(car_info[1], car_info[2], car_info[3], car_info[4], adjustedPrice)
            carList.append(newcar)
            functions.removeCar(selection)

            clr.prRed("{: >4} {: >11} {: >5} {: >10} {: >10}".format('MAKE', 'MODEL', 'YEAR', 'COLOR', 'PRICE($)'))
            for car in carList:
                clr.prCyan("{: >5} {: >10} {: >5} {: >10} {: >10}".format(car.getMake(), car.getModel(), car.getYear(), car.getColor(), car.getPrice()))
            
            selection = input("Would you like to choose another car (y/n)?: ")
            selection = selection.lower()

            if selection == 'n':
                functions.totalPrice(carList)
                print("Thank you for visiting Continental Auto Dealers.")
                print("Please come again.")
                break

    functions.clear()