"""
Author: Evan
Date: 6/22
Purpose: Testing Arrays
"""


import unittest as ut
from Module7.fun_with_collections import sort_and_search_array
from unittest.mock import patch


class Testsort(ut.TestCase):
    @patch('Module7.fun_with_collections.sort_and_search_list.sort_list', '[5, 4, 3]')
    def test_sort(self):
        self.assertEqual(sort_and_search_array.sort_list(), "Array('I', [3, 4, 5])")

    def test_search_found(self):
        self.assertEqual(sort_and_search_array.search_list([3, 9, 7], 7), 2)

    def test_search_not_found(self):
        self.assertEqual(sort_and_search_array.search_list([3, 9, 7], 10) - 1)
