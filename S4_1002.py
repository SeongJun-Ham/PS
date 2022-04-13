import sys

T = int(sys.stdin.readline())
result = []

for i in range(T):
    inform = list(map(int, sys.stdin.readline().split()))
    if inform[2] <= inform[5]:
        small = inform[0:3]
        big = inform[3:6]
    else:
        small = inform[3:6]
        big = inform[0:3]
    
    if small == big:
        result.append(-1)
    else:    
        distance = ((big[0] - small[0])**2 + (big[1] - small[1])**2)**(1/2)
        
        if distance + small[2] == big[2] or distance + small[2] == big[2] + 2*small[2]:
            result.append(1)
        elif distance + small[2] > big[2] and distance + small[2] < big[2] + 2*small[2]:
            result.append(2)
        else:
            result.append(0)

for i in result:
    print(i)