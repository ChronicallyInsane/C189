from Module8.more_fun_with_collections import set_membership
import unittest
from unittest.mock import patch


class TestList(unittest.TestCase):

    def test_in_set_true(self):
        unittest.assertEquals(set_membership.in_set({1, 2, 3, 4}, 1), True)
    def test_in_set_false(self):
        unittest.assertNotEquals(set_membership.in_set({1, 2, 3, 4}, 7), True)


if __name__ == '__main__':
    unittest.main()
