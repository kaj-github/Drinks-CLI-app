import os 

class Person:
    def __init__(self, name):
        self.name = name


class Drink:
    def __init__(self, name):
        self.name = name


class Preference:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink


class Round:
    def __init__(self):
        self.active = False
        self.order = []

    def add_to_order(self, person, Drink):
        if self.active == True:
            self.order.append(Preference(person, drink))

    def set_active(self, status):
        self.active = status 

   
def read_lines(file_name): 
    try: 
        the_file = open(file_name, "r")
        lines = the_file.readlines()
    except: 
        return[]
    return lines 

def get_people(): 
    lines = read_lines("people.txt")
    data = [] 
    for line in lines: 
        data.append(Person(line.strip()))
    return data 

def get_drinks(): 
    lines = read_lines("drinks.txt")
    data = [] 
    for line in lines: 
        data.append(Drink(line.strip()))
    return data


#def save_option(some_file, some_data): 
  #  with open(some_file, mode = "w")

#need to define a write option that appends the drinks and person csv 
#also need one to append favourites 



#def create_person(): 
    #lines = read_lines("people.txt")
    #data = []
    #for line in lines: 
     #   data.append(Person(line.strip()))
    #return data
#change this to open csv file rather than txt file



#def create_drink(): 
 #   lines = read_lines("drinks.txt")
  #  data = []
   # for line in lines: 
    #    data.append(Person(line.strip()))
    #return data
#change this to open csv file rather than txt file


people = get_people()
drinks = get_drinks() 
prefs = {} 

def cls(): 
    os.system("clear")

def print_dict(a_dict, title, prop): 
    cls()
    print(title.upper())
    print('==' * 20)
    for key, val in a_dict.items(): 
        print(getattr(key, prop), "\t" + getattr(val, prop))

def print_list(a_list, title, prop): 
    cls()
    print(title.upper())
    print('==' * 20)
    idx = 0 
    for item in a_list: 
        print(idx, "\t" + getattr(item, prop))
        idx += 1

#def read_data(file_name):

 #   data = {}

  #  try:
    #    the_file = open(file_name, "r")
   #     lines = the_file.readlines()

     #   for line in lines:  # '0, Beer'
       #     [key, val] = line.split(', ')  # ['0','Beer']
      #      try:
        #        data.update({int(key): val.strip()})
         #   except:
          #      data.update({key: val.strip()})

        #the_file.close()

    #except FileNotFoundError:
     #   print(f"{file_name} not found")

    #return data


#def write_data(file_name, data):
 #   try:
  #      the_file = open(file_name, "w")
#
   #     for key, val in data.items():
 #           the_file.write(str(key) + ", " + val + "\n")
  #  finally:
    #    the_file.close()
        
menu = """

Please select your choice: 

=============================
|| [1] List of people      ||
|| [2] List of drinks      ||
|| [3] Create a person     ||
|| [4] Create a drink      ||
|| [5] Create a preference ||
|| [6] Exit menu           ||
=============================
"""

exit_option = 7 

print(menu)

cls() 

option = int(input("Please select a number."))

if option == 1: 
    print_list(people, "People", "name")
elif option == 2: 
    print_list(drinks, "Drinks", "name")
elif option == 3: 
    print_dict(prefs, "Preferences", "name")
elif option == 4: 
    new_person = input("Please enter a name")
    f = open("people.txt", "a")
    person_file = "\n" + new_person
    f.write(person_file)
    f.close()
elif option == 5: 
    new_drink = input("Please enter the name of the drink")
    f = open("drinks.txt", "a")
    drink_file = "\n" + new_drink
    f.write(drink_file)
    print(drink_file)
    f.close()
#elif option == 6: 
   # selected_person = None 
    #selected_drink = None 

    #print_list(people, "People", "name")
    #while selected_person == None: 
     #   try: 
      #      person_id = int(input("Please select a person"))
       #     selected_person = people[person_id] 
        #except:
         #   pass
    #print_list(drinks, "Drinks", "name")

    #while selected_drink == None: 
     #   try: 
      #      drink_id = int(input("Please select a drink"))
       #     selected_drink = drinks[drink_id]
        #except: 
         #   pass

       # new_pref = Preference(selected_person, selected_drink)
        #prefs.update = ({new_pref.person: new_pref.drink})