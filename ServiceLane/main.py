#!/usr/bin/python3

import sys

if __name__ == "__main__":

    [N, T] = [int(X) for X in sys.stdin.readline().split()]

    widths = [int(X) for X in sys.stdin.readline().split()]

    no_car = {i for i in range(N) if widths[i]<2}
    car_but_no_truck = {i for i in range(N) if widths[i]<3} - no_car

    for case in range(T):

        [i, j] = [int(X) for X in sys.stdin.readline().split()]
        segment = set(range(i, j+1))
        if segment & no_car:
            print(1)
        elif segment & car_but_no_truck:
            print(2)
        else:
            print(3)

