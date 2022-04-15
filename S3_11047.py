import sys

N, K = map(int, sys.stdin.readline().split())
value = []
result = 0

for i in range(N):
    A = int(sys.stdin.readline().rstrip())
    if A <= K:
        value.append(A)

for i in range(len(value)):
    if K == 0:
        break
    else:
        j = K//value[-i-1]
        result += j
        K -= value[-i-1]*j

print(result)