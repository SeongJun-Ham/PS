abc = 1
for _ in range(3):
    abc *= int(input())
    
dp = [0]*10
for i in str(abc):
    dp[int(i)] += 1
    
for j in dp:
    print(j)