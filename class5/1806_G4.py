import sys

N, S = map(int, sys.stdin.readline().split())
seq = tuple(map(int, sys.stdin.readline().split()))
total = sum(seq)

if total < S:
    print(0)
else:
    i, j = 0, 0
    summation = 0
    while summation < S:
        summation += seq[j]
        j += 1
    ans = j - i
    
    flag = True
    while flag:
        while summation - seq[i] >= S:
            summation -= seq[i]
            i += 1
            ans -= 1
        if j + 1 <= N:
            summation += seq[j] - seq[i]
            j += 1
            i += 1
        else:
            flag = False
    
    print(ans)