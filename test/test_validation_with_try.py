import unittest

from Module3.format_output import average_scores
from Module4.input_validation.validation_with_try import average
from Module3.test.test_average_scores import average_scores


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-95, 89, 78)


if __name__ == '__main__':
    unittest.main()
