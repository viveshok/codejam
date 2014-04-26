
import sys

N = int(sys.stdin.readline())

scores = [int(sys.stdin.readline()) for i in range(N)]
candies = [1]*N

# forward pass
for i in range(1, N):
    if scores[i]>scores[i-1]:
        candies[i] = candies[i-1] + 1

# backward pass
for i in range(N-2, -1, -1):
    if scores[i]>scores[i+1] and candies[i]<=candies[i+1]:
        candies[i] = candies[i+1] +1

print(sum(candies))

