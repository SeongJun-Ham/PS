import sys

N = int(sys.stdin.readline())
point = []
result = 0
for _ in range(N):
    point.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(N):
    result += point[-i-1][1]*point[-i][0]
    result -= point[-i-1][0]*point[-i][1]

print(abs(round(result/2, 1)))