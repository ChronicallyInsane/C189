from Module8.more_fun_with_collections import assign_average
import unittest as ut


class TestList(ut.TestCase):
    def test_A_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},
                                                       'A'), 'B')

    def test_B_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},
                                                       'B'), 'C')

    def test_C_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},
                                                       'C'), 'D')

    def test_D_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},
                                                       'D'), 'E')

    def test_E_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},

                                                       'E'), 'a')

    def test_bad_return(self):
        self.assertEqual(assign_average.switch_average({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25},
                                                       'G'), -1)


if __name__ == '__main__':
    ut.main()
