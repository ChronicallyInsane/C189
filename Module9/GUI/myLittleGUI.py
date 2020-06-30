"""
Author: Evan
Date: too late
Purpose: first GUI -- at least it's easier than the windows toolkit!
"""

import tkinter


def main():
    context = tkinter.Tk()  # menu context
    context.title('Favorite Breakfast!')
    label = tkinter.Label(context, text="No Selection Made")

    def on_button_click():
        label.config(text="Eat More Protein!")

    var1 = tkinter.IntVar()
    check = tkinter.Checkbutton(context, text="Breakfast", variable=var1).grid(row=0)
    var2 = tkinter.IntVar()
    check = tkinter.Checkbutton(context, text="2nd Breakfast", variable=var2).grid(row=1)
    var3 = tkinter.IntVar()
    check = tkinter.Checkbutton(context, text="Lunch", variable=var3).grid(row=2)
    var4 = tkinter.IntVar()
    check = tkinter.Checkbutton(context, text="Dinner", variable=var4).grid(row=3)
    button = tkinter.Button(context, text='ANNIHILATE', width=30, command=context.destroy).grid(row=6)
    context.mainloop()


if __name__ == '__main__':
    main()
