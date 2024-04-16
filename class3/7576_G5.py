import sys
input = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    stack = []
    cnt = 0
    for m in range(M):
        for n in range(N):
            if arr[n][m] == 1:
                stack.append((m, n))
            elif arr[n][m] == 0:
                cnt += 1

    time = 0
    while stack:
        tmp = []
        for _ in range(len(stack)):
            x, y = stack.pop()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0:
                    arr[ny][nx] = 1
                    cnt -= 1
                    tmp.append((nx, ny))
        stack = tmp
        time += 1

    if cnt:
        print(-1)
    else:
        print(time-1)
