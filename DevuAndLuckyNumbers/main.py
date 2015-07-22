#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import math
#import collections

def f(x, y, z):
    a = x + y + z
    if not a:
        return 0
    Psi = math.factorial(a)//(math.factorial(x)*math.factorial(y)*math.factorial(z))
    Phi = (4 * x + 5 * y + 6 * z) * int(a*'1')
    return int(Psi * Phi // a)

if __name__ == "__main__":

    [x, y, z] = [int(X) for X in sys.stdin.readline().split()]

    answer = 0
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                answer += f(i, j, k)

    print(answer % 1000000007)

