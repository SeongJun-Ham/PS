import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    count = 0
    start = (9, 1)
    for i in range(9):
        if 9 - i >= arr[M]:
            j = -start[1] + 1
            for _ in range(N):
                if j == N:
                    j = 0
                if 9 - i == arr[j]:
                    if j == M:
                        count += 1
                        result.append(count)
                        break
                    else:
                        count += 1
                        start = (arr[j], -j)
                j += 1

for i in result:
    print(i)