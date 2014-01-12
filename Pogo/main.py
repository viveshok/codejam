
import sys
#import numpy
#import math
#import pickle

#from collections import defaultdict

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

    finput = open("small.in", 'r')
    foutput = open("small.out", 'w')

#    finput = open("large.in", 'r')
#    foutput = open("large.out", 'w')

    T = int(finput.readline())

    for case in range(T):

        [X, Y] = [int(X) for X in finput.readline().split()]

        path = ''
        counter = range(10**12).__iter__()

        posX = 0
        dirX = -1 if X > 0 else 1

        while posX != X:
            posX += dirX * counter.__next__()
            path += 'E' if dirX == 1 else 'W'
            dirX *= -1

        posY = 0
        dirY = -1 if Y > 0 else 1

        while posY != Y:
            posY += dirY * counter.__next__()
            path += 'N' if dirY == 1 else 'S'
            dirY *= -1

        foutput.write("Case #"+str(case+1)+": "+path+"\n")

    finput.close()
    foutput.close()

