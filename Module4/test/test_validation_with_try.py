import unittest

import Module3.format_output.average_scores
from Module3.test.test_average_scores import average_scores


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average_scores.average(-90, 89, 78)

    def test_average_negative_input(self):
        with self.ssertRaises(ValueError):
            average_scores.average(-95, 89, 78)
