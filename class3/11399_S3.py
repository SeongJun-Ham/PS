import sys
import heapq as h

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
h.heapify(P)
result = 0
while N != 0:
  result += N*h.heappop(P)
  N -= 1

print(result)