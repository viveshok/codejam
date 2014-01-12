#!/usr/bin/python

import sys
import numpy
#import pickle

def gravity(matrix):

    (n, m) = matrix.shape
    for j in range(m):
        flattened = matrix[:, j][matrix[:, j] != 46]
        padding = 46*numpy.ones(n-flattened.size, dtype=numpy.int8)
        matrix[:, j] = numpy.hstack((padding, flattened))

    return

def max_seq(array, elem): 
    hits = numpy.hstack((False, (array==elem), False)).astype(int)
    diffs = numpy.diff(hits)
    seqs = numpy.where(diffs==-1)[0] - numpy.where(diffs==1)[0]
    return numpy.max(seqs) if seqs.size else 0

def diagonals(a):
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
    return diags

def winner(matrix, player, K):
    (n, m) = matrix.shape
    for i in range(n):
        if max_seq(matrix[i,:], player) >= K:
            return True

    for j in range(m):
        if max_seq(matrix[:,j], player) >= K:
            return True

    for diag in diagonals(matrix):
        if max_seq(diag, player) >= K:
            return True

    return False

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for case in xrange(num_cases):

        [N, K] = [int(X) for X in finput.readline().split()]

        state = [[ord(X) for X in list(finput.readline())[:-1]] for i in range(N)];

        state = numpy.rot90(numpy.array(state), 3)
        gravity(state)

        B = winner(state, 66, K)
        R = winner(state, 82, K)
        if B and R:
            result = 'Both'
        elif B:
            result = 'Blue'
        elif R: 
            result = 'Red'
        else:
            result = 'Neither'

        foutput.write("Case #"+str(case+1)+": "+result+"\n")

    finput.close()
    foutput.close()

