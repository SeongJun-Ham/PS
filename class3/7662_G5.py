import sys
import heapq as h

T = int(sys.stdin.readline())
result = ""

for i in range(T):
    minq = []
    maxq = []
    k = int(sys.stdin.readline())
    visited=[False]*k

    for i in range(k):
        func = sys.stdin.readline().split()
        if func[0] == "I":
            h.heappush(minq, (int(func[1]), i))
            h.heappush(maxq, (-int(func[1]), i))
            visited[i] = True
        elif func[1] == "1":
            if maxq:
                k = h.heappop(maxq)
                if visited[k[1]]:
                    visited[k[1]] = False
                else:
                    while not visited[k[1]]:
                        try:
                            k = h.heappop(maxq)
                        except:
                            break
                    visited[k[1]] = False
        else:
            if minq:
                k = h.heappop(minq)
                if visited[k[1]]:
                    visited[k[1]] = False
                else:
                    while not visited[k[1]]:
                        try:
                            k = h.heappop(minq)
                        except:
                            break
                    visited[k[1]] = False

    if maxq:
        maxvalue = h.heappop(maxq)
        while not visited[maxvalue[1]]:
            try:
                maxvalue = h.heappop(maxq)
            except:
                result += "EMPTY" + '\n'
                break
        if visited[maxvalue[1]]:
            minvalue = h.heappop(minq)
            while not visited[minvalue[1]]:
                minvalue = h.heappop(minq)
            result += ("{} {}".format(-maxvalue[0], minvalue[0]) + '\n')
    else:
        result += "EMPTY" + '\n'

print(result[:-1])