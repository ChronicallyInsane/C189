import unittest as ut
import Module6.more_functions.inner_functions_assignment as ifa


class MyTestCase(ut.TestCase):

    def test_measurements_rectangle(self):
        self.assertEqual(ifa.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(ifa .measurements([3.5]),  -1)


if __name__ == '__main__':
    ut.main()
