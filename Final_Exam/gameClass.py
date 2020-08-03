"""
Author: Evan
Date: 7-24 -- 8-2
Purpose: Final Project, A game of battleships

In Depth Walkthrough (README)

This is a modular, object-oriented battleships game.  The primary piece is the Gameboard, a 2D array of Ship objects.
A Ship object is an all-encompassing container for either empty ocean, or the 5 different types of ships
0 -- ocean
1 -- shuttle
2 -- destroyer
3 -- frigate
4 -- carrier
5 -- battleship
The Ship object has various stats associated with it (damaged, sunk, which direction it is facing)
The Primary gameloop consists of the player inputting sizes for the gameboard, and the program --
populating the board accordingly.
This can be played with or without the GUI.
"""
import tkinter as tk
from random import randint


class Gameboard:

    def __init__(self, x_size=10, y_size=10):  # defines gameworld made up of gridded segments.
        if x_size < 6 or x_size > 30:
            raise ValueError("bounds too high/low")

        if y_size < 6 or y_size > 30:
            raise ValueError("bounds too high/low")

        self.x = x_size
        self.y = y_size

        self.world = [[Ship(0, Position(j, i, self.y, self.x), 0) for j in range(self.y)] for i in range(self.x)]

        self.populated = 0  # whether a board has been 'made' yet; 0 for no, 1 for yes
        self.over = 0

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
        def check_occupied(i, j):  # randomly places ships in a manner that they stay in-bounds and don't overlap.
            """
            quick check to determine if square is occipied
            :param col:
            :param row:
            :return:
            """
            try:
                board.world[j][i].getclass()
            except IndexError("Out of Range"):
                return -1
            finally:
                if board.world[j][i].getclass() != 0:
                    return -1
                return 1

        journal = {"shuttle": 0, "destroyer": 0, "frigate": 0, "carrier": 0, "battleship": 0}
        while board.ispopulated() != 1:
            k = 0
            for v in journal:
                k += journal[v]
                if k == 5:  # checks if all five ships have been implemented before defining populated
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
                    randx = randint(0, board.x - 1)
                    randy = randint(0, board.y - 1)
                    if randx + 1 >= board.x - 1 or randy >= board.y:  # destroyer
                        continue
                    for i in range(0, 1):
                        if not check_occupied(i, randx):
                            continue
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
        try:
            b = Ship
        except ValueError:
            print("Bad input, try again")
            return

        if Ship.getclass() == 0:  # ocean targeted
            print("You Missed!\n")
            return
            # print GUI you missed
        if Ship.is_sunk() == 0:
            Ship.is_hit(1)  # impact
            print("You Hit!\n")
            if Ship.isfacing() == 1:  # horizontal
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
    def gameover(self): # checks for all ships sunk, if so gameover
        token = 0
        for j in range(0, self.y):
            for i in range(0, self.x):
                for k in range(1, 5):
                    if self.world[j][i].is_sunk() == 1:
                        token +=1
        if token == 5:
            self.over = 1
            return 1
        else:
            return -1

    def findship(self, gb, num):
        journ = []
        if num < 0 or num > 5:
            raise ValueError("Bad input")
        for j in range(0, gb.y):
            for i in range(0, gb.x):
                if self.world[j][i].ShipClass == num:
                    journ.append(j)
                    journ.append(i)
        return journ

    def replaceship(self, gb, num, x, y, dir):
        def check_occupied(i, j):  # randomly places ships in a manner that they stay in-bounds and don't overlap.
            """
            quick check to determine if square is occipied
            :param col:
            :param row:
            :return:
            """
            try:
                gb.world[y][x].getclass()
            except IndexError("Out of Range"):
                return -1
            finally:
                if gb.world[y][x].getclass()!=0:
                    return -1
                return 1

        if num < 0 or num > 5 or dir < 1 or dir > 2:
            raise ValueError("Bad input")
        for j in range(0, gb.y):
            for i in range(0, gb.x):
                if gb.world[j][i].ShipClass == num:
                    gb.world[j][i].setclass(0)
        if dir == 1:
            for k in range(0, num):
                if check_occupied(k, j) == -1:
                    raise ValueError("Overlapping Values")
                    return
            for k in range(0, num):
                gb.world[j][k].setclass(num)
        else:
            for k in range(0, num):
                if check_occupied(i, k) == -1:
                    raise ValueError("Overlapping Values")
                    return
            for k in range(0, num):
                gb.world[k][i].setclass(num)


class Position:  # x, y coordinate  size is array bounds, non-square boards out of scope of project.
    def __init__(self, x, y, xmax, ymax):
        if x > xmax or y > ymax or x < 0 or y < 0 or xmax < 0 or ymax < 0:
            raise IndexError("out of range:{}, {}\n".format(xmax, ymax))

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

    def is_sunk(self): # 1 for sunk, 0 for not
        return self.sunk

    def getclass(self): #explained above
        return self.ShipClass

    def getposition(self): #returns position object
        return self.position

    def isfacing(self): # returns direction ship is facing
        return self.facing

    def setworld(self, world): # #largely superfluous
        self.world = world

    def setclass(self, i): # change class on ship object
        if i < 0 or i > 5:
            raise ValueError("Bad Input")
        self.ShipClass = i


