"""
Author: Evan
Date; 6/14
Purpose: while loops

"""


def main():
    badlist()
    correctlist()


def correctlist():
    list1 = []
    print("Enter list size")
    index = int(input())
    i = 0
    while i < index:
        print("Enter a number between one and one hundred (1,100")
        cnum = int(input())
        while cnum > 100 or cnum < 1:
            print("enter correct input")
            cnum = int(input())
        list.append(list1, cnum)
        i += 1
    for j in range(0, len(list1)):
        print(list1[j])


def badlist():
    print("Enter a number between one and one hundred (1,100")
    cnum = int(input())
    list1 = []
    while cnum > 100 or cnum < 1:
        print("Enter a valid number")
        cnum = input()
    list.append(list1, cnum)
    print("print list? y/n")
    cho = input()
    if cho == "y":
        print(list1)


if __name__ == '__main__':
    main()

"""
Errors/observations:  input() is not efficient, as it treats any 
input as a string literal.  I believe I will do more looking into
alternatives that treat input explicitly as an int/float.

"""