import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
queue = []
visited = [[0]*N for i in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []
i = 0
flag = True

while i < N:
    flag = False
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            flag = True
            matrix[i][j] = 0
            queue.append((i, j))
            visited[i][j] = 1
            result.append(1)
            break
    while queue:
        current = queue.pop()
        for k in range(4):
            nx, ny = current[0] + dx[k], current[1] + dy[k]
            if nx >=0 and ny>=0 and nx < N and ny < N:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    result[-1] += 1
    if not flag:
        i += 1

result.sort()
print(len(result))
for m in result:
    print(m)