# Taking customers' main information

print ("Welcome To XX Dealership! To better assist you, please help answer the below questions")

first_name = input("Enter First Name: ")
last_name =input("Enter Last Name: " )
zip_code = input ("Enter your Zip Code: ")

# If statement to check if the customer is eligable to the veteran discount.

veteran = input("Are you a Veteran?'Yes/No': ")
 
if veteran == "Yes":
    print("Conratulations you are entitled to a discount")

else:
    print("Our prices are unbeatable")

 # Collecting customer car preferences

car_make = input("Enter Car Make: ")
car_model = input("Enter Car Model: ")
car_year = input("Enter Car Year: ")
car_color = input("Enter Car Color: ")

# Car selection
print("LIST OF CAR MAKES")
car_make=["Honda"]
print(car_make)
input("Please Type your car make ")
#car_color=["Black","Blue","Red","Silver","White"]
#car_model=["Accord","Civic","Pilot","Ridgeline"]
#car_year=["2017","2018","2019","2020","2021"]
