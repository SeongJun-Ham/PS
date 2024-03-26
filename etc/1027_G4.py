import sys

input = sys.stdin.readline


def slope(x, y1, y2):
    return (y2 - y1) / x


def visibility(i):
    _arr = list(arr)
    for j in range(1, i + 1):
        next = i - j
        if next >= 0:
            std = slope(j, arr[i], arr[next])
            k = j + 1
            while True:
                if i - k >= 0:
                    if slope(k, arr[i], arr[i - k]) <= std:
                        _arr[i - k] = 0
                else:
                    break
                k += 1
        else:
            break
            
    for j in range(1, N - i):
        next = i + j
        if next < N:
            std = slope(j, arr[i], arr[next])
            k = j + 1
            while True:
                if i + k < N:
                    if slope(k, arr[i], arr[i + k]) <= std:
                        _arr[i + k] = 0
                else:
                    break
                k += 1
        else:
            break

    return len(_arr) - _arr.count(0) - 1


if __name__ == "__main__":
    N = int(input())
    arr = tuple(map(int, input().split()))
    result = []
    ans = 0
    for i in range(N):
        ans = max(ans, visibility(i))

    print(ans)
