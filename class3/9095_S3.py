import sys

T = int(sys.stdin.readline())

dp = [0, 1, 2, 4]

for i in range(T):
    n = int(sys.stdin.readline())
    while True:
        try:
            print(dp[n])
            break
        except:
            dp.append(dp[-3] + dp[-2] + dp[-1])