"""
Author: Evan
Date: too late
Purpose:
"""

import tkinter
import random


class NumberGuesser:

    def __init__(self):
        self.guessed_list = list()
        self.canary = 0

    def add_guess(self, int_t):
        self.guessed_list.append(int_t)

    def check_list(self, j):
        if j in self.guessed_list:
            return 1
        return 0

    def canary_(self):
        return self.canary

    def set_canary(self, i):
        self.canary = i


def main():
    chlist = list()
    start(chlist)


def click(button):
    button..add_guess(button.x)
    if .check_list(button.x):
        context.showinfo("Winner", "You Guess right!")
        NG.set_canary(1)


def start(chlist):
    N = NumberGuesser()
    MAX = 10
    context = tkinter.Tk()  # menu context
    context.title('Number Game!')
    label = tkinter.Label(context, text="Guess a number")
    for i in range(0, MAX):
        chlist.append(tkinter.Button(context, text="{}".format(i),))
        chlist[i].grid(row=i, column=2, command=lambda: click(chlist[i]))
    chlist[MAX+1].append(N)
    chlist[MAX+2].append(context)
    button = tkinter.Button(context, text='ANNIHILATE', width=30, command=context.destroy).grid(row=6, column=1)
    l = random.randint(0, 10)

    while N.canary_() != 1:
        context.mainloop()  # initialize main loop for decision


if __name__ == '__main__':
    main()
