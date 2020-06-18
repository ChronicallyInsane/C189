"""
Author: Evan
Date: 6/17
Purpose: default values, exception handling, input validation
"""


def main():
    print("Enter your input: Name, Score, and optionally an error message.")
    name = input()
    score = int(input())
    msg = input()
    try:
        score_input(name, score, msg)
    except ValueError:
        print("wrong input, try again")
        exit(-1)


def score_input(test_name, test_score=0, invalid_message="Invalid Test Score, please try again!"):
    """
    :name score_input
    purpose: formatting and validating user input for score listing
    :param test_name the name of the test
    :param test_score the score of the selected test
    :param invalid_message the error message returned
    :returns the test name formatted with the score
    """
    try:
        d = int(test_score) / 2
    except ValueError:
        raise ValueError
        return -1

    if str.isascii(invalid_message) != 1:
        print("invalid, error message for invalid message try again")
        return -1
    tries = 5
    while test_score < 0 or test_score > 100:
        print(invalid_message)
        test_score = int(input())
        tries -= 1
        if tries == 0:
            raise ValueError(invalid_message)
            exit(-1)
    result = test_name+": ",test_score
    return result


if __name__ == '__main__':
    main()
