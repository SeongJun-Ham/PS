import sys
input = sys.stdin.readline

def search(ck):
    for i in range(N):
        for j in range(N):
            if ck[i][j] == 0:
                return (i, j)
    return False


if __name__ == "__main__":
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    ans = [0, 0]
    
    while search(check):
        start = search(check)
        check[start[0]][start[1]] = 1
        key = arr[start[0]][start[1]]
        stack = [start]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0 and arr[nx][ny] == key:
                    check[nx][ny] = 1
                    stack.append((nx, ny))
        ans[0] += 1

    check = [[0]*N for _ in range(N)]
    t = {'R': 'R', 'G': 'R', 'B':'B'}
    while search(check):
        start = search(check)
        check[start[0]][start[1]] = 1
        key = t[arr[start[0]][start[1]]]
        stack = [start]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0 and t[arr[nx][ny]] == key:
                    check[nx][ny] = 1
                    stack.append((nx, ny))
        ans[1] += 1

    print(" ".join(map(str, ans)))