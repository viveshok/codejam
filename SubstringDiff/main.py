#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

def largest_common_substring(S1, S2):
    """
    >>> largest_common_substring("abacba", "abcaba")
    3
    """
    n = m = len(S1)
    l = 0
    for d in range(-m+1, n):
        j = -d if d < 0 else 0
        i = j + d
        s = 0
        tmp = min(n-i, m-j)
        for (p, (s1, s2)) in enumerate(zip(S1[i:i+tmp], S2[j:j+tmp])):
            if s1 != s2:
                s = p + 1
            if p + 2 - s > l:
                l = p + 1 - s
    return l

"""
Longest common substrings with k mismatches
Tomas Flourii, Emanuele Giaquinta, Kassian Kobert, and Esko Ukkonen
"""
def kLCF(S1, S2, k):
    """
    >>> kLCF("tabriz", "torino", 2)
    4
    >>> kLCF("helloworld", "yellomarin", 3)
    8
    """
    n = m = len(S1)
    l = 0
    Q = collections.deque()
    for d in range(-m+1, n):
        j = -d if d < 0 else 0
        i = j + d
        Q.clear()
        s = 0
        tmp = min(n-i, m-j)
        for (p, (s1, s2)) in enumerate(zip(S1[i:i+tmp], S2[j:j+tmp])):
            if s1 != s2:
                if len(Q) == k:
                    s = Q.pop() + 1
                Q.appendleft(p)
            if p + 1 - s > l:
                l = p + 1 - s
    return l

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for _case in range(T):

        [S, P, Q] = sys.stdin.readline().strip().split()
        P = list(P)
        Q = list(Q)
        S = int(S)
        if S:
            print(kLCF(P, Q, S))
        else:
            print(largest_common_substring(P, Q))

