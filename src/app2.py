

def create_drink(): 
    mycursor = mydb.cursor()
    drink_choice = input("Select a drink please." /n)
    createDrinkQuery = "INSERT INTO drink (drink_name) VALUES (%s)"
    mycursor.execute(createDrinkQuery, (drink_choice))
    mydb.commit()
    mycursor.close()
    mydb.close()


def display_drink():
    
    mycursor = mydb.cursor()
    getDrinkQuery = "SELECT * FROM drink"
    mycursor.execute(getDrinkQuery)
    myresult = mycursor.fetchall()
# print(len(myresult))
    print(myresult)
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
    person_choice = input("Please choose a person." /n)
    createPersonQuery = "INSERT INTO person(drink_choice) VALUES (%s)"
    mycursor.execut(createDrinkQuery, (person_choice))
    mydb.commit()
    mycursor.close()
    mydb.close()



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

print(menu)