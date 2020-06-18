import unittest as ut
from Module6.more_functions import string_functions


class MyTestCase(ut.TestCase):

    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string("Ayah", 3.0), "AyahAyahAyah")


if __name__ == '__main__':
    ut.main()
