
import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        ans = (2**(N//2+1)-1)*2**(N%2)
        print(ans)

