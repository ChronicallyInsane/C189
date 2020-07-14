class Customer:
    def __init__(self, lname, fname, num, addr, id):
        self.last_name = lname
        self.first_name = fname
        self.number = num
        self.address = addr
        try:
            id / 2
        except ValueError:
            print("Enter a valid ID")
            exit(-1)
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
        self.id_c = id

    def display(self):
        print(self.id_c, " ", self.last_name + " " + self.first_name, "\n", self.address, "\n", self.number)


emp = Customer('Ruiz', 'Matthew')  # call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())  # display returns a str, so print the information
del emp  # clean up!
