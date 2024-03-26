import sys
input = sys.stdin.readline


def update(i, diff, toggle):
    if toggle == 0:
        while i <= N:
            even[i] += diff
            i += i & -i
    elif toggle == 1:
        while i <= N:
            odd[i] += diff
            i += i & -i


def prefix_sum(i, toggle):
    result = 0
    if toggle == 0:
        while i > 0:
            result += even[i]
            i -= i & -i
    elif toggle == 1:
        while i > 0:
            result += odd[i]
            i -= i & -i
    return result


def interval_sum(a, b, toggle):
    return prefix_sum(b, toggle) - prefix_sum(a-1, toggle)


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    even = [0]*(N+1)
    odd = [0]*(N+1)
    
    for a in enumerate(A):
        update(a[0] + 1, 1, a[1]%2)

    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            if A[query[1] - 1] % 2 == 0 and query[2] % 2 == 1:
                update(query[1], -1, 0)
                update(query[1], 1, 1)
                A[query[1] - 1] = query[2]
            elif A[query[1] - 1] % 2 == 1 and query[2] % 2 == 0:
                update(query[1], -1, 1)
                update(query[1], 1, 0)
                A[query[1] - 1] = query[2]

        elif query[0] == 2:
            print(interval_sum(query[1], query[2], 0))

        elif query[0] == 3:
            print(interval_sum(query[1], query[2], 1))
