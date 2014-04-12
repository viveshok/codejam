#!/usr/bin/python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        answer1 = int(sys.stdin.readline())

        cards1 = list()
        for i in range(4):
            cards1.append({int(X) for X in sys.stdin.readline().split()})

        answer2 = int(sys.stdin.readline())

        cards2 = list()
        for i in range(4):
            cards2.append({int(X) for X in sys.stdin.readline().split()})

        candidates = cards1[answer1-1] & cards2[answer2-1]
        if len(candidates) == 0:
            print("Case #", case+1, ": Volunteer cheated!", sep="")
        elif len(candidates) == 1:
            print("Case #", case+1, ": ", candidates.pop(), sep="")
        else:
            print("Case #", case+1, ": Bad magician!", sep="")

