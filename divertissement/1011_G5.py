import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    D = y - x
    n = int((D)**(1/2))
    print(2*n + (D - n**2 - 1)//n)