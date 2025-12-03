import sys
input = sys.stdin.readline

n = int(input())
arr = [[], [], [], []]

for _ in range(n):
    token = tuple(map(int, input().split()))
    for i in range(4):
        arr[i].append(token[i])

arr_l = []
arr_r = []

for i in range(n):
    for j in range(n):
        arr_l.append(arr[0][i]+arr[1][j])
        arr_r.append(arr[2][i]+arr[3][j])

arr_l.sort()
arr_r.sort()

ans = 0
i = 0 # pointer
j = n**2-1 # pointer
while (0 <= i < n**2) and (0 <= j < n**2):
    if arr_l[i] + arr_r[j] == 0:
        a = 1
        while arr_l[i] == arr_l[i+a]:
            a += 1
            if i+a >= n**2:
                break
        b = 1
        while arr_r[j] == arr_r[j-b]:
            b += 1
            if j-b < 0:
                break
        ans += a*b
        i += a
        j -= b
    elif arr_l[i] + arr_r[j] > 0:
        j -= 1
    elif arr_l[i] + arr_r[j] < 0:
        i += 1
print(ans)