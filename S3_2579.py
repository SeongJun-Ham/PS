import sys

N = int(sys.stdin.readline())
score = [0]

for i in range(N):
    score.append(int(sys.stdin.readline()))

if N == 1:
    print(score[1])
elif N == 2:
    print(score[1] + score[2])

else:
    dp = [0 for i in range(N + 1)]
    dp[0] = [0, 0]
    dp[1] = [score[1], score[1]]
    for i in range(N-1):
        dp[i+2] = [dp[i+1][1] + score[i+2], max(dp[i][0], dp[i][1]) + score[i+2]]
    
    print(max(dp[-1][0], dp[-1][1]))