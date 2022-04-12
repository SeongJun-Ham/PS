import sys

T = int(sys.stdin.readline())

dp = [0, 1, 1, 1, 2, 2]
for i in range(97):
    dp.append(dp[-2] + dp[-3])

for i in range(100):
    print(dp[i])