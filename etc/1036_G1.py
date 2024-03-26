import sys


def arr_sync():
    for i in range(36):
        for j in range(50):
            token = divmod(arr[i][j], 36)
            arr[i][j] = token[1]
            arr[i][j + 1] += token[0]


def piority():
    tmp = [(arr[i][::-1], i) for i in range(36)]
    tmp.sort()
    return tmp


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num = [['-1' for _ in range(51)] for _ in range(N)]
    arr = [[0 for _ in range(51)] for _ in range(36)]

    abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {}
    rd = {}
    for i, j in enumerate(abc):
        d[j] = i
        rd[i] = j

    for i in range(N):
        tmp = str(sys.stdin.readline().strip())
        for j in range(len(tmp)):
            num[i][j] = tmp[len(tmp) - j - 1]

    for n in range(N):
        for i in range(51):
            token = num[n][i]
            if token == '-1':
                break
            arr[d[token]][i] += 35 - d[token]

    arr_sync()

    pio = piority()
    storage = [0 for _ in range(52)]

    for n in range(N):
        for i in range(51):
            if num[n][i] == '-1':
                break
            storage[i] += d[num[n][i]]

    K = int(sys.stdin.readline())
    for k in range(K):
        token = pio.pop()
        for i in range(51):
            storage[i] += token[0][50 - i]

    for s in range(51):
        token = divmod(storage[s], 36)
        storage[s] = token[1]
        storage[s + 1] += token[0]

    ans = ""
    flag = False
    for i in range(51, -1, -1):
        if storage[i] != 0:
            flag = True
        if flag:
            ans += rd[storage[i]]

    if ans == "":
        print("0")
    else:
        print(ans)
