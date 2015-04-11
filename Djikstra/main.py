#!/usr/bin/python3

import sys
#import math
#import collections

multiply = {('-1','i'):'-i', ('-1','j'):'-j', ('-1','k'):'-k', ('1','i'):'i', ('1','j'):'j', ('1','k'):'k', ('-i','i'):'1', ('-i','j'):'-k', ('-i','k'):'j', ('i','i'):'-1', ('i','j'):'k', ('i','k'):'-j', ('-j','i'):'k', ('-j','j'):'1', ('-j','k'):'-i', ('j','i'):'-k', ('j','j'):'-1', ('j','k'):'i', ('-k','i'):'-j', ('-k','j'):'i', ('-k','k'):'1', ('k','i'):'j', ('k','j'):'-i', ('k','k'):'-1'}

divide = {('1','1'):'1', ('i','i'):'1', ('j','j'):'1', ('k','k'):'1', ('i','1'):'i', ('-1','i'):'i', ('k','j'):'i', ('-j','k'):'i', ('j','1'):'j', ('-k','i'):'j', ('-1','j'):'j', ('i','k'):'j', ('k','1'):'k', ('j','i'):'k', ('-i','j'):'k', ('-1','k'):'k', ('-1','1'):'-1', ('-i','i'):'-1', ('-j','j'):'-1', ('-k','k'):'-1', ('-i','1'):'-i', ('1','i'):'-i', ('-k','j'):'-i', ('j','k'):'-i', ('-j','1'):'-j', ('k','i'):'-j', ('1','j'):'-j', ('-i','k'):'-j', ('-k','1'):'-k', ('-j','i'):'-k', ('i','j'):'-k', ('1','k'):'-k', ('i','-i'):'-1', ('j','-j'):'-1', ('k','-k'):'-1', ('i','-1'):'-i', ('-1','-i'):'-i', ('k','-j'):'-i', ('-j','-k'):'-i', ('j','-1'):'-j', ('-k','-i'):'-j', ('-1','-j'):'-j', ('i','-k'):'-j', ('k','-1'):'-k', ('j','-i'):'-k', ('-i','-j'):'-k', ('-1','-k'):'-k', ('-1','-1'):'1', ('-i','-i'):'1', ('-j','-j'):'1', ('-k','-k'):'1', ('-i','-1'):'i', ('1','-i'):'i', ('-k','-j'):'i', ('j','-k'):'i', ('-j','-1'):'j', ('k','-i'):'j', ('1','-j'):'j', ('-i','-k'):'j', ('-k','-1'):'k', ('-j','-i'):'k', ('i','-j'):'k', ('1','-k'):'k'}

def ijk(cummult):
    if cummult[-1] == '-1':
        for (i, c) in enumerate(cummult[:-1]):
            if c == 'i':
                break
        for (j, c) in enumerate(cummult[i+1:-1]):
            if c == 'k':
                return True

    return False

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        (L, X) = (int(X) for X in sys.stdin.readline().split())

        line = sys.stdin.readline().strip()

        current = line[0]
        cummult = [current]
        for i in range(X):
            for c in line[1:]:
                current = multiply[(current, c)]
                cummult.append(current)

        result = "YES" if ijk(cummult) else "NO"

        print("Case #", case+1, ": ", result, sep="")

