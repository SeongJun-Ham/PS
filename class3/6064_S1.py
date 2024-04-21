import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    elif a%b == 0:
        return b
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    T = int(input())
    ans = ''
    for _ in range(T):
        M, N, X, Y = map(int, input().split())
        if X % gcd(M, N) != Y % gcd(M, N):
            ans += '-1\n'
        else:
            next = (M+X)%N
            key = (next-X)%N

            MOD = 0
            value = X
            while True:
                if (value%N) == (Y%N):
                    break
                value = (value+key)%N
                MOD +=1

            ans += f"{M*MOD+X}\n"
    print(ans.rstrip())
