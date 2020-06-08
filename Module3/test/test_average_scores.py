"""
Author:evan
Purpose: To test the average function
date:6/7
"""

from Module3.format_output import average_scores
import unittest
import unittest.mock as mock


class MyTestCase(unittest.TestCase):
    def test_average(self):
        # with mock.patch('builtins.input', side_effects=[85, 90, 95]):
        assert average_scores.average(85, 90, 95) == 90
        # with mock.patch('buildins.input', side_effects=[42, 25, 56]):
        assert average_scores.average(42, 25, 56) == 41
        # with mock.patch('buildins.input', side_effects=[95, 25, 56]):
        assert average_scores.average(95, 25, 56) == 41


if __name__ == '__main__':
    unittest.main()
