"""
author: Evan
Date: 6/8
Purpose: testing if/elif statements.
"""


def main():
    print("Please choose your Programmer's Toolkit, monthly subscription!" +
          "\nThe different levels are Platinum,Gold,Silver,Bronze, and our free version. ")
    result = input()
    if result == "platinum":
        print("60 Dollars")
    elif result == "Gold":
        print("50 Dollars")
    elif result == "silver":
        print("40 Dollars")
    elif result == "Bronze":
        print("30 Dollars")
    elif str.find(result, "free"):
        print("Free trial is free!")
    elif str.isalnum(result) == 0:
        print("wrong input")


if __name__ == '__main__':
    main()

"""
Test(s):
input:free o: Free trial is free!
input:Gold o: 50 Dollars!
"""
