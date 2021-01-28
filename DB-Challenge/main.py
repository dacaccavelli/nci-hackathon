from os import name as osname
from os import system, environ
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

#func.readStudentInfo()

# Inserting a new user
# fname = input("What's your first name? >> ")
# lname = input("What's your last name? >> ")
# age= int(input("What's your age? >> "))
# func.insertStudentInfo(fname, lname, age)

# Creating two functions:
#       one to update,
#       one to delete,
# similar to the insert function we created in class.

# Needed for updating a student first name at a specific id #.
fname = input("What do you want to change the first name to?: ")
id_index = input("Which entry do you want to change?: ")
func.updateStudentInfo(fname, id_index)

# # Deleting an entire entry using the id #.
# id_index = input("Which entry do you want to delete?: ")
# func.deleteStudentInfo(id_index)