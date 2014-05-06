#!/usr/bin/python3

import sys
import math
#import collections

if __name__ == "__main__":

    N = int(sys.stdin.readline())
    Nbang = math.factorial(N)

    soln = 0
    for x in range(Nbang+1, 2*Nbang):

        print(Nbang, x)
        if x != Nbang and 1/((1/Nbang)-(1/x)) % 1 < 0.0000001:
#            print(x, 1/((1/Nbang)-(1/x)))
            soln +=1

    print((2*soln+1)%1000007)

