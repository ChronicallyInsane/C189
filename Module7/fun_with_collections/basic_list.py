"""
Author: Evan
Date: 6/20
Purpose: To demonstrate the usage of lists within a multi-function context
"""


def main():
    list1 = []
    while 1:
        list1 = make_list()
        if list1 == -1:
            continue
        else:
            print(list1)
            exit(1)


def make_list(list = []):
    """
    @:name max_list
    @:param none
    @:returns user input or -1 depending on error level
    """

    print("max list size?")
    MAX = int(input())
    print(MAX)
    for i in range(0, MAX):
        list.append(0)
    for j in range(0, MAX):
        list[j] = get_input()
        if list[j] == -1:
            print("bad input try again")
            list[j] = 0
            j -= 1
        if list[j] < 1 or list[j] > 50:
            raise ValueError

    return list


def get_input():
    """
    :param n/a
    :returns user input, -1 if error
    """
    imp = 0
    print("enter input: ")
    try:
        imp = float(input())
    except ValueError:
        return -1

    return imp


if __name__ == '__main__':
    main()
"""
Errors:
had a nested try/catch statement within the for loop function call chain.  this had the unexpeted behavior of double the input
and breaking the forloop, with the listed inputs exceeding the range.  this was fixed.
"""