import sys
from itertools import permutations as per

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
ope = ""
ope += "+"*operator[0] + "-"*operator[1] + "*"*operator[2] + "/"*operator[3]
oper = list(per(ope, len(ope)))
result = []

for i in oper:
    SN = num[0]
    for j in range(N-1):
        if i[j] == '+':
            SN += num[j + 1]
        elif i[j] == '-':
            SN -= num[j + 1]
        elif i[j] == '*':
            SN *= num[j + 1]
        elif i[j] == '/':
            if SN >= 0:
                SN = SN//num[j + 1]
            elif SN < 0:
                SN = abs(SN)//num[j + 1]
                SN *= -1
    result.append(SN)
    
print(max(result))
print(min(result))