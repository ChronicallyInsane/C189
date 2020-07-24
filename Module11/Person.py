"""
Evan
Date: Too late
Purpose: student/person interaction.  Person design copied as instructed.
"""
from datetime import datetime, timedelta


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
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address


class Student:
    """Student string extending person"""

    def __init__(self, person, major="no major", gpa=0.00, start_date="00/00/2000"):
        self.Person = person
        self.major = major
        self.gpa = gpa
        self.date = start_date

    def change_major(self, n_major):
        self.major = n_major

    def update_gpa(self, n_gpa):
        self.gpa = n_gpa

    def update_date(self):
        self.date = datetime.now()

    def display(self):
        print(self.Person.display(),
              "\nGPA: {}".format(self.gpa) + "\n Major:{}".format(self.major) + "\n Start Date:{}".format(self.date))


the_dude = Person("dude", "the", "like, nowhere man")

poor_student = Student(the_dude, "vibing, bro", 4.00)
poor_student.change_major("Being Awesome!")
poor_student.update_gpa(3.00)
poor_student.display()
del poor_student
del the_dude