import sys

input = sys.stdin.readline


def tree_size():
    i = 1
    while i < 2*N:
        i <<= 1
    return i


def compare_child(node):
    if arr[tree[2*node]] == arr[tree[2*node+1]]:
        return min(tree[2*node], tree[2*node+1])
    elif arr[tree[2*node]] < arr[tree[2*node+1]]:
        return tree[2*node]
    else:
        return tree[2*node+1]


def init(l, r, node):
    if l == r:
        tree[node] = l
        return
    mid = (l + r) // 2
    init(l, mid, 2*node)
    init(mid+1, r, 2*node+1)
    tree[node] = compare_child(node)


def minV(l, r, node, LEFT, RIGHT):
    if r < LEFT or RIGHT < l:
        return
    if LEFT <= l and r <= RIGHT:
        global ans
        if arr[ans] == arr[tree[node]]:
            ans = min(ans, tree[node])
        elif arr[ans] > arr[tree[node]]:
            ans = tree[node]
        return
    mid = (l+r)//2
    minV(l, mid, 2*node, LEFT, RIGHT)
    minV(mid+1, r, 2*node+1, LEFT, RIGHT)


def update(l, r, node, idx):
    if not l <= idx <= r:
        return
    if l == r:
        return
    mid = (l + r) // 2
    update(l, mid, 2*node, idx)
    update(mid+1, r, 2*node+1, idx)
    tree[node] = compare_child(node)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.append(10e+9)
    tree = [-1 for _ in range(tree_size())]
    init(0, N-1, 1)
    M = int(input())
    for _ in range(M):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            arr[query[1]-1] = query[2]
            update(0, N-1, 1, query[1]-1)
        elif query[0] == 2:
            ans = N
            minV(0, N-1, 1, query[1]-1, query[2]-1)
            print(ans+1)
