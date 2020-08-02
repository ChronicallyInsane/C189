"""
Author: Evan
Date: 7-24 -- 8-2
Purpose: Final Project, A game of battleships
"""

from random import randint


class Gameboard:
    def __init__(self, x_size=10, y_size=10):  # defines gameworld made up of gridded segments.
        self.world = [[0]*y_size]*x_size
        for i in range(0, x_size):
            for j in range(0, y_size):
                self.world[j][i] = Ship(0, Position(i, j, x_size, y_size))
        self.populated = 0  # whether a board has been 'made' yet; 0 for no, 1 for yes
        self.x = x_size
        self.y = y_size

    def __str__(self):

    def populate(board):
        shipJournal = {"shuttle": 0, "destroyer": 0, "frigate": 0, "carrier": 0, "battleship": 0}
        i=1
        while board.populated != 1:
            randx = randint(0, board.x)
            randy = randint(0, board.y)



        """
        Populates a gameboard,
        0 for ocean,
        1 for shuttle,
        2 for destroyer
        3 for frigate,
        4 for carrier,
        5 for battleship
        :return: populated Gameboard object
        """

    def fire(self, Ship):
        if Ship.getclass() == 0:  # ocean targeted
            pass
            # print GUI you missed
        elif Ship.facing == 1:
            if Ship.is_sunk() == 0:
                for i in range (Ship.loca)



        # print GUI you hit!


class Position:# x, y coordinate  size is array bounds, non-square boards out of scope of project.
    def __init__(self, x, y, xmax, ymax):
        if x > xmax or y > ymax or x < 0 or y < 0:
            raise IndexError("out of range:{}\n".format(self.size))

        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.journal = []

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        if x > self.xmax or x < 0:
            raise IndexError("out of range:{}\n".format(self.size))
        self.x = x

    def setY(self, y):  # greater than max length or less than zero
        if y > self.ymax or y < 0:
            raise IndexError("out of range:{}\n".format(self.size))

    def setjournal(self, value):
        self.journal.append(value)

    def getjournal(self):
        return self.journal


class Ship:
    def __init__(self, sclass, position, facing=0):  # defines ship object with grid coordinates and destroyed
        self.ShipClass = sclass  # defined above with shiptypes or ocean.

        # Position object, container for x, y coordinates
        if facing == 1 or facing == 2 or facing == 0:
            self.facing = facing  # 1 for horizontal, 2 for vertical, 0 for empty ocean
        else:
            raise ValueError("direction invalid")  # input validation
        self.hit = 0
        self.sunk = 0

    def hit(self):
        self.hit = 1

    def sunk(self):
        self.sunk = 1

    def is_hit(self, hit):
        if hit == 1 or hit == 0:
            self.hit = hit
        else:
            raise ValueError("Invalid Input")

    def is_sunk(self, sunk):
        if sunk == 1 or sunk == 0:
            self.sunk = sunk
        else:
            raise ValueError("Invalid Input")

    def getclass(self):
        return self.ShipClass

    def getposition(self):
        return self.position


w = Gameboard(10, 10)
for i in range(0, 9):
    for j in range(0, 9):
        pass