#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import math
#import collections

def bit_at_i(x, i):
    remainder = x % (2**(i+1))
    if i == 0:
        return remainder
    if remainder:
        return int(math.log(remainder, 2**i))
    return 0

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [A, B] = [int(X) for X in sys.stdin.readline().split()]

        ans = 0
        for i in range(int(math.log(B, 2)), -1, -1):
            bit_at_i_in_A = bit_at_i(A, i)
            bit_at_i_in_B = bit_at_i(B, i)
            if bit_at_i_in_A + bit_at_i_in_B == 2:
                ans += 2**i
            elif bit_at_i_in_A + bit_at_i_in_B == 1:
                break

        print(ans)

