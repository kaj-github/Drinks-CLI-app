import mysql.connector

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="demo"
)

# welcome_msg = "welcome, please select an option."
# print(welcome_msg)
# insert_forename = input("What is your first name?")
# insert_surname = input("What is your last name?")

# mycursor = mydb.cursor()
# getPeopleQuery = "SELECT * FROM People"
# createPersonQuery = "INSERT INTO People (forename, surname) VALUES (s%, s%)"
# mycursor.execute(getPeopleQuery)
# myresult = mycursor.fetchall()
# print(len(myresult))
# for row in myresult:
#     print(row)

# mycursor.execute(createPersonQuery, (insert_forename, insert_surname"))
# mydb.commit()
# mycursor.close()
# mydb.close()


# mycursor = mydb.cursor()
# id_choice = input("Create drink ID")
# drink_choice = input("Select a drink.")

# print(drink_choice)

# createDrinkQuery = "INSERT INTO drink (drink_id, drink_name) VALUES (%s, %s)"
# mycursor.execute(createDrinkQuery, (id_choice, drink_choice))
# mydb.commit()


# getDrinkQuery = "SELECT * FROM drink"
# mycursor.execute(getDrinkQuery)
# myresult = mycursor.fetchall()
# # print(len(myresult))
# for row in myresult:
#      print(row)
# mycursor.close()
# mydb.close()

def display_preference(): 
    mycursor = mydb.cursor()

    preference = "SELECT person.person_forename, drink.drink_name FROM person LEFT JOIN drink ON person.person_id = drink.drink_id"

    mycursor.execute(preference)
    myresult = mycursor.fetchall()

    for x in myresult: 
        print(x)

    mycursor.close()
    mydb.close()

display_preference()

class Drink:

    def __init__(self, drink_id, drink_name):
        self.drink_id = drink_id
        self.drink_name = drink_name
        # self.price = drinkprice
        # self.temp = drinktemp
        # self.vol = drinkvol
        # self.alcoholic = drinkalcoholic

#ask user if drink is alcolic or non alcoholic 
#eg drink_quest = input("is your drink alcoholic?")
#if drink_quest = yes
    #drink_price = 8.00


    def __str__(self):
        return str(self.drink_id) + "\t" + str(self.drink_name)
#do for each item

        
class Person:

    def __init__(self, firstname, age, networth):
        self.firstname = firstname
        self.age = age
        self.networth = networth

def display_drink():
    mycursor = mydb.cursor()
    getDrinkQuery = "SELECT * FROM drink"
    mycursor.execute(getDrinkQuery)
    myresult = mycursor.fetchall()
    for row in myresult:
        row = Drink(row[0],row[1])
        print(row)
    mycursor.close()
    mydb.close()

display_drink()


def display_drink():
    try:
        getDrinkQuery = "SELECT * FROM drink"
        mycursor.execute(getDrinkQuery)
        myresult = mycursor.fetchall()
    
#*** trying to get it to print headers
    
    #num_fields = len(mycursor.description)
    # field_names = [i[0] for i in mycursor.description]
    # print(field_names)
    # columns = mycursor.description 
    # result = [{columns[index][0]:column for index, column in enumerate(value)} for value in myresult()]
    # print(result)
        print("DRINKS")
        for row in myresult:
            row = Drink(row[0], row[1], row[2], row[3], row[4])
            print(row)
        time.sleep(8)
    except:
        print("Sorry, we could not process your request. Please try again later or speak to a member of staff.")
# def display_drink():
#     mycursor = mydb.cursor()
#     getDrinkQuery = "SELECT * FROM drink"
#     mycursor.execute(getDrinkQuery)
#     myresult = mycursor.fetchall()
    
    #*** trying to get it to print headers
    
    #num_fields = len(mycursor.description)
    
    # field_names = [i[0] for i in mycursor.description]
    # print(field_names)


    # columns = mycursor.description 
    # result = [{columns[index][0]:column for index, column in enumerate(value)} for value in myresult()]
    # print(result)

    # for row in myresult:
    #     row = Drink(row[0], row[1], row[2], row[3], row[4])
    #     print(row)
    # mycursor.close()
    # mydb.close()

#display_drink()


# def display_person(): 
#     mycursor = mydb.cursor()
#     getPersonQuery = "SELECT * FROM person"
#     mycursor.execute(getPersonQuery)
#     myresult = mycursor.fetchall()
#     for row in myresult:
#         row = Person(row[0], row[1], row[2], row[3])
#         print(row)
#     mycursor.close()
#     mydb.close()

# display_person()
# display_drink()
