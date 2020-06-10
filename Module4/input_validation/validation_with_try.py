import Module3.format_output.average_scores


def main():
    average(-1, 3, 4)


def average(one, two, three):
    if one < 0 or two < 0 or three < 0:
        raise ValueError
        exit()
    else:
        total = one + two + three
    NUM_TESTS = 3
    return (total / NUM_TESTS)


if __name__ == '__main))':
    main()
