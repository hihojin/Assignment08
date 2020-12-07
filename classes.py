# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# HyojinK,12.4.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        HyojinK,12.4.2020,Modified code to complete assignment 8
    """

 #constructor
    def __init__(self, name, price):
        # attributes
        self.__name = name
        self.__price = price

#properties
    @property
    def name(self):
        return str(self.__name).title()

    @name.setter
    def name(self, value):
        if str(value).isnumeric() == False:
            self.__name= value
        else:
            raise Exception('Names cannot be numbers')

    @property
    def price(self):
        return float(self.__price)

    @price.setter
    def price(self, value):
        self.__price = value

#methods
    def __str__(self):
        return self.name + ', ' + str(self.price)
    def To_String(self):
        return self.__str__()

# Data -------------------------------------------------------------------- #
# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        HyojinK,12.4.2020,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        try:
            file= open(file_name, 'r')
            for row in file:
                name, price= row.split(',')
                lstOfProductObjects.append(Product(name, price))
            file.close()
            return lstOfProductObjects
        except Exception:
            print('could not load data from file')

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data(file_name, list_of_product_objects):
        try:
            file = open(file_name, 'a')
            for i in list_of_product_objects:
                file.write(i.__str__() + '\n')
            file.close()
            print('saved')
        except Exception:
            print('not saved')
# Processing  ------------------------------------------------------------- #
# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """input and output codes class"""
    # TODO: Add code to show menu to user
    @staticmethod
    def menu_options():
        print("""
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        """)
        print()

    # TODO: Add code to get user's choice
    @staticmethod
    def menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()
        return choice

    # TODO: Add code to show the current data from the file to user

    @staticmethod
    def show_current_data(list_of_product_objects):
        for row in list_of_product_objects:
            print(row.name, ',', row.price)

    # TODO: Add code to get product data from user
    @staticmethod
    def questions():
        name= input("what is the name of the product? ")
        price= float(input("what is the price of the product? "))
        return name, price

# Presentation (Input/Output)  -------------------------------------------- #
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName)

while(True):
    choice= ''
# Show user a menu of options
    IO.menu_options()
# Get user's menu option choice
    strChoice= IO.menu_choice()
# Show user current data in the list of product objects
    if strChoice == '1':
        (IO.show_current_data(lstOfProductObjects))
# Let user add data to the list of product objects
    if strChoice == '2':
        name, price= IO.questions()
        lstOfProductObjects.append(Product(name, price))
# let user save current data to file and exit program
    if strChoice == '3':
        (FileProcessor.save_data(strFileName, lstOfProductObjects))
    if strChoice == '4': 
        print("You are done!")
        break
# Main Body of Script  ---------------------------------------------------- #
