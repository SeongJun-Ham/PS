import sys

p = 1000000007
def fac(m):
    k = 1
    for i in range(m):
        k *= i+1
        k = k%p
    return k

def power(m, n):
    if n == 0:
        return 1
    
    x = power(m, n//2) % p
    
    if n%2 == 0:
        return x*x
    else:
        return x*x*m

M = int(input())
arr = []
maxValue = 0
for _ in range(M):
    T = tuple(map(int, sys.stdin.readline().split()))
    maxValue = max(maxValue, T[0])
    arr.append(T)

result = []
resultQuery = {}
facQuery = {0:1}

for i in range(maxValue):
    facQuery[i+1] = (i+1)*facQuery[i] % p

for c in arr:
    N, K = c[0], c[1]
    
    if N//2 < K:
        K = N - K
    
    try:
        result.append(resultQuery[(N, K)])
    except:
        B = facQuery[K]*facQuery[N-K]
        R = int(facQuery[N]*power(B, p-2)%p)
        result.append(R)
        resultQuery[(N, K)] = R
print("\n".join(map(str, result)))