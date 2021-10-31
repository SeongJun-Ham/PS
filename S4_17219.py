import sys

N, M = map(int, sys.stdin.readline().split())
ID = {}
for i in range(N):
    key, value = sys.stdin.readline().split()
    ID[key] = value

for j in range(M):
    address = sys.stdin.readline()[:-1]
    print(ID[address])