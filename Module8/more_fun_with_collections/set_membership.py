def main():
    pass


def in_set(my_set, value):
    for i in range(0, len(my_set)):
        if value == my_set[i]:
            return True
    return False


def init_set():
    i = 'y'
    my_set = set()
    while i != 'n':
        i = input("Enter Set Contents, n to stop")
        if i != 'n':
            my_set.add(i)
    return my_set


if __name__ == '__main__':
    main()
