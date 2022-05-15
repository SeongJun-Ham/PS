import sys

N = int(sys.stdin.readline())

dp =[0, 0, 1, 1]
if N < 4:
    print(dp[N])
else:
    for i in range(4, N+1):
        dp.append(dp[-1]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    print(dp[N])