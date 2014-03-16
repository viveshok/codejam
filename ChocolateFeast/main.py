
import sys

def wrapper_to_chocolates(wrappers, M, acc):
    if wrappers < M:
        return acc
    else:
        new_choc = wrappers//M
        return wrapper_to_chocolates(new_choc+wrappers%M, M, acc+new_choc)

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [N, C, M] = [int(X) for X in sys.stdin.readline().split()]

        num_afford = N//C
        Ans = num_afford + wrapper_to_chocolates(num_afford, M, 0)

        print(Ans)

