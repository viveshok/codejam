#!/usr/bin/python3

import sys

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def cayley(n):

    assert(n>0)

    if n==1:
        return 1
    else:
        return n**(n-2)

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        beads = [int(X) for X in sys.stdin.readline().split()]

        cayleys = [cayley(bead) for bead in beads]

        if N == 1:
            answer = cayleys[0]
            print(answer%1000000007)
        else:

            answer = product(beads) * sum(beads)**(N-2)
            answer *= product(cayleys)

            print(answer%1000000007)

