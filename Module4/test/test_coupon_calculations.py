import unittest
from Module4.store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        unittest.assertEquals(calculate_price(8,5,10),2.7)
        unittest.assertEquals(calculate_price(9,4,15),2.5)
        unittest.assertEquals(calculate_price(6,5,20),0.8)
        unittest.assertEquals(calculate_price(9,10,10),-1.2)

    def test_price_under_between_ten_thirty(self):
        unittest.assertEquals(calculate_price(10,5,10),4.5)
        unittest.assertEquals(calculate_price(12,6,15),5.1)
        unittest.assertEquals(calculate_price(15,1,20),11.2)
        unittest.assertEquals(calculate_price(30,10,50),10)

    def test_price_under_between_thirty_fifty(self):
        pass

    def test_price_under_over_fifty(self):
        pass


if __name__ == '__main__':
    unittest.main()
