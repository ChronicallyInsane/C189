"""
Author: Evan
Date: 6/22
Purpose; Basic implementation of a dictionary building off of sets in Python
"""


def main():
    d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    in_dict(d, 'A')#yes
    in_dict(d, 'G')#no


def in_dict(dict_t, value):
    for i in dict_t:
        if i == value:
            return True
    return False


if __name__ == '__name__':
    main()
