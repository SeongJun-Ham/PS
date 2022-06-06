import sys

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
        parent[max(a, b)] = min(a, b)
    elif parent[a] == a:
        parent[a] = find(b)
    elif parent[b] == b:
        parent[b] = find(a)
    else:
        parent[find(max(a, b))] = find(min(a,b))

print(0)