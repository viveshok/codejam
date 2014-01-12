
import sys
#import numpy
#import math
#import pickle

#from collections import defaultdict

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    C = int(finput.readline())

    for case in range(C):

        print "Case ", case + 1, "of", C, "..."

        [N, K, B, T] = [int(X) for X in finput.readline().split()]
        Xi = [int(X) for X in finput.readline().split()]
        Vi = [int(X) for X in finput.readline().split()]
        chicks = zip(Xi, Vi)

        fast_enough = 0
        num_swaps = 0
        num_chicks = N
        i = num_chicks - 1
        while fast_enough < K and i >= 0:
            if float(B - chicks[i][0])/chicks[i][1] <= T:
                num_swaps += num_chicks - i - 1
                num_chicks -= 1
                fast_enough += 1
            i -= 1

        result = str(num_swaps) if fast_enough == K else "IMPOSSIBLE"

        foutput.write("Case #"+str(case+1)+": "+ result + "\n")

    finput.close()
    foutput.close()

