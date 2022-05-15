import sys
import heapq as h

V, E = map(int, sys.stdin.readline().split())
adjacencyList = [[] for _ in range(V+1)]
price = {}

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())

    try:
        price[(min(A, B), max(A, B))] = min(price[(min(A, B), max(A, B))], C)
    except:
        price[(min(A, B), max(A, B))] = C
        adjacencyList[A].append(B)
        adjacencyList[B].append(A)

visited = [0 for _ in range(V+1)]
visited[1] = 1
cur = [0, 0, 1]
result = 0
queue = []

for _ in range(V-1):
    for i in adjacencyList[cur[2]]:
        if visited[i] == 0:
            h.heappush(queue, [price[(min(cur[2], i), max(cur[2], i))], cur[2], i])
        
    while True:
        cur = h.heappop(queue)
        if visited[cur[2]] == 0:
            break
    
    visited[cur[2]] = 1
    result += cur[0]
    
print(result)