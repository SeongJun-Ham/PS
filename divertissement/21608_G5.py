import sys
input = sys.stdin.readline


def sitting(favor):
    global table
    value = []
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for x in range(N):
        for y in range(N):
            if table[x][y] == 0:
                tmp = [0, 0]
                for delta in range(4):
                    next = (x + dx[delta], y + dy[delta])
                    if 0 <= next[0] < N and 0 <= next[1] < N:
                        if table[next[0]][next[1]] in favor:
                            tmp[0] += 1
                        else:
                            if not table[next[0]][next[1]]:
                                tmp[1] += 1
                tmp.extend([-x, -y])
                value.append(tmp)
    value.sort(reverse=True)
    return (value[0][2], value[0][3])


def satisfaction(x, y):
    global satisfy
    global table
    global N
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    result = 0
    returnValue = [0, 1, 10, 100, 1000]

    for i in range(4):
        next = (x + dx[i], y + dy[i])
        if 0 <= next[0] < N and 0 <= next[1] < N:
            if table[next[0]][next[1]] in satisfy[table[x][y]]:
                result += 1
    return returnValue[result]


if __name__ == "__main__":
    N = int(input())
    table = [[0]*N for _ in range(N)]
    satisfy = {}
    ans = 0

    for n in range(N**2):
        nth = list(map(int, input().split()))
        satisfy[nth[0]] = nth[1:]
        next = sitting(nth[1:])
        table[-next[0]][-next[1]] = nth[0]

    for x in range(N):
        for y in range(N):
            ans += satisfaction(x, y)

    print(ans)
