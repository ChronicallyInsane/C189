"""
evan
date; too late
purpose: derived classes, newly separated student/person.
"""
from datetime import datetime, timedelta
import Module11.Person as p


class Student(p.Person):
    """Student string extending person"""

    def __init__(self, id, major="Computer Science", gpa=0.00, start_date="00/00/2000"):
        self.major = major
        self.gpa = gpa
        self.date = start_date
        self.id = id

    def change_major(self, n_major):
        self.major = n_major

    def update_gpa(self, n_gpa):
        self.gpa = n_gpa

    def update_date(self):
        self.date = datetime.now()

    def display(self):
        print(self.Person.display(),
              "\nGPA: {}".format(self.gpa) + "\n Major:{}".format(self.major) + "\n Start Date:{}".format(self.date))


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
