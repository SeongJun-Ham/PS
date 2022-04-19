import sys

N = int(sys.stdin.readline())
A = list(set(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = tuple(map(int, sys.stdin.readline().split()))

A = tuple(sorted(A))
C = tuple(sorted(set(list(B))))

check = {}
j = 0

for i in range(len(C)):
    if C[i] > A[-1] or j > len(A) - 1:
        break
    else:
        for j in range(j, len(A)):
            if C[i] == A[j]:
                check[A[j]] = 1
                j += 1
                break
            elif C[i] < A[j]:
                break

for i in B:
    try:
        print(check[i])
    except:
        print(0)