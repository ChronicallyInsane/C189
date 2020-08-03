import Final_Exam.gameClass

w = Final_Exam.gameClass.Gameboard(int(input("Enter the max col size")), int(input("enter the max row size")))
Final_Exam.gameClass.Gameboard.populate(w)

"""for i in range(0, w.x):
    for j in range(0, w.y):
        w.fire(w.world[j][i])
        print("{}...{}".format(w.world[j][i].getclass(), w.world[j][i].is_sunk()))
"""
i = 0
j = 0
while w.gameover() != 1:
    x = int(input("Enter the X coordinate"))

    y = int(input("Enter the Y coordinate"))

    w.fire(w.world[j][i])
