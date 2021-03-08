from importingmysql import db
from classes2 import Drink, Person, Preference
import time

mydb = db()
mycursor = mydb.cursor()

def display_drink():
    try:
        getDrinkQuery = "SELECT * FROM drink"
        mycursor.execute(getDrinkQuery)
        myresult = mycursor.fetchall()
        print("DRINKS")
        for row in myresult:
            row = Drink(row[0], row[1], row[2], row[3], row[4])
            print(row)
        time.sleep(8)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")


def display_person():
    try:
        getPersonQuery = "SELECT * FROM person"
        mycursor.execute(getPersonQuery)
        myresult = mycursor.fetchall()
        print("PEOPLE")
        for row in myresult:
            row = Person(row[0], row[1], row[2], row[3])
            print(row)
        time.sleep(8)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
    

def create_drink(): 
    try:
        createDrinkQuery = "INSERT INTO drink (drink_name, drink_price, drink_volume, drink_alcoholic) VALUES (%s, %s, %s, %s)"
        drink_choice = input("Select a drink please." "\n")
        drink_volume = input("Please input the volume of the drink." "\n")
        drink_alcoholic = int(input("Is the drink alcoholic? Please type 1 for yes or 2 for no." "\n"))
    
        if drink_alcoholic == 1:
            drink_price = 8
            drink_alcoholic = "Yes"
        else:
            drink_price = 4
            drink_alcoholic = "No"

        mycursor.execute(createDrinkQuery, (drink_choice, drink_price, drink_volume, drink_alcoholic,))
        mydb.commit()
        print("The drinks list has been updated.")
        time.sleep(2)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")

def create_person(): 
    try:
        person_forename = input("Please type your forename." "\n")
        person_surname = input("Please type your surname." "\n")
        person_age = int(input("Please type your age." "\n"))
        createPersonQuery = "INSERT INTO person(person_forename, person_surname, person_age) VALUES (%s, %s, %s)"
        mycursor.execute(createPersonQuery, (person_forename, person_surname, person_age,))
        mydb.commit()
        print("The list of people has been updated.")
        time.sleep(2)
    except: 
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
        time.sleep(2)


def display_preference(): 
    try:
        preference = "SELECT person.person_forename, drink.drink_name FROM person LEFT JOIN drink ON person.person_id = drink.drink_id"

        mycursor.execute(preference)
        myresult = mycursor.fetchall()

        print("PREFERENCES")
        for row in myresult: 
            row = Preference(row[0], row[1])
            print(row)
        time.sleep(8)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
        time.sleep(2)

def create_preference(): 
    try:
        create_person()
        create_drink()
        print("The preferences list has been updated.")
        time.sleep(2)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
        time.sleep(2)

def update_people():
    try: 
        update_id = int(input("Please type the ID number of the person you would like to update." "\n"))
        update_forename = input("Please type your forename." "\n")
        update_surname = input("Please type your surname." "\n")
        update_age = int(input("Please type your age." "\n"))

        updatePersonQuery = "UPDATE person SET person_forename = %s, person_surname = %s, person_age = %s WHERE person_id = %s"
        person_update_input = (update_forename, update_surname, update_age, update_id)
        mycursor.execute(updatePersonQuery, person_update_input)
        mydb.commit()
        print("The list of people has been updated.")
        time.sleep(2)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
        time.sleep(2)


def update_drinks(): 
    try: 
        update_id = int(input("Please type the ID number of the drink you would like to update." "\n"))
        update_drinkname = input("Please choose the name of a drink." "\n")
        update_volume = int(input("Please choose a volume." "\n"))
        update_alcoholic = int(input("Is the drink alcoholic? Please type 1 for yes or 2 for no." "\n"))
        if update_alcoholic == 1:
            update_alcoholic = "Yes"
            update_price = 8
        else:
            update_alcoholic = "No"
            update_price = 4
        
        updateDrinkQuery = "UPDATE drink SET drink_name = %s,  drink_volume = %s, drink_alcoholic = %s, drink_price = %s WHERE drink_id = %s"
        drink_update_input = (update_drinkname, update_volume, update_alcoholic, update_price, update_id)
        mycursor.execute(updateDrinkQuery, drink_update_input)
        mydb.commit()
        print("The list of drinks has been updated.")
        time.sleep(2)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
        time.sleep(2)
    


def menu_card():

    welcome_msg = "Welcome to K's cafe. Please choose an option. \nPlease note that all of our prices are in pounds and all drink volumes are in ml."
    print(welcome_msg)

    menu = """

    Please take a look at our interactive menu: 

    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    ¦¦        Kay's Cafe           ¦¦
    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    ¦¦   [1] List of people        ¦¦
    ||   [2] List of drinks        ||
    ¦¦   [3] Create a person       ¦¦
    ||   [4] Create a drink        ||
    ¦¦   [5] Display preferences   ¦¦
    ||   [6] Choose preferences    ||
    ¦¦   [7] Update people         ¦¦
    ||   [8] Update drinks         ||
    ¦¦   [9] Exit menu             ¦¦
    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    """
    print(menu)

def clear_screen():
    import os
    os.system('cls') 
    