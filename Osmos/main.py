#!/usr/bin/python

import sys
#import numpy
#import pickle

#import sys
#sys.setrecursionlimit(100000) 

def chops(mole, moles, acc):

    num_moles = len(moles)

    if num_moles == 0:
        return acc

    hd = moles[0]

    if mole > hd:
        return chops(mole+hd, moles[1:], acc)

    if mole == 1:
        return acc + num_moles

    return min(chops(2*mole-1, moles, acc+1), chops(mole, moles[:-1], acc+1))


if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for i,case in enumerate(range(num_cases)):

        print "case",i,"of",num_cases

        [A, N] = [int(X) for X in finput.readline().split()]

        moles = sorted([int(X) for X in finput.readline().split()])

        result = chops(A, moles, 0)

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

