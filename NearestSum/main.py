
# how to
# $ python3 -m doctest -v main.py # to test
# $ python3 main.py < input > output # to run

import sys
#import math
#import collections

def  closest_subtring(intList, n):

    best_score = abs(n - intList[0])
    start, end = 0, 0
    for j in range(1, len(intList)):
        for i in range(start, j + 1):
            score = abs(n - sum(intList[i:j + 1]))
            if score < best_score:
                best_score = score
                start, end = i, j

    return (start, end)

if __name__ == "__main__":

    inputs = [int(line) for line in sys.stdin]

    print(closest_subtring(inputs[:-1], inputs[-1]))
