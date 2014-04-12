#!/usr/bin/python3

import sys

# 0 -> is not neighboring a bomb
# 1 -> no bomb but is neighboring one
# 2 -> is bomb

def solve(board, target):

    if len([x==2 for x in board.values()]) == target:
        return draw(board)

    if len([x==2 for x in board.values()]) == 0: # manually set first bomb in upper left corner
        if all([has_zero_neighbor(c, board) for c in neighbors((0,0))]):
            board[(0,0)] = 2
            return solve(board, target)
        else:
            return "Impossible"

    for candidate in [k for k, v in board if board[k] < 2]:
        if all([has_zero_neighbor(c, board) for c in neighbors(candidate)]):




if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        print("Case #", case+1, ":", sep="")

        [R, C, M] = [int(X) for X in sys.stdin.readline().split()]

        board = {(i,j):0 for i in range(R) for j in range(C)}
        answer = solve(board, M)

