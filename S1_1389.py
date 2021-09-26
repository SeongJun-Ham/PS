N, M = map(int, input().split())
vertexList = list(range(1, N+1))
edgeList = []

for x in range(M):
    A, B = map(int, input().split())
    cdn = [A, B]
    rcdn = [B, A]
    edgeList.append(cdn)
    edgeList.append(rcdn)

adjacencyList = [[] for vertex in vertexList]

for edge in edgeList:
    adjacencyList[edge[0] - 1].append(edge[1])

KevinBaconList = []

for x in vertexList:
    visitedList = []
    visitedList.append(x)
    quene = []
    quene.append([x, 0])
    KevinBacon = 0

    while quene:
        current = quene.pop(0)
        for neibor in adjacencyList[current[0] - 1]:
            if not neibor in visitedList:
                visitedList.append(neibor)    
                quene.append([neibor, current[1] + 1])
                KevinBacon += current[1] + 1
    
    KevinBaconList.append(KevinBacon)

print(KevinBaconList.index(min(KevinBaconList)) + 1)