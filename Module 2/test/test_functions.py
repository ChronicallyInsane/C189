"""
Author: Evan
Date: 6/1
Purpose: Test the camper_age_input.py file.
"""


import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, True)

    def test_age(self):
        self.assertEquals(camper_age_input.convert_to_months(2), 24)
        self.assertEquals(camper_age_input.convert_to_months(5), 60)
        self.assertFalse(camper_age_input.convert_to_months(-2), 24)
        self.assertRaises(camper_age_input.convert_to_months("string"))


if __name__ == '_main__':
    unittest.main()





