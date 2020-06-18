import unittest
from Module6 import more_functions
class MyTestCase(unittest.TestCase):

    def test_multiple_string(self):
        unittest.assertEquals(multiply_string("Ayah", 3.0),"AyahAyahAyah")


if __name__ == '__main__':
    unittest.main()

