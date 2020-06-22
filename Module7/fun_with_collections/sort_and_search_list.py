from Module7.fun_with_collections import basic_list

"""
Author: Evan
Date: 6/21
Purpose: sorting and searching lists

"""


def main():
    lst = []

    lst = basic_list.make_list()
    print(lst)
    sort_list(lst)
    print(lst)
    j = search_list(lst, input("value to search"))
    if j == -1:
        print("value not found")

    else:
        print("value found at index ", j)


def search_list(list, val):
    for i in range(0, len(list)):
        if list[i] == float(val):
            return i
    return -1


def sort_list(list):  # no return statement included because lst is updated via the function, returning isn't necessary
    buffer = 0
    min = 0
    for i in range(0, len(list)):  # basic sort implementation
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        buffer = list[i]
        list[i] = list[min]
        list[min] = buffer


if __name__ == '__main__':
    main()
