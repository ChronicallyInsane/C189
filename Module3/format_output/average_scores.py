"""
Author:Evan
Purpose: Testing formatting
Date: 6/7 (unfortunately there was a power outage the night of the seventh, prohibiting submission)
"""


def main():
    read_input()
    exit()


def read_input():
    # i = 1  # i determines which list is used, hardcoded to three for minimalism
    list1 = []

    print("Please enter the first name, last name, age, and three scores.")

    for j in range(0, 6):
        list.append(list1, input())  # j is the iterating value

    print(list1)
    avg = average(int(list1[3]), int(list1[4]), int(list1[5]))
    last_name = list1[1]
    first_name = list1[0]
    age = list1[2]
    print(last_name + "," + first_name + ":" + " " + age + " average grade: ", avg)


def average(one, two, three):
    result = one + two + three
    result = result / 3
    return result


if __name__ == '__main__':
    main()

"""
Tests:
Various combinations of numbers outputting correct averages.
Errors/Problems:  Errors regarding str being unable to be operated on with the / operation.
I realized that because my list was begun with a string, python treated the *whole* list as strings.
I fixed the problem by casting the correct values to int.  
"""