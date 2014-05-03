#!/usr/bin/python3

import sys
import collections

def sum_of_distance(points):
    median = sorted(points)[len(points)//2]
    distance = 0
    for point in points:
        distance += abs(point-median)
    return distance

def compress_string(string):
    result = [(string[0], 1)]
    for i in range(len(string)-1):
        if string[i+1] == string[i]:
            char, old_count = result[-1]
            result[-1] = (char, old_count + 1)
        else:
            result.append((string[i+1], 1))

    return result

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        strings = list()
        for n in range(N):
            strings.append(sys.stdin.readline().strip())

        compressed_strings = [compress_string(x) for x in strings]
        strings_sets = {"".join([k for k,v in compressed_string]) for compressed_string in compressed_strings}

        if len(strings_sets) == 1:
            distance = 0
            for i in range(len(compressed_strings[0])):
                points = [string[i][1] for string in compressed_strings]
                distance += sum_of_distance(points)

            print("Case #", case+1, ": ", distance, sep="")
        else:
            print("Case #", case+1, ": Fegla Won", sep="")

