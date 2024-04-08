import sys
input = sys.stdin.readline

def bfs(coor):
    stack = [coor]
    result = 0
    visited = [[0]*M for _ in range(N)]
    
    while stack:
        x, y = stack.pop()
        if arr[x][y] == 'P':
            result += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] != 'X':
                    stack.append((nx, ny))
                    visited[nx][ny] = 1

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    flag = False
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 'I':
                flag = True
            if flag: break
        if flag: break
    ans = bfs((n, m))

    if ans:
        print(ans)
    else:
        print("TT")
