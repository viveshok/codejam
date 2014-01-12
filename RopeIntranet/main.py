#!/usr/bin/python

import sys
#import numpy
#import pickle

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for case in xrange(num_cases):

        N = int(finput.readline())

        wires = [[int(X) for X in finput.readline().split()] for i in range(N)];

        intersects = 0

        res = [1 for [a1,b1] in wires for [a2,b2] in wires if (a1>a2)!=(b1>b2)]

        foutput.write("Case #"+str(case+1)+": "+str(len(res)/2)+"\n")

    finput.close()
    foutput.close()

