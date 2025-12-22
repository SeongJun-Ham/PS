def cnt(a, b):
    result = 0
    for idx in range(8):
        if a[idx] == b[idx]:
            result += 1
    return result

row, col = map(int, input().split())
arr =  [input() for _ in range(row)]
flag = {0: "BWBWBWBW", 1: "WBWBWBWB"}

ans = 32
for i in range(row-7):
    for j in range(col-7):
        tmp = 0
        for k in range(8):
            tmp += cnt(flag[k%2], arr[i+k][j:j+8])
        ans = min(ans, tmp, 64-tmp)

print(ans)