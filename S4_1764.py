import sys

N, M = map(int, sys.stdin.readline().split())

notLS = {}
result = []
count = 0

for i in range(N):
    notlisten = sys.stdin.readline()
    notLS[notlisten] = True
for i in range(M):
    notsee = sys.stdin.readline()
    if notLS.get(notsee):
        result.append(notsee[:-1])
        count += 1

result.sort()

print(count)
for i in result:
    print(i)