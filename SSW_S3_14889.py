import sys
from itertools import combinations as com

N = int(sys.stdin.readline())
status = []
addStatus = [[0 for i in range(N)]for j in range(N)]
result = []

for i in range(N):
    status.append(list(map(int, sys.stdin.readline().split())))
    
items = [i for i in range(N)]
comList = list(com(items, N//2))
    
for i in range(N):
    for j in range(N):
        addStatus[i][j] = status[i][j] + status[j][i]

for i in comList:
    a = 0
    b = 0
    for j in range(N):
        for k in range(j, N):
            if j in i and k in i:
                a += addStatus[j][k]
            elif j not in i and k not in i:
                b += addStatus[j][k]
    result.append(abs(a-b))

print(min(result))