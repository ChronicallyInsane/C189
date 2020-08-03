import Final_Exam.gameClass
"""
Author: Evan
Purpose: Basic Driver to demonstrate functionality.  
"""
w = Final_Exam.gameClass.Gameboard(input("Enter the max col size"), input("enter the max row size"))
Final_Exam.gameClass.Gameboard.populate(w)

"""for i in range(0, w.x):
    for j in range(0, w.y):
        w.fire(w.world[j][i])
        print("{}...{}".format(w.world[j][i].getclass(), w.world[j][i].is_sunk()))
"""
i = 0
j = 0
p = 0
lazy = []
for i in range(1, 6):
    p = w.findship(w,i)[0]
    lazy.append(p)
    p = w.findship(w, i)[1]
    lazy.append(p)
while w.gameover() != 1:
    print("CHEAT: \n1: {} {} \n 2: {} {}\n 3: {} {}\n4: {} {}\n 5: {} {}".format(lazy[0], lazy[1], lazy[2], lazy[3], lazy[4], lazy[5], lazy[6], lazy[7], lazy[8], lazy[9]))
    x = int(input("Enter the X coordinate"))

    y = int(input("Enter the Y coordinate"))
    s = w.world[y][x]
    w.fire(s)
