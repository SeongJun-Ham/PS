import sys

T = int(sys.stdin.readline())
result = []

for i in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    D.insert(0, 0)
    beforeList = [[] for i in range(N + 1)]
    order = []
    visited = []
    dp = [0 for i in range(N + 1)]
    
    for i in range(K):
        order.append(tuple(map(int, sys.stdin.readline().split())))
    
    for i in range(len(order)):
        beforeList[order[i][1]].append(order[i][0])
        
    goal = int(sys.stdin.readline())

    queue = [goal]
    
    while queue:
        current = queue[-1]
        flag = True
        maxvalue = D[current]
        for i in beforeList[current]:
            maxvalue = max(maxvalue, D[current] + dp[i])
            if i not in visited and i not in queue:
                queue.append(i)
                flag = False
                break
        if flag:
            current = queue.pop()
            visited.append(current)
            dp[current] = maxvalue
    result.append(max(dp))

    
for i in result:
    sys.stdout.write(str(i) + '\n')