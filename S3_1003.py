import sys

T = int(sys.stdin.readline())
dp = [[1, 0], [0, 1]]
result = ""

for i in range(39):
    dp.append([dp[-2][0]+dp[-1][0], dp[-2][1]+dp[-1][1]])

for i in range(T):
    N = int(sys.stdin.readline())
    result += "{} {}\n".format(dp[N][0], dp[N][1])

print(result[:-1])