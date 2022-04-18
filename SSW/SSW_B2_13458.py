import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

result = N

for i in A:
    current = i - B
    if current > 0:
        if current % C == 0:
            result += current // C
        elif current % C != 0:
            result += current // C + 1
            
print(result)