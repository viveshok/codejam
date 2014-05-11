#!/usr/bin/python3

import sys
#import math
import collections

def is_valid(train):

    new_train = train[0]
    for i, car in enumerate(train[:-1]):
        if train[i+1] != car:
            if train[i+1] in set(new_train):
                return False
            else:
                new_train += train[i+1]

    return new_train

def solve(train, cars):
    result = 0
    if cars:
        for car in cars:
            if car[0] == train[-1] and set(car) & set(train) == {car[0]}:
                new_cars = list(cars)
                new_cars.remove(car)
                result += solve(train+car, new_cars)
            elif not set(car) & set(train):
                new_cars = list(cars)
                new_cars = list(cars)
                new_cars.remove(car)
                result += solve(train+car, new_cars)

    else:
        return 1

    return result

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        cars = [is_valid(car) for car in sys.stdin.readline().split()]

        if not all(cars):
            print("Case #", case+1, ": ", 0, sep="")
            continue

        result = 0
        for car in cars:
            remaining_cars = list(cars)
            remaining_cars.remove(car)
            result += solve(car, remaining_cars)


        print("Case #", case+1, ": ", result, sep="")

