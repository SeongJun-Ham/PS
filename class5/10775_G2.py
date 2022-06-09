import sys
sys.setrecursionlimit(10**5)
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parent = [i for i in range(G+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

ans = 0
for g in range(P):
    g = int(sys.stdin.readline())
    f = find(g)
    if f == 0:
        print(ans)
        sys.exit(0)
    parent[f] -= 1
    ans += 1
        
print(ans)