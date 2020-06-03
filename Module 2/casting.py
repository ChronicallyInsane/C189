"""
Program: casting.py
Author: Evan
Modified: 6/1/2020

The purpose of this program is to accept input from the user and cast it into an integer.  The input should be able to handle any and all variable types.
"""

to_convert = input()

try:
    int(float(to_convert))
except:
    print("Enter valid statement")
    s = str(to_convert)
    try: print(int(s))
    except: print("Invalid input")
    exit()
finally:
    print(int(float(to_convert)))

#python doesn't accept conversions through int from input().  Thus additional conversion was required in advance.
#152.2 >> 152
#0.0 >> 0
