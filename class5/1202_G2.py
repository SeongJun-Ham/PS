import sys
import heapq as h

N, K = map(int, sys.stdin.readline().split())
jew = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]

jew.sort()
bag.sort()
save = []
result = 0
i = 0
for k in bag:
    while jew and i < N and k >= jew[i][0]:
        h.heappush(save, -jew[i][1])
        i += 1
    
    if save:
        result -= h.heappop(save)
    elif i == N:
        break
    
print(result)