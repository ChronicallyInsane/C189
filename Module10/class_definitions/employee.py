"""
Author: Evan
Date: TBD
Purpose: Class based Programming.
"""

from datetime import datetime, timedelta


class Employee:
    '''Employee Class '''

    # Constructor
    def __init__(self, lname, fname, num="1231231234", addr="123 Python Rd.\n Ames, IA"
                 , sal=0.0, salied=False):
        self.last_name = lname
        self.first_name = fname
        self.number = num
        self.address = addr
        self.salary = sal
        self.salaried = salied
        self.start_date = datetime.now()

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_phone_number(self, num):
        self.number = num

    def set_salaried(self, boolean):
        self.salaried = boolean

    def set_address(self, addr):
        self.address = addr

    def set_salary(self, sal):
        self.salary = sal

    def display(self):
        print(self.last_name + " " + self.first_name, "\n", self.address, "\n")
        if self.salaried:
            print("Salaried Employee: ", self.salary, "/year\n", "Start Date: ", self.start_date)
        else:
            print("Hourly Employee: ", self.salary, "/hour\n", "Start Date: ", self.start_date)

    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)

    def __repr__(self):
        return 'Person(first_name={}, last_name={}'.format(self.first_name, self.last_name)


emp = Employee('Ruiz', 'Matthew')  # call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())  # display returns a str, so print the information
del emp  # clean up!
