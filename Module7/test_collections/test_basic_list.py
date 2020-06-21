from Module7.fun_with_collections import basic_list
import unittest
from unittest.mock import patch


class TestList(unittest.TestCase):
    @patch('basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
