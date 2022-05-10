N, M, K = map(int, input().split())

if K > 1000000000:
    print(-1)
else:
    result = ""
    dp = [[1]*(M+1) for _ in range(N+1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            dp[n][m] = dp[n-1][m] + dp[n][m-1]

    if dp[N][M] < K:
        print(-1)
    else:
        while N != 1 and M != 1:
            if dp[N-1][M] >= K:
                result += "a"
                N -= 1
            else:
                K -= dp[N-1][M]
                result += "z"
                M -= 1

        if N == 1:
            result += "z"*(K-1)
            result += "a"
            result += "z"*(M-K+1)
        else:
            result += "a"*(N-K+1)
            result += "z"
            result += "a"*(K-1)

        print(result)