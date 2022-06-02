import sys
import heapq as h
N, M = map(int, sys.stdin.readline().split())
degree = [0 for i in range(N+1)]
edge = [[] for i in range(N+1)]
for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    degree[b] += 1
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

print(" ".join(map(str, result)))