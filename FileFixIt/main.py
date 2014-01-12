#!/usr/bin/python

import sys
#import numpy
#import math
#import pickle

#from collections import defaultdict

class Directory():

    def __init__(self, path):

        self.name = path[0]
        self.subdirectories = dict()
        
        if len(path)>1:
            self.subdirectories[path[1]] = Directory(path[1:])

    def mkdir(self, path):
        if not path:
            return 0

        if path[0] in self.subdirectories:
            return self.subdirectories[path[0]].mkdir(path[1:])

        self.subdirectories[path[0]] = Directory(path)
        return len(path)

    def __str__(self):
        result = self.name + "{"
        for directory in self.subdirectories.values():
            result += directory.__str__() + ","
        result += "}"
        return result


if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    T = int(finput.readline())

    for case in range(T):

        print "Case ", case + 1, "of", T, "..."

        [N, M] = [int(X) for X in finput.readline().split()]

        root = Directory("/")

        for n in range(N):
            path = finput.readline()[1:-1].split('/')
            root.mkdir(path)

        result = 0
        for m in range(M):
            path = finput.readline()[1:-1].split('/')
            result += root.mkdir(path)

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

