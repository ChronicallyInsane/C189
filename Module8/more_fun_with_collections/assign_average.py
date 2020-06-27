"""
Author: Evan
Date: later than it should be
purpose: very, very messy switch statement.
"""


def main():
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'a': 0.5, 'b': 0.25}
    switch_average(d, input("enter Key, A-E, a-b"))


def switch_average(dict_t, i):
    index = ret_key(dict_t, i)
    if index == 1:
        print("you selected A")
        return 'B'
    elif index == 2:
        print("you selected B")
        return 'C'
    elif index == 3:
        print("you selected C")
        return 'D'
    elif index == 4:
        print("you selected D")
        return 'E'
    elif index == 5:
        print("you selected E")
        return 'a'
    elif index == 0.5:
        print("you selected a")
        return 'b'
    elif index == 0.25:
        print("you selected b")
        return 'A'
    else:
        print("input not recognized")
        return -1


def ret_key(dict_t, i):
    for key, value in dict_t.items():
        if i == key:
            return value


if __name__ == '__main__':
    main()
