import os 
import time

names = {1: "Homer", 2: "Marge", 3: "Lisa", 4: "Bart", 5: "Maggie"}
drinks = {1: "Beer", 2: "Wine", 3: "Juice", 4: "Coffee", 5: "Milk"}
fav_drinks = {}


def clearScreen(): 
    os.system("clear")

def read_data(file_name):
    idx = 0
    data = {}
    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()

        for line in lines:
            data.update({idx: line.strip()})
            idc += 1
        the_file.close()
    except FileNotFoundError:
        print(f"{file_name} not found")
        return data

def write_data(file_name, data):

    try:
        the_file = open(file_name, "w")

        for line in data.values():
              the_file.write(line + "\n")
    finally:
        the_file.close()

def save_exit(): 
    write_data("people.txt", people)
    write_data("drinks.txt", drinks)

people = read_data("people.txt")

drinks = read_data("drinks.txt")


def print_table(menu_dict):
    for key, val in menu_dict.items(): 
        print(key, val)

welcome_msg = """
Welcome to BrIW v0.1!
Please select an option by entering a number: 

[1] A list of all people 
[2] A list of all drinks 
[3] List all favourites 
[4] Select Person's favourite 
[5] Exit

"""
def app(): 
    clearScreen()
    option = 0 
    while option!= 5:
        
        while True: 
            try: 
                option = int(input(welcome_msg))
                option = int(option)
                break 
            except ValueError: 
                pass
            print("Please enter a valid number!")
        
        if option == 1: 
            print_table(names)      
            time.sleep(3)
        elif option == 2: 
            print_table(drinks)    
            time.sleep(3)
        elif option == 3: 
            print_table(fav_drinks)
            time.sleep(3)
        elif option == 4: 
            print_table(names)
            while True:
                try:
                    person_id = int(input("Please select a person: "))
                    person_id = int(person_id)
                    person_val = names.get(person_id)
                    break
                except ValueError: 
                    pass
                print("Please enter a valid number!")
    
            while True: 
                try:
                    print_table(drinks)
                    drink_id = int(input("Please select a drink: "))
                    drink_val = drinks.get(drink_id) 
                    break
                except ValueError: 
                    pass
                print("Please enter a valid number!")

            fav_drinks.update({person_val: drink_val})
            
            #with open('drinkslist.txt', 'w+') as text_file:
             #   text_file.write(str(fav_drinks))
            
            #with open('drinkslist.txt', 'r') as text_file:
             #   text_file = text_file.read()
              #  print(text_file)

           

            time.sleep(3)
        elif option == 5: 
            print("Goodbye!")
            time.sleep(3)
            exit()
        else: 
            print("Please choose a number from 1-5")

app()

class Round:

    def __init__(self, buyer_name, drinks, price):
        self.name = buyer_name
        self.drinks = drinks
        self.price = price

round1 = Round("Kajal", "Beer, Wine, Juice", 15.00)

print(round1.buyer_name)
print(round1.drinks)
print(round1.price)

class Drink: 

    def __init__(self, name, price, temp, vol, alcoholic):
        self.name = drinkname
        self.price = drinkprice 
        self.temp = drinktemp 
        self.vol = drinkvol
        self.alcoholic = drinkalcoholic

