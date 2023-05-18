from fractions import Fraction

n, m = map(int, input().split())

def Fac(a, b):
    num = 1
    while a != b:
        num *= a
        a -= 1
    return num

if m >= n//2:
    m = n-m

if m == 0:
    print(1)
else:
    ans = int(Fraction(Fac(n, n-m), Fac(m, 1)))
    print(ans)