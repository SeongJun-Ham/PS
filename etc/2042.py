import sys
input = sys.stdin.readline

def update(i, diff):
    while i <= N:
        fenwick_tree[i] += diff
        i += i & -i


def prefix_sum(i):
    result = 0
    while i > 0:
        result += fenwick_tree[i]
        i -= i & -i
    return result


def interval_sum(a, b):
    return prefix_sum(b) - prefix_sum(a - 1)


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    fenwick_tree = [0]*(N + 1)
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    for a in enumerate(arr):
        update(a[0] + 1, a[1])

    for _ in range(M+K):
        query = tuple(map(int, input().split()))

        if query[0] == 1:
            update(query[1], query[2] - arr[query[1] - 1])
            arr[query[1] - 1] = query[2]

        elif query[0] == 2:
            print(interval_sum(query[1], query[2]))
