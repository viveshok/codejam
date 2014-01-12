#!/usr/bin/python

import sys
#import numpy
#import pickle
import math

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

    finput = open("small.in", 'r')
    foutput = open("small.out", 'w')

#    finput = open("large.in", 'r')
#    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for case in xrange(num_cases):

        [r, t] = [long(X) for X in finput.readline().split()]

        a = 0.5
        b = r-0.5
        c = -t/math.pi
        result = int(math.floor((-b+math.sqrt(b*b-4*a*c))/(2.0*a)))

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

