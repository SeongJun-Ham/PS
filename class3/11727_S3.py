N = int(input())
t = [0]*(N+2)
t[1] = 1
t[2] = 3

for i in range(3, N+1):
    t[i] = (2*t[i-2]+t[i-1])%10007

print(t[N])