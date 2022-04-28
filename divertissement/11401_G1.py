p = 1000000007
def facmn(m, n):
    k = 1
    for i in range(m, n+1):
        k *= i
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

N, K = map(int, input().split())

if N//2 < K:
    K = N - K
    
result = facmn(N-K+1, N)*power(facmn(1, K), p-2)
print(int(result)%p)