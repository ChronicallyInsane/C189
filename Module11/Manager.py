"""
Evan
Date: too late
Purpose: multiple inheritance.
"""
import Module11.Person as Person
import Module11.employee as Employee
from datetime import datetime, timedelta


class Manager(Employee.SalariedEmployee, Person.Person):

    def __init__(self, lname, fname, pay, department, direct_reports):
        super(Manager, self).__init__(lname, fname, datetime.now(), pay)
        self.Department = department
        self._iterator = 0
        self.direct_reports = list()
        self.direct_reports.append(direct_reports)

    def change_department(self, desired):
        self.Department = desired

    def add_staff(self, employee): # adds employee object to directory
        self.direct_reports.append(employee)

    def print_reports(self):
        for i in range(0, len(self.direct_reports)):
            self.direct_reports[i].display()

#driver
the_dude = Employee.HourlyEmployee("dude", "the", 1.00, datetime.now())
bob = Manager("Robert", "Evanidus", 40000, "tedium", the_dude)
bob.display() #Displays Employee display()
bob.give_raise(42000)
bob.print_reports() #iterates through list of Employee objects
bob.display() # SalariedEmployee display()
del bob
del the_dude