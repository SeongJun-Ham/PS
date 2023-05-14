N, L, I = map(int, input().split()) # 입력


dp = [[0]*N for _ in range(N)] # dp에 파스칼 삼각형 담기
dp[0][0] = 1
for n in range(1, N):
    dp[n][0] = 1
    for j in range(1, n+1):
        dp[n][j] = dp[n-1][j-1] + dp[n-1][j]
dp[0][0] = 2
    
    
result = [0]*N # result에 이진수 담기
for l in range(L, 0, -1):
    tmp = 0
    i = 0
    while tmp + sum(dp[i][:l]) < I:
        tmp += sum(dp[i][:l])
        i += 1
        
    if i == 0 and I == 2: # 파스칼삼각형 0번째 줄에는 1이 아닌 2를 저장해주었으므로 따로 판별
        result[0] = 1
    elif i != 0:
        result[i] = 1
        I -= tmp
    
ans = '' # result에 담긴 이진수 차례로 빼기
while result:
    ans += str(result.pop())
    
print(ans)