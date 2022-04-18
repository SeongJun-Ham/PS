import sys

N, M, V = map(int, sys.stdin.readline().split())
edgeList = []
vertexList = [i for i in range(N+1)]
adjacencyList = [[] for vertex in vertexList]
result = ""

for i in range(M):
    edge = list(map(int, sys.stdin.readline().split()))
    adjacencyList[edge[0]].append(edge[1])
    adjacencyList[edge[1]].append(edge[0])

for i in vertexList:
    adjacencyList[i].sort()

queue = []
visited = []
queue.append(V)
visited.append(V)

while queue:
    current = queue[-1]

    for i in adjacencyList[current]:
        if i not in visited and i not in queue:
            queue.append(i)
            visited.append(i)
            break
    
    if current == queue[-1]:
        queue.pop()

for i in visited:
    result += '{} '.format(i)
result += '\n'

queue = []
visited = []
queue.append(V)

while queue:
    current = queue.pop(0)

    for i in adjacencyList[current]:
        if i not in visited and i not in queue:
            queue.append(i)

    visited.append(current)

for i in visited:
    result += '{} '.format(i)

print(result)