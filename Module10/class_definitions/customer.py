"""
Author: Evan
Date: TDB
Purpose: seventh circle of hell.

"""


def chk_id(i):
    try:
        int(i) / 2
    except ValueError:
        print("E'Customer' object has no attribute 'cid'")
        exit(-1)


class Customer:

    def __init__(self, lname, fname, num=1231231234, addr="123 Python Dr.", id=0000000):
        self.last_name = lname
        self.first_name = fname
        self.number = num
        self.address = addr
        chk_id(id)
        self.id_c = id

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def set_lname(self, lname):
        self.last_name = lname

    def set_fname(self, fname):
        self.first_name = fname

    def set_phone_number(self, num):
        self.number = num

    def set_address(self, addr):
        self.address = addr

    def set_id(self, id):
        chk_id(id)
        self.id_c = id

    def display(self):
        print(self.id_c, " ", self.last_name + " " + self.first_name, "\n", self.address, "\n", self.number)


#emp = Customer('Ruiz', 'Matthew')  # call the construtor, needs to have a first and last name in parameter
#emp.set_fname('Matt')
#print(emp.display())  # display returns a str, so print the information
#del emp  # clean up!
#customer2 = Customer('Robert', 'Evanidus')
#customer2.set_id("abcd")
#customer2.display()
#del customer2
