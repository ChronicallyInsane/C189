from Module7.fun_with_collections import basic_list_exception
import unittest
from unittest.mock import patch


class TestList(unittest.TestCase):
    @patch('Module7.fun_with_collections.basic_list_exception.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic_list_exception.make_list(), [5, 5, 5])

    @patch('Module7.fun_with_collections.basic_list.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list_exception.make_list()  # call the function!

    def test_make_list_below_range(self, input):
        self.assertRaises(basic_list_exception.make_list(), [-1, 5, 10])



if __name__ == '__main__':
    unittest.main()
