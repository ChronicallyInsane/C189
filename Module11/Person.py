"""
Evan
Date: Too late
Purpose: student/person interaction.  Person design copied as instructed.
"""

class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'
               + self.address.display()
class Student:
    """Student string extending person"""
    def __init__(self, person, major="no major", gpa=0.00, start_date):
        self.Person = person
        self.major = major
        self.gpa = gpa
        self.date = start_date

    def change_major(self, n_major):
        self.major = n_major

    def update_gpa(self, n_gpa):
        self.gpa = n_gpa

    def display(self):
        print(self.Person.display(), "\nGPA: {}".format(self.gpa)+ "\n Major:{}".format(self.major))