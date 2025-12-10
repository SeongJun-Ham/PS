import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(row, col, cur_len, condition):
    global ans
    global cnt

    if cur_len > ans:
        return
    if cnt[condition][row][col] <= cur_len:
        return
    cnt[condition][row][col] = cur_len

    if row == N-1 and col == M-1:
        if condition == 1:
            return
        ans = min(cur_len, ans)
        return

    for i in range(4):
        if (0<=row+dy[i]<N) and (0<=col+dx[i]<M) and (visited[row+dy[i]][col+dx[i]]):
            visited[row+dy[i]][col+dx[i]] -= 1
            if condition == 0 and arr[row+dy[i]][col+dx[i]] <= 13:
                dfs(row+dy[i], col+dx[i], cur_len, 1)
            elif condition == 0 and arr[row+dy[i]][col+dx[i]] > 13:
                dfs(row+dy[i], col+dx[i], cur_len+1, 2)
            elif condition == 1 and arr[row+dy[i]][col+dx[i]] > 13:
                dfs(row+dy[i], col+dx[i], cur_len+1, 2)
            elif condition == 2 and arr[row+dy[i]][col+dx[i]] <= 13:
                dfs(row+dy[i], col+dx[i], cur_len, 0)
            visited[row+dy[i]][col+dx[i]] += 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if arr[0][0] <= 13:
        ans = sys.maxsize
        cnt = [[[sys.maxsize]*M for _ in range(N)] for _ in range(3)]
        visited = [[2]*M for _ in range(N)]
        visited[0][0] = 1
        dfs(0, 0, 0, 1)
        if ans == sys.maxsize:
            print("BAD")
        else:
            print(ans)
    else:
        print("BAD")
