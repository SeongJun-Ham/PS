N, K = map(int, input().split())
arr = [[1 for i in range(N + 1)] for i in range(K + 1)]
arr[1][1] = 1
for i in range(2, K + 1):
    for j in range(1, N + 1):
        arr[i][j] = sum(arr[i - 1][:j + 1])%1000000000
        
print(arr[K][N])