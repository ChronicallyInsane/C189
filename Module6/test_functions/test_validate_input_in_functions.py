import unittest as ut
from Module6.more_functions import validate_input_in_functions as val


class MyTestCase(ut.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(val.score_input("test_name"), "test_name: 0")  # tests name, and mandatory functions

    def test_score_input_test_score_valid(self):
        self.assertEqual(val.score_input("name", 50), "name: 50")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(val.score_input("name", -1), -1)

    def test_score_input_test_score_above_range(self):
        self.assertEqual(val.score_input("name", 101), -1)

    def test_test_score_non_numeric(self):
        self.assertRaises(val.score_input("test", "test"))


if __name__ == '__main__':
    ut.main()
