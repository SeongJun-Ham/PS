import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    ans = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        coins = list(map(int, sys.stdin.readline().split()))
        M = int(sys.stdin.readline())
        dp = [0 for i in range(M + 1)]

        for coin in coins:
            dp[coin] += 1
            for i in range(len(dp)):
                if dp[i] != 0 and i + coin < len(dp):
                    dp[i + coin] += dp[i]

        ans.append(dp[M])

    for a in ans:
        print(a)
