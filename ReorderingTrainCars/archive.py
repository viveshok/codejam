#!/usr/bin/python3

import sys
#import math
import collections

def is_valid(train):

    seens = set()
    for i, car in enumerate(train[:-1]):
        if train[i+1] != car and train[i+1] in seens:
            return False

    return True

class Train:
    def __init__(self, train_string):
        self.train = train_string
        self.hd = train_string[0]
        self.tl = train_string[-1]

    def connect(self, other_train):
        if not is_valid(other_train):
            return False
        elif other_train[0] != self.tl:
            return False
        elif set(other_train) & set(self.train) != set(self.tl):
            return False
        else:
            return Train(self.train+other_train)

def solve(train, cars):
    result = 0
    print(train.train, train.tl, cars)
    if train.tl in cars and cars[train.tl]:
        print('here1')
        for car in cars[train.tl]:
            if is_valid(car):
                new_train = train.connect(car)
                if new_train:
                    new_cars = dict(cars)
                    new_cars[train.tl] = list(cars[train.tl]).remove(car)
                    result += solve(new_train, new_cars)

    else:
        print('here0')
        if any(cars.values()):
            return 0
        else:
            return 1

    return result

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        cars_string = sys.stdin.readline().split()
        cars = collections.defaultdict(tuple)
        for car in cars_string:
            cars[car[0]] = cars[car[0]] + (car,)

        for car in cars_string:
            tmp1 = list(cars[car[0]])
            tmp1.remove(car)
            tmp2 = tuple(tmp1) if tmp1 else tuple()
            new_cars = dict(cars)
            new_cars[car[0]] = tmp2
            solve(Train(car), new_cars)
#            print(solve(Train(car), new_cars))

#        print("Case #", case+1, ": ", Ans, sep="")

