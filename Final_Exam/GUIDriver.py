import tkinter as tk
import Final_Exam.gameClass as BS


def main():
    def pressed(i, j):
        selection = i
        butlist[i][j]["state"]=tk.DISABLED

    def start(i):
        for button in butlist:
            button["state"] = tk.NORMAL

    def stop(i):
        Window.destroy()
    game = BS.Gameboard(10, 10)
    game.populate()
    Window = tk.Tk()
    Window.title("BattleShips!")
    label = tk.Label(Window, text="Guess Squares and try to sink the enemy fleet!")
    label0 = tk.Label(Window, text="*************************************************")
    label.grid(row=0, column=0)
    label0.grid(row=1, column=0)
    butlist = [[0 for j in range(0, game.y)] for i in range(0, game.x)]
    start_i = []
    end = []
    for i in range(0, 1):
        startGame = tk.Button(Window, text="Start", command=lambda: start(i))
        endGame = tk.Button(Window, text="Stop", command=lambda index=i : stop(i))
        start_i.append(startGame)
        end.append(endGame)
    start_i[0].grid(row=15, column=0)
    end[0].grid(row=16, column=0)
    for j in range(0, game.y):
        for i in range(0, game.x):
            button = tk.Button(Window, text=0, command=lambda index=i: pressed(index, j))
            butlist[j][i] = button

    for j in range(0, game.y):
        for i in range(0, game.x):
            butlist[j][i].grid(row=j+5, column=i+2)
    Window.mainloop()




if __name__ == '__main__':
    main()
