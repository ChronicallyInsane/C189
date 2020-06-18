"""
Author:Evan
Date: 6/14
Purpose: Playing with loops
"""


def main():
    fplist = [42.0, 256.2, 192.5]
    for i in range(0, 3):
        print(fplist[i])
    for j in range(100, 32, -1):
        if j % 2 > 0:
            print(j)


if __name__ == '__main__':
    main()

"""
Errors: used the wrong index to print odd numbers, lots of confusion.
"""