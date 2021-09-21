from collections import deque
import time

start = time.time()
testList = []

for x in range(30):
    for y in range(30):

        def bfs(v):
            count = 0
            q = deque([[v, count]])
            while q:
                v = q.popleft()
                e = v[0]
                count = v[1]
                if not visited[e]:
                    visited[e] = True
                    if e == K:
                        return count
                    count += 1
                    if (e * 2) <= 100000:
                        q.append([e * 2, count])
                    if (e + 1) <= 100000:
                        q.append([e + 1, count])
                    if (e - 1) >= 0:
                        q.append([e - 1, count])
            return count
                        
        N, K = x, y
        visited = [False] * 100001
        sol1 = int(bfs(N))

        testList.append(sol1)

print(testList)
print(len(testList))
print('time :', time.time() - start)