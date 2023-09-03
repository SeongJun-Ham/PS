MAX = 1<<10
MOD = 10**9


if __name__ == "__main__":
    N = int(input())
    tmp = [[[0]*MAX for _ in range(N)] for _ in range(10)]
    for i in range(1, 10):
        tmp[i][0][1<<i] = 1
    for n in range(N-1):
        for j in range(10):
            for k in range(MAX):
                if j == 0:
                    tmp[1][n+1][k|1<<1] += (tmp[0][n][k]%MOD)
                elif j == 9:
                    tmp[8][n+1][k|1<<8] += (tmp[9][n][k]%MOD)
                else:
                    tmp[j+1][n+1][k|1<<j+1] += (tmp[j][n][k]%MOD)
                    tmp[j-1][n+1][k|1<<j-1] += (tmp[j][n][k]%MOD)

    ans = 0
    for i in range(10):
        ans += tmp[i][N-1][MAX-1]
    
    print(ans%MOD)
