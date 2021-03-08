class Drink:

    def __init__(self, drink_id, drink_name, drink_price, drink_volume, drink_alcoholic):
        self.drink_id = drink_id
        self.drink_name = drink_name
        self.drink_price = drink_price
        self.drink_volume = drink_volume
        self.drink_alcoholic = drink_alcoholic 

    def __str__(self):
            print("~="*25)
            return str(self.drink_id) + "\t" + str(self.drink_name) + "\t"*2 + str(self.drink_price) + "\t" + str(self.drink_volume) + "\t"+ str(self.drink_alcoholic)

class Person:

    def __init__(self, person_id, person_forename, person_surname, person_age):
        self.person_id = person_id
        self.person_forename = person_forename
        self.person_surname = person_surname
        self.person_age = person_age

    def __str__(self):
            print("~="*25)
            return str(self.person_id) + "\t" + str(self.person_forename) + "\t"*2  + str(self.person_surname) + "\t"*2 + str(self.person_age)
        

class Preference: 
    def __init__(self, person_forename, drink_name):
        self.person_forename = person_forename
        self.drink_name = drink_name

    def __str__(self): 
        print("~="*15)
        return str(self.person_forename) + "\t" + str(self.drink_name)

