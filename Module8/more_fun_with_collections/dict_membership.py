"""
Author: Evan
Date: 6/23
Purpose; advanced implementation of dictionaries
"""
from string import ascii_lowercase


def main():
    # d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    # in_dict(d, 'A')#yes
    # in_dict(d, 'G')#no
    print("Average Score: ", average_scores(get_test_scores()))


def in_dict(dict_t, val):
    for key, value in dict_t:
        if val == dict_t[key]:
            return True
    return False


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("input desired number of scores"))
    i = 0
    while i <= num_scores:
        i += 1
        ind = input("input score")
        try:
            int(ind) / 2
        except TypeError:
            print("invalid entry, try again")
            i -= 1
            continue
        finally:

            if int(ind) < 0 or int(ind) > 100:
                print("invalid score, try again.")
                i -= 1
                continue
            scores_dict.update({ascii_lowercase[i]: "%s".format(ind)})
            continue

    return scores_dict


def average_scores(s_dict):
    total = 0
    for key, value in s_dict.items():
        total += int(value)
    return total / len(s_dict)


if __name__ == '__main__':
    main()
