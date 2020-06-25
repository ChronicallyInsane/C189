"""
Author: Evan
Date: 6/23
Purpose; advanced implementation of dictionaries
"""


def main():
    # d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    # in_dict(d, 'A')#yes
    # in_dict(d, 'G')#no
    print("Average Score: ", average_scores(get_test_scores()))


def in_dict(dict_t, value):
    for i in dict_t:
        if i == value:
            return True
    return False


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("input desired number of scores"))
    i = 0
    while i <= num_scores:
        ind = input("input score")
        if ind < 0 or ind > 100:
            print("invalid score, try again.")
            continue
        try:
            str.capitalize(ind)
        except ValueError:
            print("invalid entry, try again.")
            continue
        scores_dict.update(i, ind)
        i += 1
    return scores_dict


def average_scores(s_dict):
    total = 0
    for value in s_dict.items():
        total += value
    return total / len(s_dict)


if __name__ == '__name__':
    main()
