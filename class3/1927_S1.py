import sys
import heapq as h

N = int(sys.stdin.readline())

qL = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(qL) == 0:
            print(0)
        else:
            print(h.heappop(qL))
    else:
        h.heappush(qL, x)