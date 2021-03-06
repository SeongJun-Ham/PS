import sys

T = int(sys.stdin.readline())
for i in range(T):
    M, N, K= map(int, sys.stdin.readline().split())

    count = 0
    qL =[]

    for i in range(K):
        Q = list(map(int, sys.stdin.readline().split()))
        qL.append(Q)

    while qL:
        queue = []
        queue.append(qL.pop(0))

        while queue:
            current = queue.pop(0)
            adjacencyList = []
            adjacencyList.append([current[0] + 1, current[1]])
            adjacencyList.append([current[0], current[1] - 1])
            adjacencyList.append([current[0], current[1] + 1])
            adjacencyList.append([current[0] - 1, current[1]])

            for neibor in adjacencyList:
                if neibor in qL:
                    queue.append(qL.pop(qL.index(neibor)))
        
        count += 1
    
    print(count)