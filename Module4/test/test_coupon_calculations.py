"""
Author: Evan
Purpose: test coupon calc
date: 6/9

"""

import unittest
from Module4.store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(calculate_price(8.0, 5.0, 10.0), 2.7)
        self.assertAlmostEqual(calculate_price(9.0, 4.0, 15.0), 2.5)
        self.assertAlmostEqual(calculate_price(6.0, 5.0, 20.0), 0.8)
        self.assertAlmostEqual(calculate_price(9.0, 10.0, 10.0), -0.9)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(calculate_price(10.0, 5.0, 10.0), 4.5)
        self.assertAlmostEqual(calculate_price(12.0, 6.0, 15.0), 5.1)
        self.assertAlmostEqual(calculate_price(15.0, 1.0, 20.0), 11.2)
        self.assertAlmostEqual(calculate_price(30.0, 10.0, 50.0), 10.0)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(calculate_price(35.0, 20.0, 30.0), 10.5)
        self.assertAlmostEqual(calculate_price(40.0, 10.0, 40.0), 18.0)
        self.assertAlmostEqual(calculate_price(49.0, 48.0, 50.0), 0.5)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(calculate_price(50, 25, 50), 12.5)
        self.assertAlmostEqual(calculate_price(100, 50, 10), 45)
        self.assertAlmostEqual(calculate_price(90, 50, 10), 36)


if __name__ == '__main__':
    unittest.main()
"""
Errors: function returns total PLUS the shipping, thus throwing tests off.  this has been fixed.
"""