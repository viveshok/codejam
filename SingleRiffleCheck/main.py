#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    first_half = [int(X) for X in sys.stdin.readline().split()]
    second_half = [int(X) for X in sys.stdin.readline().split()]
    deck = [int(X) for X in sys.stdin.readline().split()]

    first_half_set = frozenset(first_half)
    second_half_set = frozenset(second_half)

    first = [card for card in deck if card in first_half_set] == first_half
    second = [card for card in deck if card in second_half_set] == second_half
    print(first and second)

