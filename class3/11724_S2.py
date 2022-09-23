import sys
sys.setrecursionlimit(10**3 + 1)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ma = find(max(a, b))
    mi = find(min(a, b))
    parent[max(ma, mi)] = min(ma, mi)
    
for i in range(1, N+1):
    parent[i] = find(i)
    
parent = set(parent)
print(len(parent) - 1)