"""
Author: Evan
Date: not early enough
Purpose: modularity
"""

AUTHOR = "EVAN"


def hello_world():
    print("Hello World")


def author():
    print("Author: ", AUTHOR)


def print_dict(dict_t):
    for key, value in dict_t:
        print(key, value, "\n")


def print_set(set_t):
    for i in set_t:
        print(set_t[i], "\n")


