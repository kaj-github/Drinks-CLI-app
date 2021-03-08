#from classes2 import *
#from app_sections import *
#this is my main app file (she said hopefully)

import mysql.connector
from testingsql import display_preference

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="demo"
    )


def create_drink(): 
    mycursor = mydb.cursor()
    createDrinkQuery = "INSERT INTO drink (drink_name) VALUES (%s)"
    drink_choice = input("Select a drink please." "\n")
    mycursor.execute(createDrinkQuery, (drink_choice,))
    mydb.commit()
    mycursor.close()
    mydb.close()


def display_drink():
    mycursor = mydb.cursor()
    getDrinkQuery = "SELECT * FROM drink"
    mycursor.execute(getDrinkQuery)
    myresult = mycursor.fetchall()
# print(len(myresult))
    for row in myresult:
        row = Drink(row[0],row[1],[2])
        print(row)
    mycursor.close()
    mydb.close()

def display_person(): 
    mycursor = mydb.cursor()
    getPersonQuery = "SELECT * FROM person"
    mycursor.execute(getPersonQuery)
    myresult = mycursor.fetchall()
    for row in myresult:
        row = Drink(row[0],row[1], row[2], row[3])
    mycursor.close
    mydb.close()

def create_person(): 
    mycursor = mydb.cursor()
    person_forename = input("Please type your forename." "\n")
    person_surname = input("Please type your surname." "\n")
    createPersonQuery = "INSERT INTO person(forename, surname) VALUES (%s, %s)"
    mycursor.execute(createPersonQuery, (person_forename, person_surname,))
    mydb.commit()
    mycursor.close()
    mydb.close()

# def preferences(): 
#     mycursor = mydb.cursor()

#     preference = "SELECT p.forename, d.drink_name FROM person p LEFT JOIN drink_name d ON p.name_id = d.drink_id; 

#     mycursor.execute(preference)
#     myresult = mycursor.fetchall()

#     for x in myresult: 
#         print(x)



welcome_msg = "Welcome to K's cafe. Please choose an option. \n Please note that all of our prices are in pounds and all drink volumes are in ml."
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
¦¦   [7] Exit menu             ¦¦
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
"""



exit_menu = 0 

#while exit_menu != 6:
print(menu)

#is_ready = input("are you ready to choose?")
# if yes then option blah blah 

option = int(input("Please choose a number."))
if option == 1: 
    display_person()
elif option == 2: 
    display_drink()
elif option == 3: 
    create_person()
elif option == 4: 
    create_drink()
# if option == 5: 
    display_preference()
# if option == 6: 
