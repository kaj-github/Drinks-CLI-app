import mysql.connector

mydb = mysql.connector.connect(
    port="33066",
    user="root",
    password="insecure",
    database="demo"
)

#print(mydb)
#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM People")
#myresult = mycursor.fetchall()

#print(len(myresult))
#print(myresult)

mycursor = mydb.cursor()
getPeopleQuery = "SELECT * FROM People"
createPersonQuery = "INSERT INTO People (forename, surname) VALUES (%s, %s)"
mycursor.execute(getPeopleQuery)
myresult = mycursor.fetchall()
print(len(myresult))
for row in myresult:
    print(row)

mycursor.execute(createPersonQuery, ("Jay", "Son"))
mydb.commit()
mycursor.close()
mydb.close()

#mycursor.execute(createPersonQuery, ("Marge", "Simpson"))

mycursor = mydb.cursor()
getPeopleQuery = "SELECT * FROM People"
createPersonQuery = "INSERT INTO People (forename, surname) VALUES (%s, %s)"
mycursor.execute(getPeopleQuery)
myresult = mycursor.fetchall()
print(len(myresult))
for row in myresult:
    print(row)

mycursor = mydb.cursor()
getDrinkQuery = "SELECT * FROM Drinks"
# createDrinkQuery = "INSERT INTO Drinks (Drink_name) VALUES (%s)"
mycursor.execute(getDrinkQuery)
myresult = mycursor.fetchall()
print(len(myresult))
for row in myresult:
    print(row)
mycursor.close()
mydb.close()