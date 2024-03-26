N, K, M = map(int, input().split())

notation = [1]

while M*notation[-1] <= N:
    notation.append(M*notation[-1])

n = []
k = []

i = 1
while i != len(notation) + 1:
    T = N//notation[-i]
    n.append(T)
    N -= T*notation[-i]
    i += 1

i = 1
while i != len(notation) + 1:
    T = K//notation[-i]
    k.append(T)
    K -= T*notation[-i]
    i += 1

def facmn(m, n):
    k = 1
    for i in range(m, n+1):
        k *= i
        k = k%M
    return k

def power(m, n):
    if n == 0:
        return 1
    
    x = power(m, n//2) % M
    
    if n%2 == 0:
        return x*x
    else:
        return x*x*m

if N//2 < K:
    K = N - K

result = 1
for i in range(1, len(notation) + 1):
    if n[-i] < k[-i]:
        result = 0
        break
    result *= facmn(n[-i]-k[-i]+1, n[-i])*power(facmn(1, k[-i]), M-2)
print(int(result)%M)