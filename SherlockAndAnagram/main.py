#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        S = sys.stdin.readline().strip()

        anagrams = collections.defaultdict(int)
        answer = 0
        for i in range(len(S)):
            for j in range(i+1, len(S)+1):
                anagram = "".join(sorted(S[i:j]))
                answer += anagrams[anagram]
                anagrams[anagram] += 1

        print(answer)

