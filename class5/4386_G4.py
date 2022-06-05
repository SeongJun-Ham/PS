import sys
import heapq as h

def dis(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
pos = [(0, 0)]
minValue = (1500, 0, 0)
for _ in range(N):
    pos.append(tuple(map(float, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i+1, N+1):
        distance = dis(pos[i], pos[j])
        h.heappush(arr[i], (distance, i, j))
        h.heappush(arr[j], (distance, j, i))
        minValue = min(minValue, (distance, i, j))


result = 0
queue = [h.heappop(arr[minValue[1]])]
visited = [0 for _ in range(N+1)]
visited[minValue[1]] = 1
for n in range(N-1):
    while True:
        cur = h.heappop(queue)
        if visited[cur[2]] == 0:
            break
        else:
            h.heappush(queue, h.heappop(arr[cur[1]]))
    visited[cur[2]] = 1
    result += cur[0]

    while True:
        if arr[cur[1]]:
            save = h.heappop(arr[cur[1]])
            if visited[save[2]] == 0:
                h.heappush(queue, save)
                break
        else:
            break
    while True:
        if arr[cur[2]]:
            save = h.heappop(arr[cur[2]])
            if visited[save[2]] == 0:
                h.heappush(queue, save)
                break
        else:
            break

print(round(result, 2))