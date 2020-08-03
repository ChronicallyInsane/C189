import unittest as ut
import Final_Exam.gameClass

"""
Author: Evan
Purpose: Various tests for the battleship project
"""


class TestB(ut.TestCase):
    def test_A(self):
        b = Final_Exam.gameClass.Gameboard(10, 10)  # populates a grid of size 10 x 10
        b.populate()  # populates the grid
        l = []
        l = b.findship(b, 1)  # find shuttle class ship, returns list of coords
        for i in range(0, len(l), 2):
            b.fire(b.world[l[i]][l[i + 1]])
        x = l[0]
        y = l[1]
        self.assertEqual(b.world[l[0]][l[1]].is_sunk(), 1)  # passes intermittently, based on rand -- quite vexing
        # fixed

    def test_b(self):
        b = Final_Exam.gameClass.Gameboard(10, 10)  # populates a grid of size 10 x 10
        b.populate()  # populates the grid
        self.assertEqual(b.x, 10)  # tests initialization

    def test_c(self):  # tests input validation
        b = 0
        with self.assertRaises(ValueError):
            Final_Exam.gameClass.Gameboard(-1, 10)  # populates a grid of size 10 x 10

    def test_d(self):  # tests facing assignment, call
        b = Final_Exam.gameClass.Ship(5, Final_Exam.gameClass.Position(1, 2, 10, 10), 2)
        self.assertEqual(b.isfacing(), 2)

    def test_e(self):  # tests input validation for Position entities
        with self.assertRaises(IndexError):
            Final_Exam.gameClass.Position(1, 2, 10, -1)

    def test_f(self):  # tests findship
        g = Final_Exam.gameClass.Gameboard()
        s = Final_Exam.gameClass.Ship(1, Final_Exam.gameClass.Position(1, 2, 10, 10), 2)
        g.world[2][1] = s
        a = g.findship(g, 1)
        b = []
        b.append(2)
        b.append(1)
        self.assertEqual(a, b)

    def test_g(self):  # #tests replaceship
        g = Final_Exam.gameClass.Gameboard()
        g.replaceship(g, 2, 1, 2, 1)
        a = g.findship(g, 2)
        b = []
        b.append(9)
        b.append(0)
        b.append(9)
        b.append(1)
        self.assertEqual(a, b)
