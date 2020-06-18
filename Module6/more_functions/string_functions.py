"""
Author: Evan
Date: 6/17
Purpose: expansion on string handling
"""


def main():
    print(multiply_string("apple", 5))


def multiply_string(string, mult_value):
    if str.isascii(string) != 1:
        print("enter correct string")
        exit(-1)

    return string * int(mult_value)


if __name__ == '__main__':
    main()
