
import sys

def display(array):
    [print(x, end=" ") for x in array]
    print()

N = int(sys.stdin.readline())

array = [int(X) for X in sys.stdin.readline().split()]

num = array[-1]

for i in range(N-2, -1, -1):
    if array[i] > num and i != 0:
        array[i+1] = array[i]
        display(array)
    elif array[i] > num and i == 0: 
        array[i+1] = array[i]
        display(array)
        array[i] = num
        display(array)
    else:
        array[i+1] = num
        display(array)
        break

