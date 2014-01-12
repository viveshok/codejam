
import sys
#import numpy
#import math
#import pickle

#from collections import defaultdict

if __name__ == "__main__":

    finput = open("sample.in", 'r')
    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

#    finput = open("large.in", 'r')
#    foutput = open("large.out", 'w')

    T = int(finput.readline())

    for case in range(T):

        print "Case ", case + 1, "of", T, "..."

        [N, K] = [int(X) for X in finput.readline().split()]

        foutput.write("Case #"+str(case+1)+": "+str("result")+"\n")

    finput.close()
    foutput.close()

