"""
Author: Evan
Date: TBD
Purpose: Class based Programming.
"""

from datetime import datetime, timedelta


class Employee:
    '''Employee Class '''

    # Constructor
    def __init__(self, lname, fname, num="1231231234", addr="123 Python Rd.\n Ames, IA"):
        self.last_name = lname
        self.first_name = fname
        self.number = num
        self.address = addr

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_phone_number(self, num):
        self.number = num

    def set_address(self, addr):
        self.address = addr

    def display(self):
        print("{}, {}\n{}\n{}".format(self.last_name, self.first_name, self.number, self.address))


class SalariedEmployee(Employee):
    # derived class
    def __init__(self, lname, fname, start_date, salary):
        super.__init__(lname, fname)
        self.SD = start_date
        self.sal = salary

    def give_raise(self, salary):
        sal = salary

    def display(self):
        print("{}, {}, \nSalary:{}\nStart Date: {}".format(self.last_name, self.first_name, self.sal, self.SD))


class HourlyEmployee(Employee):
    # derived class of Employee
    def __init__(self, lname, fname, h_pay, start_date):
        super.__init__(lname, fname)
        self.hourly = h_pay
        self.SD = start_date

    def give_raise(self, n_pay):
        self.hourly = n_pay

    def display(self):
        print("{}, {}, \nHourly Pay:{}\nStart Date: {}".format(self.last_name, self.first_name, self.hourly, self.SD))


# driver
#book = Employee("book", "Shepard", 1, "Space, the final frontier ")
SE = SalariedEmployee("book","Shepard", datetime.now(), 40000)
SE.set_address("Space, the final frontier")
SE.display()
SE.give_raise(45000)
SE.display()
del SE

HE = HourlyEmployee("book","Shepard", datetime.now(), 10.00)
HE.set_address("Misery")
HE.display()
HE.give_raise(12.00)
HE.display()
del HE
