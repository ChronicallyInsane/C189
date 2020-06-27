from Module8.more_fun_with_collections import assign_average
import unittest as ut


class TestList(ut.TestCase):
    def test_A_return(self):
        self.assertEqual(assign_average.switch_average())


if __name__ == '__main__':
    ut.main()
