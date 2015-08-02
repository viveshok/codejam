#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import random
#import math
#import collections

if __name__ == "__main__":

    array = [int(X) for X in sys.stdin.readline().split()]

    print(array)

    N = len(array)
    for i in range(N):
        swap_index = random.randrange(i, N)
        tmp = array[i]
        array[i] = array[swap_index]
        array[swap_index] = tmp

    print(array)

