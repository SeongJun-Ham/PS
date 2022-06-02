import sys
import heapq as h
N, M = map(int, sys.stdin.readline().split())
degree = [0]*(N+1)
edge = [[] for _ in range(N+1)]
for m in range(M):
    pd = tuple(map(int, sys.stdin.readline().split()))
    if pd[0] != 0 and pd[1] != 0:
        for b in range(2, pd[0] + 1):
            for a in range(1, b):
                if pd[b] not in edge[pd[a]]:
                    edge[pd[a]].append(pd[b])
                    degree[pd[b]] += 1
                    
queue = []
result = []
for i in range(1, N+1):
    if degree[i] == 0:
        h.heappush(queue, i)

while queue:
    current = h.heappop(queue)
    result.append(current)
    for c in edge[current]:
        degree[c] -= 1
        if degree[c] == 0:
            h.heappush(queue, c)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)