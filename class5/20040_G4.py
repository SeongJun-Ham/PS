import sys
sys.setrecursionlimit(10**5)
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
ans = 0

for i in range(m):
    ans += 1
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(ans)
        sys.exit(0)
    elif parent[a] == a and parent[b] == b:
        parent[b] = a
    elif parent[a] == a:
        parent[a] = find(b)
    elif parent[b] == b:
        parent[b] = find(a)
    else:
        parent[find(a)] = find(b)

print(0)