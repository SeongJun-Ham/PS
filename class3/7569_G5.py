import sys
input = sys.stdin.readline

def search_ripe_tomato(array):
    global check
    result = []
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    check[h][n][m] = 1
                    result.append((m, n, h))
    return result


def search_unripe_tomato():
    global check
    result = True
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if check[h][n][m] == 0 and arr[h][n][m] == 0:
                    result = False
                    break
            if not result: break
        if not result: break
    return result


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    check = [[[0]*M for _ in range(N)] for _ in range(H)]

    current = search_ripe_tomato(arr)
    next = []
    ans = 0
    while current:
        for c in current:
            x, y, z = c
            for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                nx, ny, nz = x+dx, y+dy, z+dz
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                    if check[nz][ny][nx] == 0 and arr[nz][ny][nx] == 0:
                        check[nz][ny][nx] = 1
                        next.append((nx, ny, nz))
        current = next
        next = []
        if current: ans += 1
    
    if search_unripe_tomato():
        print(ans)
    else:
        print(-1)
