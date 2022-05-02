import sys
import math as m

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 1

for i in range(N):
    if arr[i] != 0 and arr[i] != (i+1):
        point = arr[i] - 1
        save = arr[i] - 1
        arr[i] = 0
        k = 1
        while point != i:
            point = arr[point] - 1
            arr[save] = 0
            save = point
            k += 1
        result = m.lcm(result, k)

print(result)