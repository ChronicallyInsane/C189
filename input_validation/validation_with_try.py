import Module3.format_output.average_scores


def main():
    try:
        avg = average(-70, 90, 100)
        print("average score is: ", avg)
    except ValueError:
        print("input valid scores")
        exit()


def average(one, two, three):
    if one < 0 or two < 0 or three < 0:
        raise ValueError
        exit()
    else:
        total = one + two + three
    NUM_TESTS = 3
    return total / NUM_TESTS


if __name__ == '__main__':
    main()
