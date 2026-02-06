import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

ans = 0
for i in range(N):
    ans = max(ans, arr[i]+i+2)
print(ans)