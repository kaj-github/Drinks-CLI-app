from classes2 import Drink, Person, Preference
from app_sections import mycursor, display_drink, display_person, display_preference
from importingmysql import db
import time
import unittest
from unittest import mock


#can't get this to work :(
# class TestDisplayDrink(unittest.TestCase):

#     def display_drink_test(self):

#         expected = [(1, "Beer", 8, 300, "Yes")]
#         getDrinkQuery = "SELECT * FROM drink WHERE drink_id = 1"
#         mycursor.execute(getDrinkQuery)
#         actual = mycursor.fetchall()
#         mycursor.close()

#         self.assertEqual(actual, expected)

# if __name__ == "__main__":
#     unittest.main()



# SELECTING DRINKS
def test_selectdrink():

    getDrinkQuery = "SELECT * FROM drink WHERE drink_id = 1"
    mycursor.execute(getDrinkQuery)
    actual = mycursor.fetchall()
    mycursor.close()
    expected = [(1, 'Beer', 8, 300, 'Yes')]

    print(actual)
    print(expected)

    assert actual == expected

# SELECTING PEOPLE

def test_selectperson():

    getPersonQuery = "SELECT * FROM person WHERE person_id = 1"
    mycursor.execute(getPersonQuery)
    actual_person = mycursor.fetchall()
    mycursor.close()
    expected_person = [(1, 'Kajal', 'Patel', 24)]

    print(actual_person)
    print(expected_person)

    assert actual_person == expected_person


test_selectperson()