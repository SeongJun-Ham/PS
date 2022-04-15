import sys
import heapq as h

N = int(sys.stdin.readline())

heap = []
result = []
for _ in range(N):
    fun = int(sys.stdin.readline())
    if fun == 0:
        try:
            result.append(h.heappop(heap)[1])
        except:
            result.append(0)
    else:
        h.heappush(heap, (-fun, fun))

for i in result:
    print(i)