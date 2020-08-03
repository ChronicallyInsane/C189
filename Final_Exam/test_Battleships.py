import unittest as ut
import Final_Exam.gameClass


class TestB(ut.TestCase):
    def test_A(self):
        b = Final_Exam.gameClass.Gameboard(10, 10)  # populates a grid of size 10 x 10
        b.populate()  # populates the grid
        l = []
        l = b.findship(b, 1)  # find shuttle class ship, returns list of coords
        for i in range(0, len(l), 2):
            b.fire(b.world[i][i+1])
        for i in range(0, len(l), 2):
            self.assertEqual(b.world[i][i+1].is_sunk(), 1)  # passes intermittently, based on rand -- quite vexing

    def test_b(self):
        b = Final_Exam.gameClass.Gameboard(10, 10)  # populates a grid of size 10 x 10
        b.populate()  # populates the grid
        self.assertEqual(b.x, 10) # tests initialization

    def test_c(self):
        b = Final_Exam.gameClass.Gameboard(10, 10)  # populates a grid of size 10 x 10
        b.populate()  # populates the grid
        self.assertEqual()