import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(20)]
TP = []

for i in range(N):
    TP.append(tuple(map(int, sys.stdin.readline().split())))
for i in range(N):
    dp[i + TP[i][0]] = max(max(dp[:i + 1]) + TP[i][1], dp[i + TP[i][0]])
    
dp = dp[:N + 1]
print(max(dp))