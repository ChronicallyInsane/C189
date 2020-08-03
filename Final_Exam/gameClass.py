"""
Author: Evan
Date: 7-24 -- 8-2
Purpose: Final Project, A game of battleships
"""
import tkinter as tk
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
        for i in range(0, self.x):
            for j in range(0, self.y):
                print("{}, {}, {], {}".format(self.world[j][i].getclass(), self.world[j][i].position, self.world[j][i].
                                              isfacing(), self.ispopulated()))

    def __repr__(self):
        print("Gameboard({}, {})".format(self.x, self.y))

    def ispopulated(self):
        return self.populated

    def populate(board):  # This is a hack, but it saves implementation time/bug fixing
        def check_occupied(i, j):
            """
            quick check to determine if square is occipied
            :param col:
            :param row:
            :return:
            """
            try:
                board.world[randy][randx].getclass()
            except IndexError("Out of Range"):
                return -1
            finally:
                return 1

        journal = {"shuttle": 0, "destroyer": 0, "frigate": 0, "carrier": 0, "battleship": 0}
        while board.ispopulated() != 1:
            k = 0
            for v in journal:
                k += journal[v]
                if k == 5:
                    board.populated = 1

            randx = randint(0, board.x - 1)  # random placement of ships
            randy = randint(0, board.y - 1)
            if journal["shuttle"] == 0:  # checks if ship type has been built
                if randint(1, 2) == 1:  # horizontal or vertical
                    if randx or randy > board.x - 1:  # shuttle
                        continue
                    if not check_occupied(randy, randx):
                        continue
                    board.world[randy][randx] = Ship(1, Position(randx, randy, board.x, board.y), 1)
                    journal["shuttle"] = 1
                else:
                    if randx or randy > board.y:
                        continue
                    if not check_occupied(randy, randx):
                        continue
                    board.world[randy][randx] = Ship(1, Position(randx, randy, board.x, board.y), 2)
                    journal["shuttle"] = 1
            if journal["destroyer"] == 0:
                randx = randint(0, board.x - 1)
                randy = randint(0, board.y - 1)
                if randint(1, 2) == 1:
                    if randx + 1 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 1):
                        if not check_occupied(randy, i):
                            continue

                    board.world[randy][randx] = Ship(2, Position(randx, randy, board.x, board.y), 1)
                    board.world[randy][randx + 1] = Ship(2, Position(randx + 1, randy, board.x, board.y), 1)
                    journal["destroyer"] = 1
                else:
                    if randx + 1 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 1):
                        if not check_occupied(i, randx):
                            continue
                    randx = randint(0, board.x - 1)
                    randy = randint(0, board.y - 1)
                    board.world[randy][randx] = Ship(2, Position(randx, randy, board.x, board.y), 2)
                    board.world[randy + 1][randx] = Ship(2, Position(randx, randy + 1, board.x, board.y), 2)
                    journal["destroyer"] = 1
            if journal["frigate"] == 0:
                randx = randint(0, board.x - 1)
                randy = randint(0, board.y - 1)
                if randint(1, 2) == 1:
                    if randx + 2 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 2):
                        if not check_occupied(randy, i):
                            continue
                    board.world[randy][randx] = Ship(3, Position(randx, randy, board.x, board.y), 1)
                    board.world[randy][randx + 1] = Ship(3, Position(randx + 1, randy, board.x, board.y), 1)
                    board.world[randy][randx + 2] = Ship(3, Position(randx + 2, randy, board.x, board.y), 1)

                    journal["frigate"] = 1
                else:
                    randx = randint(0, board.x - 1)
                    randy = randint(0, board.y - 1)
                    if randy + 2 >= board.y or randx >= board.x:
                        continue
                    for i in range(0, 2):
                        if not check_occupied(i, randx):
                            continue
                    board.world[randy][randx] = Ship(3, Position(randx, randy, board.x, board.y), 2)
                    board.world[randy + 1][randx] = Ship(3, Position(randx, randy + 1, board.x, board.y), 2)
                    board.world[randy + 2][randx] = Ship(3, Position(randx, randy + 2, board.x, board.y), 2)
                    journal["frigate"] = 1
            if journal["carrier"] == 0:
                randx = randint(0, board.x - 1)
                randy = randint(0, board.y - 1)
                if randint(1, 2) == 1:
                    if randx + 3 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 3):
                        if not check_occupied(randy, i):
                            continue
                    board.world[randy][randx] = Ship(4, Position(randx, randy, board.x, board.y), 1)
                    board.world[randy][randx + 1] = Ship(4, Position(randx + 1, randy, board.x, board.y), 1)
                    board.world[randy][randx + 2] = Ship(4, Position(randx + 2, randy, board.x, board.y), 1)
                    board.world[randy][randx + 3] = Ship(4, Position(randx + 3, randy, board.x, board.y), 1)

                    journal["carrier"] = 1
                else:
                    randx = randint(0, board.x - 1)
                    randy = randint(0, board.y - 1)
                    if randy + 3 >= board.y or randx >= board.x:
                        continue
                    for i in range(0, 3):
                        if not check_occupied(i, randx):
                            continue
                    board.world[randy][randx] = Ship(4, Position(randx, randy, board.x, board.y), 2)
                    board.world[randy + 1][randx] = Ship(4, Position(randx, randy + 1, board.x, board.y), 2)
                    board.world[randy + 2][randx] = Ship(4, Position(randx, randy + 2, board.x, board.y), 2)
                    board.world[randy + 3][randx] = Ship(4, Position(randx, randy + 3, board.x, board.y), 2)

                    journal["carrier"] = 1
            if journal["battleship"] == 0:
                randx = randint(0, board.x - 1)
                randy = randint(0, board.y - 1)
                if randint(1, 2) == 1:
                    if randx + 4 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 4):
                        if not check_occupied(randy, i):
                            continue
                    board.world[randy][randx] = Ship(5, Position(randx, randy, board.x, board.y), 1)
                    board.world[randy][randx + 1] = Ship(5, Position(randx + 1, randy, board.x, board.y), 1)
                    board.world[randy][randx + 2] = Ship(5, Position(randx + 2, randy, board.x, board.y), 1)
                    board.world[randy][randx + 3] = Ship(5, Position(randx + 3, randy, board.x, board.y), 1)
                    board.world[randy][randx + 4] = Ship(5, Position(randx + 4, randy, board.x, board.y), 1)

                    journal["battleship"] = 1
                else:
                    randx = randint(0, board.x - 1)
                    randy = randint(0, board.y - 1)
                    if randy + 4 >= board.y or randx > board.x:
                        continue
                    for i in range(0, 4):
                        if not check_occupied(i, randx):
                            continue
                    board.world[randy][randx] = Ship(5, Position(randx, randy, board.x, board.y), 2)
                    board.world[randy + 1][randx] = Ship(5, Position(randx, randy + 1, board.x, board.y), 2)
                    board.world[randy + 2][randx] = Ship(5, Position(randx, randy + 2, board.x, board.y), 2)
                    board.world[randy + 3][randx] = Ship(5, Position(randx, randy + 3, board.x, board.y), 2)
                    board.world[randy + 4][randx] = Ship(5, Position(randx, randy + 3, board.x, board.y), 2)

                    journal["battleship"] = 1

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
            return
            # print GUI you missed
        if Ship.is_sunk() == 0:
            Ship.is_hit(1)  # impact
            if Ship.isfacing() == 1:# horizontal
                token = 0
                for i in range(0, self.x):
                    if self.world[Ship.position.y][i].hit() == 1:
                        if self.world[Ship.position.y][i].getclass() == Ship.getclass():
                            Ship.position.setjournal(Ship.position.y, i)
                            token += 1
                if token == Ship.getclass():
                    for i in range(0, len(Ship.position.journal), 2):
                        self.world[Ship.position.getjournal(i)][Ship.position.getjournal(i + 1)].sink()
            else:
                token = 0
                for i in range(0, self.y):
                    if self.world[i][Ship.position.x].hit() == 1:
                        if self.world[i][Ship.position.x].getclass() == Ship.getclass():
                            Ship.position.setjournal(i, Ship.position.x)
                            token += 1
                if token == Ship.getclass():
                    for i in range(0, len(Ship.position.journal), 2):
                        self.world[Ship.position.getjournal(i)][Ship.position.getjournal(i + 1)].sink()

        # print GUI you hit!

    def findship(self, gb, num):
        journ = []
        if num < 0 or num > 5:
            raise ValueError("Bad input")
        for j in range(0, gb.y - 1):
            for i in range(0, gb.x - 1):
                if self.world[j][i].ShipClass == num:
                    journ.append(j)
                    journ.append(i)
        return journ


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

    def setjournal(self, value, val2):
        self.journal.append(value)
        self.journal.append(val2)

    def getjournal(self, i):
        return self.journal[i]


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
        self.damage = 0
        self.sunk = 0

    def hit(self):
        return self.damage

    def sink(self):
        self.sunk = 1
        # GUI print you've sunk my Ship.getClass()!

    def is_hit(self, hit):
        if hit == 1 or hit == 0:
            self.damage = hit
        else:
            raise ValueError("Invalid Input")

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


"""
w = Gameboard(10, 10)
Gameboard.populate(w)
l = []
for i in range(0, w.x):
    for j in range(0, w.y):

        w.fire(w.world[j][i])
        print("{}...{}".format(w.world[j][i].getclass(), w.world[j][i].is_sunk()))


        l = b.findship(b, 1)  # find shuttle class ship, returns list of coords
        for i in range(0, len(l), 2):
            b.fire(b.world[i][i+1])
        for i in range(0, len(l), 2):
            self.assertEqual(b.world[i][i+1].is_sunk(), 1)
"""