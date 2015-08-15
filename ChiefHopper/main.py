#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import math
#import collections

if __name__ == "__main__":

    _N = int(sys.stdin.readline())

    hs = reversed([int(X) for X in sys.stdin.readline().split()])

    watermark = math.ceil(hs.__next__()/2)

    for h in hs:
        watermark = math.ceil((watermark+h)/2)

    print(watermark)

