import sys
input = sys.stdin.readline

def search_start(array):
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 2:
                return (x, y)


def bfs(start_point):
    stack = [start_point]
    result = [[-1]*m for _ in range(n)]
    
    result[start_point[0]][start_point[1]] = 0
    arr[start_point[0]][start_point[1]] = 3

    distance = 1
    while stack:
        tmp = []
        while stack:
            x, y = stack.pop()
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1:
                        result[nx][ny] = distance
                        tmp.append((nx, ny))
                    elif arr[nx][ny] == 0:
                        result[nx][ny] = 0
                    arr[nx][ny] = 3
        distance += 1
        stack = tmp

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result[i][j] = 0

    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    ans = bfs(search_start(arr))
    for a in ans:
        print(" ".join(map(str, a)))
