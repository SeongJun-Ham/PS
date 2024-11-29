import sys
input = sys.stdin.readline

def find_parent(x):
    if tail[x] != x:
        return find_parent(tail[x])
    return tail[x]

def find_tail(x):
    if tail[x] != x:
        tail[x] = find_tail(tail[x])
    return tail[x]


if __name__ == "__main__":
    N = int(input())
    name_list = [0]*(N+1)
    for i in range(1, N+1):
        name_list[i] = input().rstrip()

    parent = [i for i in range(N+1)]
    tail = [i for i in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        parent[b] = find_parent(a)
        tail[a] = find_tail(b)

    end = find_tail(a)
    ans = [0]*N
    for i in range(1, N+1):
        ans[-i] = name_list[end]
        end = parent[end]
    print("".join(ans))
