import Final_Exam.gameClass as gc


gb = gc.Gameboard(10, 10)
gb.populate()
with open('gameboard.txt', 'w') as reader:
    for j in range(0, gb.y):
        reader.write("\n")
        for i in range(0, gb.x):
            reader.write("{} ".format(gb.world[j][i].getclass()))
reader.close()

