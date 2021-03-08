import mysql.connector


mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="demo"
)


def create_person(): 
    mycursor = mydb.cursor()
    person_forename = input("Please type your forename." "\n")
    person_surname = input("Please type your surname." "\n")
    createPersonQuery = "INSERT INTO person(forename, surname) VALUES (%s, %s)"
    mycursor.execute(createPersonQuery, (person_forename, person_surname,))
    mydb.commit()
    mycursor.close()
    mydb.close()

create_person()

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="demo"
    )



def display_drink():
    mycursor = mydb.cursor()
    getDrinkQuery = "SELECT * FROM drink"
    mycursor.execute(getDrinkQuery)
    myresult = mycursor.fetchall()
# print(len(myresult))
    for row in myresult:
        row = Drink(row[0],row[1],row[2])
        print(row)
    mycursor.close()
    mydb.close()


def create_drink(): 
    mycursor = mydb.cursor()
    createDrinkQuery = "INSERT INTO drink (drink_name) VALUES (%s)"
    drink_choice = input("Select a drink please." "\n")
    mycursor.execute(createDrinkQuery, (drink_choice,))
    mydb.commit()
    mycursor.close()
    mydb.close()

def display_person(): 
    mycursor = mydb.cursor()
    getPersonQuery = "SELECT * FROM person"
    mycursor.execute(getPersonQuery)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
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
