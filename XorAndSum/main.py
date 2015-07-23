#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    a = int(sys.stdin.readline(), 2)

    b = int(sys.stdin.readline(), 2)

    answer = ( a ^ ( b * ( 2 ** 314160 - 1 ) ) ) % 1000000007

    print(answer)

