import sys
import heapq as h
input = sys.stdin.readline


def tree_size():
    size = 1
    while size < 2*N:
        size <<= 1
    return size


def init(l, r, n):
    if l == r:
        t[n] = a[l]
        return t[n]
    mid = (l+r)//2
    t[n] = min(init(l, mid, 2*n), init(mid+1, r, 2*n+1))
    return t[n]


def update(l, r, n, i):
    if not l <= i <= r:
        return
    if l == r:
        t[n] = a[i]
        return t[n]
    mid = (l+r)//2
    update(l, mid, 2*n, i)
    update(mid+1, r, 2*n+1, i)
    t[n] = min(t[2*n], t[2*n+1])
    

def minV(l, r, n, L, R):
    if r < L or R < l:
        return
    if L <= l and r <= R:
        global result
        h.heappush(result, t[n])
        return
    mid = (l+r)//2
    minV(l, mid, 2*n, L, R)
    minV(mid+1, r, 2*n+1, L, R)
        

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    t = [0]*tree_size()
    init(0, N-1, 1)

    M = int(input())
    for _ in range(M):
        q = tuple(map(int, input().split()))
        if q[0] & 1:
            a[q[1]-1] = q[2]
            update(0, N-1, 1, q[1]-1)
        else:
            result = []
            minV(0, N-1, 1, q[1]-1, q[2]-1)
            print(result[0])
