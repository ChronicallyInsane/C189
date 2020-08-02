"""
Author: Evan
Date: 7-24 -- 8-2
Purpose: Final Project, A game of battleships
"""

from random import randint


class Gameboard:

    def __init__(self, x_size=10, y_size=10):  # defines gameworld made up of gridded segments.
        if x_size < 0 or x_size > 30:
            raise ValueError("bounds too high/low")
        if y_size < 0 or y_size > 30:
            raise ValueError("bounds too high/low")
        self.x = x_size
        self.y = y_size

        self.world = [[Ship(0, Position(j, i, self.y, self.x), 0) for j in range(self.y)] for i in range(self.x)]

        self.populated = 0  # whether a board has been 'made' yet; 0 for no, 1 for yes

    def __str__(self):
        return "Gameboard({}, {})".format(self.x, self.y)

    def populate(board):
        shipJournal = {"shuttle": 0, "destroyer": 0, "frigate": 0, "carrier": 0, "battleship": 0}
        i = 1
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
            if Ship.is_sunk() == 0:
                Ship.is_hit(1)  # impact

        # print GUI you hit!


class Position:  # x, y coordinate  size is array bounds, non-square boards out of scope of project.
    def __init__(self, x, y, xmax, ymax):
        if x > xmax or y > ymax or x < 0 or y < 0:
            raise IndexError("out of range:{}, {}\n".format(self.xmax, self.ymax))

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
            raise IndexError("out of range:{}\n".format(self.xmax))
        self.x = x

    def setY(self, y):  # greater than max length or less than zero
        if y > self.ymax or y < 0:
            raise IndexError("out of range:{}\n".format(self.ymax))

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
        if position.x > position.xmax or position.x < 0:
            raise ValueError("X Location Invalid")

        if position.y > position.ymax or position.y < 0:
            raise ValueError("Y Location Invalid")
        self.position = position
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
        if Ship.isfacing() == 1:
            pass

    def is_sunk(self):
        return self.sunk

    def getclass(self):
        return self.ShipClass

    def getposition(self):
        return self.position

    def isfacing(self):
        return self.facing

    def setworld(self, world):
        self.world = world


w = Gameboard(10, 10)
for i in range(0, 9):
    for j in range(0, 9):
        pass
