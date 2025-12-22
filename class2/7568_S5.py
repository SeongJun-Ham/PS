N = int(input())
arr = []
for i in range(N):
    w, h = map(int, input().split())
    arr.append([w, h, i])
arr.sort()

ans = []
for i in range(N):
    weight, height = arr[i][0], arr[i][1]
    rank = 0
    ans.append([arr[i][2]])
    while i < N:
        if arr[i][0] > weight and arr[i][1] > height:
            rank += 1
        i += 1
    ans[-1].append(rank+1)

ans.sort()
for a in ans:
    print(a[1], end=' ')