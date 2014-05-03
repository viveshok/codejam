#!/usr/bin/python3

import sys
import collections

if __name__ == "__main__":

    sys.stdin.readline()

    A = [int(X) for X in sys.stdin.readline().split()]

    sys.stdin.readline()

    B = [int(X) for X in sys.stdin.readline().split()]

    Adict = collections.defaultdict(int)
    for a in A:
        Adict[a] +=1

    Bdict = collections.defaultdict(int)
    for b in B:
        Bdict[b] += 1

    diff = set(Bdict.items()) - set(Adict.items())
    answers = sorted([x for (x,y) in diff])
    for answer in answers:
        print(answer, end=" ")
    print()

