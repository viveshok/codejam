#!/usr/bin/python3

import sys
import math

if __name__ == "__main__":

    text = sys.stdin.readline().strip()
    sqrt = math.sqrt(len(text))
    num_rows = math.floor(sqrt)
    num_columns = math.ceil(sqrt)

    for i in range(num_columns):
        for j in range(i, len(text), num_columns):
            print(text[j], end="")
        print(" ", end="")

