import sys

R, C = map(int, input().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
queue = [(0, 0, arr[0][0], 1)]
ans = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
word = ""

while queue:
    if ans == 26:
        break
    else:
        cur = queue[-1]
        word += queue[-1][2]
        for i in range(4):
            x, y = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= x < R and 0 <= y < C and arr[x][y] not in word:
                queue.append((x, y, arr[x][y], cur[3] + 1))
        
        if cur == queue[-1]:
            ans = max(queue[-1][3], ans)
            save = queue.pop()
            word = word[:-1]
            while queue and save[3] - 1 == queue[-1][3]:
                save = queue.pop()
                word = word[:-1]
        
print(ans)