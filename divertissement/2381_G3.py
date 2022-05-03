import sys
N = int(sys.stdin.readline())
ma = 0
mb = 0
T = tuple(map(int, sys.stdin.readline().split()))
ma = T[1] - T[0]
mb = T[1] + T[0]
a = [T[1] - T[0]]
b = [T[1] + T[0]]


for i in range(N-1):
    T = tuple(map(int, sys.stdin.readline().split()))
    a.append(T[1] - T[0])
    ma = max(ma, T[1] - T[0])
    b.append(T[1] + T[0])
    mb = max(mb, T[1] + T[0])

result = 0
for i in a:
    result = max(result, abs(ma - i))
for i in b:
    result = max(result, abs(mb - i))

print(result)