N, K = map(int, input().split())

dp = [N - i for i in range(N + 1)]

for i in range(N+1, K + 2):
    dp.append(dp[i-1] + 1)

    if i%2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if dp[i] < dp[i-1]:
        dp[i-1] = min(dp[i]+1, dp[i-2]+1)

print(dp[K])