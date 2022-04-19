import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
C = sorted(list(set(X)))
order = {}
result = ""
d = len(C)

for i in range(len(C)):
    order[C.pop()] = d - i - 1
    
for j in range(len(X)):
    X[j] = order[X[j]]
    
print(" ".join((map(str, X))))