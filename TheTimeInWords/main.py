#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

NUMBER_STRINGS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                  "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eigthteen", "nineteen", "twenty", "twenty one",
                  "twenty two", "twenty three", "twenty four", "twenty five",
                  "twenty six", "twenty seven", "twenty eigth", "twenty nine"]

def solve(H, M):
    """
    >>> solve(5, 47)
    'thirteen minutes to six'
    >>> solve(6, 35)
    'twenty five minutes to seven'
    >>> solve(5, 45)
    'quarter to six'
    >>> solve(7, 29)
    'twenty nine minutes past seven'
    """

    if M == 0:
        return "{} o' clock".format(NUMBER_STRINGS[H])
    if M == 15:
        return "quarter past {}".format(NUMBER_STRINGS[H])
    if M == 30:
        return "half past {}".format(NUMBER_STRINGS[H])
    if M == 45:
        return "quarter to {}".format(NUMBER_STRINGS[H+1])
    if M < 30 :
        return "{} minutes past {}".format(NUMBER_STRINGS[M], NUMBER_STRINGS[H])

    return "{} minutes to {}".format(NUMBER_STRINGS[60-M], NUMBER_STRINGS[H+1])

if __name__ == "__main__":

    H = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    print(solve(H, M))

