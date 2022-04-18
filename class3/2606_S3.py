import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adjacency = [[] for i in range(N+1)]

for i in range(M):
    K, L = map(int, sys.stdin.readline().split())
    adjacency[K].append(L)
    adjacency[L].append(K)

queue = [1]
visited = []

while True:
    if queue:
        current = queue.pop()
        visited.append(current)
        for i in adjacency[current]:
            if i not in queue and i not in visited:
                queue.append(i)
    else:
        break
            
print(len(visited)-1)