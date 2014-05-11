#!/usr/bin/python3

import sys
import math
import fractions
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [P, Q] = [int(X) for X in sys.stdin.readline().split("/")]
        tmp = fractions.Fraction(P, Q)
        P = tmp.numerator
        Q = tmp.denominator

        if P%2 == 1 and math.log(Q, 2)%1 == 0: # possible
            answer = int(math.ceil(math.log(Q/P, 2)))
            if answer > 40:
                print("Case #", case+1, ": ", "impossible", sep="")
            else:
                print("Case #", case+1, ": ", answer, sep="")
        else:
            print("Case #", case+1, ": ", "impossible", sep="")

