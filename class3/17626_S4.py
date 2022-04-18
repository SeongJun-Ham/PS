n = int(input())

dp = [4 for i in range(n+1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, int(i**(1/2)) + 1):
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1

print(dp[n])