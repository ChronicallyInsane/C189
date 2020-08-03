import Final_Exam.gameClass as gc

"""
Author : Evan
Purpose: This module reads and writes gameboards from a file
"""
"""
tests
gb = gc.Gameboard(10, 10)
gb.populate()
"""


def write_to_file(gb):
    with open('gameboard.txt', 'w') as reader:
        for j in range(0, gb.y):
            for i in range(0, gb.x):
                reader.write("{} ".format(gb.world[j][i].getclass()))
            reader.write("\n")

    reader.close()


def read_from_file(filename):
    """
    reads gameboard object from file, accepts filename as
    :return: gameboard

    """
    gb = gc.Gameboard(10, 11)
    x = 0

    with open(filename, 'r') as reader:
        page = reader.readline()

        x_1 = len(page)
        y_1 = 0
        gb.x = x_1/2
        c = 0
        while page != '':
            c=0
            for i in range(0, x_1, 2):
                if page[i] == ' ':
                    continue
                if page[i] == "\n":
                    continue

                gb.world[y_1][c].setclass(page[i])
                c+=1
            page = reader.readline()
            y_1 += 1

        reader.close()
        temp = x_1/2
        gb.x = int(temp)
        gb.y = y_1
        gb.populated = 1
        return gb


g = read_from_file("gameboard.txt")
g.__str__()
write_to_file(g)
g.__str__()