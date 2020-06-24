"""
Author: Evan
Date/ 6/21
Purpose: To demonstrate abstract, user defined constructs for input
"""


def main():
    average_scores(1, 2, 3, 4, 5, proclivity="annoyance", profession='abstract waste of time')


def average_scores(*args, **kwargs):
    total = 0
    for i in range(0, len(args)):
        total += args[i]
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value), end=' ')
    total = total / len(args)
    print("with current average: ", total)


# 'Result: name = M gpa = 3.2 course = Python with current average 30.0

if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, name='Robert', GPA='4.0', course='Python'))
    print(average_scores(50, 45, 60, 25, name='Jones', GPA='1.0', course='Not Python'))
