#!/usr/bin/python3

import sys

def war(naomis, kens):
    count = 0
    for n in reversed(naomis):
        if n > kens[-1]:
            count += 1
            kens.pop(0)
        else:
            i = 0
            while kens[i] < n:
                i += 1
            kens.pop(i)

    return count

def deceitful_war(naomis, kens):
    count = 0
    while naomis and kens:
        if naomis[-1] > kens[-1]:
            count += 1
            naomis.pop()
            kens.pop()
        else:
            naomis.pop(0)
            kens.pop()

    return count


if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline()
        naomis = sorted([float(X) for X in sys.stdin.readline().split()])
        kens = sorted([float(X) for X in sys.stdin.readline().split()])

        print("Case #", case+1, ": ", deceitful_war(list(naomis), list(kens)), " " , war(naomis, kens), sep="")

