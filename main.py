# NCI Hackathon
# Goal: Create a Dealership application where you prompt the user to
#       input the make, model, year, and color of the cars they want.
#       Prices will vary based on color, year, model, make.
#       Present the user with different options where they can see the price.
#       Pass all prices for colors and makes to another method which
#       calculates the total prices (withtaxes included).
#       If car is black, the user gets a discount of 25% the price of the car.
#       If the car is white, the customer receives a bonus of $400 towards
#       the down   payment.
#       If the customer is a war veteran or disabled, they receive 25% off the
#       cost of the car plus $500 bonus.
#       This returns total price and bonuses to the main file.
#       Pass the four values (make, model, year, and color) to another method
#       where you use the values to create objects.
#       Return the objects to the main file where you will display all of them.
# Date: 1/29/21
# Authors:  Andres Mejia
#           Daniel Caccavelli
#           John C.
#           Kylan Roberts
#           Rachid

import Modules.functions as functions
import Modules.connection
import Modules.car as carObj
import Modules.colors as clr
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        
        background_image=tk.PhotoImage(r"C:\Users\dacac\OneDrive\Pictures\crapCar.JPG")
        background_label = tk.Label(master, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Lists with types of cars
        self.makes= ['None', 'Honda', 'Toyota']
        self.hondaModels = ['None', 'Pilot', 'Accord', 'Civic', 'Ridgeline']
        self.toyotaModels = ['None', 'Highlander', 'Camry', 'Corolla', 'Tacoma']
        self.models = self.hondaModels + self.toyotaModels
        self.years = ['None', '2020', '2019', '2018', '2017']
        self.colors = ['None', 'Black', 'Red', 'Grey', 'Blue', 'White']
        
        self.carlist = []
        
        #self.pack()
        self.create_widgets()


    def create_widgets(self):

        carFrame = tk.LabelFrame(root, text='Vehicle Search', padx=5, pady=5)
        infoFrame = tk.LabelFrame(root, text='Information', padx=5, pady=5)

        headerFrame = tk.Frame(infoFrame)
        headerString = tk.Label(headerFrame, text="Welcome To Continental Auto Dealers!", anchor='n')
        headerString2 = tk.Label(headerFrame, text="To better assist you, please help answer the below questions", anchor='n')

        headerString.pack()
        headerString2.pack()

        userLabelFrame = tk.Frame(infoFrame)
        fnameString= tk.Label(userLabelFrame, text="Enter First Name: ", anchor='e',justify='right')
        lnameString =tk.Label(userLabelFrame, text="Enter Last Name: ", justify='right', anchor='e')
        zipString = tk.Label(userLabelFrame, text="Enter your Zip Code: ", justify='right', anchor='e')
        vetString = tk.Label(userLabelFrame, text="Check if you are a war veteran or disabled: ", justify='right', anchor='e')

        # fnameString.config(font =("Courier", 14)) 

        fnameString.pack(fill='both')
        lnameString.pack(fill='both')
        zipString.pack(fill='both')
        vetString.pack(fill='both')

        entryFrame = tk.Frame(infoFrame)
        first_name = tk.Entry(entryFrame)
        last_name = tk.Entry(entryFrame)
        zip_code = tk.Entry(entryFrame)
        self.vetCheck = tk.IntVar()
        veteranCheck = tk.Checkbutton(entryFrame, variable=self.vetCheck)

        first_name.pack()
        last_name.pack()
        zip_code.pack()
        veteranCheck.pack()

        carLabelFrame = tk.Frame(carFrame)
        makeString= tk.Label(carLabelFrame, text="Select your make (or skip selection)", anchor='e',justify='right')
        modelString =tk.Label(carLabelFrame, text="Select your model (or skip selection)", justify='right', anchor='e')
        yearString = tk.Label(carLabelFrame, text="Select your year (or skip selection)", justify='right', anchor='e')
        colorString = tk.Label(carLabelFrame, text="Select your color (or skip selection)", justify='right', anchor='e')

        makeString.pack(pady=5)
        modelString.pack(pady=5)
        yearString.pack(pady=5)
        colorString.pack(pady=5)

        optionMenuFrame = tk.Frame(carFrame)
        self.makeVar = tk.StringVar(root)
        self.makeVar.set(self.makes[0])
        self.makeOption = tk.OptionMenu(optionMenuFrame, self.makeVar, *self.makes)

        self.modelVar = tk.StringVar(root)
        if self.makeVar.get() == 'None':
            self.modelVar.set(self.models[0])
            self.modelOption = tk.OptionMenu(optionMenuFrame, self.modelVar, *self.models)

        elif self.makeVar.get() == 'Honda':
            self.modelVar.set(self.hondaModels[0])
            self.modelOption = tk.OptionMenu(optionMenuFrame, self.modelVar, *self.hondaModels)

        else:
            self.modelVar.set(self.toyotaModels[0])
            self.modelOption = tk.OptionMenu(optionMenuFrame, self.modelVar, *self.toyotaModels)


        self.yearVar = tk.StringVar(root)
        self.yearVar.set(self.years[0])
        self.yearOption = tk.OptionMenu(optionMenuFrame, self.yearVar, *self.years)

        self.colorVar = tk.StringVar(root)
        self.colorVar.set(self.colors[0])
        self.colorOption = tk.OptionMenu(optionMenuFrame, self.colorVar, *self.colors)

        self.makeOption.pack()
        self.modelOption.pack()
        self.yearOption.pack()
        self.colorOption.pack()

        carLabelFrame.grid(row=0, column=0)
        optionMenuFrame.grid(row=0, column=1)
        
        searchButton = tk.Button(carFrame, text="Search for a car", command = self.searchCar)   
        searchButton.grid(row=1, columnspan=2)

        #self.colorB.configure(bg = "#234")
        self.carListbox = tk.Listbox(root, width=50)
        chosenCarsFrame = tk.Frame(root)
        chosenCarsLabel = tk.Label(chosenCarsFrame, text="Your Cart:")
        self.chosenCars = tk.Listbox(chosenCarsFrame, width=50)

        chosenCarsLabel.grid(row=0, column=0)
        self.chosenCars.grid(row=1, column=0)

        finalFrame = tk.LabelFrame(root, text='Selections')
        selectButton = tk.Button(finalFrame, text="Add selected car to cart", command = self.selectCar)   
        selectButton.grid(row=0, column=1)
        self.finalizeButton = tk.Button(finalFrame, text='Finalize order.', command=self.finalize, state=tk.DISABLED) 
        self.finalizeButton.grid(row=1, column=1)

        headerFrame.grid(row=0, columnspan=2)
        userLabelFrame.grid(row=1, column=0)
        entryFrame.grid(row=1, column=1)

        infoFrame.grid(row=0,columnspan=2)
        carFrame.grid(row=2, columnspan=2)
        self.carListbox.grid(row=0, rowspan=3, column=3, columnspan=2, sticky=tk.N+tk.S+tk.W+tk.E)
        finalFrame.grid(row=4, column=1)
        chosenCarsFrame.grid(row=4, column=4, columnspan=2, sticky=tk.N+tk.S+tk.W+tk.E)


    def makeChild(self, displayString, close=None):
        # child window 
        my_w_child=tk.Toplevel(root) # Child window 
        my_w_child.geometry("400x150")  # Size of the window 
        my_w_child.title("Discounts Available")

        self.my_str1 = tk.StringVar()
        l1 = tk.Label(my_w_child,  textvariable=self.my_str1 , anchor='w', justify='left' )
        l1.grid(row=1,column=2) 
        self.my_str1.set(displayString)

        if not close:
            b3 = tk.Button(my_w_child, text='Okay',
                    command=my_w_child.destroy)
            b3.grid(row=3,column=2)
        else:
            b3 = tk.Button(my_w_child, text='Okay',
                    command=root.destroy)
            b3.grid(row=3,column=2)

    def searchCar(self):

        # Calls the function which selects all cars which meet the user's choices.
        self.carListbox.delete(0,tk.END)
        functions.searchCar(app, self.makeVar.get(), self.modelVar.get(), self.yearVar.get(), self.colorVar.get())


    def selectCar(self):

        selection = self.carListbox.get(self.carListbox.curselection())
        selection = int(selection[0:4])
        car_info = functions.selectCar(selection)
                
        # Catches weird entries (out of range of table)
        if car_info == None:
            self.makeChild("Sorry, we ran into an issue.")
        else:
            # Function
            adjustedPrice, childString = functions.priceAdjust(float(car_info[5]), car_info[4], self.vetCheck.get())
            newcar = carObj.Car(car_info[1], car_info[2], car_info[3], car_info[4], adjustedPrice)
            self.carlist.append(newcar)
            self.chosenCars.insert(0,"{: >6} {: >11} {: >5} {: >10} ${: >8}".format(newcar.getMake(), newcar.getModel(), newcar.getYear(), newcar.getColor(), newcar.getPrice()))
            self.finalizeButton['state'] = tk.NORMAL
            functions.removeCar(selection)
            self.makeChild(childString)


    def finalize(self):
        childString = functions.totalPrice(self.carlist)

        childString += "Thank you for visiting Continental Auto Dealers.\n"
        childString += "Please come again."
        self.makeChild(childString,True)


root = tk.Tk()
root.geometry('1200x600') # Size WxH
root.option_add('*Font', 'Courier 12')
root.title('Continental Auto Dealers')
app = Application(master=root)
app.mainloop()
