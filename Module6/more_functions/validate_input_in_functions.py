"""
Author: Evan
Date: 6/17
Purpose: default values, exception handling, input validation
"""


def main():
    print("Enter your input: Name, Score, and optionally an error message.")
    name = input()
    score = input()
    msg = input()
    result = ""
    try:
        if len(score) < 1 and len(msg) < 1:
            msg = score_input(name)
        elif len(str(score)) > 0 and len(msg) < 1:
            msg = score_input(name, int(score))
        else:
            msg = score_input(name, int(score), msg)
    except ValueError:
        print("wrong input, try again")
        return -1
    print(msg)


def score_input(test_name, test_score=0, invalid_message="Invalid Test Score, please try again!"):
    """
    :name score_input
    purpose: formatting and validating user input for score listing
    :param test_name the name of the test
    :param test_score the score of the selected test
    :param invalid_message the error message returned
    :returns the test name formatted with the score
    """
    if test_score != 0:
        try:
            d = int(test_score) / 2
        except ValueError:
            return -1
    if str.isdigit(str(invalid_message)) == 1:
        return -1
    tries = 5
    while test_score < 0 or test_score > 100:
        print(invalid_message)
        test_score = int(input())
        tries -= 1
        if tries == 0:
            raise ValueError(invalid_message)
            return -1
    result = test_name + ": " + str(test_score)
    return result


if __name__ == '__main__':
    main()
