#!/usr/bin/python3

import sys

if __name__ == "__main__":

    indices = {c:i for (i, c) in enumerate("abcdefghijklmnopqrstuvwxyz")}
    occurences = [0]*26

    string = sys.stdin.readline().rstrip('\n')

    for c in string:
        occurences[indices[c]] += 1

    if len(string)%2==0:
        if any([i%2 for i in occurences]):
            print("NO")
        else:
            print("YES")
    else:
        if sum([i%2 for i in occurences])>1:
            print("NO")
        else:
            print("YES")

