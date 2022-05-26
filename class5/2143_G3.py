import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = tuple(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = tuple(map(int, sys.stdin.readline().split()))

save = [0]

for a in A:
    save.append(save[-1] + a)
sumA = []
i = 0
while i <= n:
    for j in range(i + 1, n + 1):
        sumA.append(save[j] - save[i])
    i += 1
sumA.sort()
    
save = [0]

for b in B:
    save.append(save[-1] + b)
sumB = []
i = 0
while i <= m:
    for j in range(i + 1, m + 1):
        sumB.append(save[j] - save[i])
    i += 1
sumB.sort(reverse=True)

i, j = 0, 0
ans = 0

while i < len(sumA) and j < len(sumB):
    S = sumA[i] + sumB[j]
    if S == T:
        ca = 1
        cb = 1
        while i+1 < len(sumA) and sumA[i] == sumA[i+1]:
            i += 1
            ca += 1
        while j+1 < len(sumB) and sumB[j] == sumB[j+1]:
            j += 1
            cb += 1
        ans += ca*cb
        i += 1
        j += 1
    elif S > T:
        j += 1
    else:
        i += 1
        
print(ans)