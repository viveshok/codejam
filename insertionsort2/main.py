
import sys

def display(array):
    [print(x, end=" ") for x in array]
    print()

N = int(sys.stdin.readline())

array = [int(X) for X in sys.stdin.readline().split()]

for i in range(1, N):
    num = array[i]

    for j in range(i-1, -1, -1):
        if array[j] > num and j != 0:
            array[j+1] = array[j]
        elif array[j] > num and j == 0: 
            array[j+1] = array[j]
            array[j] = num
        else:
            array[j+1] = num
            break

    display(array)

