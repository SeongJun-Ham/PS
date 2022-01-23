import sys
import itertools as it

def Distance(a, b):
    return (a**2 + b**2)**(1/2)

T = int(sys.stdin.readline())

for i in range(T):
    result = 282842.712474619038
    N = int(sys.stdin.readline())
    coorList = []
    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coorList.append((x, y))
    
    sign = [i for i in range(N)]
    c = list(it.combinations(sign, N//2))
            
    for i in c:
        xv = 0
        yv = 0
        for j in range(N):
            if j in i:
                xv += coorList[j][0]
                yv += coorList[j][1]
            elif j not in i:
                xv -= coorList[j][0]
                yv -= coorList[j][1]
        dis = Distance(xv, yv)
        result = min(result, dis)
        
    print(result)