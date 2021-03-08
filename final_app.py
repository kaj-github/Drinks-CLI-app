from classes2 import Drink, Person, Preference
from app_sections import mycursor, display_drink, display_person, display_preference, create_drink, create_person, create_preference, menu_card, clear_screen, update_people, update_drinks
from importingmysql import db
import time


exit_menu = 7
option = 0
mydb = db()


while option != exit_menu: 
    clear_screen()
    menu_card()
    time.sleep(1)
    try: 
        option = int(input("Please choose a number." "\n"))

    except: 
        print("Oops, sorry! Please choose a valid number.")
    
    if option == 1: 
        display_person()
    elif option == 2: 
        display_drink()
    elif option == 3: 
        create_person()
    elif option == 4:
        create_drink()
    elif option == 5: 
        display_preference()
    elif option == 6: 
        create_preference()
    elif option == 7:
        update_people()
    elif option == 8:
        update_drinks()
    elif option == 9: 
        mycursor.close()
        mydb.close()
        print("Goodbye, see you soon!")
        time.sleep(1)
        break
    elif option >= 10: 
        print("Oops, sorry!Please choose a valid number.")
        time.sleep(2)