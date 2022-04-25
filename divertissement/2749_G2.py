import sys

n = int(sys.stdin.readline())

dp = [0, 1]

n = n%(15*(10**5))

for i in range(n):
    if dp[-1] > 1000000:
        dp[-1] = dp[-1]%1000000
    dp.append(dp[i] + dp[i + 1])
    
print(dp[n])