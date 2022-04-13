import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    category = {}
    result = 1
    
    for _ in range(n):
        _, y = map(str, sys.stdin.readline().split())
        if y in category:
            category[y] += 1
        else:
            category[y] = 1
    print(category.values())
    for i in tuple(category.values()):
        result *= i + 1
                
    print(result - 1)