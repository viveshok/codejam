#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        w = sys.stdin.readline().strip()

        maximum = w[-1]
        s = None
        for i in range(len(w)-1, -1, -1):
            if w[i] < maximum:
                new_val = min([x for x in w[i+1:] if x > w[i]])
                tail = list(w[i:])
                tail.remove(new_val)
                tail.sort()
                s = w[:i] + new_val + ''.join(tail)
                break
            else:
                maximum = w[i]

        print(s if s else "no answer")

