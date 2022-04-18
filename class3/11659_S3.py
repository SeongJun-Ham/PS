import sys

N, M = map(int, sys.stdin.readline().split())
num = tuple(map(int, sys.stdin.readline().split()))
arr = [0 for i in range(N+1)]

for i in range(N):
	arr[i+1] = arr[i] + num[i]	

for i in range(M):
	x, y = map(int, sys.stdin.readline().split())
	print(arr[y]-arr[x-1])