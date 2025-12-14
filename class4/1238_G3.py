import sys
import heapq as h
input = sys.stdin.readline
# T의 최댓값은 (N-1)*100이지만 sys.maxsize로 계산

if __name__ == "__main__":
    N, M, X = map(int, input().split())
    value = [[sys.maxsize]*(N) for _ in range(N)]

    # price of i-to-i is 0
    for i in range(N):
        value[i][i] = 0

    # input edgeValue
    for _ in range(M):
        a, b, t = map(int, input().split())
        value[a-1][b-1] = min(value[a-1][b-1], t)

    # Start from X
    queue = []
    for i in range(N):
        if value[X-1][i] != sys.maxsize:
            h.heappush(queue, (value[X-1][i], X-1, i))

    visited = [[0]*N for _ in range(N)]
    while queue:
        cur_v, start, end = map(int, h.heappop(queue))
        if visited[start][end] == 1:
            continue
        
        if value[start][end] < cur_v:
            continue

        visited[start][end] = 1
        for i in range(N):
            if value[start][i] > cur_v + value[end][i]:
                value[start][i] = cur_v + value[end][i]
                h.heappush(queue, (value[start][i], start, i))

    # Go to X
    queue = []
    for i in range(N):
        if value[i][X-1] != sys.maxsize:
            h.heappush(queue, (value[i][X-1], i, X-1))
    
    visited = [[0]*N for _ in range(N)]
    while queue:
        cur_v, start, end = map(int, h.heappop(queue))
        if visited[start][end] == 1:
            continue
        
        if value[start][end] < cur_v:
            continue

        visited[start][end] = 1
        for i in range(N):
            if value[i][end] > value[i][start] + cur_v:
                value[i][end] = value[i][start] + cur_v
                h.heappush(queue, (value[i][end], i, end))

    ans = 0
    for i in range(N):
        ans = max(ans, value[X-1][i] + value[i][X-1])
    print(ans)