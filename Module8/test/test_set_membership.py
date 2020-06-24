from Module8.more_fun_with_collections import set_membership
import unittest as ut


class TestList(ut.TestCase):

    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set({1, 2, 3, 4}, 1), True)

    def test_in_set_false(self):
        self.assertEqual(set_membership.in_set({1, 2, 3, 4}, 7), True)


if __name__ == '__main__':
    ut.main()
