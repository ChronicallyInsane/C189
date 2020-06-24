"""
Author: Evan
Date: 6/22
Purpose: to implement arrays
"""

import array as array
from Module7.fun_with_collections import basic_list


def main():
    list1 = []
    list1 = basic_list.make_list()
    arr = array.array("I")
    for i in range(0, len(list1)):
        j = list1[i]
        j = int(j)
        arr.append(j)
    print(arr)
    search_list(arr, 7)
    sort_list(arr)
    print(arr)


def search_list(arr, val):
    try:
        return arr.index(val)
    except ValueError:
        return -1


def sort_list(arr):  # no return statement included because lst is updated via the function, returning isn't necessary

    buffer = 0
    min = 0
    for i in range(0, len(arr)):  # basic sort implementation
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        buffer = arr[i]
        arr[i] = arr[min]
        arr[min] = buffer


if __name__ == '__main__':
    main()
