import sys

R, C, M = map(int, sys.stdin.readline().split())
arr = [[0]*C for _ in range(R)]
for inform in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    if d == 1 or d == 2:
        arr[r][c] = [s%(2*R-2), d, z]
    elif d == 3 or d == 4:
        arr[r][c] = [s%(2*C-2), d, z]
result = 0
for t in range(C):
    for f in range(R):
        if arr[f][t] != 0:
            result += arr[f][t][2]
            arr[f][t] = 0
            break

    queue = []
    for a in range(R):
        for b in range(C):
            if arr[a][b] != 0:
                queue.append([a, b] + arr[a][b])
                arr[a][b] = 0

    while queue:
        current = queue.pop()
        after = current
        if current[3] == 1:
            after[0] -= current[2]
            if after[0] < 0:
                after[0] *= -1
                after[3] = 2
                if after[0] >= R:
                    after[0] = 2*R - after[0] - 2
                    after[3] = 1
        elif current[3] == 2:
            after[0] += current[2]
            if after[0] >= R:
                after[0] = 2*R - after[0] - 2
                after[3] = 1
                if after[0] < 0:
                    after[0] *= -1
                    after[3] = 2
        elif current[3] == 3:
            after[1] += current[2]
            if after[1] >= C:
                after[1] = 2*C - after[1] - 2
                after[3] = 4
                if after[1] < 0:
                    after[1] *= -1
                    after[3] = 3
        elif current[3] == 4:
            after[1] -= current[2]
            if after[1] < 0:
                after[1] *= -1
                after[3] = 3
                if after[1] >= C:
                    after[1] = 2*C - after[1] - 2
                    after[3] = 4
        if arr[after[0]][after[1]] == 0:
            arr[after[0]][after[1]] = after[2:]
        else:
            if arr[after[0]][after[1]][2] < after[4]:
                arr[after[0]][after[1]] = after[2:]

print(result)