"""
Evan
Date: Too Late
Purpose: reverse engineering the invoice class -- since it's closed and I didn't get to it in time.  Blame Corona.

"""
import Module10.class_definitions.customer

# I don't have access to the proper Invoice design Doc (I left it for too late due to IRL difficulties)
# Thus I had to design it based on your example string (thus the imperfections.)
# I hope I accomplished more or less what was intended.

class Invoice:

    def __init__(self, id, customer_c):
        self.cid = id

        self.Customer = customer_c

        self.register = dict()

    def add_item(self, dict_t):

        self.register.update(dict_t)
        #print("added")

    def create_invoice(self):
        print("Customer# {}".format(self.cid))
        print(self.Customer.display(), self.__total_register__())
        #print("created")

    def __total_register__(self):
        total = 0
        for key, value in self.register.items():
            print("{}....${}".format(key, value))
            total += int(value)
        print("Total....{}".format(total))


# Driver
captain_mal = Module10.class_definitions.customer.Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in '
                                                                                              'the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
del captain_mal
del invoice