#!/usr/bin/python3

import sys

if __name__ == "__main__":

    indices = {c:i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}

    T = int(sys.stdin.readline())

    for case in range(T):

        string = sys.stdin.readline().rstrip('\n')

        length = len(string)

        if length%2==1:
            print(-1) # anagrams must have same length
        else:
            
            string1 = string[:length//2]
            list1 = [0] * 26
            for c in string1:
                list1[indices[c]] += 1

            string2 = string[length//2:]
            list2 = [0] * 26
            for c in string2:
                list2[indices[c]] += 1

            print(sum([abs(a-b) for a,b in zip(list1, list2)])//2)

