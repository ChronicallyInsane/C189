from Module8.more_fun_with_collections import dict_membership
import unittest as ut


class TestList(ut.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'A'), True)

    def test_in_dict_false(self):
        self.assertNotEqual(dict_membership.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'G'), True)


if __name__ == '__main__':
    ut.main()
