#!/usr/bin/python

import sys
import math
#import numpy
#import pickle

from operator import mul    # or mul=lambda x,y:x*y

nCk = lambda n,k: int(round(
    reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)
))

def the_sum(n,k):
    sum_ = 0;
    for i in range(k):
        sum_ += nCk(n,i+1)
    return sum_

if __name__ == "__main__":

    finput = open("sample.in", 'r')
    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

#    finput = open("large.in", 'r')
#    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for i, case in enumerate(range(num_cases)):

        print "Case ", i, "of", num_cases, "..."

        [N, X, Y] = [int(x) for x in finput.readline().split()]

#        print "N:",N,", X:",X,", Y:",Y

        m = math.floor(-0.5 + math.sqrt(0.25+2*N))

        if Y + abs(X) < m:
            result = 1
        elif Y + abs(X) > m+1:
            result = 0
        else:
            rem = int(N - 0.5 * m * (m+1))
            result = long(the_sum(Y,rem))/long(2**rem)

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

