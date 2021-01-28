import Modules.functions as functions
import Modules.connection

# Taking customers' main information
print ("Welcome To XX Dealership! To better assist you, please help answer the below questions")
first_name=input("Enter First Name: ")
last_name =input("Enter Last Name: " )
zip_code = input ("Enter your Zip Code: ")
 
list_of_cars = []
#while True: 

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

    