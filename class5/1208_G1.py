from itertools import combinations as c

N, S = map(int, input().split())
seq = tuple(map(int, input().split()))
a = seq[:N//2]
b = seq[N//2:]
al = [0]
bl = [0]
ar = []
br = []

for i in range(1, len(a) + 1):
    t = list(c(a, i))
    for j in t:
        al.append(sum(j))
        
for i in range(1, len(b) + 1):
    t = list(c(b, i))
    for j in t:
        bl.append(sum(j))
    
al.sort()
bl.sort(reverse=True)

i = 0
j = 0
result = 0
ie = len(al)
je = len(bl)

while i < ie and j < je:
    cur = al[i] + bl[j]
    if cur == S:
        c1 = 0
        c2 = 0
        while True:
            c1 += 1
            try:
                if al[i+1] == al[i]:
                    i += 1
                else:
                    break
            except:
                break
        while True:
            c2 += 1
            try:
                if bl[j+1] == bl[j]:
                    j += 1
                else:
                    break
            except:
                break
        result += c1*c2
        i += 1
        j += 1
    elif cur > S:
        j += 1
    elif cur < S:
        i += 1
        
if S == 0:
    print(result-1)
else:
    print(result)