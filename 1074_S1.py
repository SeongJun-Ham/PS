N, r, c = map(int, input().split())
s = 0
for x in range(N):
    k = N - x - 1
    d, p = int(r/2**k), int(c/2**k)
    s += 2*d*2**(2*k) + p*2**(2*k)
    r, c = r - d*2**k, c - p*2**k
print(s)